# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2 :
#         return True 
#     if n%2 == 0 :
#         return False
     
#     i = 3
#     while i * i <= n :
#         if n % i == 0 :
#             return False
#         i += 2
#         return True
#     l = int(input("enter l : "))
#     r = int(input("enter r : "))

#     print(f"Prime numbers between {l} and {r}:")
#     for num in range(l, r + 1):
#         if is_prime(num):
#             print(num, end=" ")


def prime (l,r):
    for num in range(l, r+1):
        if num < 2:
            continue
        flag = True
        for i in range (2 , num ):
            if num % i == 0:
                flag = False
                break

                
        if (flag):
            print(num)

prime(5,50)           
        