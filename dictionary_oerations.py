people={'Arham':'Red','Lisa':'White','Vinod':'Blue','Jenny':'Green'}
k=[]

#print total no. of student
print("no. of student in list is ",len(people))

#change favorite color of Lisa
people['Lisa']='White'
print("Lisa favorite color is changed to",people['Lisa'])
del people['Jenny']
print(people)


#sort student name
for i in people.keys():
    k.append(i)
k.sort()

#print student name
for o in k:
    print(o,"favorite color is",people[o])
