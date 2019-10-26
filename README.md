# weatherUSA
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


# weatherUSA

This Library allows Developers to Get all weather data based on Zip code in json format 

## Installation

```bash
pip install weatherusa
```
## Usage

```python
import sys
from weatherusa.weatherusa import Weather

obj = Weather()
print(obj.weather_get(zip='06604'))

```


## Authors

* **Soumil Nitin Shah** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

