python3 location_json_to_txt.py >> locations.txt
cat locations.txt | sort | uniq > locations.txt.2
mv locations.txt.2 locations.txt
