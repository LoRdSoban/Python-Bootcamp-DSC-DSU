from bs4 import BeautifulSoup
import json, csv
import requests as res

schl_codes =[]
schl_details=[]

def GetSchoolCodes():
    schl_infos_raw = res.get('https://directory.ntschools.net/api/System/GetAllSchools')
    schl_infos_parsed = json.loads(schl_infos_raw.content.decode())
    
    for i in range(50):
        schl_info = schl_infos_parsed[i]
        schl_codes.append(schl_info["itSchoolCode"])


def GetSchoolInfos():
    schl_detail = {"school_name":"",
                       "address":"",
                       "admin_name":"",
                       "admin_position":"",
                       "admin_email":"",
                       "school_tele_num":""}    

    for schl_code in schl_codes:
        schl_detail_raw = res.get('https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='+schl_code)
        schl_detail_parsed = json.loads(schl_detail_raw.content.decode())

        schl_detail["school_name"] = schl_detail_parsed["name"]
        schl_detail["address"] = (schl_detail_parsed["physicalAddress"])["displayAddress"].replace(',', '')

        if len(schl_detail_parsed["schoolManagement"]) > 1:
            first_name = ((schl_detail_parsed["schoolManagement"])[1])["firstName"]
            last_name = ((schl_detail_parsed["schoolManagement"])[1])["lastName"]
            schl_detail["admin_email"] = ((schl_detail_parsed["schoolManagement"])[1])["email"]
            schl_detail["admin_position"] = ((schl_detail_parsed["schoolManagement"])[1])["position"]
        else:
            first_name = ((schl_detail_parsed["schoolManagement"])[0])["firstName"]
            last_name = ((schl_detail_parsed["schoolManagement"])[0])["lastName"]
            schl_detail["admin_position"] = ((schl_detail_parsed["schoolManagement"])[0])["position"]

        schl_detail["admin_name"] = (f"{first_name} {last_name}")
        schl_detail["school_tele_num"] = schl_detail_parsed["telephoneNumber"]

        schl_details.append(schl_detail.copy())


def WriteToCsv():
    with open("School Details.csv", mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        # Writes relevant titles in the file
        csv_writer.writerow(["School Name","Address","Principal/Admin Name","Principal/Admin Position","Principal/Admin Email","School Telephone Number"])

        for schl_detail in schl_details:
             csv_writer.writerow([schl_detail["school_name"],schl_detail["address"],schl_detail["admin_name"],schl_detail["admin_position"],schl_detail["admin_email"],schl_detail["school_tele_num"]])

            

def main():
    GetSchoolCodes()
    GetSchoolInfos()
    WriteToCsv()


if __name__ == "__main__":
    main()