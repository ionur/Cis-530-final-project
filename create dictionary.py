import xml.etree.ElementTree as ET
import os
import json

def readXml(path):
    field_to_tag = {}
    for filename in os.listdir(path):
        # parse an xml file by name
        tree = ET.parse(path+'/'+filename)
        root = tree.getroot()
        tags = root[1]
        text = root[0].text.split('\n')

        item_to_tag ={}

        for child in tags:
            tag = child.attrib
            start = int(tag['start'])
            end = int(tag['end'])
            type = tag['TYPE']
            name = root[0].text[start:end]
            item_to_tag[name] = type

        for line in text:
            splits = line.split(':')

            if len(splits) == 2:
                trimmed_name = splits[1][:-1].strip()
                if trimmed_name in item_to_tag.keys():
                    field_to_tag[splits[0].strip()] = item_to_tag[trimmed_name]
            elif len(splits) == 3:
                second_split=splits[1].rsplit(' ',1)
                item1 = second_split[0].strip()
                item2= second_split[1].strip()
                trimmed_name = splits[2][:-1].strip()
                if item1 in item_to_tag.keys():
                    field_to_tag[splits[0].strip()] = item_to_tag[item1]
                if trimmed_name in item_to_tag.keys():
                    field_to_tag[item2] = item_to_tag[trimmed_name]
    return field_to_tag

field_dict=readXml('data/train/xml');
# with open('result.txt','w') as f:
#     json.dump(field_dict,f)