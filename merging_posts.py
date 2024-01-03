import json
import glob

CHANNEL_NAME = 'zen_of_python'
json_objects = []

# Сольет в один все файлы в текущей директории
for f in glob.glob("*.json"):
    try:
        with open(f, "r", encoding='utf-8') as infile:
            file_content = json.load(infile)
            json_objects.append(file_content)
    except json.JSONDecodeError as e:
        pass

with open(f"{CHANNEL_NAME}.json", "w", encoding='utf-8') as outfile:
    json.dump(json_objects, outfile, ensure_ascii=False, indent=4)