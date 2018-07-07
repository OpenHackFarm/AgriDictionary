# http://data.coa.gov.tw/Service/OpenData/AgriculturalPests.aspx

import json

f = open('AgriculturalPests.aspx')
data = json.load(f)

pests = {}

for d in data:
    family = d['中文科別'].strip()
    specie = d['害蟲中文名'].strip()

    if family and family != specie:
        if family not in pests:
            pests[family] = []

        if specie not in pests[family]:
            pests[family].append(specie)

#print(pests)

print(json.dumps(pests, indent=4, sort_keys=True, ensure_ascii=False))
