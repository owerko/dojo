# # Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def fo(a):
    temp = [str(s) for s in str(a)]
    temp = sorted(temp, reverse=True)
    int2 = int(''.join(temp))
    return(int2)

print(fo(1236289))

