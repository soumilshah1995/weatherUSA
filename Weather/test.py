import sys
from weatherusa.weatherusa import Weather

obj = Weather()
print(obj.weather_get(zip='06604'))
print("All modules loaded ")
