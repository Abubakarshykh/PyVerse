# list comprehension in  loops

cubes = [x**3 for x in range(5) if x%3==0]
print(cubes)

labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ➝ ['even', 'odd', 'even', 'odd', 'even']

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # ➝ [1, 2, 3, 4, 5, 6]


table = [[i * j for j in range(1, 6)] for i in range(1, 4)]
print(table)  # ➝ [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]


vowels = [ch for ch in "education" if ch in "aeiou"]
print(vowels)  # ➝ ['e', 'u', 'a', 'i', 'o']

# ---------------for ppatters-------------
for i in range (1,6):
    print(" * "*i)
    
for x in range(6,0,-1):
    print("*"*x)
    
for p in range(1,6):
    print(" "*(5-p)+"*"*(2*p-1))