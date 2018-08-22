'''
Exercise: int set
Consider the following code from the last lecture video:
'''

class Intset():
    """An Intset is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e_e):
        """Assumes e is an integer and inserts e into self"""
        if not e_e in self.vals:
            self.vals.append(e_e)

    def member(self, e_e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e_e in self.vals

    def remove(self, e_e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e_e)
        except:
            raise ValueError(str(e_e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e_e) for e_e in self.vals]) + '}'

    def __len__(self):
        '''
        length
        '''
        return len(self.vals)

    def intersect(self, other):
        '''
        intersect
        '''
        return [value for value in self.vals if value in other.vals]

# Your task is to define the following two methods for the Intset class:
#   1. Define an intersect method that returns a new Intset containing elements that
#   appear in both sets. In other words,
#      s1.intersect(s2)
#      would return a new Intset of integers that appear
#       in both s1 and s2. Think carefully - what should happen if s1 and s2 have no
#      elements in common?

#   2. Add the appropriate method(s) so that len(s)
#   returns the number of elements in s.

# Hint: look through the Python docs to figure out
#   what you'll need to solve this problem.



def main():
    '''
    main
    '''
    set_a = Intset()
    set_b = Intset()
    data = input()
    data1 = input()
    l_l = data.split()
    l_l = data1.split()
    for i_i in l_l:
        set_a.insert(int(i_i))
    for j_j in l_l:
        set_b.insert(int(j_j))
    print(set_a.intersect(set_b))

if __name__ == "__main__":
    main()
