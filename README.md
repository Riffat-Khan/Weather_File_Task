# Weather_File_Task

in this task we've to filter the data based the requirments from the given data

# Folder Structure

argparser folder includes the argparser.py file in which the data is parsed
utils folder consists of multiple .py files in which the requirment based filtering methods are placed within separate classes
export folder includes the write_csv.py file which includes the code for the export of filtered data

main.py is the main file running the main code

# Run main.py

Open the terminal and route to the file location
Then run this command with your arguments 

--file weather_1_1.csv = file name from which the data is being filtered
--start 2016-01-01 = the start point from which the data will start filtering
--end 2016-07-28 = the end point till which the data will be filtered
--city Cordova = Station.City if you want the data for a specific city
--stats max = stats are for either you want min, or max or avg
--stats max, --stats min, --stats avg
--col maxTState = col name is for on which you want to implement the utils
--col avgT, --col maxT, --col minT, --col ws, --col wd, --col count, --col maxTState


python3 main.py --file weather_1_1.csv --start 2016-01-01 --end 2016-07-28 --city Cordova --stats max --col maxTState
