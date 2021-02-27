#!/usr/bin/env python3
"""
`keyboard` implementation and driver

@author:
"""

def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""

    with open(filename, "r") as r:
        inputcase = int(r.readline())
        for inputs in range(inputcase):
            line = r.readline().split(" ")
            target = line[0]
            total_test = int(line[1])
            scores = {}
            for idx in range(total_test):
                word = r.readline()[:-1]
                score = word_score(target,word)
                if score not in scores.keys():
                    scores[score] = [word]
                else:
                    scores[score].append(word)
            for score_key in scores:
                scores[score_key].sort()
            sorted_keys = sorted(scores)
            for sorted_key in sorted_keys:
                for word in scores[sorted_key]:
                    print(word, sorted_key)


keyboard_dict = {
    1: {"q":1,"w":2,"e":3,"r":4,"t":5,"y":6,"u":7,"i":8,"o":9,"p":10},
    2: {"a":1,"s":2,"d":3,"f":4,"g":5,"h":6,"j":7,"k":8,"l":9},
    3: {"z":1,"x":2,"c":3,"v":4,"b":5,"n":6,"m":7}
}
    
def word_score(target, word):
    score = 0
    for idx in range (len(target)):
        first_letter = target[idx]
        second_letter = word[idx]
        vertical = 0
        horizontal = 0
        row1 = 0
        row2 = 0

        for first_row in keyboard_dict.keys():
            if first_letter in keyboard_dict[first_row].keys():
                row1 = first_row
        
        for second_row in keyboard_dict.keys():
            if second_letter in keyboard_dict[second_row].keys():
                row2 = second_row

        horizontal = abs(keyboard_dict[row1][first_letter] - keyboard_dict[row2][second_letter])
        vertical = abs(row1-row2)

        score += horizontal
        score += vertical  
    
    return(score)
    #scores[sorted_key].sort()

    



def main():
    """Entry point"""
    spell_check("data/projects/keyboard/sample.in")
    


if __name__ == "__main__":
    main()
