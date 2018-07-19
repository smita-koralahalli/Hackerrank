'''Sample Input

2
Hacker
Rank

Sample Output

Hce akr
Rn ak

Explanation

Test Case 0:

The even indices are H, C, and E, and the odd indices are A, K, and R. We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().

Test Case 1:

The even indices are R and N and the odd indices are A and K. We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().'''

for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])
