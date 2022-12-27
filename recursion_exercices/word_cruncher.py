chars = input().split(', ')
target = input()

expression = []
phrase_combinations = []


def cycling_thru_chars(curr_target):
    for char in chars:
        if char in curr_target:
            if curr_target.index(char) == 0:
                if char not in expression:
                    expression.append(char)
                    if ''.join(expression) in target:
                        if ''.join(expression) == target:
                            temp = ' '.join(expression)
                            if temp not in phrase_combinations:
                                phrase_combinations.append(temp)
                                print(temp)
                                del expression[-1]
                            else:
                                cycling_thru_chars(curr_target[len(char):])
                                del expression[-1]
                        else:
                            cycling_thru_chars(curr_target[len(char):])
                            del expression[-1]


cycling_thru_chars(target)
