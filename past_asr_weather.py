import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pylab
import re

date = []
years = []
months = []
def temperature(month,year):
	print(month,year)
	date.append(str(month)+'-'+str(year))
	years.append(str(year))
	months.append(str(month))
	hi_lo_avg=[]
	page = requests.get("https://www.timeanddate.com/weather/india/amritsar/historic?month={0}&year={1}".format(month,year))
	#page = requests.get("https://www.timeanddate.com/weather/india/amritsar/historic?month=1&year=2011")
	soup = BeautifulSoup(page.content,'html.parser')
	all = soup.find('div',class_='eight columns')
	tr1 = all.find_all('td')
	data=[x.get_text() for x in tr1]
	temps = data[0::3]
	high=temps[0]
	low=temps[1]
	avg=temps[2]
	print(high,low,avg)
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
	print("OOOOOOOOOKKKKKKKK")	
	print(high,low,avg)
	hi_lo_avg.append(high)
	hi_lo_avg.append(low)
	hi_lo_avg.append(avg)
	return hi_lo_avg

def make_cols_for_df(temps):
	high1.append(temps[0])
	low1.append(temps[1])
	avg1.append(temps[2])
	
def make_df(date,high,low,avg,months,years):
	weather = pd.DataFrame({
	'month/year':date,
	'month':months,
	'year':years,
	'high':high,
	'low':low,
	'avg':avg})
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
	
high1=[]
low1=[]
avg1=[]		
m,y=1,2010
for i in range(5):
	m=0
	for i in range(12):
		m=m+1
		temps=temperature(m,y)
		make_cols_for_df(temps)
	y=y+1

#print(high)
#print(low)
#print(avg)

high1 = list(map(int, high1))
low1 = list(map(int, low1))		
avg1 = list(map(int, avg1))

#print(high)
#print(low)
#print(avg)

df=make_df(date,high1,low1,avg1,months,years)
groupby_df=df.groupby(df['year'])
print(df)
for x in list(groupby_df):
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

