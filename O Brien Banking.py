import csv

def addaccount():
    customerID = input("Enter a Customer ID: ")
    if customerID == (""):
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    firstname = input("Enter the Customer's first name: ")
    if firstname == (""):
        print("Invalid input. Try again")
        addaccount()
    elif firstname.isnumeric() == True:
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    surname = input("Enter the Customer's second name: ")
    if surname == (""):
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    elif surname.isnumeric() == True:
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    DOA = input("Enter the Customer's date of Opening an Account: ")
    if DOA == (""):
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    openbal = input("Enter the Customer's Opening Balance: ")
    if openbal == (""):
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    elif openbal.isnumeric() == False:
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
    acctype = input("Enter the Customer's Account Type: ")
    if acctype == (""):
        print("Invalid Account Type. Try again")
        print("***************************************")
        addaccount()
    elif acctype.isnumeric() == True:
        print("Invalid input. Try again")
        print("***************************************")
        addaccount()
        
    #use a series of imput statements
    with open ('Bank Details.txt','a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([str(customerID),firstname,surname,DOA,openbal,acctype])
        print ("Successfully added")
    csvfile.close()
    
    #use a series of imput statements
    print("")
    menu()
    


def searchaccount():
    found = 0
    print("***Searching for a Customer***")
    surname = input("Enter the Customer's Surname: ")
    with open ('Bank Details.txt','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == []:
                pass
            elif surname == row[2]:
               print("") 
               print("***Customer has been found***")
               print("First Name is:", row[1])
               print("Surname is:", row[2])
               print("Date of Opening the Account is:", row[3])
               print("The Opening Balance is:", row[4])
               print("Account Type is:", row[5])
               found = 1
    if (found == 1):
        print("")
        print("Customer has been displayed.")
        print("Sending back to Menu")
        print("")
        menu()

    elif (found == 0):
        print("")
        print("Customer can not be found. Try again.")
        menu()
        
       

    
def openingbalances():
    found = 0
    print("***Display all Opening Balances of £1000+***")
    proceed = input("Are you sure?(Yes or No): ")
    if proceed == 'Yes' or proceed == 'yes':
        with open ('Bank Details.txt','r',)as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                displaybal = row[4]
                row[4] = int(row[4])
                if row == []:
                    pass
                elif int(row[4])> 1000:
                    #str(row[4]) = int(row[4]) 
                    found = 1
                    print("")
                    print("Customer name is: " + row[1] + " " + row[2])
                    print("Opening Balance is: " + displaybal)
                    
    elif proceed == 'No' or proceed == 'no':
        menu()
        
    else:
        print("Error. Incorrect option")
        menu()
        
    if found == 1:
        print("")
        print("Customer(/s) has been found")
        print("Sending back to Menu")
        menu()
    elif found == 0:
        print("")
        print("No customers have an Opening Balance of £1000+")
        menu()


    
def depositaccounts():
    found = 0
    print("***Display all Deposit Accounts***")
    proceed = input("Are you sure?(Yes or No): ")
    print("***************************************")
    if proceed == 'Yes' or proceed == 'yes':
        with open ('Bank Details.txt','r',)as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif row[5] == "Deposit":
                    found = 1
                    print("")
                    print("Customer ID is: " + row[0])
                    print("Customer name is: " + row[1] + " " + row[2])
                    print("This user's account type is Deposit")
        csvfile.close()
                          
    elif proceed == 'No' or proceed == 'no':
        print("Sending back to Menu")
        print("***************************************")
        menu()

    if found == 1:
        print("")
        print("Customer(/s) have been found and displayed")
        print("")
        menu()

    elif found == 0:
        print("")
        print("There are no Deposit accounts in the system")
        print("")
        menu()


    
def currentaccounts():
    found = 0
    print("***Display all Current Accounts***")
    proceed = input("Are you sure?(Yes or No): ")
    print("***************************************")
    if proceed == 'Yes' or proceed == 'yes':
        with open ('Bank Details.txt','r',)as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif row[5] == "Current":
                    found = 1
                    print("")
                    print("Customer ID is: " + row[0])
                    print("Customer name is: " + row[1] + " " + row[2])
                    print("This user's account type is Current")
        csvfile.close()
                          
    elif proceed == 'No' or proceed == 'no':
        print("Sending back to Menu")
        print("***************************************")
        menu()

    if found == 1:
        print("")
        print("Customer(/s) have been found and displayed")
        print("")
        menu()

    elif found == 0:
        print("")
        print("There are no Current accounts in the system")
        print("")
        menu()

def savingsaccounts():
    found = 0
    print("***Display all Savings Accounts***")
    proceed = input("Are you sure?(Yes or No): ")
    print("***************************************")
    if proceed == 'Yes' or proceed == 'yes':
        with open ('Bank Details.txt','r',)as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif row[5] == "Savings":
                    found = 1
                    print("")
                    print("Customer ID is: " + row[0])
                    print("Customer name is: " + row[1] + " " + row[2])
                    print("This user's account type is Savings")
        csvfile.close()
                          
    elif proceed == 'No' or proceed == 'no':
        print("Sending back to Menu")
        print("***************************************")
        menu()

    if found == 1:
        print("")
        print("Customer(/s) have been found and displayed")
        print("")
        menu()

    elif found == 0:
        print("")
        print("There are no Savings accounts in the system")
        print("")
        menu()



def deleteaccount():
    found = 0
    deletecustomerID = input("Enter the Customers's ID of what which you'd like to delete: ")
    while (deletecustomerID == ""):
        print("Please enter a valid ID.")
        deleteaccount()
        
    proceed = input("Are you sure?: ")
    if proceed == 'No' or proceed == 'no':
        print("Sending back to Menu")
        menu()
    elif proceed == 'Yes' or proceed == 'yes':
        #Create a new storage space
        deleterecords = []
        #Open the file in read mode
        with open ('Bank Details.txt','r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif row[0] != deletecustomerID:
                    deleterecords.append(row)
                    found = 1
                else:
                    pass
        csvfile.close()
        print(deleterecords)

        if found == 0:
            print(deletecustomerID + " can not be found.")
        else:
            with open ('Bank Details.txt','w') as csvfile:
                writer = csv.writer(csvfile)
                for row in deleterecords:
                    writer.writerow(row)
                    
            csvfile.close()
            print("Customer ID", deletecustomerID + " has been found and deleted")

    print("")
    menu()



def menu():
       print('********************************************************************************')
       print('***************************Welcome to O Brien Banking***************************')
       print('--------------------------------------------------------------------------------')
       print('How may our Banking System help you today?')
       print("-----Option List-----")
       print('1: Create a New Account')
       print('2: Search for a Customer')
       print('3: Search for Accounts with £1000+ Opening Balances')
       print('4: Find all Deposit accounts')
       print('5: Find all Current accounts ')
       print('6: Find all Savings accounts ')
       print('7: Delete an account')
       print("")
       option = input('Select an Option: ')

       if option == '1':
            addaccount()
       elif option == '2':
            searchaccount()
       elif option == '3':
            openingbalances()
       elif option == '4':
            depositaccounts()
       elif option == '5':
            currentaccounts()
       elif option == '6':
           savingsaccounts()
       elif option == '7':
           deleteaccount()
       else:
           print("Invalid Option. Try again")
           print("")
           menu()
              


#program starts here
menu()

