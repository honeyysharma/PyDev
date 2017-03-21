#binary gap problem (CODILITY)
def binaryGap(n):
    gap = 0
    binary_gap = 0
    x = str(bin(n)).strip("0b")
#     print int('1001000100000001',2)
    list = map(int,str(x))
    for i,b in enumerate(list):
        if b == 0:
            gap = gap+1
        if b == 1:
            if list[i-gap-1] and i-gap-1 != -1 and binary_gap < gap:
                binary_gap = gap
            gap = 0

    return binary_gap
                

print binaryGap(37121)
