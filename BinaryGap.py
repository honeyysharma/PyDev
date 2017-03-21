def binaryGap(n):
    gap = 0
    binary_gap = 0
    x = bin(n)[2:].zfill(8)
    #print int('1001000',2)
    #print x
    list = map(int, str(x))
    for i, b in enumerate(list):
        if b == 0:
            gap = gap + 1
        if b == 1:
            # list[i-gap-1] == 1 checks if the gap is having 1 on the left too
            # i-gap-1 != -1 checks if the index is becoming less than 0
            # 0 0 0 0 1 0 0 1 ---- input
            # 0 1 2 3 4 5 6 7 ---- indices
            # when index = 4; gap = 4; So i - gap -1 = -1; It is less than zero and list[-1] = list[7]
            # when index = 7; gap = 2; So i - gap -1 = 4; It is not less than zero and list[4] = 1
            if list[i - gap - 1] == 1 and i - gap - 1 != -1 and binary_gap < gap:
                binary_gap = gap
            gap = 0

    return binary_gap


print ("binary gap: %d" % binaryGap(72))
print ("binary gap: %d" % binaryGap(9))
print ("binary gap: %d" % binaryGap(529))
print ("binary gap: %d" % binaryGap(20))
print ("binary gap: %d" % binaryGap(15))
