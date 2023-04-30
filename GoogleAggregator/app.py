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
# urls = False
# titles = False
# descriptions = False

outputColumns = [] 

def checkInput(inpt, val):
    inpt.lower()
    print(inpt)
    if inpt == "y" or inpt == "yes":
        outputColumns.append(val)
        print(val + " selected")
        return

    if inpt == "n" or inpt == "no":
        print(val + " not Selected")
        return

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

checkInput(urlq, "URL")
print(outputColumns)


titleq = input("{}Title y or n: {}".format(lightRed, stopColor))
checkInput(titleq, "TITLE")
print(outputColumns)

descq = input("{}Description y or n: {}".format(yellow, stopColor))
checkInput(descq, "DESCRIPTION")
print(outputColumns)



print()
numResults = input("{}Enter the number of searches you would like to tabulate: {}".format(lightGreen, stopColor))

print()
print("{}A CSV file with {} rows and the columnns of: {} {} will be generated".format(lightWhite, numResults, outputColumns, stopColor))

numResults = int(numResults)
search = search(query, num_results=numResults, advanced=True)

outputArray = []

if len(outputColumns) == 1 and outputColumns[0] == "URL":
    for s in search:
        s.url = s.url.replace(',', ' ')
        outputArray.append([s.url])

if len(outputColumns) == 1 and outputColumns[0] == "TITLE":
    for s in search:
        s.title = s.title.replace(',', ' ')
        outputArray.append([s.title])

if len(outputColumns) == 1 and outputColumns[0] == "DESCRIPTION":
    for s in search:
        s.description = s.description.replace(',', ' ')
        outputArray.append([s.description])

if len(outputColumns) == 2 and outputColumns[0] == "URL" and outputColumns[1] == "TITLE":
    for s in search:
        s.url = s.url.replace(',', ' ')
        s.title = s.title.replace(',', ' ')
        outputArray.append([s.url, s.title])

if len(outputColumns) == 2 and outputColumns[0] == "URL" and outputColumns[1] == "DESCRIPTION":
    for s in search:
        s.url = s.url.replace(',', ' ')
        s.description = s.description.replace(',', ' ')
        outputArray.append([s.url, s.description])

if len(outputColumns) == 2 and outputColumns[0] == "TITLE" and outputColumns[1] == "DESCRIPTION":
    for s in search:
        s.title = s.title.replace(',', ' ')
        s.description = s.description.replace(',', ' ')
        outputArray.append([s.title, s.description])


if len(outputColumns) == 3:
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