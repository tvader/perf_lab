import argparse
import json

parser = argparse.ArgumentParser(description='Fullfilling first .json with values from the second one')
parser.add_argument('json1', metavar='js1', type=str, help='name of the first .json file')
parser.add_argument('json2', metavar='js2', type=str, help='name of the second .json file')
args = parser.parse_args()

def val_by_id(val_list, id):
	for d in val_list:
		if d["id"] == id:
			return (d["value"])
	return (None)

def merge(list1, list2):
	for v in list1:
		if val_by_id(list2, v["id"]):
			v["value"] = val_by_id(list2, v["id"])
		if "values" in v.keys():
			merge(v["values"], list2)

with open(args.json1) as json1:
	dict1 = json.load(json1)
with open(args.json2) as json2:
	dict2 = json.load(json2)
list1 = dict1["tests"]
list2 = dict2["values"]
merge(list1, list2)
with open("report.json", "w") as res_file:
	json.dump(dict1, res_file, indent=4)
