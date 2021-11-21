# fitness_tracking

Whoop Downloader API source: https://github.com/irickman/whoop-downloader

## Create a whoop.ini 
```
[whoop]
username=<your-username>
password=<your-password>
```

## Download .fit file from Wahoo app

## Generate plot
```
pipenv install
pipenv run python3 plot.py 2021-11-20-FITNESS.fit whoop.ini '2021-11-20 18:00:00' '2021-11-20 19:00:00'
```
