import copy


#Initialisation
average = 0
total = 0
highest = 0
lowest = 999
record = []
info = {"name":"",
        "rollno":"",
        "age":"",
        "marks":""
        }
entries = ""


while (True): #Infinite Loop

    try:
        entries = int(input("Enter number of entries:")) # Inputs number of entries
    except:
        print("\nERROR! Enter a valid number.\n")  # Outputs message in case of any error 

    if type(entries) == int: # Condition that needs to be fulfilled in order to exit the loop
        break




for entry in range(entries):

    info["name"] = input("\n\nEnter name:")

    info["rollno"] = int(input("Enter roll number:")) # Inputs roll number

    while (True): # Infinite Loop
        try:
            info["age"] = int(input("Enter age:")) # Inputs age
        except:
            print("\nERROR! Enter a valid number.\n") # Outputs message in case of any error 

        if type(info["age"]) == int: # Condition that needs to be fulfilled in order to exit the loop
            break

    while (True): # Infinite Loop
        try:
            info["marks"] = int(input("Enter marks:")) # Inputs marks
        except:
            print("\nERROR! Enter a valid number.!\n") # Outputs message in case of any error 

        if type(info["marks"]) == int: # Both the conditions that needs to be fulfilled in order to exit the loop

            if info["marks"] < 0 or info["marks"] > 100:
                print("\nERROR! Enter marks between 0 to 100.\n")
            else:
                break
       

    record.append(info.copy()) # Adds record(dict) of a student in list


                                
    # Output in tabular form   ||
    #                          || 
    #                        __||__
    #                        \    /
    #                         \  /
    #                          ∨   
                     
print("\n\n\nROLL NO |   NAME   |  AGE  |  MARKS(out of 100)")
for entry in range(entries):

    print(f"{(record[entry])['rollno']}  |  {(record[entry])['name']}  |  {(record[entry])['age']}  |  {(record[entry])['marks']}")

    total += (record[entry])['marks'] 
    if (record[entry])['marks'] < lowest:
        lowest = (record[entry])['marks']
    if (record[entry])['marks'] > highest:
        highest = (record[entry])['marks']

average = total/entries

print(f"\n\n Highest marks:{highest}  Lowest marks:{lowest}  Average marks:{average}")