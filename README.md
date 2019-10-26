
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


<img width="386" alt="Screen Shot 2019-10-26 at 4 57 15 PM" src="https://user-images.githubusercontent.com/39345855/67625851-bcf7ce00-f811-11e9-9661-afd5f82a82be.png">





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

