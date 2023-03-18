import json
import xml.etree.ElementTree as ET

pages = ET.parse('pages.xml')
root = pages.getroot()

pages_json = {}

for page in root:
    page_name = page.attrib['name']
    page_json = {}
    for element in page:
        element_name = element.attrib['name']
        element_json = {}
        for locator_node in element:
            locator_attributes = locator_node.attrib
            platform = locator_attributes['platform']
            locator_type = locator_attributes['locator_type']
            locator_value = locator_node.text
            platform_locator = {platform: [locator_type, locator_value]}
            if not element_json:
                element_json[element_name] = platform_locator
            else:
                element_json[element_name].update(platform_locator)
        page_json.update(element_json)
    pages_json[page_name] = page_json

print(pages_json)


with open('pages.json', 'w') as f:
    json.dump(pages_json, f, indent=4)
