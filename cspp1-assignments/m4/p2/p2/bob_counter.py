'''
@author: shanmukhsurendra
here we print how many time the sub string is repeated in the main string
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''
@author: shanmukhsurendra
here we print how many time the sub string is repeated in the main string
'''
    n_in = input()
    s_s = "bob"
    c_n = 0
    for i_n in range(0, len(n_in) - 2):
        j_n = 0
        k_n = i_n
        v_n = 0
        while(j_n < 3 and n_in[k_n] == s_s[j_n]):
            v_n += 1
            k_n += 1
            j_n += 1
            if v_n == 3:
                c_n += 1
    print(c_n)

if __name__ == "__main__":
    main()
