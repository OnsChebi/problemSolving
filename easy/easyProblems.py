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

#############Count the number of vowels in a string
vowls=['a','e','i','o','u','y']
def count_vowls(word):
    count=0
    for i in word:
        if i in vowls:
            count+=1
    return count
print(count_vowls('hello noussa'))
#######sorting word's letters in a specific order
s=input("write your word \n")
if (0<len(s)<1000):
    lowerS=""
    upperS=""
    oddS=""
    evenS=""
    for i in s:
        if (i.islower()):
            lowerS+=i
            

        elif (i.isupper()):
            upperS+=i
        elif (i.isdigit() and i%2!=0):
            oddS+=i
    
        else:
            evenS+=i
    lowerS="".join(sorted(lowerS))
    upperS="".join(sorted(upperS))
    oddS="".join(sorted(oddS))
    evenS="".join(sorted(evenS))

    print(f"your new word is {lowerS+upperS+oddS+evenS}")

def numbers (n):
    if 1<=n <= 150:
            result=1
            
            for i in range(2,n+1):
                if i<10:
                    result=(result*10)+i
                
                if (i>=10):
                    result=(result*100)+i
                if(i>=100):
                    result=(result*1000)+i
            return result
    else:
        print("the number should be between 1 and 150")
        n= int(input())
        return numbers(n)
     
n = int(input())
print(numbers(n))


##########remove duplication from a list
lst=[1,1,2,2,3,4,4]
def remove_duplicated(lst):
    result=[]
    for i in lst:
        if i not in result:
            result.append(i)
    return result
print(f"the list after removing duplicated numbers is: {remove_duplicated(lst)}")