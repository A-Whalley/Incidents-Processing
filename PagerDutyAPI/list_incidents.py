#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json
import pprint
import datetime

# Update to match your API key
API_KEY = '#'

# Update to match your chosen parameters
SINCE = ''
UNTIL = ''
DATE_RANGE = ''
STATUSES = []
INCIDENT_KEY = ''
SERVICE_IDS = []
TEAM_IDS = []
USER_IDS = []
URGENCIES = []
TIME_ZONE = 'UTC'
SORT_BY = []
INCLUDE = []

limitvalue = 100
def get_url(offsetvalue): #, queryserviceid):
    return 'https://api.pagerduty.com/incidents?total=true&limit=' + str(limitvalue) + '&offset=' + str(offsetvalue) + '&statuses%5B%5D=resolved&service_ids%5B%5D=PUPGFY0'# + str(queryserviceid)

#def get_incidents_for_service(serviceid):
    #list_incidents(serviceid)

def get_date(date_time):
    return datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%SZ")

def get_sec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

def list_incidents():
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY
    }
    payload = {
        'since': SINCE,
        'until': UNTIL,
        'date_range': DATE_RANGE,
        'statuses': STATUSES,
        'incident_key': INCIDENT_KEY,
        'service_ids': SERVICE_IDS,
        'team_ids': TEAM_IDS,
        'user_ids': USER_IDS,
        'urgencies': URGENCIES,
        'time_zone': TIME_ZONE,
        'sort_by': SORT_BY,
        'include': INCLUDE
    }

    offsetby = 0

    r = requests.get(get_url(offsetby), headers=headers)
    pprint.pprint('Status Code: ' + str(r.status_code))
    incidents = r.json()['incidents']
    pprint.pprint((r.json()['limit'], r.json()['offset'], r.json()['more'], r.json()['total']))
    while r.json()['more'] == True:
        offsetby = offsetby + limitvalue
        print(r.json()['limit'], r.json()['offset'])
        r = requests.get(get_url(offsetby), headers=headers)
        incidents = incidents + r.json()['incidents']
    for incident in incidents:
        creation_time = incident['created_at']
        #pprint.pprint(incident['id'])
        resolution_time = incident['last_status_change_at']

        #time1
        #2015-11-10T01:02:52Z
        #0123_56_89____45_78_
        resolution_datetime = get_date(resolution_time)
        creation_datetime = get_date(creation_time)
        time_to_resolve_str = get_sec(str(resolution_datetime - creation_datetime))
        time_to_resolve = int(time_to_resolve_str)
        print('resolved in:', time_to_resolve, 'seconds')
        #print('created at:  ', creation_datetime)
        #resolution_datetime.utcfromtimestamp(0)
        #time1 = (resolution_time[0:4], resolution_time[5:7], resolution_time[8:10], + resolution_time[14:16], resolution_time[17:19])
        #time1 = tuple(map(int, time1))
        #print(time1)
        #time1 = datetime.datetime(time1)
        #time2 = (creation_time[0:4], creation_time[6:7], creation_time[9:0], creation_time[15:16], creation_time[18:19])
        #time2 = int(time2)
        #time2 = datetime.datetime(time2)
        #time1_seconds = (time1-datetime.datetime(1970,1,1)).total_seconds()
        #time2_seconds = (time2-datetime.datetime(1970,1,1)).total_seconds()
        #time_to_resolve = time1_seconds - time2_seconds
        #print(time_to_resolve)
        #time_to_resolve = resolution_time - creation_time
        print(incident['id'])#, time_to_resolve)

if __name__ == '__main__':
    list_incidents()
