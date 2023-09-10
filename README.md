# Gogle form abuse script
This example of script using for autofill google forms within a given time

## About
The script runs until it fills in all the data from dict, which is stored in `MAP_PATH`.

During the `PERIOD`, a random time is selected to fill in the field. A new time is assigned only after the `PERIOD` expires

## Set up
0) Install the driver for your version of Chrome
1) Create file settings.py for settings:
- `MAP_PATH` - path to map with data
- `DRIVER_PATH` - google driver path
- `URL` - url for autofill
- `PERIOD` - the time during which one filling will be completed
2) Convert data to pickle format from dict (pickle_converter.py)

## Run
```bash
python3 main.py
```

## Requirements
- chromedriver (https://chromedriver.chromium.org/)
- pickle
- selenium
- fake_useragent