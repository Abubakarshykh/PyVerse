# for i in range(10):
#     print(i)
    
#     print("A loop whhich have ranges 1 to < 10 and increment  2\n")
    
# for n in range(1,10,2):
#     print(n)
    
# print("to iterates the loop in reverse order\n")

# for r in range(10,1,-1):
#     print(r)
    
# str = "Abubakar"
# for o in str:
#     print(o)
    
    
#     print("Noow lets do While loop\n")
    
#     count = 0
#     while count < 7:
#         print(count)
#         count = count + 1
        
#     for a in range(10):
#         if a == 5:
#             break
#         print(a)
        
        
#     for b in range(15):
#         if b % 2 == 0:
#             continue
#         print(b)
    
#     # range (1,10,1)   ----------first number indicates where loop starts,
#     # second number indicates before which num loop terminates
#     # the third number indicates the increment like +1
    
#     # -------------Nested Loop-------------------
    
#     for i in range(4):
#         for j in range(3):
#             print(f"i:{i} and j:{j}")
            
            
#             # while looop------------
            
#             n = 10
#             sum = 0
#             count = 1
            
#             while count<=n:
#                 sum = sum + count 
#                 count = count+1
#                 print("sum of first 10  natural numbers",sum)
                
                
#                 for p in range(1,5):
#                     if p>1:
#                         for m in range(2,p):
#                             if p%m==0:
#                                 break
#                             else:
#                                 print(p)
# square = [num**2 for num in range(10)]
# print(square)

# # list comprehension in  loops

# cubes = [x**3 for x in range(5) if x%3==0]
# print(cubes)

# labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# print(labels)  # ➝ ['even', 'odd', 'even', 'odd', 'even']

# matrix = [[1, 2], [3, 4], [5, 6]]
# flat = [num for row in matrix for num in row]
# print(flat)  # ➝ [1, 2, 3, 4, 5, 6]


# table = [[i * j for j in range(1, 6)] for i in range(1, 4)]
# print(table)  # ➝ [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]


# vowels = [ch for ch in "education" if ch in "aeiou"]
# print(vowels)  # ➝ ['e', 'u', 'a', 'i', 'o']

# ---------------for ppatters-------------
for i in range (1,6):
    print(" * "*i)
    
for x in range(6,0,-1):
    print("*"*x)
    
for p in range(1,6):
    print(" "*(5-p)+"*"*(2*p-1))

                                
                                