import re
import json

data = open('input.txt','r').read()

res = re.finditer(r'value="(.*)">(.*)<\/option>', data)
ldict = []
for r in res:
    ldict.append({ 'key': r.group(1), 'value': r.group(2), })



with open('output.json',"w") as f:
    # don't need to ensure ascii
    json.dump(ldict, f, indent=4, ensure_ascii=False)


