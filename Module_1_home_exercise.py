import numpy as np   

def Rand(start,end,num): ####Function to create random numbers based on the required range (start and end)
    res = []
    for j in range(num):
        res.append(np.random.randint(start, end))
 
    return res


def Sorted(s): # Function to sort the numbers in increasing order
    for k in range(len(s)):
        for m in range(len(s)-1):
            if s[m]>s[m+1]:
                s[m],s[m+1] = s[m+1],s[m]
    return s



def Average_odd_even(r): #Function to split the numbers to odd and even and get the corresponding average value
    odd_numbers = 0
    even_numbers = 0
    sum_odd = 0
    sum_even = 0
    odd_List = []
    even_List = []
    
    for ele in r:
        if ele % 2 == 1:
            sum_odd = sum_odd + ele
            odd_numbers += 1
            odd_List.append(ele)
        if ele % 2 == 0:
            sum_even = sum_even + ele
            even_numbers += 1
            even_List.append(ele)
    return sum_odd/odd_numbers , sum_even/even_numbers , odd_List , even_List
    
 
# Driver Code 
num = 100 # Total randon numbers to be created
start = 1 # Starting range of random numbers
end = 1001 # Ending range of random numbers
#print(Rand(start, end, num))
p  = Rand(start, end, num) # function call to create random numbers
z = Sorted(p) # function call to sort the random numbers

c , d , e , f = Average_odd_even(z) # function call to get the odd number list , even number list and average of odd and even numbers

print('Odd number list is :' , e) #Prints the list of odd numbers
print('Average of odd numbers is :' , c) #Prints the average of odd numbers

print('Even number list is :' , f) #Prints the list of even numbers
print('Average of even numbers is :' , d)  #Prints the average of even numbers

