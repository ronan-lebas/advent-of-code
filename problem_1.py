def solve(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        list1, list2 = [], []
        for line in lines:
            a = line.split('   ')
            list1.append(int(a[0]))
            list2.append(int(a[1]))
    list1.sort()
    list2.sort()
    distances = []
    for a, b in zip(list1, list2):
        distances.append(abs(a - b))
    return sum(distances)

if __name__ == '__main__':
    print(solve('input_1.csv'))