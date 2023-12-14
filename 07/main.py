from collections import Counter
FILE_NAME="input07.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

hand_strange = {'2':1,
                '3':2,
                '4':3,
                '5':4,
                '6':5,
                '7':6,
                '8':7,
                '9':8,
                'T':9,
                'J':10,
                'Q':11,
                'K':12,
                'A':13}

hand_value = {}
card_counter = 1
hand_number=1


if __name__=="__main__":
    lines=load_file(FILE_NAME)
    lines = lines.split('\n')

    for hand in lines:
        used_card=[]

        for card in (hand.split(' ')[0]):
            used_card.append(card)
            print (used_card)

        for letter in used_card:
            counts = [used_card.count(letter) for letter in used_card]

        print (counts)

        if 5 in counts:
            hand_value[hand_number] = 7
        elif 4 in counts:
            hand_value[hand_number] = 6
        elif 3 in counts:
            if 2 in counts:
                hand_value[hand_number] = 5
            else:
                hand_value[hand_number] = 4
        elif counts.count(2) == 4:
            hand_value[hand_number] = 3
        elif 2 in counts:
            hand_value[hand_number] = 2
        else:
            hand_value[hand_number] = 1

           
        print("dalsi ruka")
        hand_number+=1
    print (hand_value)     
    