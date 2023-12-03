FILE_NAME="input02.txt"

def load_file(file_name):
    file=open(file_name, "r")
    lines=file.readlines()
    return lines

def process_games(lines):
    game_id=1
    correct_ids=[]
    powers=[]
    for game in lines:
        max_red=0
        max_green=0
        max_blue=0   
        for char in game.split():
            if char.isdigit():
                current_number=int(char)
                continue
            elif char == 'red' or char == 'red,' or char == 'red;':
                if current_number>max_red:
                    max_red=current_number
            elif char == 'green' or char == 'green,' or char=='green;':
                if current_number>max_green:
                    max_green=current_number
            elif char == 'blue' or char =='blue,' or char=='blue;':
                if current_number>max_blue:
                    max_blue=current_number

        power=(max_red * max_blue * max_green) 
        powers.append(power)
        
        
        if max_red <= 12 and max_green <= 13 and max_blue<=14:
            correct_ids.append(game_id)
        game_id+=1

    print('Sum of powers is: ', sum(powers))
    print('Sum of IDs is: ', sum(correct_ids))


if __name__=="__main__":
    lines=load_file(FILE_NAME)
    process_games(lines)
    
    