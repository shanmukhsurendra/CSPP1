#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    L = []
    count = 0
    print ((aDict.values()))
    for i in aDict.values():
        if type(i) == list or type(i) == tuple:
            L.extend(i)
        else:
            L.extend(i)
    return len(L)
    

def main():
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print(how_many(animals))
if __name__ == "__main__":
    main() 