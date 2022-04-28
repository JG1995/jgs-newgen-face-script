
from __future__ import print_function
import time
import asyncio
import random
import os.path
import os
import glob
import pickle
import json
import re
import shutil
import sys


##### Nations datas #####
listnations = [{ "flag": "AFG","nation": "Afghanistan","ethnicgroup": "MENA"}, { "flag": "AIA","nation": "Anguilla","ethnicgroup": "African"}, { "flag": "ALB","nation": "Albania","ethnicgroup": "YugoGreek"}, { "flag": "ALG","nation": "Algeria","ethnicgroup": "MENA"}, { "flag": "AND","nation": "Andorra","ethnicgroup": "SAMed"}, { "flag": "ANG", "nation": "Angola", "ethnicgroup": "African" }, { "flag": "ARG", "nation": "Argentina", "ethnicgroup": "South American" }, { "flag": "ARM", "nation": " Armenia", "ethnicgroup": "MENA" }, { "flag": "ARU", "nation": "Aruba", "ethnicgroup": "South American" }, { "flag": "ASA", "nation": "American Samoa", "ethnicgroup": "South American" }, { "flag": "ATG", "nation": "Antigua", "ethnicgroup": "African" }, { "flag": "aus" , "nation": "Australia", "ethnicgroup": "SpanMed" }, { "flag": "AUT", "nation": "Austria", "ethnicgroup": "Central European" }, { "flag": "AZE", "nation": "Azerbaijan", "ethnicgroup": "MENA" }, { "flag": "BAH", "nation": "Bahamas", "ethnicgroup": "African" }, { "flag": "BAN", "nation": "Bangladesh", "ethnicgroup": "MESA" }, { "flag": "BAR", "nation": "Barbados" , "ethnicgroup": "African" }, { "flag": "BDI", "nation": "Burundi", "ethnicgroup": "African" }, { "flag": "BEL", "nation": " Belgium", "ethnicgroup": "Central European" }, { "flag": "BEN", "nation": "Benin", "ethnicgroup": "African" }, { "flag": "BER", "nation": "Bermuda", "ethnicgroup": "African" }, { "flag": "BFA", "nation": "Burkina Faso", "ethnicgroup": "African" }, { "flag": "BHR" , "nation": "Bahrain", "ethnicgroup": "MENA" }, { "flag": "BHU", "nation": "Bhutan", "ethnicgroup": "MESA" }, { "flag": "BIH", "nation": "Bosnia", "ethnicgroup": "YugoGreek" }, { "flag": "blr", "nation": "Belarus", "ethnicgroup": "EECA" }, { "flag": "BLZ", "nation": "Belize", "ethnicgroup": "African" }, { "flag": "BOL", "nation": "Bolivia", "ethnicgroup": "South American" } , { "flag": "BOT", "nation": "Botswana", "ethnicgroup": "African" }, { "flag": "BRA", "nation": "Brazil", "ethnicgroup": "South American" }, { "flag": "BRU", "nation": "Brunei", "ethnicgroup": "Seasian" }, { "flag": "BUL", "nation": "Bulgaria", "ethnicgroup": "YugoGreek" }, { "flag": "CAM", "nation": "Cambodia", "ethnicgroup": "Seasian" }, { "flag": "CAN", "nation": "Canada", "ethnicgroup": "Caucasian" }, { "flag": "CAY", "nation": "Cayman Islands", "ethnicgroup": " African" }, { "flag": "CGO", "nation": "Congo", "ethnicgroup": "African" }, { "flag": "CHA", "nation": "Chad", "ethnicgroup" : "African" }, { "flag": "CHI", "nation": "Chile", "ethnicgroup": "South American" }, { "flag": "CHN", "nation": "China", "ethnicgroup": "Asian" }, { "flag": "CIV", "nation": "Ivory Coast", "ethnicgroup": "African" }, { "flag": "CMR", "nation" : "Cameroon", "ethnicgroup": "African" }, { "flag": "COD", "nation": "DR Congo", "ethnicgroup": "African" }, { "flag": "COK", "nation": "Cook Islands", "ethnicgroup": "South American" }, { "flag": "COL", "nation": "Colombia", "ethnicgroup": "South American" }, { "flag": "COM", "nation": "Comores", "ethnicgroup": "African" }, { "flag": "CPV", "nation": "Islands of Cape Verde", "ethnicgroup": "African" }, { "flag": "CRC", "nation": "Costa Rica", "ethnicgroup": "South American" }, { "flag": "CRO", "nation": "Croatia", "ethnicgroup": "YugoGreek" }, { "flag": "CTA", "nation": "Central African Republic", "ethnicgroup": "African" }, { "flag": "CUB", "nation": "Cuba", "ethnicgroup": "South American" }, { "flag": "CUW", "nation": "Curacao", "ethnicgroup": "African" }, { "flag": "cyp", "nation": "Cyprus", "ethnicgroup": "YugoGreek" }, { "flag": "CZE", "nation": "Czech Republic", "ethnicgroup": "Central European" }, { "flag": "DEN", "nation": "Denmark", "ethnicgroup": "Scandinavian" }, { "flag": "DJI", "nation": "Djibouti", "ethnicgroup": "African" }, { "flag": "DMA", "nation": "Dominica", "ethnicgroup": "African" }, { "flag": "DOM", "nation": "Dominican Republic", "ethnicgroup": "South American" }, { "flag": "ECU", "nation": "Ecuador ", "ethnicgroup": "South American" }, { "flag": "EGY", "nation": "Egypt", "ethnicgroup": "MENA" }, { "flag": "ENG", "nation" : "England", "ethnicgroup": "Caucasian" }, { "flag": "EQG", "nation": "Equatorial Guinea", "ethnicgroup": "African" }, { "flag": "ERI" , "nation": "Eritrea", "ethnicgroup": "African" }, { "flag": "ESP", "nation": "Spain", "ethnicgroup": "SpanMed" }, { "flag": "east", "nation": "Estonia", "ethnicgroup": "Scandinavian" }, { "flag": "ETH", "nation": "Ethiopia", "ethnicgroup": "African" }, { "flag": "FIJ", "nation": "Fiji Islands", "ethnicgroup": "South American" }, { "flag": "FIN", "nation": "Finland", "ethnicgroup": "Scandinavian" }, { "flag": "fra", "nation": "France", "ethnicgroup": "SpanMed" }, { "flag": "FRO", "nation": "Faroe Islands", "ethnicgroup" : "Scandinavian" }, { "flag": "GAB", "nation": "Gabon", "ethnicgroup": "African" }, { "flag": "GAM", "nation": "Gambia", "ethnicgroup": "African" }, { "flag": "GEO", "nation": "Georgia", "ethnicgroup": "YugoGreek" }, { "flag": "GER", "nation": "Germany", "ethnicgroup": "Caucasian" }, { "flag": "GHA", "nation": " Ghana", "ethnicgroup": "African" }, { "flag": "gib", "nation": "Gibraltar", "ethnicgroup": "SpanMed" }, { "flag": "GNB", "nation": "Guinea-Bissau", "ethnicgroup": "African" }, { "flag": "GRE", "nation": "Greece", "ethnicgroup": "YugoGreek" }, { "flag": " GRN", "nation": "Grenada", "ethnicgroup": "African" }, { "flag": "GUA", "nation": "Guatemala", "ethnicgroup": "South American" }, { "flag": "GUI", "nation": "Guinea", "ethnicgroup": "African" }, { "flag": "GUM", "nation": "Guam", "ethnicgroup": "Asian" }, { "flag": "GUY", "nation": "Guyana", "ethnicgroup": "African" }, { "flag": "HAI", "nation": "Haiti", "ethnicgroup": "African" }, { "flag": "HKG", "nation": "Hong Kong", "ethnicgroup": "Asian" }, { "flag": "HON", "nation": "Honduras", "ethnicgroup": "South American" }, { "flag": "HUN", "nation": "Hungary", "ethnicgroup": "Central European" }, { "flag": "IDN", "nation": "Indonesia", "ethnicgroup": "Seasian" }, { "flag": "IND", "nation": "India", "ethnicgroup": "MESA" }, { "flag": "IRL", "nation": "Ireland", "ethnicgroup": "Caucasian" }, { "flag": "IRN", "nation": "Iran", "ethnicgroup": "MENA" }, { "flag": "IRQ", "nation": "Iraq", "ethnicgroup": "MENA" }, { "flag": "ISL", "nation": "Iceland", "ethnicgroup": "Scandinavian" }, { "flag": "ISR", "nation": "Israel", "ethnicgroup": "MENA" }, { "flag": "ITA", "nation": "Italy", "ethnicgroup": "Italmed" }, { "flag": "JAM", "nation": "Jamaica", "ethnicgroup": "African" }, { "flag": "JOR", "nation": "Jordan", "ethnicgroup": "MENA" }, { "flag": "JPN", "nation": "Japan", "ethnicgroup": "Asian" }, { "flag": "KAZ", "nation": "Kazakhstan", "ethnicgroup": "MESA" }, { "flag": " KEN", "nation": "Kenya", "ethnicgroup": "African" }, { "flag": "KGZ", "nation": "Kyrgyzstan ", "ethnicgroup": "MESA" }, { "flag": "KOR", "nation": "South Korea", "ethnicgroup": "Asian" }, { "flag": "KSA", "nation": "Saudi Arabia", "ethnicgroup": "MENA" }, { "flag": "KUW", "nation": "Kuwait", "ethnicgroup": "MENA" }, { "flag": "KVX", "nation": "Kosovo", "ethnicgroup": "YugoGreek" }, { "flag": "LAO", "nation": "Laos", "ethnicgroup": "Seasian" }, { "flag": "LBR", "nation": "Liberia", "ethnicgroup": "African" }, { "flag": "LBY", "nation": "Libya", "ethnicgroup": "MENA" }, { "flag": "LCA", "nation": "Saint Lucia", "ethnicgroup": "African" }, { "flag": "LES", "nation": "Lesotho", "ethnicgroup": "African" }, { "flag": "LIB", "nation": "Lebanon", "ethnicgroup": "MENA" }, { "flag": "LIE", "nation": "Liechtenstein" , "ethnicgroup": "Central European" }, { "flag": "LTU", "nation": "Lithuania", "ethnicgroup": "Scandinavian" }, { "flag": "LUX", "nation" : "Luxembourg", "ethnicgroup": "Central European" }, { "flag": "LVA", "nation": "Latvia", "ethnicgroup": "Scandinavian" }, { "flag": "MAC", "nation": "Macao", "ethnicgroup": "Asian" }, { "flag": "MAD", "nation": "Madagascar", "ethnicgroup": "African" }, { "flag": "MAR", "nation": "Morocco", "ethnicgroup": "MENA" }, { "flag": "MAS", "nation": "Malaysia", "ethnicgroup": "Seasian" }, { "flag": "MDA", "nation": "Moldova", "ethnicgroup": "EECA" }, { "flag": " MDV", "nation": "Maldives", "ethnicgroup": "MESA" }, { "flag": "MEX", "nation": "Mexico", "ethnicgroup": "South American" }, { "flag": "MGL", "nation": "Mongolia", "ethnicgroup": "Asian" }, { "flag": "MKD", "nation": "Macedonia", "ethnicgroup": "YugoGreek" }, { "flag": "MLI", "nation": "Mali", "ethnicgroup": "African" }, { "flag": "MLT", "nation": "Malta", "ethnicgroup": "YugoGreek " }, { "flag": "MNE", "nation": "Montenegro", "ethnicgroup": "YugoGreek" }, { "flag": "MOZ", "nation": "Mozambique", "ethnicgroup" : "African" }, { "flag": "MRI", "nation": "Mauritius", "ethnicgroup": "A frican" }, { "flag": "MSR", "nation": "Montserrat", "ethnicgroup": "African" }, { "flag": "MTN", "nation": "Mauritania", "ethnicgroup" : "African" }, { "flag": "MWI", "nation": "Malawi", "ethnicgroup": "African" }, { "flag": "MYA", "nation": "Burma", "ethnicgroup": "Seasian" }, { "flag": "NAM", "nation": "Namibia", "ethnicgroup": "African" }, { "flag": "NCA", "nation": "Nicaragua ", "ethnicgroup": "South American" }, { "flag": "NCL", "nation": "New Caledonia", "ethnicgroup": "South American" }, { "flag": "NED", "nation": "Netherlands", "ethnicgroup": "Caucasian" }, { "flag": "NEP", "nation": "Nepal", "ethnicgroup": "MESA" }, { "flag": " NGA", "nation": "Nigeria", "ethnicgroup": "African" }, { "flag": "NIG", "nation": "Niger", "ethnicgroup": "African" }, { "flag": "NIR", "nation": "Northern Ireland", "ethnicgroup": "Caucasian" }, { "flag": "NOR", "nation": "Norway", "ethnicgroup": "Scandinavian" }, { "flag": "NZL", "nation": "New Zealand", "ethnicgroup": "SpanMed" }, { "flag": "OMA", "nation": "Oman", "ethnicgroup": "MENA" }, { "flag": "PAK", "nation": "Pakistan", "ethnicgroup": " MESA" }, { "flag": "PAL", "nation": "Palestine", "ethnicgroup": "MENA" }, { "flag": "PAN", "nation": "Panama", "ethnicgroup": "South American" }, { "flag": "PAR", "nation": "Paraguay", "ethnicgroup": "South American" }, { "flag": "PER", "nation": "Peru" , "ethnicgroup": "South American" }, { "flag": "PHI", "nation": "Philippines", "ethnicgroup": "Seasian" }, { "flag": "PNG", "nation": "Papua New Guinea", "ethnicgroup": "South American" }, { "flag": "POL", "nation": "Poland", "ethnicgroup": "Central European" }, { "flag": " POR", "nation": "Portugal", "ethnicgroup": "SpanMed" }, { "flag": "PRK", "nation": "North Korea", "ethnicgroup": "Asian" }, { "flag": "PUR", "nation": "Puerto Rico", "ethnicgroup": "South American" }, { "flag": "QAT", "nation": "Qatar", "ethnicgroup": "MENA" }, { "flag": "ROU", "nation": "Romania", "ethnicgroup": "YugoGreek" }, { "flag": "RSA", "nation": "South African", "ethnicgroup": "African" }, { "flag": "RUS", "nation": "Russia", "ethnicgroup" : "EECA" }, { "flag": "RWA", "nation": "Rwanda", "ethnicgroup": "African" }, { "flag": "SAM", "nation": "Samoa", "ethnicgroup": "South American" }, { "flag": "SCO", "nation": "Scotland", "ethnicgroup": "Caucasian" }, { "flag": "SEN", "nation": " Senegal", "ethnicgroup": "African" }, { "flag": "SEY", "nation": "Seychelles", "ethnicgroup": "African" }, { "flag": "SIN", "nation" : "Singapore", "ethnicgroup": "Asian" }, { "flag": "SKN", "nation": "Saint Kitts and Nevis", "ethnicgroup": "African" }, { "flag": "SLE", "nation": "Sierra Leone", "ethnicgroup": "African" }, { "flag": "SLV", "nation": "Salvador", "ethnicgroup": "South American" }, { "flag": "SMR", "nation": "San Marino", "ethnicgroup": "Italmed" }, { "flag": "SOL", "nation": "Solomon Islands", "ethnicgroup" : "South American" }, { "flag": "SOM", "nation": "Somalia", "ethnicgroup": "African" }, { "flag": " SRB", "nation": "Serbia", "ethnicgroup": "YugoGreek" }, { "flag": "SRI", "nation": "Sri Lanka", "ethnicgroup": "MESA" }, { "flag": "SSD", "nation": "South Sudan", "ethnicgroup": "African" }, { "flag": "STP", "nation": "São Tomé and Príncipe", "ethnicgroup": "African" }, { "flag": "SUD", "nation": "Sudan", "ethnicgroup": "African" }, { "flag": "SUI", "nation": "Switzerland", "ethnicgroup": "Central European" }, { "flag": "SUR", "nation": "Suriname", "ethnicgroup": "African" }, { "flag": "SVK", "nation": " Slovakia", "ethnicgroup": "Central European" }, { "flag": "SVN", "nation": "Slovenia", "ethnicgroup": "YugoGreek" }, { "flag": "SWE", "nation": "Sweden", "ethnicgroup": "Scandinavian" }, { "flag": "SWZ", "nation": "Swaziland", "ethnicgroup": "African" }, { "flag": "SYR ", "nation": "Syria", "ethnicgroup": "MENA" }, { "flag": "TAH", "nation": "Tahiti", "ethnicgroup": "South American" }, { "flag": "TAN", "nation": "Tanzania", "ethnicgroup": "African" }, { "flag": "TCA", "nation": " Turks and Caicos Islands", "ethnicgroup": "African" }, { "flag": "TGA", "nation": "Tonga Islands", "ethnicgroup": "South American" }, { "flag": " THA", "nation": "Thailand", "ethnicgroup": "Seasian" }, { "flag": "TJK", "nation": "Tajikistan", "ethnicgroup": "MESA" }, { "flag": "TKM", "nation": "Turkmenistan", "ethnicgroup": "MESA" }, { "flag": "TLS", "nation": "East Timor", "ethnicgroup": "Seasian " }, { "flag": "TOG", "nation": "Togo", "ethnicgroup": "African" }, { "flag": "TPE", "nation": "Chinese Taipei", "ethnicgroup" : "Asian" }, { "flag": "TRI", "nation": "Trinidad and Tobago", "ethnicgroup": "African" }, { "flag": "TUN", "nation": "Tunisia", "ethnicgroup": "MENA" }, { "flag": "TUR", "nation": "Turkey", "ethnicgroup": "MENA" }, { "flag": "UAE", "nation": "United Arab Emirates", "ethnicgroup": "MENA" }, { "flag": "UGA", "nation": "Uganda", "ethnicgroup": "African" }, { "flag": "UKR", "nation": "Ukraine", "ethnicgroup": "EECA" }, { "flag": "URU", "nation": "Uruguay", "ethnicgroup": "South American" }, { "flag": "USA", "nation": "United States", "ethnicgroup": "SpanMed" }, { "flag": "UZB", "nation": "Uzbekistan", "ethnicgroup": "MESA" }, { "flag": "VAN", "nation": "Vanuatu", "ethnicgroup": "South American" }, { "flag": "VEN", "nation": "Venezuela", "ethnicgroup": "South American" }, { "flag": "VGB", "nation": "Virgin Islands", "ethnicgroup": "African" }, { "flag": "LIFE", "nation": "Vietnam", "ethnicgroup": "Seasian" }, { "flag": "VIN", "nation": "Saint -Vincent", "ethnicgroup": "African" }, { "flag": "VIR", "nation": "US Virgin Islands", "ethnicgroup": "African" }, { "flag": "WAL", "nation": "nation of Wales", "ethnicgroup": "Caucasian" }, { "flag": "YEM", "nation": "Yemen", "ethnicgroup": "MENA" }, { "flag": "ZAM", "nation": "Zambia", "ethnicgroup": "African" }, { "flag": "ZIM", "nation": "Zimbabwe", "ethnicgroup": "African" } ]

# Start timer & counter
startTime = time.time()
playersProcessed = 0

# Check if the .rtf file exists, if it does, open it. If it doesn't, throw an error.
if os.path.exists(".\\Newgen_Faces.rtf") == True:
    newgen_faces_rtf = open(".\\Newgen_Faces.rtf", "r+", encoding="utf8")
    text_lines = newgen_faces_rtf.readlines()
else : 
    print("ERROR : \"Newgen_Faces.rtf\" DOES NOT EXIST.")
    sys.exit()

# Read the lines in Newgen_Faces.rtf one-by-one.
try:
    for line in text_lines:
        # First, check if the line is a valid player line, or filler.
        if line.startswith('\n') or line.startswith('| --------') or line.startswith('| UID') :
            continue
        else:
            # Search for the data in Newgen_Faces.rtf
            info = line[2:].split('| ')
            playerUID = info[0].strip()

            # Check if the data is in a valid format, ie. using the supplied FM22 View.
            if playerUID.isdigit() == False:
                print("ERROR : PLEASE MAKE SURE YOU ARE USING A VALID VIEW FILTER THAT IS COMPATIBLE WITH THIS SCRIPT")
                continue
                
            # Grab the data from the View and clean it up.
            playerNationality = info[1].strip()
            playerSecondNationality = info[2].strip()
            playerName = info[3].strip()
            playerHairLength = info[4].strip()
            playerHairColour = info[5].strip()
            playerSkinColour = info[6].strip()
            print("• "+playerName+" - NAT : "+playerNationality+' - ID : '+playerUID)

            # Open config.xml, check if current Player ID already exists. If it exists, skip it.
            config_xml = open("config.xml")
            if(playerUID in config_xml.read()):
                continue
            else:

                ##### Here we check the ethnic group with the game ethnic value #####
                if playerSkinColour == '1':
                    playerEthnicity = 'South American'
                elif playerSkinColour == '2':
                    playerEthnicity = 'MENA'
                elif playerSkinColour == '3':
                    playerEthnicity = 'African'
                elif playerSkinColour == '4':
                    playerEthnicity = 'MESA'
                elif playerSkinColour == '5':
                    playerEthnicity = 'Seasian'
                elif playerSkinColour == '6':
                    playerEthnicity = 'MESA'
                elif playerSkinColour == '7':
                    playerEthnicity = 'South American'
                elif playerSkinColour == '8' :
                    playerEthnicity = 'Seasian'
                elif playerSkinColour == '9':
                    playerEthnicity = 'African'
                elif playerSkinColour == '10':
                    playerEthnicity = 'Asian'
                ##### For europeans I applied some differences, I define the ethnic group by nation #####
                else:
                    for nation in listnations:
                        if nation["flag"].upper() == playerNationality:
                            playerEthnicity = nation['ethnicgroup']
                            playerNation = nation['nation']
                            print(nation)
    #                        if playerEthnicity == 'South european' or playerEthnicity == 'North european':            ##### Not necessary since secondary nationalities are already sorted by skin color before #####
    #                            if playerSecondNationality == '':
    #                                playerEthnicity = nation['ethnicgroup']
    #                            else:
    #                                for nation2 in listnations:
    #                                    if nation2['flag'] == playerNationality:
    #                                        playerEthnicity = nation2['ethnicgroup']


                #for nation in listnations:
                    #if nation['flag'].upper() == playerNationality:
                        #playerNation = nation['nation']

                ##### Here we pick a face for the player in the good ethnic group folder #####
                listFaces = os.listdir('.\\' + str(playerEthnicity) + '\\')
                playerFace = random.choice(listFaces)
                fileName, fileExtension = os.path.splitext(playerFace)

                ##### Here we put the picked face in the folder and write the line for the config.xml #####
                #shutil.copy(".\\Faces ethnic script\\"+playerEthnicity+'\\'+playerFace,".\\Faces ethnic script\\IN GAME Faces Regens\\"+str(playerUID)+".png")
                line = "\t\t<record from='"+str(playerEthnicity)+"/"+str(fileName)+"' to='graphics/pictures/person/"+str(playerUID)+"/portrait'/>\n"
                my_file = open("config.xml", "r")
                config = my_file.readlines()
                config.insert(-3, line)
                my_file.close()
                my_file = open("config.xml", "w")
                config = "".join(config)
                my_file.write(config)
                my_file.close()

                # Counter for myself
                playersProcessed += 1

                print('\t=> Face added : '+playerName+' - '+playerUID+'\n')
                #print('\t=> Face added : '+playerName+' - '+playerNation+' - '+playerEthnicity+'\n')
except:
    print(nation.keys())
    raise

endTime = time.time()
timePassedSeconds = endTime - startTime
timePassedMinutes = timePassedSeconds / 60
print(str(timePassedSeconds)+' seconds '+' / '+str(timePassedMinutes)+' minutes have elapsed, processing '+str(playersProcessed)+' players')

print("-------- END OF THE SCRIPT YOU CAN CLOSE IT --------")



