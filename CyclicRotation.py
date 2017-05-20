def solution(A, k):
    return A[-k:]+A[:-k]

print solution([1,2,3,4,5,6],5)
