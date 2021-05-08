# network-analysis-sample-snippets

This repo contains two sample python scripts, `count-ap.py` and `analyze-pings.py`.

## Requirements
1. Python v3.5+
2. `pandas` (to install, run `pip install pandas`)

## count-ap.py
The first script, `count-ap.py`, takes as input a CSV file found in the same directory as itself, and count the different access points names between a start date and an end date.

To use the script, after cloning the repo, run the following command:
```
python ./count-ap.py XCC_StationEventsLog.csv 5C:A8:6A:8E:66:7A --start "May 5, 2021 7:00:00 PM" --end "May 5, 2021 7:05:00 PM"
```

`python ./count-ap.py --help` will give you further instructions.

## analyze-pings.py
The second script, `analyze-pings.py`, will take an IP address, look for a `.txt.` file with the same name as that IP address in a folder called `wireless-ping`, and report on the success rate, timeout count, outliers, minimum, maximum, average and other statistics.

To use the script, after cloning the repo, run the following command:
```
python .\analyze-pings.py 134.141.123.1
```

`python ./analyze-pings.py --help` will give you further instructions.

