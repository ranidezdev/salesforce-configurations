import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def calculate_depth_and_dependencies_xml(node, depth=0):
    current_depth = depth + 1
    max_depth = current_depth
    total_dependencies = len(node)  

    for child in node:
        child_depth, child_dependencies = calculate_depth_and_dependencies_xml(child, current_depth)
        max_depth = max(max_depth, child_depth)
        total_dependencies += child_dependencies 

    return max_depth, total_dependencies


def calculate_depth_and_dependencies_html(node, depth=0):
    current_depth = depth + 1
    max_depth = current_depth
    total_dependencies = len(node.find_all(recursive=False))  

    for child in node.find_all(recursive=False): 
        if child.name is not None:  
            child_depth, child_dependencies = calculate_depth_and_dependencies_html(child, current_depth)
            max_depth = max(max_depth, child_depth)
            total_dependencies += child_dependencies  

    return max_depth, total_dependencies


def analyze_file(file_path):
    try:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            max_depth, total_dependencies = calculate_depth_and_dependencies_xml(root)
            file_type = "XML"
        except ET.ParseError:
            with open(file_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
                max_depth, total_dependencies = calculate_depth_and_dependencies_html(soup)
                file_type = "HTML"

        return file_type, max_depth, total_dependencies
    except Exception as e:
        print(f"Fehler beim Laden oder Parsen der Datei: {e}")
        return None, None, None


if __name__ == "__main__":
    file_path = "Configuration_Example_Queue.queue-meta.xml" 
    file_type, max_depth, total_dependencies = analyze_file(file_path)
    
    if file_type is not None:
        print(f"Dateityp: {file_type}")
        print(f"Maximale Verschachtelungstiefe: {max_depth}")
        print(f"Anzahl von Abhängigkeiten: {total_dependencies}")
