"""
10---------------------------85
X                            Y
distance = X-Y = 85-10 = 75
Divide distance by fixed jump distance (D = 30)
75/30 = 2.5
ceil(2.5) = 3.0
"""
import math
def solution(X, Y, D):
    # write your code in Python 2.7
        return int(math.ceil((Y-X)/float(D)))
        
print solution(10,85,30)


"""
Alternate solution avoiding casting
10---------------------------85
X                            Y
distance = X-Y = 85-10 = 75
Check if distance is equal to jump distance then add 1 to the solution ((Y-X)/D)+1 else return 1 by (Y-X)/D
"""
def solution(X, Y, D):
    if (Y-X) % D > 0:
        print ((Y-X)/D)+1
    else:
        print (Y-X)/D


print solution(10,85,75)
