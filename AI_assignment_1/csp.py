import heapq


class chess:
    def __init__(self, n):
        self.queen = [[0 for i in range(n)] for j in range(n)]
        self.queen.insert(0, [])
        self.confirmed = []
        self.size = n*n

    def copy_chess(self, board):
        for i in range(1, len(board.queen)):
            copy_column = []
            for j in range(len(board.queen[i])):
                copy_column.append(board.queen[i][j])
                self.queen[i] = copy_column
        self.confirmed = [i for i in board.confirmed]

    def get_size(self):
        self.size = 0
        for i in self.queen:
            self.size += len(i)
        return self.size

    def __lt__(self, other):
        return self.get_size() < other.get_size()


def constrain(queen, col, row):
    # col은 index고 row는 값인데 그 column에 row가 하나밖에 없음

    for y in range(1, len(queen)):
        this_column = []
        if y == col:
            continue
        for x in queen[y]:
            if x != row and abs(y-col)/abs(x-row) != 1:
                this_column.append(x)
        queen[y] = this_column


def write(N, queen):
    filename = [str(N), '_csp_output.txt']
    filename = "".join(filename)
    print(filename)
    output = open(filename, "w")
    for i in queen:
        output.write(str(i[0]))
        output.write(' ')
    output.close()


def dfs(parent):
    N = len(parent.queen) - 1

    if len(parent.confirmed) == N:
        parent.queen.pop(0)  # 의미 없는 column 날리고
        write(N, parent.queen)
        return True

    column_length = []
    for col in range(1, len(parent.queen)):
        if col not in parent.confirmed:
            column_length.append(len(parent.queen[col]))
        else:
            column_length.append(98765)

    # most constrained column 고르기
    most_constrained_column = []
    for i in range(len(column_length)):
        if column_length[i] == min(column_length):
            most_constrained_column.append(i+1)

    # 어느 column의 어느 row부터 확정할지 정하자
    Q = []

    for col in most_constrained_column:
        constraining_sum = 0
        board_list = []     # constrain
        for row in parent.queen[col]:
            board = chess(N)    # (col, row)를 확정한 board를 만들고
            board.copy_chess(parent)
            board.queen[col] = [row]
            if col not in board.confirmed:
                board.confirmed.append(col)     # 이 column은 확정됨 + 원래 부모가 확정했던거
            constrain(board.queen, col, row)  # constrain 시키고 size를 return함.
            constraining_sum += board.get_size()
            heapq.heappush(board_list, (-board.get_size(), board))
        heapq.heappush(Q, (constraining_sum, board_list))

    # 확정했다고 치고 recursion 시작
    while len(Q) != 0:
        col = heapq.heappop(Q)[1]

        while len(col) != 0:
            row = heapq.heappop(col)[1]
            OK = True
            for i in row.queen[1:]:
                if len(i) == 0:     # 하나라도 empty set 있으면 안 OK
                    OK = False
                    break
            if OK and dfs(row):
                return True

    return False


def csp(N):
    start = chess(N)
    start.queen = [[i for i in range(1, N+1)] for j in range(N)]
    start.queen.insert(0, [])
    if not dfs(start):
        filename = [str(N), '_csp_output.txt']
        filename = "".join(filename)
        print(filename)
        output = open(filename, "w")
        output.write("no solution")
        output.close()
