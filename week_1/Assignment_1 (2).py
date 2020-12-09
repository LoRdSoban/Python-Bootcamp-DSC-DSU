
# Assignment 1

# Divided into functions




def UpperDiagonal(letter):

   if letter != 0:
    spaces = letter * 2
    for  i in range(spaces):
        print(" ", end = "")
   print(name[letter], end = "")

def UpperStaright(letter):

   spaces_2 = (lenght - letter) * 2
   for  i in range(spaces_2):
            print(" ", end = "")
   print(name[letter], end = "")

def UpperReverseDiagonal(letter):

   spaces_3 = (lenght - letter) * 2
   for  i in range(spaces_3):
            print(" ", end = "")
   print(name[letter])

def LowwerDiagonal(letter):

    if letter != 0:
        spaces = letter * 2
        for  i in range(spaces):
            print(" ", end = "")
    print(name[letter], end = "")

def LowwerStaright(letter):

    spaces_2 = (lenght - letter) * 2
    for  i in range(spaces_2):
            print(" ", end = "")
    print(name[letter], end = "")

def LowwerReverseDiagonal(letter):
    spaces_3 = (lenght - letter) * 2
    for  i in range(spaces_3):
            print(" ", end = "")
    print(name[letter])


def Upper():
    for letter in range(lenght):
        print(" ", end = "")
        UpperDiagonal(letter)
        UpperStaright(letter)
        UpperReverseDiagonal(letter)

def Lower():    
    for letter in range(lenght-1, -1, -1):
        print(" ", end = "")
        LowwerDiagonal(letter)
        LowwerStaright(letter)
        LowwerReverseDiagonal(letter)

def main():

    global name, lenght

    # Inputs any name from user
    name = input("Enter any name: ")
    lenght = len(name)
    Upper()
    Lower()


if __name__ == "__main__":
    main()







