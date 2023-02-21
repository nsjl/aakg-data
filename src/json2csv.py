import sys  
import json

# Example script to read a JSON results file and output
# either perform or effect duration data as CSV file
# in the form title,action,label

# Usage: py json2csv.py <filename> <category> <confidence>
# where confidence = 1, 2, or 3 and catgory = perform or effect

# e.g. py json2csv.py len10-sample.json effect 1
  
with open(sys.argv[1]) as f:
    data = json.load(f)

category = sys.argv[2]

confidence = int(sys.argv[3])  

print("title,action,label")  

for i in data:
    for action in i["actions"]:
        if action[category]["confidence"] == confidence:
            print( i["displaytitle"] + "," + action["description"] + "," + action[category]["period"])


