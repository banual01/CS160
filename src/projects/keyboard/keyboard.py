#!/usr/bin/env python3
"""
`keyboard` implementation and driver

@author:
"""

def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""
    
    keyboard_dict = {
        1: {"q":1,"w":2,"e":3,"r":4,"t":5,"y":6,"u":7,"i":8,"o":9,"p":10},
        2: {"a":1,"s":2,"d":3,"f":4,"g":5,"h":6,"j":7,"k":8,"l":9},
        3: {"z":1,"x":2,"c":3,"v":4,"b":5,"n":6,"m":7}
    }
    first_string = "ifpv"
    second_strings = ["iopc", "icpc", "gcpc"]
    
    def word_score(first_string, second_string):
        score = 0
        for idx in range (len(first_string)):
            first_letter = first_string[idx]
            second_letter = second_string[idx]
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

    scores = {}
    for second_string in second_strings:
        score = word_score(first_string,second_string)
        if word_score(first_string,second_string) not in scores.keys():
            scores[score] = [second_string]
        else:
            scores[score].append(second_string)
    sorted_keys = sorted(scores)
    for sorted_key in sorted_keys:
        for word in scores[sorted_key]:
            print(word, sorted_key)




def main():
    """Entry point"""
    spell_check("data/projects/keyboard/sample.in")
    


if __name__ == "__main__":
    main()
