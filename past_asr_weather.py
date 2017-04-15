import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pylab
import re
import sys

date = []
years = []
months = []
high_temps = []
low_temps = []
avg_temps = []

def past_year_stats(city,month,year):
	date.append(str(month)+'-'+str(year))
	years.append(str(year))
	months.append(str(month))
	page = requests.get("https://www.timeanddate.com/weather/india/{0}/historic?month={1}&year={2}".format(city,month,year))
	soup = BeautifulSoup(page.content,'html.parser')
	all = soup.find('div',class_='eight columns')
	tr1 = all.find_all('td')
	data=[x.get_text() for x in tr1]
	temps = data[0::3]
	high=temps[0]
	low=temps[1]
	avg=temps[2]
	if "°F" in high:
		high_F=int(high.rpartition('°')[0])
		high=(high_F-32)*(5/9)
	else:
		high=high[0:2]
	if "°F" in low:
		low_F=int(low.rpartition('°')[0])
		low=(low_F-32)*(5/9)
	else:
		low=low[0:2]	
	if "°F" in avg:
		avg_F=int(avg.rpartition('°')[0])
		avg=(avg_F-32)*(5/9)
	else:
		avg=avg[0:2]		
	print(year,month,high,low,avg)
	high_temps.append(high)
	low_temps.append(low)
	avg_temps.append(avg)	


def make_df(date,high,low,avg,months,years):
	weather = pd.DataFrame({
	'month-year':date,
	'month':months,
	'year':years,
	'high':high_temps,
	'low':low_temps,
	'avg':avg_temps
	})
	return weather


legend_avg1=[]
legend_print_avg1=[]

def plot_average(year,df):
	plt.figure(1)
	avg=pd.to_numeric(df['avg'])
	month=pd.to_numeric(df['month'])
	legend_avg, = plt.plot(month,avg)
	plt.xticks(month)
	legend_avg1.append(legend_avg)
	legend_print_avg1.append('AVERAGE TEMP-{}'.format(year))
	plt.xlabel("Month")
	plt.ylabel("Temperature(celcius)")
	plt.title("HISTORY OF AMRITSAR AVERAGE TEMPERATURE")
	print("DONE")

legend_high1=[]
legend_print_high1=[]
def plot_high(year,df):
	plt.figure(2)
	high=pd.to_numeric(df['high'])
	month=pd.to_numeric(df['month'])
	legend_high, = plt.plot(month,high)
	plt.xticks(month)
	legend_high1.append(legend_high)
	legend_print_high1.append('HIGH TEMP-{}'.format(year))
	plt.xlabel("Month")
	plt.ylabel("Temperature(celcius)")
	plt.title("HISTORY OF AMRITSAR HIGH TEMPERATURE")
	print("DONE")
	
legend_low1=[]
legend_print_low1=[]
def plot_low(year,df):
	plt.figure(3)
	low=pd.to_numeric(df['low'])
	month=pd.to_numeric(df['month'])
	legend_low, = plt.plot(month,low)
	plt.xticks(month)
	legend_low1.append(legend_low)
	legend_print_low1.append('LOW TEMP-{}'.format(year))
	plt.xlabel("Month")
	plt.ylabel("Temperature(celcius)")
	plt.title("HISTORY OF AMRITSAR LOW TEMPERATURE")
	print("DONE")	

city = sys.argv[1]
start_year = int(sys.argv[2])
end_year = int(sys.argv[3])

while end_year>=start_year:
	m=1
	while m<=12:
		past_year_stats(city,m,start_year)
		m+=1
	start_year+=1

high_temps = list(map(int, high_temps))
low_temps = list(map(int, low_temps))		
avg_temps = list(map(int, avg_temps))

weather = make_df(date,high_temps,low_temps,avg_temps,months,years)
print(weather)
groupby_df=weather.groupby(weather['year'])
for x in list(groupby_df):
	plot_average_test(x[0],x[1])
	plot_average(x[0],x[1])
	plot_high(x[0],x[1])
	plot_low(x[0],x[1])	

plt.figure(1)	
plt.legend(legend_avg1,legend_print_avg1)
plt.figure(2)
plt.legend(legend_high1,legend_print_high1)
plt.figure(3)
plt.legend(legend_low1,legend_print_high1)
plt.show()	
