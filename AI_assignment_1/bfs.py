# bfs


class chess:
    def __init__(self, n):
        self.queen = [0 for i in range(n+1)]
        self.level = 0

    def copy_queen(self, parent):
        for i in range(len(parent)):
            self.queen[i] = parent[i]


# 체스판의 (x,y) 좌표에 퀸을 놓아도 될 지
def is_ok(queen, x, y):
    for y_ in range(1, y):  # 각 column별 퀸이 나를 잡아먹을지
        x_ = queen[y_]
        if x_ == x:
            return False
        elif abs(y-y_) / abs(x-x_) == 1:
            return False
    return True


def write(N, queen):
    filename = [str(N), '_bfs_output.txt']
    filename = "".join(filename)
    print(filename)
    output = open(filename, "w")
    for i in queen:
        output.write(str(i))
        output.write(' ')
    output.close()


def bfs(N):
    q = []

    for i in range(1, N+1):
        board = chess(N)
        board.queen[1] = i
        board.level = 1
        if N == 1:
            board.queen.pop(0)
            write(N, board.queen)
            return
        else:
            q.append(board)

    while len(q) != 0:
        board = q.pop(0)

        for i in range(1, N+1):     # level번째 column의 i번째 row에 퀸을 추가할 수 있을 것인가?
            child = chess(N)
            child.level = board.level + 1
            child.copy_queen(board.queen)

            if is_ok(child.queen, i, child.level):
                child.queen[child.level] = i

                if child.level == N:
                    child.queen.pop(0)
                    write(N, child.queen)
                    return
                else:
                    q.append(child)

    filename = [str(N), '_bfs_output.txt']
    filename = "".join(filename)
    print(filename)
    output = open(filename, "w")
    output.write("no solution")
    output.close()

