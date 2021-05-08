f"""
Prints out the minimum and maximum of the timeouts.

The outputs from ping stdout needs to be in a folder
called 'wireless-ping' and named by IP address, for example:
wireless-ping/134.141.123.1.txt


Usage example:
python ./analyze-pings.py 134.141.123.1
"""


from argparse import ArgumentParser, RawTextHelpFormatter
import pandas as pd
import re
import os

parser = ArgumentParser(description=__doc__,
                        formatter_class=RawTextHelpFormatter)
parser.add_argument('ip_address',
                    help='IP Address that was pinged.')
args = parser.parse_args()

ping_times = list()
attempt_count = 0
timeout_count = 0
with open(os.path.join('wireless-ping', args.ip_address + '.txt')) as ping_log_file:
    for line in ping_log_file:
        attempt_count += 1
        m = re.search(r'\[([0-9]+)\s+ms\]$', line)
        if m:
            ping_times.append(int(m[1]))
        elif 'Request timed out.' in line:
            timeout_count += 1



pings = pd.DataFrame({'ping_time': ping_times})
outlier_pings = pings['ping_time'] > pings['ping_time'].quantile(.97)
outlier_count = sum(outlier_pings)
success_rate = round(1 - timeout_count / attempt_count, 2)
print(f"For the IP {args.ip_address}:")
print(f"Success rate: {success_rate} ({timeout_count} timeouts out of {attempt_count})")
print(f"{outlier_count} outliers have been dropped.")
print(f"Minimum, maximum and other descriptive stats for the remaining ping times:")
print(pings[~outlier_pings].describe(percentiles=[.25, .5, .75, .9, .98, .99]))