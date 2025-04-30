import os
import hashlib
from xml.etree import ElementTree as ET

addons_folder = '.'
addons = []

for addon in os.listdir(addons_folder):
    if os.path.isdir(addon) and addon.startswith('plugin.'):
        try:
            tree = ET.parse(os.path.join(addon, 'addon.xml'))
            root = tree.getroot()
            addons.append(ET.tostring(root, encoding='utf-8').decode())
        except:
            pass

addons_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n' + '\n'.join(addons) + '\n</addons>'

with open('addons.xml', 'w', encoding='utf-8') as f:
    f.write(addons_xml)

md5_hash = hashlib.md5(addons_xml.encode('utf-8')).hexdigest()
with open('addons.xml.md5', 'w') as f:
    f.write(md5_hash)
