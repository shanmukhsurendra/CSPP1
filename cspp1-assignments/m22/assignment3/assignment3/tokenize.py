'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    lis_t = []
    dic_t = {}
    lis_t = string.split()
    for word in lis_t:
    	if word not in dic_t:
    		dic_t[word] = 1
    	else:
    		dic_t[word] += 1
    return	 dic_t	
            
def main():
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
