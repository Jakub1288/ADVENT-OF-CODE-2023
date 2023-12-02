FILE_NAME="input.txt"

def load_file(file_name):
    file=open(file_name, "r")
    lines=file.readlines()
    return lines

def digit_lines_list(lines):
    digit_lines=[]
    for line in lines:
        s=''.join(x for x in line if x.isdigit())
        digit_lines.append(int(s))
    return digit_lines
    
if __name__=="__main__":
    lines=load_file(FILE_NAME)
    digit_lines=digit_lines_list(lines)
    print (digit_lines)
    final_numbers=[]
    for digit_line in digit_lines:
        lst=[int(x) for x in str(digit_line)]
        concatenated_numbers= str(lst[0]) + str(lst[-1])
        final_numbers.append(int(concatenated_numbers))
        final_sum=(sum(final_numbers))
    print(final_sum)