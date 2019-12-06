#!/usr/bin/env python

# Prior to running the below script run the below command to download the ip-ranges.json file from Amazon
#curl https://ip-ranges.amazonaws.com/ip-ranges.json > ip-ranges.json

import json
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "ip-ranges.json")) as file:
     json_text =  file.read()

     json_data = json.loads(json_text)

# Loop through the ip prefixes in the JSON data and print out each
# record.
     for prefix in json_data["prefixes"]:
       #use the below if statement to filter, below is based on showing all the global cloudfront ip addresses
       if prefix["region"] == "GLOBAL" and prefix["service"] == "CLOUDFRONT":
         #Use the below to show the prefix info, choose as required
          print (prefix["ip_prefix"])
#         print (prefix["region"])
#         print (prefix["service"])
