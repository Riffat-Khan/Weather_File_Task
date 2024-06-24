import csv
from ArgParser.ArgParser import ArgParser
from utils.TempDisplay import TemperatureDisplay
from utils.MaxTempLocState import MaxTempLocState
from utils.MaxStateCount import MaxStateOccurance
from utils.State import state
from utils.month import month
from utils.year import year
from utils.day import day
from export.write_csv import export_to_csv, read_result_file

def read_csv(file_path):

  with open(file_path, mode='r') as csvFile:
    file = csv.DictReader(csvFile)
    data = list(file)

    avgMaxTemp, avgMinTemp = TemperatureDisplay(data).avgMaxMinTemp()
    avgWindDirection = TemperatureDisplay(data).avgWindDirection()
    avgWindSpeed = TemperatureDisplay(data).avgWindSpeed()
    
    MaxTempofMaxCol, Location, State = MaxTempLocState(data).LocationStateDisplay()

    MaxStateOccur, count  = MaxStateOccurance(data).MaxStateOccur()
    
    StateMaxTemp, MTCity, MTLocation, MTCode, MTState = state(data).StateMaxTemp()
    
    StateMaxWindSpeed, MWSCity, MWSLocation, MWSCode, MWSState = state(data).StateMaxWindSpeed()
    StateMinTemp, MinTCity, MinTLocation, MinTCode, MinTState = state(data).StateMinTemp()
    StateMinWindSpeed, MinWSCity, MinWSLocation, MinWSCode, MinWSState = state(data).StateMinWindSpeed()
    
    monthName, monthAvgTempMax = month(data).monthAvgTempMax()
    
    yearNo, yearAvgTempMin = year(data).YearAvgTempMin()
    
    date, dayAvgTempMax = day(data).dayAvgTempMax()
    
    #dictData
    dictData = {}
    dictData['Average.Temperature Max'] = avgMaxTemp
    dictData['Average.Temperature Min'] = avgMinTemp
    dictData['Average.Wind.Direction'] =  avgWindDirection
    dictData['Average.Wind.Speed'] = avgWindSpeed

    return dictData, MaxTempofMaxCol, Location, State, MaxStateOccur, count, StateMaxTemp, MTCity, MTLocation, MTCode, MTState, StateMaxWindSpeed, MWSCity, MWSLocation, MWSCode, MWSState, StateMinTemp, MinTCity, MinTLocation, MinTCode, MinTState, StateMinWindSpeed, MinWSCity, MinWSLocation, MinWSCode, MinWSState, monthName, monthAvgTempMax, yearNo, yearAvgTempMin, date, dayAvgTempMax
      

def main():
  argParser = ArgParser()
  args = argParser.parse_args()

  file_path = args.file

  #python dictReader.py -f weather_1_1.csv
  print("The Max Temp from the Max Col with the Location and state is:" , read_csv(file_path)[1:4])
  print("The state that occured for the max times and the count is: ", read_csv(file_path)[4:6])
  print("The Max Temp with their city, location, code and state is: ", read_csv(file_path)[6:11])
  print("The Max Wind Speed with their city, location, code and state is: ", read_csv(file_path)[11:16])
  print("The Min Temp with their city, location, code and state is: ", read_csv(file_path)[16:21])
  result = (read_csv(file_path)[0])
  print("The Min Wind Speed with their city, location, code and state is: ", read_csv(file_path)[21:26])
  print("The max avg Temp with the month is: ", read_csv(file_path)[26:28])
  print("The min avg Temp with the year is: ", read_csv(file_path)[28:30])
  print("The max avg Temp with the date is: ", read_csv(file_path)[30:32])
  export_to_csv('res_file.csv', result)
  
  print("The data exported to res_file.csv is : ", read_result_file('res_file.csv'))

if __name__ == '__main__':
  main()