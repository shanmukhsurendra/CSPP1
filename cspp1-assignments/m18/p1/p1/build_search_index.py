'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file
import re
FILENAME = "stopwords.txt"
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(docs):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    '''
    lis_t = []
    # docs = ((re.sub(r'[^\w\s]', '', docs)).lower()).split()
    # # print(input1_list)
    # for i in docs:
    #     for word in i:
    #         if i not in stop_words and i not in '1234567890':
    #             lis_t.append(i)
    for i in range(len(docs)):
        lis_t.append((docs[i].lower()).strip())
    

    
    # stop_words = {}
    # stop_words = load_stopwords("stopwords.txt")
    # # lis2_t = []
    # input1_list = ((re.sub(r'[^\w\s]', '', text)).lower()).split()
    # #print(input1_list)
    # # input2_list = ((re.sub(r'[^\w\s]', '', dict2)).lower()).split()
    # for i in input1_list:
    #     if i not in stop_words and i not in '1234567890':
    #         lis_t.append(i)
    # print(lis_t)
    # for i in input2_list:
    #     if i not in stop_words and i not in '1234567890':
    #         lis2_t.append(i)
    # print(lis_t)
    '''
    input1_list = ((re.sub(r'[^\w\s]', '', docs)).lower()).split()
    print(input1_list)
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    
    #print(input1_list[0])
    # dict_empty = {}
    # doc_new = []
    # doc_id = []
    # for i in doc_new:
    #     doc_id.append(doc_new.index(i))
    # print(doc_id)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    search_index = {}
    for index,word in enumerate(docs):
        if word in search_index.key():
            search_index[word].append(index)
        else:
            search_index[word] = [index]
    return search_index



# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    # call print to display the search index
    #word_list(documents)
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
