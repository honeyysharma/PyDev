def solution(A):
    # write your code in Python 2.7
    lenghtOfList = len(A)
    A.sort()
    A = list(set(A))
    if A[-1]>0:
        if lenghtOfList>1:
            for i in xrange(1,A[-1]):
                if not i in A:
                    return i
        else:
            if A[0] == 1:
                return A[0]+1
            else:
                return 1
    return 1
