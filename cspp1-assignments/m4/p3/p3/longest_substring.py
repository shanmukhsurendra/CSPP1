'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the
letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
@author:shanmukhsurendra

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that
you move on to a different part of the course.
If you have time, come back to this problem after
 you've had a break and cleared your head.'''

def main():

    '''
    In the case of ties, print the first substring.
    For example, if s = 'abcbcd', then your program should print
    Longest substring in alphabetical order is: abc
    @author:shanmukhsurendra
    '''
    in_str = input()
    te_str = ""
    for i in range(len(in_str)-1):
        sub_st = in_str[i]
        while i+1 < len(in_str) and in_str[i] <= in_str[i+1]:
            i += 1
            sub_st += in_str[i]
        if len(sub_st) > len(te_str):
            te_str = sub_st
    print(te_str)

if __name__ == "__main__":
    main()
