from googlesearch import search
import csv
import sys

# All color and other escape sequences are stored heare
clearScreen = '\x1b[2J'
lightWhite = "\x1b[1;37m"
green = "\x1b[0;32m"
lightGreen = "\x1b[1;32m"
lightPurple = "\x1b[1;35m"
lightRed = "\x1b[1;31m"
yellow = "\x1b[1;33m"
stopColor = "\x1b[0m"

# Variables affected by the users prompts
urls = False
titles = False
descriptions = False

columns = ""

def checkInput(prompt, bool):
    prompt.lower()
    if prompt == "y" or prompt == "yes":
        urls = True
        columns += "URL "
        print("urls selected")

    if prompt == "n" or urlq == "no":
        print("urls not Selected")

    else:
        print("Invalid input, exiting program")
        sys.exit()
    


print(clearScreen)
print("{}Welcome to the Google Search Data Aggerator{}".format(lightPurple, stopColor))

print("-------------------------------------------------------")
print("6609798{}Google{}gyu9450td3209d{}Search{}2156D5677811y876oiu86p".format(green, stopColor, green, stopColor))
print("cweonjf{}Data{}3940t340{}Aggerator{}zoc8zc96a6a86q9adf90w8fd7wf".format(green, stopColor, green, stopColor))
print('-------------------------------------------------------')
print()

query = input("{}Enter the search you would like to make: {}".format(lightGreen, stopColor))

print()
print("{}Select the parameters you would like to tabulate: {}".format(lightGreen, stopColor))

urlq = input("{}Urls y or n: {}".format(lightPurple, stopColor))
urlq.lower()
if urlq == "y" or urlq == "yes":
    urls = True
    columns += "URL "
    print("urls selected")

if urlq == "n" or urlq == "no":
    print("urls not Selected")

else:
    print("Invalid input, exiting program")
    sys.exit()


titleq = input("{}Title y or n: {}".format(lightRed, stopColor))
titleq = titleq.lower()
if titleq == "y" or titleq == "yes":
    titles = True
    columns += "TITLE "
    print("titles selected")

elif titleq == "n" or titleq == "no":
    print("titles not Selected")

else:
    print("Invalid input, exiting program")
    sys.exit

descq = input("{}Description y or n: {}".format(yellow, stopColor))
descq = descq.lower()
if descq == "y" or descq == "yes":
    descriptions = True
    columns += "DESCRIPTIONS "
    print("titles selected")

elif descq == "n" or descq == "no":
    print("Descriptions not Selected")

else:
    print("Invalid input, exiting program")
    sys.exit

print()
numResults = input("{}Enter the number of searches you would like to tabulate: {}".format(lightGreen, stopColor))

print()
print("{}A CSV file with {} rows and the columnns of {}: {}".format(lightWhite, numResults, columns, stopColor))

search = search(query, num_results=numResults, advanced=True)

outputArray = []
for s in search:
    s.url = s.url.replace(',', ' ')
    s.title = s.title.replace(',', ' ')
    s.description = s.description.replace(',', ' ')
    outputArray.append([s.url, s.title, s.description])



# sys.exit()

with open('results.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)

    # write the header
    writer.writerow(["URL", "Title", "Description"])

    # write multiple rows
    writer.writerows(outputArray)