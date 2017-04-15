# WeatherData_extraction

This Repositary contains scripts related to weather data. The following tools/Liberaries are used:

Python v3

Website Used for data extraction : http://www.accuweather.com/en/in/saket/2999619/february-weather/2999619?monyr=2/1/2017&view=table

Various Python Libraries Used :
-Requests
-Matplotlib
-BeautifulSoup

###### Short Description of Scripts:

**1.past_asr_weather.py**

It is a script with which we can extract data of as many past years as we want (until and unless it is available at "https://www.timeanddate.com/weather/india/{city_name}/").The sample output of this script are shown in 3 png files named 'High_Temp.png', 'Low_Temp.png', 'Average_Temp.png'

Use `python past_asr_weather.py amritsar 2012 2015` to plot temperature of city amritsar from year 2012 till 2015.

**2.weather_underground_api**

www.wunderground.com's API is used to get weather data in json format. The data is parsed, filtered and plotted on graph such that graph shows 10 days forecast consiting of HIGH and LOW temperature. 'forecast_10_days.png' is the sample output of this script.

Use `python weather_underground_api.py amritsar` to plot 10 days forecast of city amritsar.
