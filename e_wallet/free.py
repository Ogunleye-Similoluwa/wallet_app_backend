if __name__ == "__main__":
    arr = ['s', 'e', 'm', 'i', 'c', 'o', 'l', 'o', 'n']
    print(arr[::-1])
    for item in range(len(arr)-1, -1, -1):
        print(arr[item], end='')
