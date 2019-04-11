import json

# read file
with open('data/data.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

examples = {"test"}
# show values
for example in obj['rasa_nlu_data']['common_examples']:
    if(example != ''):
        #examples.add("  utter_" + example['intent'] + ":")
        examples.add(" - " + example['intent'])
    
for example in (examples):
    print (example)