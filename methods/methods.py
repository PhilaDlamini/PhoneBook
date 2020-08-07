#All the necessary program methods so they are not in main
from models.User import User;
from custom_exceptions.command_not_found import CommandNotFoundException;
from models.PhoneBook import PhoneBook;
from sys import exit;
from os.path import isfile;

#The commands
createAccount = "'Create account'";
signInCommand = "'Sign in'";
viewPhoneBook = "'View phone book'";
viewContact = "'View contact'";
addContact = "'Add contact'";
deleteContact = "'Delete contact'";
deleteAccount = "'Delete account'";

#Command not found exception
commandNotFound = CommandNotFoundException('Command not found. Re-run program and try again');

'''All the command methods -- determine the flow of the program, and access all the moments below'''

#The first command in for authentication
def firstCommand():
    print('Welcome to PhoneBook Inc.');
    print('We need to authenticate you before you can access the PhoneBook');
    command = input('Enter ' + createAccount + ' to create an account, or ' + signInCommand + ' to sign in:\n');
    command = "'" + command.strip() + "'";
    
    if command == createAccount:
        addUser();
    elif command == signInCommand:
        signIn();
    else:
        raise commandNotFound;
    
def secondCommand(user):
    command = input('Run either of these commands for that action: ' + viewContact + ', ' + addContact + ', ' + deleteContact + ', ' + viewPhoneBook + ', or ' + deleteAccount + ':\n');
    command = "'" + command.strip() + "'";
    phoneBook = PhoneBook(user);
    
    if command == viewContact:
        phoneBook.viewContact();
    elif command == addContact:
        phoneBook.addContact();
    elif command ==  viewPhoneBook:
        phoneBook.viewPhoneBook();
    elif command == deleteAccount:
        user.deleteAccount();
    elif command == deleteContact:
        phoneBook.deleteContact();
    else:
        raise commandNotFound;

'''All methods accessed by command methods'''
#Creates a user account
def addUser():    
    print('Welcome to the create account tab!');
    name = input('Enter your name here: ');
    
    #Assign the user id
    if isfile(User.fileName):
        file = open(User.fileName, 'r');
        userID = len(file.read().split('\n'));
    else:
        userID = 1;
    
    print('Your ID is ', userID, '. Remember this ID. You will need it to access your phone book', sep = '');
    password = input('Input your password: ');
    passwordConfirmation = input('Re-enter your password: ');
    
    if password.strip() == passwordConfirmation.strip():
        user = User(name = name, password = password, userID = userID);
        usersFile = open(User.fileName, 'a');
        usersFile.write(user.toDataString());
        usersFile.close();
        print('Account created successfully!!');
    else:
        print("Passwords didn't match. Re-run program to create account");
        exit();

#Signs the user in
def signIn():
    userId = int(input('Enter your user id: '));
    user = getUser(userId);
    print('This ID is linked with', user.name);
    password = input('Is this your account? If it is, enter your password: ');
    
    if password.strip() == user.password:
        print('You logged in successfully!');
        secondCommand(user);
    else:
        print('Wrong password! Re-run program to log in again');
        exit();
    
#Returns the user instance from the database, or exits the program if it can't find one    
def getUser(userId):
    
    #Read the contents of the file
    file = open(User.fileName, 'r');
    contents = file.read();
    file.close();
    
    #Loop through all the lines
    for line in contents.split('\n'):
        user = User.fromDataString(line);
        
        if user.userID == userId:
            return user;
    
    print('A user with this ID was not found. Create an account if this is your first time using Phone Book Inc.');
    exit();

    
    

    