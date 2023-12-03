import string
import re
FILE_NAME="input03.txt"


def load_file(file_name):
    file=open(file_name, "r")
    lines=file.readlines()
    return lines

def punct_symbols():
    all_punctation=string.punctuation
    result=all_punctation.replace('.', '')
    return result

def extract_adjacent_numbers(lines):
    punctuation = punct_symbols()
    pattern = f"[{re.escape(punctuation)}]\d+|\d+[{re.escape(punctuation)}]"
    
    

    lines = [line.replace('\n', '') for line in lines]
    
    rows = len(lines)
    cols = len(lines[0])
    print(lines)
    print(rows)
    print(cols)
    table = [[lines[i][j] for j in range(cols)] for i in range(rows)]

    adjacent_numbers = []

    for i in range(rows):
        for j in range(cols):
            if lines[i][j].isdigit():
                adjacent_numbers.append(lines[i][j])

            # Check adjacent cells
            if lines[i][j] in punctuation:
                adjacent_cells = [(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2) if
                                  0 <= i + x < rows and 0 <= j + y < cols]
                for cell in adjacent_cells:
                    x, y = cell
                    if lines[x][y].isdigit():
                        adjacent_numbers.append(lines[x][y])

    # Deduplicate and return the adjacent numbers
    return list(set(adjacent_numbers))



if __name__=="__main__":
    lines=load_file(FILE_NAME)
    print(lines)
    our_punct= punct_symbols()
    pattern = f"[{re.escape(our_punct)}]\d+|\d+[{re.escape(our_punct)}]"
    result = extract_adjacent_numbers(lines)
    print(result)
    #print(our_punct)
    