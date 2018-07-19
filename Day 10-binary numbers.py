Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5

Sample Output 1

1

Sample Input 2

13

Sample Output 2

2

Explanation

Sample Case 1:
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count = 0
    while n:
        n &= n << 1
        count += 1
    print(count)
    
    #print(max(bin(n).strip('0b').split('0')).count('1'))
