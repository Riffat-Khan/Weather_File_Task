import csv
from datetime import datetime
from argparser.argparser import arg_parser
from utils.temp_display import temperature_display
from utils.max_temp_loc_state import max_temp_loc_state
from utils.max_state_count import max_state_occurance
from utils.state import state_data
from utils.month import month_with_max_avg_temp
from utils.year import year_with_min_avg_temp
from utils.day import day_max_temp
from export.write_csv import export_to_csv, read_result_file

def read_csv(file_path, start_range, till_range, city_name, min_max_avg, find):

  with open(file_path, mode='r') as csvFile:
    file = csv.DictReader(csvFile)
    dataArray = list(file)
    
    dictData = {}
    subdict = {}
        
    date_based = []
    
    if start_range and till_range:
      st_range = datetime.strptime(start_range, '%Y-%m-%d')
      end_range = datetime.strptime(till_range, '%Y-%m-%d')
    elif start_range and (not till_range):
      st_range = datetime.strptime(start_range, '%Y-%m-%d')
      till_range = dataArray[-1].get('Date.Full')
      end_range = datetime.strptime(till_range, '%Y-%m-%d')
    elif till_range and (not start_range):
      start_range = dataArray[0].get('Date.Full')
      st_range = datetime.strptime(start_range, '%Y-%m-%d')
      end_range = datetime.strptime(till_range, '%Y-%m-%d')
    else:
      start_range = dataArray[0].get('Date.Full')
      till_range = dataArray[-1].get('Date.Full')
      st_range = datetime.strptime(start_range, '%Y-%m-%d')
      end_range = datetime.strptime(till_range, '%Y-%m-%d')
        
    for each_array in dataArray:
      date = each_array.get('Date.Full')          
      rangeDate = datetime.strptime(date, '%Y-%m-%d')
      if(rangeDate >= st_range and rangeDate <= end_range):
        date_based.append(each_array)  
              
    city_based = []
    if date_based and city_name:
      try:
        for each_array in date_based:
          city_Station = each_array.get('Station.City') 
          if city_Station == city_name:
            city_based.append(each_array)
            
        final_data =  city_based
      except:
        print("The range is empty or the city arg is not given")
    else:
      final_data = dataArray  
      
  if min_max_avg and find:
    try:
      if min_max_avg == 'avg':
        if find == 'maxT':
          avgMaxTemp= temperature_display(final_data).avg_max_temp()
          dictData['Average.Temperature Max'] = avgMaxTemp
          return dictData
        if find == 'minT':
          avgMinTemp = temperature_display(final_data).avg_min_temp()
          dictData['Average.Temperature Min'] = avgMinTemp
          return dictData
        if find == 'wd':
          avgWindDir = temperature_display(final_data).avg_wind_direction()
          dictData['Average.Wind.Direction'] =  avgWindDir
          return dictData
        if find == 'ws':
          avgWindSpeed = temperature_display(final_data).avg_wind_speed()
          dictData['Average.Wind.Speed'] = avgWindSpeed
          return dictData
        
      if min_max_avg == 'max':
        if find == 'count':
          MaxStateOccur, count  = max_state_occurance(final_data).max_state_occur()
          return f'The {MaxStateOccur} has maximum occurance of {count} times'
        if find == 'maxT':
          MaxTemp, Location, State = max_temp_loc_state(final_data).max_temp_loc_state()
          return f'The maxTemp of the maxTempcol is {MaxTemp} of state {State} located in {Location}'
        if find == 'avgT':
          monthName, monthAvgTempMax = month_with_max_avg_temp(final_data).max_avg_temp_month()
          return f' The max avg temperature is {monthAvgTempMax} during {monthName}'
        if find == 'maxTState':
          MaxT, City, Loc, Code, State = state_data(final_data).state_max_temp()
          subdict = {
            'Station.City' : City,
            'Station.Location' : Loc,
            'Station.Code' : Code,
            'Station.State' : State
          }
          dictData['Max Wind Speed'] = subdict
        if find == 'day':
          day, max_temp = day_max_temp(final_data).day_avg_temp_max()
          return f'The max temp is {max_temp} on {day} date'
        if find == 'ws':
          MaxWS, City, Loc, Code, State = state_data(final_data).state_max_wind_speed()
          subdict = {
            'Station.City' : City,
            'Station.Location' : Loc,
            'Station.Code' : Code,
            'Station.State' : State
          }
          dictData['Max Wind Speed'] = subdict
          return dictData
      
      if min_max_avg == 'min':
        if find == 'avgT':
          yearNo, yearAvgTempMin = year_with_min_avg_temp(final_data).min_avg_temp_year()
          return f'The min avg temp is {yearAvgTempMin} in {yearNo}'
        if find == 'minT':
          MinTemp, City, Loc, Code,State  = state_data(final_data).state_min_temp() 
          subdict = {
            'Station.City' : City,
            'Station.Location' : Loc,
            'Station.Code' : Code,
            'Station.State' : State
          }
          dictData['Max Wind Speed'] = subdict
          return dictData
        if find == 'ws':
          MinWS, City, Loc, Code, State = state_data(final_data).state_min_wind_speed()  
          subdict = {
            'Station.City' : City,
            'Station.Location' : Loc,
            'Station.Code' : Code,
            'Station.State' : State
          }
          dictData['Min Wind Speed'] = subdict
          return dictData
      
    except:
      return'-m[min/max/avg] or -t[avgT/maxT/minT/wd/ws]  argument not provided correctly'
    
  else:
    return '-m[min/max/avg] or -t[avgT/maxT/minT/wd/ws]  argument not provided'
  
  if dictData:
    return dictData

def main():
  argParser = arg_parser()
  args = argParser.parse_args()

  file_path = args.file
  start_range = args.dateFrom
  till_range = args.dateTo
  city_name = args.city
  min_max_avg = args.maxmin
  find = args.tempwind
  
  print(read_csv(file_path, start_range, till_range, city_name, min_max_avg, find))

  result = (read_csv(file_path, start_range, till_range, city_name, min_max_avg, find))
  
  if type(result) is dict:
    export_to_csv('res_file.csv', result)
    print("The data exported to res_file.csv is : ", read_result_file('res_file.csv'))

if __name__ == '__main__':
  main()