for i in range(10):
    print(i)
    
    print("A loop whhich have ranges 1 to < 10 and increment  2\n")
    
for n in range(1,10,2):
    print(n)
    
print("to iterates the loop in reverse order\n")

for r in range(10,1,-1):
    print(r)
    
str = "Abubakar"
for o in str:
    print(o)
    
    
    print("Noow lets do While loop\n")
    
    count = 0
    while count < 7:
        print(count)
        count = count + 1
        
    for a in range(10):
        if a == 5:
            break
        print(a)
        
        
    for b in range(15):
        if b % 2 == 0:
            continue
        print(b)
    
    # range (1,10,1)   ----------first number indicates where loop starts,
    # second number indicates before which num loop terminates
    # the third number indicates the increment like +1
    
    # -------------Nested Loop-------------------
    
    for i in range(4):
        for j in range(3):
            print(f"i:{i} and j:{j}")
            
            
            # while looop------------
            
            n = 10
            sum = 0
            count = 1
            
            while count<=n:
                sum = sum + count 
                count = count+1
                print("sum of first 10  natural numbers",sum)
                
                
                for p in range(1,5):
                    if p>1:
                        for m in range(2,p):
                            if p%m==0:
                                break
                            else:
                                print(p)
                                
                                