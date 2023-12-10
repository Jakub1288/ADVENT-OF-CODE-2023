FILE_NAME="input06.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

if __name__=="__main__":
    lines=load_file(FILE_NAME)
    
    list_lines = ([text.split(':') for text in lines.split('\n')])
    
    time=int(''.join([num for num in list_lines[0][1] if num.isdigit()]))    
    distance = int(''.join([num for num in list_lines[1][1] if num.isdigit()]))
    
    possible_ways = 0
    for race in range(1,time):
            hold = race
            time_left = time - race
            distance_reached = hold * time_left
            if distance_reached > distance:
                possible_ways +=1

    print(possible_ways)
    