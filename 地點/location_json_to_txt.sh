python3 location_json_to_txt.py >> location.txt
cat location.txt | sort | uniq > location.txt.2
mv location.txt.2 location.txt
