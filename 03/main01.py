import string
import re
FILE_NAME="input03.txt"


def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

symbol_position = set()
text = load_file(FILE_NAME)
field=text.split('\n')


for x, row in enumerate(field):
    for y, column in enumerate(row):
        if column.isdigit() or column == '.':
            continue
        symbol_position.add((x,y))

start_of_number = set()

for x,y in symbol_position:
    for tx in range(x-1, x+2):
        for ty in range (y-1, y+2):
            if tx < 0 or tx > len(field) or not field[tx][ty].isdigit():
                continue
            if ty <0 or ty> len(field[tx]) or not field[tx][ty].isdigit():
                continue
            while ty >0 and field[tx][ty - 1].isdigit():
                ty -= 1
            start_of_number.add((tx,ty))

final_numbers=[]
for x,y in start_of_number:
    temp = ''
    while y < len(field[x]) and field[x][y].isdigit():
        temp += field[x][y]
        y+=1
    final_numbers.append(int(temp))

print (sum(final_numbers))