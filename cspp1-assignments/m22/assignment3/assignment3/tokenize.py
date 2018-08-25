'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    lis1_t = []
    lis2_t = []
    charcter = '":,.'
    dic_t = {}
    for word in string:
        for letter in charcter:
            if charcter in word:
                word = word.replace(letter, '')
        lis1_t.append(word)
    for line in lis2_t:
        for words in line:
            if words not in dic_t:
                dic_t[words] = 1
            else:
                dic_t[words] += 1
    return dic_t
            
def main():
    lis_t = []
    n_n = int(input())
    for i in range(n_n):
        string = input()
        lis_t.append(string)
    print(tokenize(lis_t))

if __name__ == '__main__':
    main()
