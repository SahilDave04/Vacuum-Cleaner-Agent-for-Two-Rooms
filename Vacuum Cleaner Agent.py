#Taking input of total number of rooms from user
n_ro = int(input("Input number of rooms : ")) 
#List containing info if the rooms are clean
status = []  
#Cost is the number of rooms cleaned and i the counter variable
i = 0; cost = 0                                
print("Input cleaniness status of the rooms.")
print("Clean : 1 \nDirty : 0")
for i in range(n_ro):
    #Taking status of room from user and then adding it to the list "status"
    temp = int(input("Enter status : "))       
    status.append(temp)
    i = i + 1
i = 0
print("Starting vacuum ....")
while i < n_ro:
    if status[i] == 0:
        #If the status of room is O it means it is dirty, it is cleaned and the cost variable is incremented
        status[i] = 1
        cost = cost + 1 # this is the counter
    i = i + 1
cost = str(cost)
print("Successfully cleaned.")
print("Cost is " + cost)
