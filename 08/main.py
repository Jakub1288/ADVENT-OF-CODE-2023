FILE_NAME="input08.txt"

def load_file(file_name):
    file=open(file_name, "r")
    lines=file.read().splitlines()
    return lines

if __name__=="__main__":
    lines=load_file(FILE_NAME)

    instructions = (lines[0])
    instruction_list = [letter for letter in instructions]
   

    map_dict = {}
    for line in lines[2:]:
        split_line = line.split('=')
        key = split_line[0].strip()
        value = (split_line[1].strip())
        value_list = [val.strip() for val in value[1:-1].split(',')]
        map_dict[key] = value_list
   
    taken_value=''
    number_of_steps = 0
    key_for_next_step='AAA'
    
    max_steps=150000
    while taken_value != 'ZZZ' and number_of_steps < max_steps:
        number_of_steps+=1
        item = instruction_list[(number_of_steps - 1) % len(instruction_list)]
        if item == 'L':
            taken_value=map_dict[key_for_next_step][0]
        else:
            taken_value=map_dict[key_for_next_step][1]
        if taken_value == 'ZZZ':
            print ("FINISH!", f'number of steps is {number_of_steps}')
            break
        #print(f"Step: {number_of_steps}, Item: {item}, Taken Value: {taken_value}, Key for Next Step: {key_for_next_step}")
        key_for_next_step = taken_value
    else:
        print("Could not find 'ZZZ' within the maximum steps.")
    
    
    