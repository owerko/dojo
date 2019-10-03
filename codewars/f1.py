# # Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def fo(a):
    temp = sorted([str(s) for s in str(a)], reverse=True)
    return int(''.join(temp))


print(fo(1236289))
