'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    to count
    '''
    lis1_t = []
    lis2_t = []
    dic_t = {}
    for word in string:
        wo_rd = (re.sub(r'[^\w\s]', '', word))
        lis1_t.append(wo_rd)
    for lin in lis1_t:
        lis2_t.append(lin.split())
    for line in lis2_t:
        for words in line:
            if words not in dic_t.keys():
                dic_t[words] = 0
            dic_t[words] += 1
    return dic_t
def main():
    '''
    main function
    '''
    lis_t = []
    n_n = int(input())
    for i in range(n_n):
        del i
        string = input()
        lis_t.append(string)
    print(tokenize(lis_t))
if __name__ == '__main__':
    main()
