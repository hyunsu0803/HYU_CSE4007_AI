import bfs
import hc
import csp


def main():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    for line in lines:
        line = line.split()

        if line[1] == "bfs":
            bfs.bfs(int(line[0]))
        elif line[1] == "hc":
            hc.hc(int(line[0]))
        elif line[1] == "csp":
            csp.csp(int(line[0]))
    input_file.close()


if __name__ == "__main__":
    main()
