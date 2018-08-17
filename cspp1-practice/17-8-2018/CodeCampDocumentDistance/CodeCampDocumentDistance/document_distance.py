'''
    Document Distance - A detailed description is given in the PDF
'''
import re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    stop_words = {}
    input1_dict = ((re.sub(r'[^\w\s]','', dict1)).lower()).split()
    input2_dict = ((re.sub(r'[^\w\s]','', dict2)).lower()).split()
    #print(input1_dict)
    stop_words = load_stopwords("stopwords.txt")
    print(stopwords)
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    j = 0
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = j
            j += 1
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
