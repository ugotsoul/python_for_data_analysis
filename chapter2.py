# coding: utf-8
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()
open(path).readline()
import json
path
open(path, 'rb')
for line in open(path, 'rb')
line for line in open(path, 'rb')
[json.loads(line) for line in open(path, 'rb')]
get_ipython().magic(u'who')
get_ipython().magic(u'history')
records = [json.loads(line) for line in open(path, 'rb')]
records[0]
records[0]['tz']
print records[0]['tz']
time_zones = [line[tz] for line in records]
time_zones = [line['tz'] for line in records]
time_zones = [line['tz'] for line in records if line['tz']]
time_zones = [line['tz'] for line in records if 'tz' in line]
time_zones[0]
