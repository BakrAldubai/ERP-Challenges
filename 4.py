from colorama import Fore
list_of_people = list()
while True:
    print(Fore.YELLOW," How many people do you want to invite to the party ?")
    number = input()
    if number.isdigit():
       number = int(number)
       if 0 < number < 10 :
           for i in range(number) :
               print(Fore.BLUE," Enter the host no.",i+1,"  name : ")
               name = input()

               while  not name.isalpha() :
                    print(Fore.RED ,"Error : wrong name ,please enter the host no.",i+1," right name : ")
                    print(Fore.BLUE,name," -----> has been invited")
               list_of_people.append(name)
           break
       elif number == 0 :
           print(Fore.RED,"Error : the number should be more than 0")
       else :
           print(Fore.RED,"Error :", number, " is too many people ")

    else:
        print(Fore.RED,"Error :please enter a number")

print(Fore.YELLOW,"People invited are :")
for i in list_of_people:
    print(Fore.YELLOW,i)


