#!/usr/bin/env python

import sys
import json
import urllib

#hash = "this is hash area"
hash= "hash かく"

url= "https://www.virustotal.com/vtapi/v2/file/report"
param = {"resource":hash, "apikey": "自分のapiキーかく"}

data= urllib.urlencode(param)
req=urllib.urlopen(url,data)
json=req.read()
print json
