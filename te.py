list = [4, 5, 70, 9, 50]


def pr(list, num):
    senn=set()
    for n in list:
        if num - n in senn:
            return True
        senn.add(n)
    return False

print(pr(list,17))
