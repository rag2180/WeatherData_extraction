import urllib3
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time

http = urllib3.PoolManager()

def get_current_temp(city):
	f = http.request('GET','http://api.wunderground.com/api/ae958626c5664e55/conditions/q/india/{0}.json'.format(city))
	#print(f)
	data = f.data.decode('utf-8')
	#print(data)
	#print("\n")
	data = json.loads(data)
	#print(data)
	#print("\n")
	location=data['current_observation']['display_location']
	#print(location['city'],location['state_name'])
	location=location['city']
	temp = data['current_observation']['temp_c']
	print("Current temperature is %s at %s " %(temp,location))

def forecast(city):
	forecast = http.request('GET','http://api.wunderground.com/api/ae958626c5664e55/forecast10day/lang/q/India/{0}.json'.format(city))
	data=forecast.data.decode('utf-8')
	#print(data)
	#print("\n")
	data_json = json.loads(data)
	#print(data_json)
	#print(type(data_json)) #A dictionary
	#print("\n")
	d = data_json['forecast']['simpleforecast']
	#print(d)
	#print("\n")
	#print(d['forecastday'])
	#print("\n")
	#print("\n")
	low=[]
	high=[]
	date=[]
	month=[]
	epoch=[]
	for x in d['forecastday']:
		date_full=x['date']
		epoch1 = date_full['epoch']
		date1=date_full['day']
		month1=date_full['month']
		month_name=date_full['monthname']
		low_temp=x['low']
		high_temp=x['high']
		low_c=low_temp['celsius']
		high_c=high_temp['celsius']
		low.append(low_c)
		high.append(high_c)
		epoch.append(epoch1)
		epoch = list(map(int, epoch))
	return epoch,high,low

def make_df(date,high,low):
	weather_forecast=pd.DataFrame({
	'date':date,
	'high_temp':high,
	'low_temp':low
	})
	weather_forecast=weather_forecast.set_index(weather_forecast['date'])
	return weather_forecast
		
def plot_forecast(df,city):
	print(df)
	df['high_temp']=pd.to_numeric(df['high_temp'])
	df['low_temp']=pd.to_numeric(df['low_temp'])
	df.plot(grid=True)
	#legend_high, = plt.plot(date,high)
	#legend_low, = plt.plot(date,low)
	#plt.legend([legend_high,legend_low],["HIGH","LOW"])
	#plt.xticks(date)
	plt.xlabel("Date")
	plt.ylabel("Temperature(celcius)")
	plt.title("NEXT 10 DAYS TEMPERATURE FORECAST OF {0}".format(city))
	print("DONE")
	plt.show()
	
city='Amritsar'
epoch,high,low=forecast(city)
epoch = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)) for x in epoch]
date = [x.rpartition(' ')[0] for x in epoch]
weather_forecast = make_df(date,high,low)
plot_forecast(weather_forecast,city)