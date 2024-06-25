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
  
def validate_arguments(file_path, start_range, till_range):
  data = read_csv_file(file_path)
  st_range = datetime.strptime(start_range if start_range else data[0].get('Date.Full'), '%Y-%m-%d')
  end_range = datetime.strptime(till_range if till_range else data[-1].get('Date.Full'), '%Y-%m-%d')
  return st_range, end_range

def date_based_filtering(file_path, start_range, till_range):
  data = read_csv_file(file_path)
  st_range, end_range = validate_arguments(file_path, start_range, till_range)
  date_based = []
  for record in data:
    date = record.get('Date.Full')          
    rangeDate = datetime.strptime(date, '%Y-%m-%d')
    if(rangeDate >= st_range and rangeDate <= end_range):
      date_based.append(record)
    
    return date_based if date_based else data

def city_based_filtering(file_path, start_range, till_range, city_name):
  date_based = date_based_filtering(file_path, start_range, till_range)
  if city_name:
    city_based =  [record for record in date_based if record.get('Station.City') == city_name]
    return city_based
  else:
    return date_based
    
def apply_arguments(file_path, start_range, till_range, city_name, min_max_avg, col_find):
  final_data = city_based_filtering(file_path, start_range, till_range, city_name)
  dict_data = {}
  if final_data: 
    if min_max_avg and col_find:
      if min_max_avg == 'avg':
        if col_find == 'maxT':
          dict_data['Average.Temperature Max'] = TemperatureDisplay(final_data).avg_max_temp()
        if col_find == 'minT':
          dict_data['Average.Temperature Min'] = TemperatureDisplay(final_data).avg_min_temp()
        if col_find == 'wd':
          dict_data['Average.Wind.Direction'] = TemperatureDisplay(final_data).avg_wind_direction()
        if col_find == 'ws':
          dict_data['Average.Wind.Speed'] = TemperatureDisplay(final_data).avg_wind_speed()
          
        return dict_data
          
      if min_max_avg == 'max':
        if col_find == 'count':
          max_state_occur, count  = MaxStateOccurance(final_data).max_state_occur()
          return f'The {max_state_occur} has maximum occurance of {count} times'
        if col_find == 'maxT':
          max_temp, location, state = MaxTempLocState(final_data).location_state_display()
          return f'The maxTemp of the maxTempcol is {max_temp} of state {state} located in {location}'
        if col_find == 'avgT':
          month_name, month_avg_tempMax = MonthWithMaxAvgTemp(final_data).max_avg_temp_month()
          return f' The max avg temperature is {month_avg_tempMax} during {month_name}'
        if col_find == 'maxTState':
          max_temp, city, loc, code, state = StateData(final_data).state_max_temp()
          dict_data['Max Temperature'] = {
            'Station.City' : city,
            'Station.Location' : loc,
            'Station.Code' : code,
            'Station.State' : state
          }
          return dict_data
        if col_find == 'day':
          day, max_temp = DayMaxTemp(final_data).day_avg_temp_max()
          return f'The max temp is {max_temp} on {day} date'
        if col_find == 'ws':
          max_ws, city, loc, code, state = StateData(final_data).state_max_wind_speed()
          dict_data['Max Wind Speed'] = {
            'Station.City' : city,
            'Station.Location' : loc,
            'Station.Code' : code,
            'Station.State' : state
          }
          return dict_data
      
      if min_max_avg == 'min':
        if col_find == 'avgT':
          year_no, year_avg_temp_min = YearWithMinAvgTemp(final_data).min_avg_temp_year()
          return f'The min avg temp is {year_avg_temp_min} in {year_no}'
        if col_find == 'minT':
          min_temp, city, loc, code, state  = StateData(final_data).state_min_temp() 
          dict_data['Min Temperature'] = {
            'Station.City' : city,
            'Station.Location' : loc,
            'Station.Code' : code,
            'Station.State' : state
          }
          return dict_data
        if col_find == 'ws':
          min_ws, city, loc, code, state = StateData(final_data).state_min_wind_speed()  
          dict_data['Min Wind Speed'] = {
            'Station.City' : city,
            'Station.Location' : loc,
            'Station.Code' : code,
            'Station.State' : state
          }
          return dict_data
      
    else:
      return '-m or -t arguments not provided'
  else:
    return 'filtered data is empty'
  
  if dict_data:
    return dict_data

def main():
  parser = CustomArgumentParser()  
  args = parser.parse_args()

  file_path = args.file
  start_range = args.start
  till_range = args.end
  city_name = args.city
  min_max_avg = args.maxminavg
  col_find = args.col
 
  print(apply_arguments(file_path, start_range, till_range, city_name, min_max_avg, col_find))

  result = (apply_arguments(file_path, start_range, till_range, city_name, min_max_avg, col_find))
  
  if type(result) is dict:
    export_to_csv('res_file.csv', result)
    print("The data exported to res_file.csv is : ", read_result_file('res_file.csv'))

if __name__ == '__main__':
  main()