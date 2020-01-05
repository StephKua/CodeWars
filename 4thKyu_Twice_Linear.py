# Consider a sequence u where u is defined as follows:

# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

# Task:

# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

# Example:

# dbl_linear(10) should return 22

# Note:

# Focus attention on efficiency

def dbl_linear(n):
    u = [1]
    a = 0
    b = 0
    while len(u) != n+1:
        y = u[a]*2+1
        z = u[b]*3+1
        if y < z:
          u.append(y)
          a+=1
        elif y > z:
          u.append(z)
          b+=1
        else:
          u.append(y)
          a+=1
          b+=1
    return (u[n])

from datetime import datetime 
start = datetime.now()
dbl_linear(100000)
print('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now() - start))

## Average 85ms for 100,000 as input
