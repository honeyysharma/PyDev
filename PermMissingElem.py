def solution(A):
    N = len(A) + 1
    sum_N = (N * (N + 1)) / 2
    return sum_N-sum(A)

print solution([2,3])
print solution([2,3,1,5])
print solution([2])
solution([3])
solution([])
