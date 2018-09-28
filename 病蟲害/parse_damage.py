
# damage = {}
    # damage[row['拉丁科別']] = row['中文科別']
data = r.json()
# for row in data:
for row in data:
import json
import requests
# print(json.dumps(damage, indent=4, sort_keys=True, ensure_ascii=False))
    print(row['作物名稱'])
r = requests.get('http://data.coa.gov.tw/Service/OpenData/AgriculturalPests.aspx')
