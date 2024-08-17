def digitize(n):
    # numbers = []
    # for char in str(n):
    #    numbers.append(int(char))
    numbers = [int(i)for i in str(n)]
    return numbers[::-1]


print(digitize(3458349534))
