'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    a_a = ""
    # for letter in string:
    #     if letter in islower():
    #         a_a += letter
    # return a_a
    string = (re.sub(r'[^\w\s]', '', string))
    a_a = string.replace(" ", "")
    return a_a
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
