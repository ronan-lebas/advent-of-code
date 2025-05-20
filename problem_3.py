import re

def solve1(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        c = 0
        for line in lines:
            matches = re.findall(r"mul\((\d+),(\d+)\)", line)    
            for pair in matches:
                a, b = int(pair[0]), int(pair[1])
                c += a * b
    return c

def solve2(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        c = 0
        enabled = True
        for line in lines:
            matches = re.findall(r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)", line)    
            for pair in matches:
                if pair[0] == 'do()':
                    enabled = True
                elif pair[0] == "don't()":
                    enabled = False
                elif enabled:
                    a, b = int(pair[1]), int(pair[2])
                    c += a * b
    return c

if __name__ == '__main__':
    print(solve1('input_3.txt'))
    print(solve2('input_3.txt'))