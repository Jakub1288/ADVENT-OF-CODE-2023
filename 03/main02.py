import string
import re
FILE_NAME="input03.txt"


def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

symbol_position = set()
text = load_file(FILE_NAME)
field=text.split('\n')

result = 0
for x, row in enumerate(field):
    for y, column in enumerate(row):
        if column!= '*':
            continue
        symbol_position.add((x,y))



for x,y in symbol_position:
    start_of_number = set()
    for tx in range(x-1, x+2):
        for ty in range (y-1, y+2):
            if tx < 0 or tx > len(field) or not field[tx][ty].isdigit():
                continue
            if ty <0 or ty> len(field[tx]) or not field[tx][ty].isdigit():
                continue
            while ty >0 and field[tx][ty - 1].isdigit():
                ty -= 1
            start_of_number.add((tx,ty))


    if len(start_of_number) == 2:
        numbers=[]
        for xx,yy in start_of_number:
            temp = ""
            while yy < len(field[xx]) and field[xx][yy].isdigit():
                temp += field[xx][yy]
                yy+=1
            numbers.append(int(temp))
        result += (numbers[0] * numbers[1])
print(result)