#!/usr/bin/env python

#python 3.5.2

import sys
import json
import urllib.parse
import urllib.request

hash = "this is hash area"

url= "https://www.virustotal.com/vtapi/v2/file/report"
param = {"resource":hash, "apikey": "自分のapikey"}

data= urllib.parse.urlencode(param)
data= data.encode('ascii')
req=urllib.request.Request(url,data)
with urllib.request.urlopen(req) as res:
	json=res.read()
	print(json)
