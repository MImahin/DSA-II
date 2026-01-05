array= [10,34,56,22,9,11,87,12,45,83,23,97,32]

# 1. Prints the numbers from 1 to n.

def pr(n):
    if n==0:
        return
    pr(n-1)
    print(n, end=" ")


# pr(100)

# 2. Calculate the sum of numbers from 1 to n.


def sr(n):
    if n==0:
        return 0
    return n+sr(n-1)

# print(sr(100))

# 3. Calculate the factorial of n.

def fac(n):
    if n==0 or n==1:
        return 1
    return n*fac(n-1)

# print(fac(0))

# 4. Calculate the sum of digits of a given number n.

def cs(n):
    if n<10:
        return n
    return n%10+cs(n//10)
# print(cs(1234567890))

# 5. Count the number of digits of a given number n.

def co(n):
    if n<10:
        return 1
    return 1+co(n//10)
# print(co(1234567890))

# 6. Calculate the n th term of a Fibonacci series.

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
    
# print(fib(10))

# 7. Calculate a to the power b

def a2b(a,b):
    if b==1:
        return a
    return a * a2b(a,b-1)

# print(a2b(4,4))

# 8. Print the list elements.

def p(n):
    if len(n)==0:
        print()
        return
    print(n[0],end=" ")
    p(n[1:])
# p(array)
# but this slicing creates another list so time complexity o(n2) not optiomal 
# better:
def p2(n,i=0):
    if i==len(n):
        print()
        return
    print(n[i],end=" ")
    p2(n,i+1)
# p2(array)
# 9. Find the largest element of a given list.

def lar(n):
    if len(n)==1:
        return n[0] 
    other=lar(n[1:])
    if n[0]>other:
        return n[0]
    return other
# print(lar(array))  

# again list slicing is not optimal higher time complexity so here is better

def lar2(n,i=0):
    if len(n)==i+1:
        return n[i]
    other=lar2(n,i+1)
    if n[i]>other:
        return n[i]
    return other

# print(lar2(array))

# 10. Find the smallest element of a given list.

def small(n,i=0):
    if len(n)==i+1:
        return n[i]
    other=small(n,i+1)
    if n[i]<other:
        return n[i]
    return other

# print(small(array))


# 11. Find the largest and smallest element of a given list.

def sl(n,i=0):
    if len(n)==i+1:
        return n[i],n[i]
    sm,lr=sl(n,i+1)
    if n[i]<sm:
        return n[i],lr
    elif n[i]>lr:
        return sm,n[i]
    return sm,lr

# print(sl(array))

# 12. Check whether a given string is palindrome or not.

def palin(string,i=0):
    if i >= len(string)//2:
        return True
    elif string[i]==string[len(string)-1-i]:
        return palin(string,i+1)
    return False

# print(palin("aba"))

# 13. Remove white spaces from a string & convert upper cases to lower.

def remove(str,i=0):
    if i==len(str):
        return ""
    if str[i]==" ":
        return ""+remove(str,i+1)
    return str[i].lower()+remove(str,i+1)

# print(remove(" Hi Helloo How Are You?"))
    

# Extras: 

# Suppose that, you are at 0th stair and you have to reach at
#  nth stair. Each time you can climb 1 or 2 steps.
#  Find out the total number of distinct ways you can climb from
#  0th to nth stair.

def steps(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return steps(n-1)+steps(n-2)
# print(steps(32))


# Find if a number is a power of 4.

def check(n):
    if n<1:
        return False
    if n==1:
        return True
    if n%4==0:
        return check(n//4)
    return False


# print(check(0))
