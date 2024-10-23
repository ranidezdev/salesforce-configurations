import re

def parse_diff(diff_file_path):
    with open(diff_file_path, 'r') as file:
        lines = file.readlines()

    hunks = []
    current_hunk = 0
    in_hunk = False

    for line in lines:
        if line.startswith('+ ') or line.startswith('- '):
            current_hunk += 1
            in_hunk = True
        else:
            if in_hunk:
                hunks.append(current_hunk)
                current_hunk = 0
                in_hunk = False

    
    if current_hunk > 0:
        hunks.append(current_hunk)

    return hunks

def calculate_hunk_statistics(hunks):
    if not hunks:
        return 0, 0

    largest_hunk = max(hunks)
    average_hunk_length = round(sum(hunks) / len(hunks))

    return average_hunk_length, largest_hunk

def main(diff_file_path):
    hunks = parse_diff(diff_file_path)
    average_length, largest_hunk = calculate_hunk_statistics(hunks)

    print(f"Durchschnittliche Laenge der Change Hunks: {average_length}")
    print(f"Groeßter Change Hunk: {largest_hunk} Zeilen")

if __name__ == "__main__":
    diff_file_path = "myers_diff.txt"
    main(diff_file_path)
