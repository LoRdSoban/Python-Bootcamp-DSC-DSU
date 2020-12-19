import requests as res
from bs4 import BeautifulSoup
import csv, pyfiglet, os

page_names=[]
page_likes=[]
banner = pyfiglet.figlet_format("FB Likes Scraper") 

def ClearScreen():

   if os.name == 'posix':
      _ = os.system('clear')
   else:
    _ = os.system('cls')

def Read_Page_Names():
    with open('names.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        
        for row in csv_reader:

            if line_count != 0:
                page_names.append(row[0])
            else:
                line_count += 1 

        return page_names

def Get_Page_Likes(page_Names):

    for page_name in page_Names:
        source_code = res.get("https://www.facebook.com/"+page_name+"/likes")
        soup = BeautifulSoup(source_code.content,"html.parser")
        page_likes.append(soup.select_one("div._3xom").text)
       
    return page_likes

def Write_Page_Info(page_Names, page_Likes):

    with open('names_with_likes.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["Pages","Likes"])

        ClearScreen()
        
        print(banner)
        for page in range(len(page_Names)):
            print(f"\n\n{page_Names[page]}        {page_Likes[page]} likes")
            csv_writer.writerow([(page_Names[page]),(page_Likes[page])])
        input()
                                

def main():
    

    print(banner)
    
    print("\n Loading....", end="")

    names = Read_Page_Names()
    likes= Get_Page_Likes(names)
    Write_Page_Info(names, likes)




if __name__ == "__main__":
        main()
