import pyowm

owm = pyowm.OWM('90a4ba7a37daeeb84b8a060070c4e839')  
observation =  owm.weather_at_place('delhi,india')   
w = observation.get_weather()  
temperature = w.get_temperature('celsius')  
tomorrow = pyowm.timeutils.tomorrow()  
wind = w.get_wind()  
#print(w)  
#print('wind speed: '+str(wind['speed']))
#print('wind degree: '+str(wind['deg']))  
#print('Current temp: '+str(temperature['temp'])+ str(' degree cel'))
#print('Max Temp: '+str(temperature['temp_max'])+ str(' degree cel')) 
#print('Min Temp: '+str(temperature['temp_min'])+ str(' degree cel'))  
dict1={'wind speed: ':str(wind['speed']),'CurrentTemp:':str(temperature['temp']),'MaxTemp:':str(temperature['temp_max']),'MinTemp:':str(temperature['temp_min'])}
str1=str(dict1)
dict2=eval(str1)
print(str1)
#print(tomorrow)  
