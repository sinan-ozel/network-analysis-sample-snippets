"""
This utility counts the access points
that a given MAC address has roamed on.


Usage Example:
python ./count-ap.py XCC_StationEventsLog.csv 5C:A8:6A:8E:66:7A --start "May 5, 2021 7:00:00 PM" --end "May 5, 2021 7:05:00 PM"

"""

from argparse import ArgumentParser, RawTextHelpFormatter
import pandas as pd

parser = ArgumentParser(description=__doc__,
                        formatter_class=RawTextHelpFormatter)
parser.add_argument('LOG_FILE',
                    help='The input file.')
parser.add_argument('MAC_ADDRESS',
                    help='The MAC address of the device.')
parser.add_argument('--start', '--start-time', '-s',
                    help='Start time.')
parser.add_argument('--end', '--end-time', '-e',
                    help='End time.')
args = parser.parse_args()

log = pd.read_csv(args.LOG_FILE)
start_datetime = pd.to_datetime(args.start)
end_datetime = pd.to_datetime(args.end)
log['Time'] = pd.to_datetime(log['Time'])

ap_count = \
    log[
        log['Time'].between(start_datetime, end_datetime)
        & (log['Event Type'] == 'Roam')
        & (log['MAC Address'] == args.MAC_ADDRESS)
    ]\
    ['AP Name'].nunique()
print(f"AP Count for MAC {args.MAC_ADDRESS} between {start_datetime} and {end_datetime}: {ap_count}")
