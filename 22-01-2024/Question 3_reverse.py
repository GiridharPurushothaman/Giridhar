'''Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123
Sample Output 0

321
Sample Input 1

2341
Sample Output 1

1432'''

#using slicing 

n=int(input())
def reverseNum(n):
    n=str(n)
    n=n[::-1]         
    n=int(n)
    return n
print(reverseNum(n))

#using while loop
n = int(input())
def reverseNum(n):
    rev=0
    while (n!=0):
        digit=n%10         
        rev=rev*10+digit 
        n=n//10           
    return rev
print(reverseNum(n))


