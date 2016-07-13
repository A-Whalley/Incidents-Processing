import colorama
from colorama import Fore, Back, Style
import csv
import glob, os

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def print_times_to_resolve(service):

    seconds_to_resolve = []

    for resolution_time in service:
        if is_number(resolution_time):
            seconds_to_resolve.append(resolution_time)

    seconds_to_resolve = seconds_to_resolve
    dict = {'Total': 0, '1_minute': 0, '2_minutes': 0, '3_minutes': 0, '4_minutes': 0, '5_minutes': 0, 'Over_5_minutes': 0}
    for duration in seconds_to_resolve:
        if int(duration) >= 0:
            dict['Total'] = dict['Total'] + 1
        if int(duration) <= 60:
            dict['1_minute'] += 1
        if int(duration) <= 120 and int(duration) > 61:
            dict['2_minutes'] += 1
        if int(duration) <= 180 and int(duration) > 121:
            dict['3_minutes'] += 1
        if int(duration) <= 240 and int(duration) > 181:
            dict['4_minutes'] += 1
        if int(duration) <= 320 and int(duration) > 241:
            dict['5_minutes'] += 1
        if int(duration) >= 321:
            dict['Over_5_minutes'] += 1
    return dict

def generate_distribution(filename):
    f = open(filename, 'r')
    file = csv.reader(f)
    file.next()
    result = {}
    for row in file:
        if row[4] in result:
            result[row[4]].append(row[10])
        else:
            result[row[4]] = [row[10]]

    distribution = list()

    for service in result:
        service_dict = {'service': service, 'dist': print_times_to_resolve(result[service])}
        distribution.append(service_dict)
    return distribution

for file in os.listdir("/vagrant"):
    if file.endswith(".csv"):
        print(file)

inputfilename = raw_input('filename: ')

selection = raw_input('Sort Data By: 1 minute(1); 2 minutes(2); 3 minutes(3); 4 minutes(4); 5 minutes(5); Over 5 minutes(6); Total(7)')
if selection == "1":
    sortkey = '1_minute'
elif selection == "2":
    sortkey = '2_minutes'
elif selection == "3":
    sortkey = '3_minutes'
elif selection == "4":
    sortkey = '4_minutes'
elif selection == "5":
    sortkey = '5_minutes'
elif selection == "6":
    sortkey = 'Over_5_minutes'
elif selection == "7":
    sortkey = 'Total'
else:
    print('incorrect value!')


distribution = generate_distribution(inputfilename)
sortedlist = sorted(distribution, key=lambda  x: x['dist'][sortkey], reverse=True)
for entry in sortedlist:
    colorama.init()
    print (Fore.GREEN + entry['service'] + Style.RESET_ALL)
    print "   1 minute:       ", entry['dist']['1_minute']
    print "   2 minutes:      ", entry['dist']['2_minutes']
    print "   3 minutes:      ", entry['dist']['3_minutes']
    print "   4 minutes:      ", entry['dist']['4_minutes']
    print "   5 minutes:      ", entry['dist']['5_minutes']
    print "   Over 5 minutes: ", entry['dist']['Over_5_minutes']
    print Fore.CYAN, "  Total:         ", Fore.RED, entry['dist']['Total'], Style.RESET_ALL
