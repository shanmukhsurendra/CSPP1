'''
@author :shanmukhsurendra
This program prints string if one of the given input is string or prints bigger
 if vara > varb or prints equal if vara=varb or print smaller vara<varb
'''
VARA = 5
VARB = 7
if (isinstance(VARA, str)  or isinstance(VARB, str)):
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
elif VARA < VARB:
    print("smaller")
