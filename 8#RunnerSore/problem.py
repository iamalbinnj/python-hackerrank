def score(arr):
    lists = set(arr)
    res = sorted(lists)
    print(res[-2])


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score(arr)
    