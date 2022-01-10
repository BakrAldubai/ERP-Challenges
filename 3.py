print("enter three person's names to invite : ")
persons = []
i = 1
persons.append(input(" person " + str(i) +" :" ))
i+=1
persons.append(input(" person " + str(i) +" :" ))
i+=1
persons.append(input(" person " + str(i) +" :" ))

while True:
    ans = input("Do you want to invite more ? Y/N ")
    if ans.lower()=='y' :
        i+=1
        persons.append(input(" person " + str(i) +" :" ))
    elif ans.lower()=='n' :
        print("number of persons  = ", len(persons))
        break

