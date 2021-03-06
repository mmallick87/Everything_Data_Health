'''
Load all records associated with a single drug
Call in command line as follows: python single-drug-all.py DRUGNAME
Matthew Mallick
April 7, 2015
'''

# import module for opening URLs
import urllib2
# import module for working with JSON files
import json
# import module for command line arguments
import sys

#---------------------------------------------------------#

# generate query url using given input parameters
def query(drug_name):
    prefix = "https://api.fda.gov/drug/event.json?api_key=vZC1Gh1XyJl58wZKsMfJifZisDOFRsGBCij3G32v&search=patient.drug.openfda.brand_name:"
    q = "%22"
    return prefix + q + drug_name + q + "w"

#---------------------------------------------------------#

# store command line argument (string for drug name)
drug_name = sys.argv[1]
# load query result in json format
URL = query(drug_name)
j = urllib2.urlopen(URL)
data = json.load(j)
# process data
'''
analyze data here
'''