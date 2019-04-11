import xml.etree.ElementTree as ET

def formatQuestion(text):
    return text.lower().capitalize() + '?'

tree = ET.parse('R.U.R..aiml')
root = tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
questions = []
for child in root.iter('category'):
    for childd in child:
        if(childd.tag == "pattern"):
            questions.append(formatQuestion(childd.text))
            
for question in questions:
    print ("{ 'text': '" + question + "', 'intent': '', 'entities': [] },")


