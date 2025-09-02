l=int(input("l= "))
rev=0
while l != 0:
    digit = l%10
    rev = rev*10+digit
    l = l//10
print ("The reverse number is ", rev)