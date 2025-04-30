import os
import hashlib

def generate_addons_xml(addon_dirs):
    addons = ""
    for d in addon_dirs:
        if os.path.isdir(d):
            with open(os.path.join(d, 'addon.xml'), 'r', encoding='utf-8') as f:
                content = f.read()
                content = content.strip().replace('\n', '').replace('\r', '')
                addons += content
    return f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<addons>\n{addons}\n</addons>"

def write_files():
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, 'addon.xml'))]
    addons_xml = generate_addons_xml(dirs)
    
    with open("addons.xml", "w", encoding='utf-8') as f:
        f.write(addons_xml)

    md5_hash = hashlib.md5(addons_xml.encode('utf-8')).hexdigest()
    with open("addons.xml.md5", "w", encoding='utf-8') as f:
        f.write(md5_hash)

write_files()
