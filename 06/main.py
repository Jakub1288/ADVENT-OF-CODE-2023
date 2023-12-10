FILE_NAME="input06.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

if __name__=="__main__":
    lines=load_file(FILE_NAME)
    
    list_lines = ([text.split(':') for text in lines.split('\n')])
    times = [int(num) for num in list_lines[0][1].split() if num.strip().isdigit()]
    distances = [int(num) for num in list_lines[1][1].split() if num.strip().isdigit()]
    race_number = -1
    numbers_to_multiply = []
    result = 1
    for races in times:
        race_number += 1
        possible_ways = 0
        for race in range(1,races):
            hold = race
            time_left = times[race_number] - race
            distance_reached = hold * time_left
            if distance_reached > distances[race_number]:
                possible_ways +=1
        
        numbers_to_multiply.append(possible_ways)
        result *= possible_ways
    print(result)
    