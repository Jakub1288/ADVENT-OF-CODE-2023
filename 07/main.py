from dataclasses import dataclass
FILE_NAME="input07.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

hand_strange = {'2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E'}

@dataclass
class Hand:
    cards: str
    value: int
    type: int=-1

if __name__=="__main__":
    lines=load_file(FILE_NAME)
    lines = lines.split('\n')
    hand_value = {}
    hand_number=1

    for hand in lines:
        used_card=[]
        for card in (hand.split(' ')[0]):
            used_card.append(card)
           
        for letter in used_card:
            counts = [used_card.count(letter) for letter in used_card]

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

        hand_number+=1
       
    hands=[]
    iteration_number = 1
    for hand in lines:
        tmp = hand.split(' ')
        hand=Hand(
        cards= ''.join(hand_strange.get(char, char) for char in tmp[0]),
        value=int(tmp[1])) 
        hand.type = hand_value[iteration_number]
        iteration_number+=1
        hands.append(hand)
    
    hands.sort(key=lambda hand: (hand.type, hand.cards))
    result = 0
    for rank, hand in enumerate(hands, 1):
        result += rank * hand.value

    print(result)
        
          