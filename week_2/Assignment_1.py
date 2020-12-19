import os
from pathlib import Path 


def get_size(info):
    return info.get('size')

def initialisation():
    global file_info, files

    file_info = {"name":"",
                 "size":""}
    files = []

def input_folder_path():
    print(f"The current directory is {os.getcwd()}\n")

    folder_path = Path(input("Enter the path:"))

    return folder_path

def get_files_info(folder_path):
    for file in os.listdir(folder_path):
        file_info["name"] = file
        file_info["size"] = int((os.stat(folder_path/file)).st_size) / (1028)
        files.append(file_info.copy())
    files.sort(key=get_size, reverse = True)

def print_files_info():
    print("\n")
    for file in files:
        print(file["name"],"    ",file["size"])

def main():

    initialisation()
    
    input_path = input_folder_path()
    
    get_files_info(input_path)

    print_files_info()


if __name__ == "__main__":
    main()