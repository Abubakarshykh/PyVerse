# reading files
with open('practice.txt','r') as file:
    content = file.read()
    print(content)
    
with open('practice.txt','r') as file:
    for line in file:
        print(file)
        
with open('practice.txt','r') as file:
    for line in file:
        print(line.strip()) # removes characters saces of newline
        
with open('practice.txt','w') as file:
    print(file.write("Helloo woorld\n we have wroote something using file write")) #it overrides that u wrote

with open('practice.txt','a') as file:
    content = file.write("\nSo guys we have appended the formatioon")
    print(content)

files = ["\nFirst Line\nsecond Line\nThird Line"]
with open('practice.txt','a') as file:
    print(file.writelines(files))
    
# reading  binary files
with open('practice.bin','rb') as file:
    contentb = file.read()
    print(contentb)
    
    # writing and reading simultaneously  w+r
    
with open('new.txt','w+') as file:
    contentw = file.write("reading and writing both at the same time")
    print(contentw)
    
    file.seek(0)
    