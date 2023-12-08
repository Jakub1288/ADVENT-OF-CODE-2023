FILE_NAME="input04.txt"

def load_file(file_name):
    file=open(file_name, "r")
    lines=file.readlines()
    return lines



if __name__=="__main__":
    lines=load_file(FILE_NAME)
    
    number_of_common_elements_list = []
    
    for line in lines:
        line=line.split(':')
        splitted_lines=line[1]
        splitted_lines_two=splitted_lines.split('|')
        numbers_in_list=[list(map(int, string.split())) for string in splitted_lines_two]
       
        set_0=set(numbers_in_list[0])
        set_1=set(numbers_in_list[1])

        common_numbers = set_0.intersection(set_1)
        number_of_common_elements = sum(min(numbers_in_list[0].count(element), numbers_in_list[1].count(element)) for element in common_numbers)
        
        number_of_common_elements_list.append(number_of_common_elements)
        print (number_of_common_elements_list)
    
    points = [2**(n-1) if n>0 else 0 for n in number_of_common_elements_list]
    print(sum(points))


