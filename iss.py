#!/usr/bin/python

import sys
import time
import datetime
import json
import requests

def public_ip_address():
  r = requests.get("http://ipecho.net/plain")
  return r.text

def current_lat_lng():
  ip = public_ip_address()
  r = requests.get("http://freegeoip.net/json/" + ip)
  data = json.loads(r.text)
  return data['latitude'], data['longitude']

def pass_times(lat, long):
  uri = 'http://api.open-notify.org/iss/'
  r = requests.get('{0}?n=10&alt=80&lat={1}&lon={2}'.format(uri, lat, long))
  return json.loads(r.text)['response']

def duration_to_string(s):
  d = datetime.timedelta(seconds=s)
  times = str(d).split(":")
  return '{0}mins {1}s'.format(times[1], times[2])

lat, long = current_lat_lng()
passes = pass_times(lat, long)

print "Our latitude is " + str(lat)
print "Our longitude is " + str(long)
print "Pass times:"

for iss_pass in passes:
  localtime = time.strftime('%H:%M:%S %Y-%m-%d',time.localtime(iss_pass['risetime']))
  duration = duration_to_string(iss_pass['duration'])
  print 'ISS will pass at {0} and will be visible for {1}'.format(localtime, duration)
