import random


def climbing(queen):
    N = len(queen)-1
    now_h = heuristic(queen, queen[1], 1)
    if now_h == 0:
        return 0    # global minimum 도착!

    min_h = 987654321
    min_x = 0; min_y = 0
    heu_board = [[0 for i in range(N+1)] for j in range(N+1)]

    # (x, y)에 퀸을 놓았을 때 서로 얼마나 잡아먹는가
    for y in range(1, N+1):
        for x in range(1, N+1):
            heu_board[x][y] = heuristic(queen, x, y)

    # heuristic 값이 최소가 되는 지점을 찾자
    for i in range(1, N+1):
        for j in range(1, N+1):
            if min_h > heu_board[i][j]:
                min_h = heu_board[i][j]
                min_x = i; min_y = j

    # 원래보다 더 나아지지 못하는 상태에 도달했다면
    if now_h <= min_h:
        return -1    # 글렀다고 알려주자

    # 아니라면 heuristic 값이 최소가 되는 지점으로 퀸을 옮기자
    queen[min_y] = min_x
    return min_h    # 혹시 global minimum에 도착했어도 무리없이 결과 알려줌


# (x, y)에 퀸을 놓았을 때 서로 얼마나 잡아먹는가
def heuristic(queen, x, y):
    N = len(queen)-1
    new_queen = [i for i in queen]
    new_queen[y] = x
    h = 0   # return 할 값.

    # i번째 column이 j번째 column을 잡아먹는가
    for i in range(1, N):
        for j in range(i+1, N+1):
            y = i; x = new_queen[i]
            y_ = j; x_ = new_queen[j]

            if x == x_:
                h = h+1
            elif abs(y - y_) / abs(x - x_) == 1:
                h = h+1
    return h


def write(N, queen):
    filename = [str(N), '_hc_output.txt']
    filename = "".join(filename)
    print(filename)
    output = open(filename, "w")
    for i in queen:
        output.write(str(i))
        output.write(' ')
    output.close()


def hc(N):
    if N == 2 or N == 3:
        filename = [str(N), '_hc_output.txt']
        filename = "".join(filename)
        print(filename)
        output = open(filename, "w")
        output.write("no solution")
        output.close()
        return

    while True:
        # 시작은 랜덤으로
        queen = [i for i in range(1, N + 1)]
        random.shuffle(queen)
        queen.insert(0, 0)
        flag = False

        # local minimum에 도달할 때까지 climbing
        while True:
            climbing_result = climbing(queen)
            if climbing_result == 0:
                flag = True
                break
            elif climbing_result == -1:
                break   # climbing을 못하고 있으면 local minimum에 도달한거임. break

        if flag:
            queen.pop(0)
            write(N, queen)
            break

