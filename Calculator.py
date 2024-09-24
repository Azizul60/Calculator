 # This code will implement addition subtraction multiplication and subtraction
def main():
    X= int (input(" Enter a number :"))
    Y= int (input(" Enter a number :"))
    user= input("press 'a' for addition, 's' fro subtraction 'm' for multiplication 'd' for divition : ").strip()

    if user =='a':
        result =add(X,Y)
    elif user=='s':
         result=sub(X,Y)
    elif user=='m':
        result=multi(X,Y)
    else:
        result=div(X,Y)

    
    print(result)
    

def add(x,y):
    return x+y  
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return " Y can not be Zero "  
    
if __name__=="__main__":

    main()  