'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dic_t = {}
    for word in lis_t:
      for words in word:
        if words not in dic_t:  
          dic_t[word] = 1
      else:
          dic_t[word] += 1
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
