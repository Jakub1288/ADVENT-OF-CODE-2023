from collections import defaultdict #Lze nastavit value na 0. Klasický dict pouze na None
FILE_NAME="input04.txt"

def load_file(file_name):
    file=open(file_name, "r")
    lines=file.readlines()
    return lines



if __name__=="__main__":
    lines=load_file(FILE_NAME)

    counter = defaultdict(int)
    
    for line in lines:
        tmp=line.split(':')
        card_number = int(tmp[0].split()[1])
        counter[card_number] +=1
        all_numbers = tmp[1]
        numbers = all_numbers.split('|')
        winning_numbers = numbers[0].split()
        your_numbers = numbers[1].split()
        
        copies = 0
        for number in your_numbers:
            if number in winning_numbers:
                copies +=1
        for i in range(1, copies+1):
            counter[card_number + i] += counter[card_number]
    
    print (sum(counter.values()))
        
   