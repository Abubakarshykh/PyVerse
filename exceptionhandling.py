# try:
#     a=b
# except NameError as NE:
#     print(NE)
    
# try:
#     b=c
# except:
#     print("anoher way too handle it")
    
# try:
#     result = 1/0
# except:
#     print("An unexpected error you have divided 1 by 0 so infifnity ooccurs")
    
# try:
#     result = 1/0
# except ZeroDivisionError as zero:
#     print(zero)
    
# try:
#     result = 0/1
# except Exception as e:
#     print(e)
    
    
try:
    num = int(input("Enter a number please: "))
    result=10/num
except ValueError:
    print("THis isn't a right value and is valuerroor")
except ZeroDivisionError:    #when any error is coming
    print("Zero dividsion error")
except Exception as e:
    print(e)
else:
    print(f"Print the result is {result}")   # it will only execute if there is noo excetion
finally:
    print("Finally Exceptioon handled succesfully")   #it will execute always execute
    
    
try:
    file=open('new.txt','r')    
    c=file.read()
    print(c)
except FileNotFoundError:
    print("file not found")
except Exception as ex:
    print(ex)
else:
    print("These is no exception")
finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print('File has chosed')
    
    

