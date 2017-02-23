# WeatherData_extraction
About the file: final_code.py : Extracts a month data of weather from a website and plots it on a graph

Python v3

Website Used for data extraction : http://www.accuweather.com/en/in/saket/2999619/february-weather/2999619?monyr=2/1/2017&view=table

Various Python Libraries Used :
Requests
Matplotlib
BeautifulSoup

About the file : past_asr_weather.py
It is a script with which we can extract data of as many past years as we want (until and unless it is available at "https://www.timeanddate.com/weather/india/amritsar/")(by changing the variables m and y in the script).The sample output of this script are shown in 3 png files named 'High_Temp.png', 'Low_Temp.png', 'Average_Temp.png'

About the file : weather_underground_api
/www.wunderground.com's API is used to get weather data in json format. The data is parsed, filtered and plotted on graph such that graph shows 10 days forecast consiting of HIGH and LOW temperature. 'forecast_10_days.png' is the sample output of this script.
