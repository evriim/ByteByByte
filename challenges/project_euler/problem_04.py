"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit number is 9009 =91*99.
Find the largerst palindrome made from the product of two 3-digit numbers.
"""
PAL=0
for i in range(100,1000):
    for j in range(100,1000):
        k=i*j
        list_k = [int(x) for x in str(k)]
        list_reverse= list_k[::-1]
        if list_k == list_reverse and k>PAL:
            PAL = k

print(PAL)
