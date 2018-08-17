'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def get_frequency(lis_t, lis2_t):
    freq_dict = {}
    for i in lis_t:
        if i in freq_dict:
            freq_dict[i][0] += 1
        else:
            freq_dict[i] = [1]
        freq_dict[i].append(0)
    for i in lis2_t:
        if i in freq_dict:
            freq_dict[i][1] += 1
        else:
            freq_dict[i] = [0, 1]
    return freq_dict


def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    stop_words = {}
    lis_t = []
    lis2_t = []
    input1_list = ((re.sub(r'[^\w\s]','', dict1)).lower()).split()
    input2_list = ((re.sub(r'[^\w\s]','', dict2)).lower()).split()
    #print(input1_list)
    stop_words = load_stopwords("stopwords.txt")
    #print(stop_words)
    for i in input1_list:
        if i not in stop_words:
            lis_t.append(i)
    for i in input2_list:
        if i not in stop_words:
            lis2_t.append(i)
    word_freq = get_frequency(lis_t, lis2_t)
    number = 0
    d_1d = 0
    d_2d = 0
    for k in word_freq:
        number += word_freq[k][0]*word_freq[k][1]
        d_1d += word_freq[k][0]**2
        d_2d += word_freq[k][1]**2
    return abs((number/ (math.sqrt(d_1d) * math.sqrt(d_2d))))

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
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
