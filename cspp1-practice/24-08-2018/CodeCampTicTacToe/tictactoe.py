# def valid_matrix(read_m):
#     for i in range(3):
#         for j in  range(3):
#             for k in range(3):

def valid_input(read_m):
    co = 0
    cou = 0
    coun = 0
    count = 0
    for i in range(3):
        for j in range(3):
            if read_m[i][j] == 'x':
                co += 1 
            elif read_m[i][j] != 'o':
                cou += 1
            elif read_m[i][j] != '.':
                coun += 1
            else:
                count += 1
    if count >= 1:
        return "invalid input"
    elif co > 5 or cou > 5:
        return "invaid game"


def read_matrix():
    tic_tac_toe = []
    for i in range(3):
        lis_t = input().split(" ")
        tic_tac_toe.append(lis_t)
    return tic_tac_toe

def main():
    read_m = read_matrix()
    print(valid_matrix(read_m))
main()