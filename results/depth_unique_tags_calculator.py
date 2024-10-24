import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def calculate_depth_and_unique_tags_html(element, current_depth=0, depth_info=None):
    if depth_info is None:
        depth_info = {'max_depth': 0, 'unique_tags': set()}

    depth_info['max_depth'] = max(depth_info['max_depth'], current_depth)

    if element.name and element.name[0].isalpha():
        depth_info['unique_tags'].add(element.name)

    for child in element.find_all(recursive=False):
        calculate_depth_and_unique_tags_html(child, current_depth + 1, depth_info)

    return depth_info

def calculate_depth_and_unique_tags_xml(element, current_depth=1, depth_info=None):
    if depth_info is None:
        depth_info = {'max_depth': 0, 'unique_tags': set()}

    depth_info['max_depth'] = max(depth_info['max_depth'], current_depth)

    depth_info['unique_tags'].add(element.tag)

    for child in element:
        calculate_depth_and_unique_tags_xml(child, current_depth + 1, depth_info)

    return depth_info

def parse_document(file_path, isXML=True):
    try:
        if isXML:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            depth_info = calculate_depth_and_unique_tags_xml(root)
        else:
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')

                depth_info = calculate_depth_and_unique_tags_html(soup)

        max_depth = depth_info['max_depth']
        unique_tags = depth_info['unique_tags']

        print(f"Maximale Verschachtelungstiefe: {max_depth}")
        print(f"Anzahl eindeutiger Tags: {len(unique_tags)}")
        print(f"Eindeutige Tags: {unique_tags}")

    except ET.ParseError as e:
        print(f"Fehler beim Parsen des XML-Dokuments: {e}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


file_path = 'Configuration_Example_Queue.queue-meta.xml'
isXML = False 

parse_document(file_path, isXML)