#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:27:28 2021

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
# installing eland package (two options)

# (1) install requirements.txt (python console)
# pip install -r requirements.txt

# (2) install just eland/elasticsearch (python console)
# pip install eland


##############################################################################
# import packages
import eland as ed

##############################################################################

# change these to match your ELK IP/index name
ip_address = '127.0.0.1'
index_name = 'gtp-*'


# accessing index in lab ELK stack
ed_df = ed.DataFrame(ip_address, index_name)

# pull info about the index (like memory usage)
print(ed_df.info(), '\n')

# find the number of entries in the index
print('There are', ed_df.shape[0], 'entries in this index.\n')

# See the most common event codes
print('The top 10 event_code/count pairs are: \n', ed_df['event_code'].value_counts(), '\n')

