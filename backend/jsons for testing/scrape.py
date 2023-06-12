import requests
from bs4 import BeautifulSoup


URL = "http://dnd5e.wikidot.com/spells"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results =  soup.find("div", class_="yui-content")

href_list = []
for a_tag in results.find_all('a'):
    href = a_tag.get('href')
    href_list.append(href)

all_spell_list = []

for i in range (0,len(href_list)):
    currUrl = 'http://dnd5e.wikidot.com' + href_list[i]
    spell_page = requests.get(currUrl)
    soup = BeautifulSoup(spell_page.content, "html.parser")
    spell_name = soup.find('div', class_='page-title page-header')
    spell_result = soup.find(id='page-content')

    paragraphs = spell_result.find_all('p')

    newstr = ''
    for p in paragraphs:
        normalized_text = re.sub(r'\s', ' ', p.get_text()).strip()
        newstr+=normalized_text+'\n'

    text = newstr

    lines = text.strip().split("\n")

    source_book = lines[0].split(":", 1)[1].strip()
    school_and_level = lines[1].split(" ")

    if 'cantrip' in school_and_level:
        level = 0
        school = school_and_level[0].strip()
    else:
        level = int(re.search(r'\d+', school_and_level[0]).group())
        school = school_and_level[1].strip()
    casting_time = re.search(r'Casting Time: (\d+) (\w+)', lines[2])
    casting_time_value = int(casting_time.group(1))
    casting_time_unit = casting_time.group(2)

    range_search = re.search(r'Range: (Self \(.*?\)|\d+ \w+|\w+)', lines[2])
    range_parts = range_search.group(1).split()
    if len(range_parts) == 1 or range_parts[0] == 'Self':
        range_value = None
        range_unit = range_parts[0]
    else:
        range_value = int(range_parts[0])
        range_unit = range_parts[1]



    components = re.search(r'Components: (.*?)( \((.*?)\))? Duration:', lines[2])
    component_v = 'V' in components.group(1)
    component_s = 'S' in components.group(1)
    component_m = 'M' in components.group(1)
    material_description = components.group(3) if components.group(3) else None
    description = lines[3]
    upcast = None
    if 'At Higher Levels.' in lines[4]:
        upcast = lines[4].split('At Higher Levels. ')[1].strip()
    classes = re.split(r'\. |: ', lines[-1])[1].replace(' (Optional)', '')

    # Create the dictionary
    spell = {
        "name": re.sub('<[^<]+?>', '', str(spell_name)),
        "level": level,
        "school": school,
        "casting_time_value": casting_time_value,
        "casting_time_unit": casting_time_unit,
        "range_value": range_value,
        "range_unit": range_unit,
        "component_v": component_v,
        "component_s": component_s,
        "component_m": component_m,
        "material_description": material_description,
        "description": description,
        "upcast": upcast,
        "classes": classes,
        "source_book": source_book
    }
    all_spell_list.append(spell)


import json 
json_object = json.dumps(all_spell_list, indent = 4) 

jsonFile = open("data.json", "w")
jsonFile.write(json_object)
jsonFile.close()
