import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['LMS1']
books = mydb['BOOKS_INFORMATION']
user = mydb['USER_INFORMATION']
admin = mydb['ADMIN_INFORMATION']

def createAdmin():
    print('__admin account create__')
    print('Enter security key ')
    seNumber = str(input(''))
    if seNumber == 'pratik':
            print('Enter your username : ')
            admin_name = str(input(''))
            print('Enter your password : ')
            adminPassword1 = str(input(''))
            admin_id = adminPassword1 + admin_name
            adminAccountCreateData = {'_id' : admin_id, 'admin_user_name' : admin_name, 'admin_password' : adminPassword1}
            x = admin.insert_one(adminAccountCreateData)
            if x.inserted_id == admin_id:
                print(admin_name, ', account successfully created.\n')
            adminSecurity()
    else:
        print('Security Hint : p....k')
        exitApp()
    return
def userMenu():
    print('0. Exit')
    print('1. Issue a book')
    print('2. Return a book')
    print('3. Search a book')
    print('4. View book')
    print('5. Change password')
    userOption = int(input(''))
    if userOption == 0:
        exitApp()
    elif userOption == 1:
        print('__Issue BOOK__')
        issueBook()
    elif userOption == 2:
        print('__Return a book__')
        returnBook()
    elif userOption == 3:
        print('__Search a book__')
        searchBookByUser()
    elif userOption == 4:
        print('__View Book__')
        viewBookByUser()
    elif userOption == 5:
        print('__Change Password__')
        changeUserPasswordByUser()
    else:
        print('Wrong input. Try again.')
        userMenu()
    return

def issueBook():
    t = 0
    print('Select a option : ')
    print('1. Search by book name')
    print('2. Search a book by category')
    searchOption = int(input(''))
    if searchOption == 1:
        print('__SEARCH A BOOK BY NAME__')
        print('Enter a book name : ')
        searchBookName = str(input(''))
        for s1 in books.find({'Book_Name': searchBookName},{'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            #print(s1)
            t = 1
        if t == 1:
            print('Book found! Do you want to issue the book ?')
            print('1. Yes')
            print('2. No')
            option = int(input(''))
            if option == 1:
                dbookdata = {'Book_Name': searchBookName}
                books.delete_one(dbookdata)
                print(searchBookName, 'issued.')
                userMenu()

            elif option == 2:
                userMenu()

        elif t == 0:
            print('Not Found')
            userMenu()

    elif searchOption == 2:
        print('__SEARCH A BOOK BY CATEGORY__')
        s2Category = selectBookCategory()
        print('Enter a book name : ')
        searchBookName1 = str(input(''))
        for s2 in books.find({'Category': s2Category, 'Book_Name': searchBookName1}, {'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            #print(s2)
            t = 1

        if t == 1:
            print('Book found! Do you want to issue the book ?')
            print('1. Yes')
            print('2. No')
            option = int(input(''))
            if option == 1:
                dbookdata = {'Category': s2Category, 'Book_Name': searchBookName1}
                books.delete_one(dbookdata)
                print(searchBookName1, 'issued.')
                userMenu()
            elif option == 2:
                userMenu()
        elif t == 0:
            print('Not Found')
            userMenu()
    return

def returnBook():
    bookCategory = selectBookCategory()
    print('Enter book name : ')
    bookName = str(input(''))
    print('Enter writter name : ')
    writterName = str(input(''))
    bookId = bookCategory + bookName + writterName
    abookData = {'_id': bookId, 'Category': bookCategory, 'Book_Name': bookName, 'Writter_Name': writterName, 'Number_OF_Books': 1}
    x = books.insert_one(abookData)
    if x.inserted_id == bookId:
        print(bookName, 'returned successfully.\n')
    userMenu()
    return

def searchBookByUser():
    t = 0
    print('Select a option : ')
    print('1. Search by book name')
    print('2. Search a book by category')
    searchOption = int(input(''))
    if searchOption == 1:
        print('__SEARCH A BOOK BY NAME__')
        print('Enter a book name : ')
        searchBookName = str(input(''))
        for s1 in books.find({'Book_Name': searchBookName},{'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            print(s1)
            t = 1
        if t == 0:
            print('Not Found')
        userMenu()

    elif searchOption == 2:
        print('__SEARCH A BOOK BY CATEGORY__')
        s2Category = selectBookCategory()
        print('Enter a book name : ')
        searchBookName1 = str(input(''))
        for s2 in books.find({'Category': s2Category, 'Book_Name': searchBookName1},{'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            print(s2)
            t = 1
        if t == 0:
            print('Not Found')
        userMenu()
    return

def changeUserPasswordByUser():
    us2 = 0
    print('__CHANGE USER PASSWORD__')
    print('Enter username : ')
    UserName3 = str(input(''))
    print('Enter user password : ')
    Password3 = str(input(''))
    for s1 in user.find({'user_Name': UserName3, 'user_Password': Password3},{'_id': 0, 'user_Name': 1, 'user_Password': 1}):
        # print(s1)
        us2 = 1
    if us2 == 1:
        print('Enter your new password : ')
        NewPassword = str(input(''))
        oldPassword1 = {'user_Password': Password3}
        newPassword1 = {'$set': {'user_Password': NewPassword}}
        user.update_one(oldPassword1, newPassword1)
        print('Password change successfully!')
        userMenu()

    elif us2 == 0:
        print('Wrong username or password! Try again.')
        changeUserAccountPassword()
    return

def userLogIn():
    as1 = 0
    print('__USER SECURITY CHECK__')
    print('Enter your username : ')
    UserName = str(input(''))
    print('Enter your password : ')
    Password = str(input(''))
    for s1 in user.find({'user_Name': UserName, 'user_Password': Password},{'_id': 0, 'user_Name': 1, 'user_Password': 1}):
        # print(s1)
        as1 = 1
    if as1 == 1:
        print(UserName, ',successfully logged in!')
        userMenu()
    elif as1 == 0:
        print('Wrong username or password! Try again.')
        userLogIn()
    return

def viewBookByUser():
    v = 0
    print('Select a option : ')
    print('1. View books of a category')
    print('2. View all books')
    viewBookOption = int(input(''))
    if viewBookOption == 1:
        print('__VIEW ALL BOOKS OF A CATEGORY__')
        v1Category = selectBookCategory()
        for v1 in books.find({'Category': v1Category},{'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            print(v1)
            v = 1
        if v == 0:
            print('No book are stored in the category!')
        userMenu()

    elif viewBookOption == 2:
        for v2 in books.find({}, {'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            print(v2)
            v = 1
        if v == 0:
            print('No book are stored!')
        userMenu()
    else:
        print('Wrong Input! Try again.')
        viewBooks()
    return

def createUserAccount():
    print('__USER ACCOUNT CREATE__')
    print('Enter username : ')
    userName1 = str(input(''))
    print('Enter user password : ')
    user1Password = str(input(''))
    userID = userName1 + user1Password
    userAccountCreateData = {'_id' : userID, 'user_Name' : userName1, 'user_Password' : user1Password}
    a = user.insert_one(userAccountCreateData)
    if a.inserted_id == userID:
        print(userName1 ,',account successfully created!')
        adminMenu()
    return

def adminLogInOrSignUp():
    print('Select a option : ')
    print('1. Sign Up')
    print('2. Log In')
    check1option = int(input(''))
    if check1option == 1:
        createAdminAccount()
    elif check1option == 2:
        adminSecurity()
    else:
        print('Wrong input. Try again.')
        adminLogInOrSignUp()
    return

def adminSecurity():
    as1 = 0
    print('__ADMIN SECURITY CHECK__')
    print('Enter your username : ')
    adminUserName = str(input(''))
    print('Enter your password : ')
    adminPassword = str(input(''))
    for s1 in admin.find({'admin_user_name' : adminUserName, 'admin_password' : adminPassword}, {'_id' : 0, 'admin_user_name' : 1, 'admin_password' : 1}):
        #print(s1)
        as1 = 1
    if as1 == 1:
        print(adminUserName, 'successfully logged in!')
        adminMenu()
    elif as1 == 0:
        print('Wrong username or password! Try again.')
        adminSecurity()
    return

def selectAccountType():
    print('Select account type : ')
    print('1. Admin')
    print('2. User')
    acType = int(input(''))
    if acType == 1:
        print('__ADMIN__')
        adminLogInOrSignUp()
        #adminSecurity()
        #adminMenu()
    elif acType == 2:
        print('__USER__')
        userLogIn()
    else:
        print('Wrong input! Try Again.')
        selectAccountType()
    return

def adminMenu():
    print('\nSelect an option : ')
    print('0. Exit')
    print('1. Add book')
    print('2. Search a book')
    print('3. Delete a book')
    print('4. Edit book information')
    print('5. View book')
    print('6. Create a user account')
    print('7. Change user account password')
    print('8. Delete a user account')
    print('9. Change admin password')
    print('10. Delete admin account')
    print('11. View all admin account')
    print('12. View all user account')
    print('')
    adminOption = int(input(''))
    if adminOption == 0:
        exitApp()
    elif adminOption == 1:
        print('__ADD BOOK__')
        addBook()
    elif adminOption == 2:
        print('__Search Book__')
        searchBooks()
    elif adminOption == 3:
        print('__DELETE BOOK__')
        deleteBook()
    elif adminOption == 4:
        print('__EDIT BOOK INFORMATION__')
        editInformation()
    elif adminOption == 5:
        print('__VIEW BOOKS__')
        viewBooks()
    elif adminOption == 6:
        createUserAccount()
    elif adminOption == 7:
        changeUserAccountPassword()
    elif adminOption == 8:
        deleteUserAccount()
    elif adminOption == 9:
        print('__CHANGE PASSWORD__')
        changeAdminPassword()
    elif adminOption == 10:
        print('__DELETE ADMIN ACCOUNT__')
        deleteAdminAccount()
    elif adminOption == 11:
        print('__VIEW ALL ADMIN ACCOUNT__')
        viewAdminAccounts()
    elif adminOption == 12:
        print('__VIEW USER ACCOUNT__')
        viewUserAccounts()
    else:
        print('Wrong Input! Try again.')
        adminMenu()
    return

def changeUserAccountPassword():
    us2 = 0
    print('__CHANGE USER PASSWORD__')
    print('Enter username : ')
    UserName3 = str(input(''))
    print('Enter user password : ')
    Password3 = str(input(''))
    for s1 in user.find({'user_Name': UserName3, 'user_Password': Password3},{'_id': 0, 'user_Name': 1, 'user_Password': 1}):
        # print(s1)
        us2 = 1
    if us2 == 1:
        print('Enter your new password : ')
        NewPassword = str(input(''))
        oldPassword1 = {'user_Password': Password3}
        newPassword1 = {'$set': {'user_Password': NewPassword}}
        user.update_one(oldPassword1, newPassword1)
        print('Password change successfully!')
        userMenu()

    elif us2 == 0:
        print('Wrong username or password! Try again.')
        changeUserAccountPassword()
    return

def deleteUserAccount():
    ua = 0
    print('Enter user username : ')
    user11name = str(input(''))
    for s1 in user.find({'user_Name': user11name}, {'_id': 0, 'user_Name': 1, 'user_Password': 1}):
        # print(s1)
        ua = 1
    if ua == 1:
        user11data = {'user_Name': user11name}
        user.delete_one(user11data)
        print(user11name, ',account deleted!')
        adminMenu()

    elif ua == 0:
        print('Wrong username! Try again.')
        adminMenu()
    return 0

def viewUserAccounts():
    sa = 0
    for v2 in user.find({}, {'_id': 0, 'user_Name': 1, 'user_Password': 1}):
        print(v2)
        sa = 1
    if sa == 0:
        print('No user accounts!')
    adminMenu()
    return

def viewAdminAccounts():
    va = 0
    for v2 in admin.find({}, {'_id' : 0, 'admin_user_name' : 1, 'admin_password' : 1}):
        print(v2)
        va = 1
    if va == 0:
        print('No admin accounts!')
    adminMenu()
    return

def deleteAdminAccount():
    da = 0
    print('Enter admin username : ')
    admin11name = str(input(''))
    for s1 in admin.find({'admin_user_name' : admin11name}, {'_id' : 0, 'admin_user_name' : 1, 'admin_password' : 1}):
        #print(s1)
        da = 1
    if da == 1:
        admin11data = {'admin_user_name' : admin11name}
        admin.delete_one(admin11data)
        print(admin11name, 'account deleted!')
        adminMenu()

    elif da == 0:
        print('Wrong username! Try again.')
        adminMenu()
    return 0

def changeAdminPassword():
    as2 = 0
    print('__CHANGE ADMIN PASSWORD__')
    print('Enter your username : ')
    adminUserName3 = str(input(''))
    print('Enter your password : ')
    adminPassword3 = str(input(''))
    for s1 in admin.find({'admin_user_name': adminUserName3, 'admin_password': adminPassword3},{'_id': 0, 'admin_user_name': 1, 'admin_password': 1}):
        # print(s1)
        as2 = 1
    if as2 == 1:
        print('Enter your new password : ')
        adminNewPassword = str(input(''))
        oldPassword = {'admin_password' : adminPassword3}
        newPassword = {'$set': {'admin_password': adminNewPassword}}
        admin.update_one(oldPassword, newPassword)
        print('Password change successfully!')
        adminSecurity()

    elif as2 == 0:
        print('Wrong username or password! Try again.')
        changeAdminPassword()
    return

def editInformation():
    t = 0
    print('Select a option : ')
    print('1. Search by book name')
    print('2. Search a book by category')
    searchOption = int(input(''))
    if searchOption == 1:
        print('__SEARCH A BOOK BY NAME__')
        print('Enter a book name : ')
        searchBookName = str(input(''))
        for s1 in books.find({'Book_Name': searchBookName}, {'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            t = 1
        if t == 1:
            print(searchBookName, 'found!')
            print('Select a option : ')
            print('1. Change book name.')
            print('2. Change writer name.')
            print('3. Change number of books.')
            upoption = int(input(''))

            if upoption == 1:
                print('Enter new book name : ')
                upBookName = str(input(''))
                oldName = {'Book_Name': searchBookName}
                newName = {'$set': { 'Book_Name': upBookName }}
                books.update_one(oldName, newName)
                print(searchBookName, 'changed to', upBookName)
                adminMenu()

            elif upoption == 2:
                print('Enter old writter name : ')
                oldWriterName = str(input(''))
                print('Enter new writter name : ')
                newWritterName = str(input(''))
                oldName2 = {'Writter_Name': oldWriterName}
                newName2 = {'$set': {'Writter_Name': newWritterName}}
                books.update_one(oldName2, newName2)
                print(oldWriterName, 'changed to', newWritterName)
                adminMenu()

            elif upoption == 3:
                print('Enter current number of books : ')
                currentNumberofBooks =int(input(''))
                print('Enter new number of books : ')
                newNumberofBooks = int(input(''))
                oldName1 = {'Number_OF_Books': currentNumberofBooks}
                newName1 = {'$set': {'Number_OF_Books': newNumberofBooks}}
                books.update_one(oldName1, newName1)
                print(currentNumberofBooks, 'changed to', newNumberofBooks)
                adminMenu()

            else:
                print('Wrong input! Try again.')
                adminMenu()

        elif t == 0:
            print('Not Found')
        adminMenu()

    elif searchOption == 2:
        print('__SEARCH A BOOK BY CATEGORY__')
        s2Category = selectBookCategory()
        print('Enter a book name : ')
        searchBookName1 = str(input(''))
        for s2 in books.find({'Category': s2Category, 'Book_Name': searchBookName1}, {'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            print(s2)
            t = 1
        if t == 1:
            print('Select a option : ')
            print('1. Change book name.')
            print('2. Change writer name.')
            print('3. Change number of books.')
            upoption = int(input(''))
            if upoption == 1:
                print('Enter new book name : ')
                upBookName = str(input(''))
                oldName = {'Book_Name': searchBookName1}
                newName = {'$set': { 'Book_Name': upBookName }}
                books.update_one(oldName, newName)
                print(searchBookName1, 'changed to', upBookName)
                adminMenu()

            elif upoption == 2:
                print('Enter old writter name : ')
                oldWriterName = str(input(''))
                print('Enter new writter name : ')
                newWritterName = str(input(''))
                oldName2 = {'Writter_Name': oldWriterName}
                newName2 = {'$set': {'Writter_Name': newWritterName}}
                books.update_one(oldName2, newName2)
                print(oldWriterName, 'changed to', newWritterName)
                adminMenu()

            elif upoption == 3:
                print('Enter current number of books : ')
                currentNumberofBooks =int(input(''))
                print('Enter new number of books : ')
                newNumberofBooks = int(input(''))
                oldName1 = {'Number_OF_Books': currentNumberofBooks}
                newName1 = {'$set': {'Number_OF_Books': newNumberofBooks}}
                books.update_one(oldName1, newName1)
                print(currentNumberofBooks, 'changed to', newNumberofBooks)
                adminMenu()

            else:
                print('Wrong input! Try again.')
                adminMenu()
        if t == 0:
            print('Not Found')
        adminMenu()

    else:
        print('Wrong input! Try again!')
        searchBooks()
    return

def viewBooks():
    v = 0
    print('Select a option : ')
    print('1. View books of a category')
    print('2. View all books')
    viewBookOption = int(input(''))
    if viewBookOption == 1:
        print('__VIEW ALL BOOKS OF A CATEGORY__')
        v1Category = selectBookCategory()
        for v1 in books.find({'Category': v1Category}, {'_id' : 0, 'Category' : 1, 'Book_Name' : 1, 'Writter_Name' : 1, 'Number_OF_Books' : 1}):
            print(v1)
            v = 1
        if v == 0:
            print('No book are stored in the category!')
        adminMenu()
    elif viewBookOption == 2:
        for v2 in books.find({}, {'_id' : 0, 'Category' : 1, 'Book_Name' : 1, 'Writter_Name' : 1, 'Number_OF_Books' : 1}):
            print(v2)
            v = 1
        if v == 0:
            print('No book are stored!')
        adminMenu()
    else:
        print('Wrong Input! Try again.')
        viewBooks()
    return

def searchBooks():
    t = 0
    print('Select a option : ')
    print('1. Search by book name')
    print('2. Search a book by category')
    searchOption = int(input(''))
    if searchOption == 1:
        print('__SEARCH A BOOK BY NAME__')
        print('Enter a book name : ')
        searchBookName = str(input(''))
        for s1 in books.find({'Book_Name' : searchBookName}, {'_id' : 0, 'Category' : 1, 'Book_Name' : 1, 'Writter_Name' : 1, 'Number_OF_Books' : 1}):
            print(s1)
            t = 1
        if t == 0:
            print('Not Found')
        adminMenu()

    elif searchOption == 2:
        print('__SEARCH A BOOK BY CATEGORY__')
        s2Category = selectBookCategory()
        print('Enter a book name : ')
        searchBookName1 = str(input(''))
        for s2 in books.find({'Category': s2Category, 'Book_Name': searchBookName1},{'_id': 0, 'Category': 1, 'Book_Name': 1, 'Writter_Name': 1, 'Number_OF_Books': 1}):
            print(s2)
            t = 1
        if t == 0:
            print('Not Found')
        adminMenu()

    else:
        print('Wrong input! Try again!')
        searchBooks()
    return

def selectBookCategory():
    category =''
    print('Chose category of the book : ')
    print('1. CSE')
    print('2. Software')
    print('3. IT')
    print('4. EEE')
    print('5. Civil')
    print('6. BBA')
    selectCategory = int(input(''))
    if selectCategory == 1:
        category = 'CSE'
    elif selectCategory == 2:
        category = 'Software'
    elif selectCategory == 3:
        category = 'IT'
    elif selectCategory == 4:
        category = 'EEE'
    elif selectCategory == 5:
        category = 'Civil'
    elif selectCategory == 6:
        category = 'BBA'
    else:
        print('Wrong input. Try again!')
        category = selectBookCategory()
    return category

def addBook():
    bookCategory = selectBookCategory()
    print('Enter book name : ')
    bookName = str(input(''))
    print('Enter writter name : ')
    writterName = str(input(''))
    print('How many books you want to store : ')
    numberOfBooks = int(input(''))

    bookId = bookCategory + bookName + writterName
    abookData = {'_id' : bookId, 'Category' : bookCategory, 'Book_Name' : bookName, 'Writter_Name' : writterName, 'Number_OF_Books' : numberOfBooks}
    x = books.insert_one(abookData)

    if x.inserted_id == bookId:
        print(numberOfBooks, bookName, 'added successfully.\n')
    adminMenu()
    return

def deleteBook():
    d1 = 0
    print('Select a option : ')
    print('1. Delete a book')
    print('2. Delete all books of category')
    print('3. Delete all books')
    doption = int(input(''))

    if doption == 1:
        print('__DELETE A SINGLE BOOk__')
        dbookCategory = selectBookCategory()
        print('Enter book name : ')
        dbookName = str(input(''))
        for s1 in books.find({'Book_Name' : dbookName}, {'_id' : 0, 'Category' : 1, 'Book_Name' : 1, 'Writter_Name' : 1, 'Number_OF_Books' : 1}):
            d1 = 1
        if d1 == 1:
            print(dbookName, 'book found!')
            print('Do you want to delete the book : ')
            print('1. Yes')
            print('2. No')
            d1Option = int(input(''))
            if d1Option == 1:
                print('How many books you want to delete?')
                #dNumberofBook = int(input(''))
                dbookdata = {'Category': dbookCategory, 'Book_Name': dbookName}
                books.delete_one(dbookdata)
                print(dbookName, 'deleted.')
                adminMenu()

            elif d1Option == 2:
                adminMenu()

            else:
                print('Wrong Input! Try again.')
                adminMenu()
        elif d1 == 0:
            print(dbookName, 'book not found!')
            adminMenu()

    elif doption == 2:
        print('__DELETE ALL BOOKS OF A CATEGORY__')
        dcbookCategory = selectBookCategory()
        d2 = books.delete_many({'Category': dcbookCategory})
        print(d2.deleted_count, 'books deleted.')
        adminMenu()

    elif doption == 3:
        print('__DELETE ALL BOOKS__')
        d3 = books.delete_many({})
        print(d3.deleted_count, 'books deleted.')
        adminMenu()

    else:
        print('Wrong answer! Try again.')
        adminMenu()
    return

def exitApp():
    exit(0)

def welcomeText():
     print('Library Management System V-1.0')
     return

welcomeText()

selectAccountType()