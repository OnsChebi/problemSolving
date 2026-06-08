###############reverse fucntion
def reverse (word):
    reversed_word=""
    for i in range(len(word)-1, -1, -1):
        reversed_word+=word[i]
    return reversed_word
print(reverse('noussa'))

####### get prime numbers from a list and sort them in order
my_list=[5,12,8,17,23,4,2,9,15]
def is_Prime(n):
    x=int(n/2+1)
    r=False
    for i in range  (2,x):
        if (n % i == 0):
            r=True
    return not r   
            
    # if r:
    #     return print (f"{n} is not a prime number")
    # else:
    #     return print (f"{n} is a prime number")


for i in my_list:
    is_Prime(i)
print ("the prime numbers in the list in order are: ")
primeNumbers=[]
for i in my_list:
    if is_Prime(i):
        primeNumbers.append(i)
primeNumbers.sort()
print (primeNumbers)