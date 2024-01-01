from math import gcd
FILE_NAME="input08.txt"

def load_file(file_name):
    file=open(file_name, "r")
    lines=file.read().splitlines()
    return lines
   
  

if __name__=="__main__":
    lines=load_file(FILE_NAME)
    instructions = lines[0]
    

    map_dict = {}
    currents = []

    for line in lines[2:]:
        split_line = line.split('=')
        key = split_line[0].strip()
        value = split_line[1].split(",")
        map_dict[key] = {
        "L": value[0][2:5],
        "R": value[1][:-1].strip()
        }
        
        if key.endswith("A"):
            currents.append(key)

   
    loops = []
    for current in currents:
        loop = []

        counter = 0
        first_goal = None
        while True:
            while counter == 0 or not current.endswith("Z"):
                current = map_dict[current][instructions[counter % len(instructions)]]
                counter +=1
            loop.append(counter)
            if not first_goal:
                first_goal = current
                counter = 0
            elif current == first_goal:
                break
        loops.append(loop)

    loops = [loop[0] for loop in loops]
    lcm = 1
    for i in loops:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)
    
    
 
    