
# Assignment 1



# Inputs any name from user
name = input("Enter any name: ")
lenght = len(name)




for letter in range(lenght):

   print(" ", end = "")

   if letter != 0:
        spaces = letter * 2
        for  i in range(spaces):
            print(" ", end = "")

   print(name[letter], end = "")

   spaces_2 = (lenght - letter) * 2
   for  i in range(spaces_2):
            print(" ", end = "")
   print(name[letter], end = "")

   spaces_3 = (lenght - letter) * 2
   for  i in range(spaces_3):
            print(" ", end = "")
   print(name[letter])


for letter in range(lenght-1, -1, -1):

    print(" ", end = "")
   
    if letter != 0:
        spaces = letter * 2
        for  i in range(spaces):
            print(" ", end = "")
    print(name[letter], end = "")

    spaces_2 = (lenght - letter) * 2
    for  i in range(spaces_2):
            print(" ", end = "")
    print(name[letter], end = "")

    spaces_3 = (lenght - letter) * 2
    for  i in range(spaces_3):
            print(" ", end = "")
    print(name[letter])