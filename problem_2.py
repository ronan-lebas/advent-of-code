def isSafe(report):
    c = (report == sorted(report) or report == sorted(report, reverse=True)) and [1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1)] == [True for _ in range(len(report) - 1)]
    return c

def solve1(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        reports = []
        for line in lines:
            reports.append(list(map(int, line.split(' '))))
    c = 0
    for report in reports:
        if isSafe(report):
            c+= 1
    return c

def solve2(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        reports = []
        for line in lines:
            reports.append(list(map(int, line.split(' '))))
    c = 0
    for report in reports:
        cond = isSafe(report)
        for i in range(len(report)):
            cond = cond or isSafe(report[:i] + report[i+1:])
        c += 1 if cond else 0
    return c


if __name__ == '__main__':
    print(solve1('input_2.csv'))
    print(solve2('input_2.csv'))