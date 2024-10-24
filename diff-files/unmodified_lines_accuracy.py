from collections import Counter

def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def compare_files(file1_lines, file2_lines):
    file1_lines = [line.strip() for line in file1_lines if line.strip()]
    file2_lines = [line.strip() for line in file2_lines if line.strip()]

    counter_file1 = Counter(file1_lines)
    counter_file2 = Counter(file2_lines)

    matching_count = 0
    for line in counter_file1:
        if line in counter_file2:
            matching_count += min(counter_file1[line], counter_file2[line])

    return matching_count
    
def main(pre_change_file_path, post_change_file_path, diff_file_path):
    file1_lines = load_file(pre_change_file_path)
    file2_lines = load_file(post_change_file_path)
    diff_file_lines = load_file(diff_file_path)
    
    actual_unchanged_lines = compare_files(file1_lines, file2_lines)
    diff_unchanged_lines = compare_files(file1_lines, diff_file_lines)
    percentage_of_lines= (diff_unchanged_lines / actual_unchanged_lines) * 100

    print(f"Anzahl der uebereinstimmenden Zeilen vor und nach Aenderung der Datei: {actual_unchanged_lines}")
    print(f"Anzahl der uebereinstimmenden Zeilen zwischen Datei vor Änderungen und Diff Datei: {diff_unchanged_lines}")
    print(f"Richtig als unveraendert erkannte Zeilen: {percentage_of_lines}%")
    

if __name__ == "__main__":
    pre_change_file_path = "Create_Case_pre_change.flow-meta.xml"
    post_change_file_path = "Create_Case_post_change.flow-meta.xml"
    diff_file_path = "histogram_diff.txt"
    main(pre_change_file_path, post_change_file_path, diff_file_path)