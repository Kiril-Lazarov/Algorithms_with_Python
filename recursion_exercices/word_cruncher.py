chars = input().split(', ')
word = input()

ll = []


def compare_chars(start_idx, lll):
    for char in chars:
        if char in word:
            for i in range(len(word)):
                if i == 0 and char == word[i: i + len(char)]:
                    ll.append(char)
                    start_idx = i + len(char)
                    lll.remove(char)
                    compare_chars(start_idx, lll)


compare_chars(0, chars)
print(chars)
