def valid_matrix(read_m):
    if read_m[0][0] == read_m[0][1] == read_m[0][2] or read_m[0][0] == read_m[1][0] == read_m[2][0] or read_m[0][0] == read_m[1][1] == read_m[2][2]:
        return read_m[0][0]
    elif read_m[1][0] == read_m[1][1] == read_m[1][2]:
        return read_m[1][0]
    elif read_m[2][0] == read_m[2][1] == read_m[2][2]:
        return read_m[2][0]
    elif read_m[2][2] == read_m[1][2] == read_m[0][2] or read_m[2][0] == read_m[1][1] == read_m[0][2]:
        return read_m[2][2]


def valid_input_game(read_m):
    co = 0
    cou = 0
    coun = 0
    count = 0
    for i in range(3):
        for j in range(3):
            if read_m[i][j] == 'x':
                co += 1 
            elif read_m[i][j] == 'o':
                cou += 1
            elif read_m[i][j] == '.':
                coun += 1
            else:
                count += 1
    if count >= 1:
        return (False, "invalid input")
    elif co > 5 or cou > 5 or co == cou == coun == 3:
        return (False, "invalid game")
    return (True,"")


def read_matrix():
    tic_tac_toe = []
    for i in range(3):
        lis_t = input().split(" ")
        tic_tac_toe.append(lis_t)
    return tic_tac_toe

def main():
    read_m = read_matrix()
    tuple_output = valid_input_game(read_m)
    if tuple_output[0] == True:
        print(valid_matrix(read_m))
    else:
        print(tuple_output[1])
main()