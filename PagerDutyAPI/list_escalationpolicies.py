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

# Update to match your API key
API_KEY = '#'

# Update to match your chosen parameters
QUERY = ''
USER_IDS = []
TEAM_IDS = []
INCLUDE = []
SORT_BY = 'name'
LIMIT = 100

def list_escalation_policies():
    url = 'https://api.pagerduty.com/escalation_policies'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY
    }
    payload = {
        'query': QUERY,
        'user_ids': USER_IDS,
        'team_ids': TEAM_IDS,
        'include': INCLUDE,
        'sort_by': SORT_BY,
    }

    r = requests.get(url, headers=headers, params=json.dumps(payload))
    pprint.pprint('Status Code: ' + str(r.status_code))
    (r.json())
    policies = r.json()['escalation_policies']
<<<<<<< HEAD
    pprint.pprint((r.json()['limit'], r.json()['offset'], r.json()['more'], r.json()['total']))
    while r.json()['more'] == True:
        offsetby = offsetby + limitvalue
        print(r.json()['limit'], r.json()['offset'])
        r = requests.get(get_url(offsetby), headers=headers, params=json.dumps(payload))
        # pprint.pprint(r.json())
        policies = policies + r.json()['escalation_policies']
    # pprint.pprint(r.json()['services'][0]['escalation_policy']['summary'])
    for policy in policies:
<<<<<<< HEAD
        #pprint.pprint(service['escalation_policy']['summary'])
        #pprint.pprint(policy['services'])
        for service in policy['services']:
            pprint.pprint(service['id'])
            incidents = list_incidents.get_incidents_for_service(service['id'])

=======
        #pprint.pprint(policy['name'])
        pprint.pprint(policy['name'])
>>>>>>> 33e804dd46e89fbfbd3fa7fdb1d732e9ff417180
=======
    # r.json()['offset'] = payload['offset']
    pprint.pprint(payload)

    #r.json()['offset'] += r.json
    for policy in policies:
        #pprint.pprint(policy['name'])
        pprint.pprint(policy['id'])
>>>>>>> parent of 74f584a... Some Issues Fixed

if __name__ == '__main__':
    list_escalation_policies()
