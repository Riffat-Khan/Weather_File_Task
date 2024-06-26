import csv
from datetime import datetime
from argparser.argparser import CustomArgumentParser
from utils.temp_display import TemperatureDisplay
from utils.max_temp_loc_state import MaxTempLocState
from utils.max_state_count import MaxStateOccurance
from utils.state import StateData
from utils.month import MonthWithMaxAvgTemp
from utils.year import YearWithMinAvgTemp
from utils.day import DayMaxTemp
from export.write_csv import export_to_csv, read_result_file

def read_csv_file(file_path):
  with open(file_path, mode='r') as csvFile:
    file = csv.DictReader(csvFile)
    data = list(file)
    return data
  
def valid_args(file_path, start, end):
  data = read_csv_file(file_path)
  st_range = datetime.strptime(start if start else data[0].get('Date.Full'), '%Y-%m-%d')
  end_range = datetime.strptime(end if end else data[-1].get('Date.Full'), '%Y-%m-%d')
  return st_range, end_range

def date_based_filtering(file_path, start, end):
  data = read_csv_file(file_path)
  st_range, end_range = valid_args(file_path, start, end)
  date_based = []
  for record in data:
    date = record.get('Date.Full')          
    rangeDate = datetime.strptime(date, '%Y-%m-%d')
    if(rangeDate >= st_range and rangeDate <= end_range):
      date_based.append(record)
    
  return date_based if date_based else data

def city_based_filtering(file_path, start, end, city):
  date_based = date_based_filtering(file_path, start, end)
  if city:
    city_based =  [record for record in date_based if record.get('Station.City') == city]
    return city_based
  else:
    return date_based
  
def avg_values(final_data, column):
  dict_data = {}
  if final_data: 
    if column:
      if column == 'maxT':
        dict_data['Average.Temperature Max'] = TemperatureDisplay(final_data).avg_max_temp()
      if column == 'minT':
        dict_data['Average.Temperature Min'] = TemperatureDisplay(final_data).avg_min_temp()
      if column == 'wd':
        dict_data['Average.Wind.Direction'] = TemperatureDisplay(final_data).avg_wind_direction()
      if column == 'ws':
        dict_data['Average.Wind.Speed'] = TemperatureDisplay(final_data).avg_wind_speed()
          
  return dict_data

def max_values(final_data, column):
  dict_data = {}
  if column == 'count':
    max_state_occur, count  = MaxStateOccurance(final_data).max_state_occur()
    return f'The {max_state_occur} has maximum occurance of {count} times'
  if column == 'maxT':
    max_temp, location, state = MaxTempLocState(final_data).location_state_display()
    return f'The maxTemp of the maxTempcol is {max_temp} of state {state} located in {location}'
  if column == 'avgT':
    month_name, month_avg_tempMax = MonthWithMaxAvgTemp(final_data).max_avg_temp_month()
    return f' The max avg temperature is {month_avg_tempMax} during {month_name}'
  if column == 'maxTState':
    max_temp, city, loc, code, state = StateData(final_data).state_max_temp()
    dict_data['Max Temperature'] = {
      'Station.City' : city,
      'Station.Location' : loc,
      'Station.Code' : code,
      'Station.State' : state
    }
    return dict_data
  if column == 'day':
    day, max_temp = DayMaxTemp(final_data).day_avg_temp_max()
    return f'The max temp is {max_temp} on {day} date'
  if column == 'ws':
    max_ws, city, loc, code, state = StateData(final_data).state_max_wind_speed()
    dict_data['Max Wind Speed'] = {
      'Station.City' : city,
      'Station.Location' : loc,
      'Station.Code' : code,
      'Station.State' : state
    }
    return dict_data
  return None
  
def min_values(final_data, column):
  dict_data = {}
  if column == 'avgT':
    year_no, year_avg_temp_min = YearWithMinAvgTemp(final_data).min_avg_temp_year()
    return f'The min avg temp is {year_avg_temp_min} in {year_no}'
  if column == 'minT':
    min_temp, city, loc, code, state  = StateData(final_data).state_min_temp() 
    dict_data['Min Temperature'] = {
      'Station.City' : city,
      'Station.Location' : loc,
      'Station.Code' : code,
      'Station.State' : state
    }
    return dict_data
  if column == 'ws':
    min_ws, city, loc, code, state = StateData(final_data).state_min_wind_speed()  
    dict_data['Min Wind Speed'] = {
      'Station.City' : city,
      'Station.Location' : loc,
      'Station.Code' : code,
      'Station.State' : state
    }
    return dict_data
  return None

def processing_stats(file_path, start, end, city, stats, column):
  final_data = city_based_filtering(file_path, start, end, city)
  if not final_data:
    return 'The filtered data based on your arguments is empty'
  else:
    if stats == 'avg':
      return avg_values(final_data, column)
    if stats == 'max':
      return max_values(final_data, column)
    if stats == 'min':
      return min_values(final_data, column)
    
def applying_args(file_path, start, end, city, stats, column):
  if stats and column:
    return processing_stats(file_path, start, end, city, stats, column)
  else:
    return '--stats and --col args are required'
  
  
def main():
  parser = CustomArgumentParser()  
  args = parser.parse_args()

  file_path = args.file
  start = args.start
  end = args.end
  city = args.city
  stats = args.stats
  column = args.col
 
  print(applying_args(file_path, start, end, city, stats, column))

  result = (applying_args(file_path, start, end, city, stats, column))
  
  if result and  type(result) is dict:
    export_to_csv('res_file.csv', result)
    print("The data exported to res_file.csv is : ", read_result_file('res_file.csv'))

if __name__ == '__main__':
  main()