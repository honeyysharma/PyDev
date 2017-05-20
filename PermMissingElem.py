def solution(A):
    #length + 1 as one element is missing.
    N = len(A) + 1
    #will take care of the boundary conditions if 1 is missing in [2,3,4]
    #or 4 is missing in [1,2,3]
    sum_N = (N * (N + 1)) / 2
    return sum_N-sum(A)

print solution([2,3])
print solution([2,3,1,5])
print solution([1,2])
solution([3])
solution([])
