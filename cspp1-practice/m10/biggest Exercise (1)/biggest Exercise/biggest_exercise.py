#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxe = 0
    ans = 0
    for i in aDict:
    	if type(aDict[i]) == list or type(aDict[i]) == tuple:
    		if len(aDict[i]) > maxe:
    			maxe = len(aDict[i])
    			ans = i
    if ans == 0 and amxe ==0:
    	ans = i
    	maxe = 1
    return ans,maxe
def main():
    aDict={}
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['a'].append('dog')
    animals['d'].append('dingo')
    print(biggest(animals))
 


if __name__== "__main__":
    main()