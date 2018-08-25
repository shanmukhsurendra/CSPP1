'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    to replace the values
    '''
    a_a = sorted(dictionary.keys())
    for i_i in a_a:
        print(i_i, "-", '#'*dictionary[i_i])

def main():
    '''
    main function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
