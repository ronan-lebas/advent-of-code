def solve1(path):
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

def solve2(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        list1, list2 = [], []
        for line in lines:
            a = line.split('   ')
            list1.append(int(a[0]))
            list2.append(int(a[1]))
    similarity = []
    for a in list1:
        c = 0
        for b in list2:
            if a == b:
                c += 1
        similarity.append(a * c)
    return sum(similarity)

if __name__ == '__main__':
    print(solve1('input_1.csv'))
    print(solve2('input_1.csv'))