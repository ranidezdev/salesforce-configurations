def parse_diff(diff_file):
    with open(diff_file, 'r') as f:
        lines = f.readlines()

    hunks = []
    hunk = {'added': [], 'removed': []}
    inside_hunk = False

    for line in lines:
        if line.startswith('+ ') or line.startswith('- '):
            inside_hunk = True
            if line.startswith('+'):
                hunk['added'].append(line[1:].strip())
            elif line.startswith('-'):
                hunk['removed'].append(line[1:].strip())
        else:
            if inside_hunk:
                hunks.append(hunk)
                hunk = {'added': [], 'removed': []}
                inside_hunk = False

    if inside_hunk:
        hunks.append(hunk)

    return hunks


def check_for_unnecessary_changes(hunks):
    unnecessary_changes = []
    
    for hunk in hunks:
        common_lines = set(hunk['added']).intersection(hunk['removed'])
        if common_lines:
            unnecessary_changes.append(common_lines)

    return unnecessary_changes


def main(diff_file):
    hunks = parse_diff(diff_file)
    unnecessary_changes = check_for_unnecessary_changes(hunks)

    if unnecessary_changes:
        print("Found falsely identified changes in the following lines:")
        for changes in unnecessary_changes:
            for line in changes:
                print(line)
    else:
        print("All unchanged lines were correctly identified.")


if __name__ == "__main__":
    diff_file = "myers_diff.txt" 
    main(diff_file)
