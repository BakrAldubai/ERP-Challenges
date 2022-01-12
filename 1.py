total = 0
while total <= 50 :
    number = input("Enter a number : ")
    if number.isdigit() :
        number = eval(number)
        total = total + number
        print("Total is : ", total)
    else :
        print(number , ' is not a number , Try again')
    
    