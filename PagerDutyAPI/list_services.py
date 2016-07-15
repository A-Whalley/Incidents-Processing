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
import requests
import logging
logging.basicConfig(level=logging.DEBUG)

# Update to match your API key
API_KEY = '1NL53_66v5-9CTqSGRJF'

# Update to match your chosen parameters
TEAM_IDS = []
TIME_ZONE = 'UTC'
SORT_BY = 'name'
QUERY = ''
INCLUDE = []

<<<<<<< HEAD
<<<<<<< HEAD
limitvalue = 50
=======
limitvalue = 100
>>>>>>> 33e804dd46e89fbfbd3fa7fdb1d732e9ff417180
def get_url(offsetvalue):
    return 'https://api.pagerduty.com/services?limit=' + str(limitvalue) + '&offset=' + str(offsetvalue) + '&total=true'

=======
>>>>>>> parent of 74f584a... Some Issues Fixed
def list_services():
    url = 'https://api.pagerduty.com/services'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY
    }
    payload = {
        'team_ids': TEAM_IDS,
        'time_zone': TIME_ZONE,
        'sort_by': SORT_BY,
        'query': QUERY,
        'include': INCLUDE
    }
    r = requests.get(url, headers=headers, params=json.dumps(payload))
    pprint.pprint('Status Code: ' + str(r.status_code))
    services = r.json()['services']
    pprint.pprint((r.json()['limit'], r.json()['offset'], r.json()['more']))
    if r.json()['more'] == True:
            payload['offset'] = r.json()['offset'] + r.json()['limit']
            pprint.pprint(r.json()['limit'])
            pprint.pprint(payload)
            r = requests.get(url, headers=headers, params=json.dumps(payload))
            pprint.pprint(r.json())
            services = services + r.json()['services']
    # pprint.pprint(r.json()['services'][0]['escalation_policy']['summary'])
    for service in services:
        pprint.pprint(service['escalation_policy']['summary'])

if __name__ == '__main__':
    list_services()
