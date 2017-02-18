import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


page = requests.get("http://www.accuweather.com/en/in/saket/2999619/february-weather/2999619?monyr=2/1/2017&view=table")
soup = BeautifulSoup(page.content,'html.parser')

feb_days = soup.find('tbody')
#print(feb_days)

day_tags = feb_days.find_all("th")
day_date = [x.get_text() for x in day_tags]
day = [x[0:3] for x in day_date]
date = [x[6::] for x in day_date]

td_tags = feb_days.find_all("td")
temps = [x.get_text() for x in td_tags]

hi_lo = temps[0::5]
high = [x[0:2] for x in hi_lo]
low = [x[4:6] for x in hi_lo]

avg_hi_lo = temps[4::5] 
avg_hi = [x[0:2] for x in avg_hi_lo]
avg_low = [x[4:6] for x in avg_hi_lo]

weather = pd.DataFrame({
          'Day':day,
	      'Date':date,
          'High Temp':high,
	      'Low Temp':low,
          'Average High':avg_hi,
	      'Average Low':avg_low,
          })

print(weather)

df=weather
high_temp=pd.to_numeric(df['High Temp'])
low_temp=pd.to_numeric(df['Low Temp'])
avg_high_temp=pd.to_numeric(df['Average High'])
avg_low_temp=pd.to_numeric(df['Average Low'])
date = pd.to_numeric(df['Date'])

plt.figure()

legend_high_temp, = plt.plot(date,high_temp)
legend_low_temp, = plt.plot(date,low_temp)
legend_avg_high_temp, = plt.plot(date,avg_high_temp)
legend_avg_low_temp, = plt.plot(date,avg_low_temp)

plt.xticks(date)
plt.legend([legend_high_temp,legend_low_temp,legend_avg_high_temp,legend_avg_low_temp],["HIGH","LOW","AVG HIGH","AVG LOW"])
plt.xlabel("Dates")
plt.ylabel("Temperature")
plt.show()
