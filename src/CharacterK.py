def PrintList(list_to_print):
    for item in list_to_print:
        print(item)


def Solve(str_list, start, end, index):
    sub_list = [] # holds a list of strings from start to end index
    if start == end:
        sub_list = str_list [start-1]
    else:
        sub_list = str_list[(start-1):end]

    joined_str = str()

    # concat all strings of interest
    for i in sub_list:
        joined_str += i

    char_at_index = joined_str[index-1] # find kth character as per q's
    return char_at_index

if __name__ == "__main__":

    # get input from user
    N = int(input())
    S = []

    for i in range(0, N):
        S.append(str(input()))

    Q = int(input())

    output = [] # results of q's

    for i in range(0, Q):
        L,R,K = map(int, input().split())
        output.append(Solve(S, L, R, K))

    PrintList(output)