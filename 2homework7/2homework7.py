# For homework
# Create
# 1 json to text parser
# 2 json to yaml parser
# 3 Yaml to json parser
# 4 Yaml to text parser


# Json to Text
import json
with open("first.json","r") as f:
	data = json.load(f)
with open("json_to_text.txt","w") as f:
	f.write(str(data))
print("The json to txt is saved as   json_to_text.txt  ")


# Json to Yaml
import yaml
with open("first.json","r") as f:
	data = json.load(f)
new = yaml.dump(data)
with open("json_to_yaml.txt","w") as f:
	f.write(str(new))
print("The json to yaml is saved as   json_to_yaml.txt  ")

# Yaml to Json
with open("first.yaml","r") as f:
	data = yaml.load(f)
new = json.dumps(data)
with open("yaml_to_json.txt","w") as f:
	f.write(str(new))
print("The Yaml to Json is saved as   yaml_to_json.txt  ")

# Yaml to text
with open("first.yaml","r") as f:
	data = yaml.load(f)
with open("yaml_to_text.txt","w") as f:
	f.write(str(data))
print("The yaml to text is saved as   yaml_to_text.txt  ")
