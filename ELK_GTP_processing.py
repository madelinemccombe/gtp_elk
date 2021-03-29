#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:27:28 2021

@author: mmccombe
"""

# Copyright (c) 2020 Palo Alto Networks
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Authors: Madeline McCombe <mmccombe@paloaltonetworks.com>

##############################################################################
# import packages
import eland as ed
import datetime as dt

# change these to match your ELK IP/index name
ip_address = '127.0.0.1'
index_name = 'gtp-*'
minute_interval = 15


# accessing index in lab ELK stack
ed_df = ed.DataFrame(ip_address, index_name)

# locate most recent 15 minute sample
sample_end = ed_df['Receive Time'].max()
sample_start = sample_end - dt.timedelta(minutes = minute_interval)
sample_end = sample_end.strftime('%Y/%m/%d %H:%M:%S')
sample_start = sample_start.strftime('%Y/%m/%d %H:%M:%S')

# query for time range
ed_sample = ed_df.es_query({"query": {"range": {"Receive Time": {"gte": sample_start, "lte": sample_end}}}})
sample_size = ed_sample.shape[0]
print('#################################################################################')
print(f'Pulling data from {sample_start} to {sample_end}, which is {sample_size} entries')
print('################################################################################# \n')

# group by IMSI/IMEI and find counts
IMSI_IMEI_groups = ed_sample.groupby(['Tunnel ID/IMSI','Monitor Tag/IMEI']).count()
#print('# of times pair appears | count \n', IMSI_IMEI_groups.tags.value_counts())
IMSI_IMEI_groups = IMSI_IMEI_groups.tags.reset_index()

# finding # of IMEI's/devices paired with each IMSI
IMSI_counts = IMSI_IMEI_groups['Tunnel ID/IMSI'].value_counts()

print('#################################################################################')
print('IMSI | # of IMEIs paired')
print(IMSI_counts.head(15))
print('################################################################################# \n')

print('#################################################################################')
print('Number of IMSIs paired with more than one IMEI:', sum(IMSI_counts>1))
print('Number of IMSIs paired with more than two IMEIs:', sum(IMSI_counts>2))
print('################################################################################# \n')

# digging into problematic IMSIs
problem_IMSIs = list(IMSI_counts[IMSI_counts>1].index)
print('#################################################################################')
print('These are the IMSIs that match to 2 or more devices in this timeframe')
print(problem_IMSIs)
print('#################################################################################')
