'''The user instance needed to create a PhoneBook'''
from os import remove, path;

class User:
    
    #Our static variable 
    fileName = 'users.txt';
    
    def __init__(self, userID,  name, password):
        self.name = name;
        self.password = password;
        self.userID = userID;
        
    def deleteAccount(self):
        #Delete the account (filter the list of users by user id, remove the one with this object's user id, then re-save)
        file = open('users.txt', 'r');
        users = file.read().split('\n');
        users = list(filter(lambda item: item != '' and item.split(':')[0] != str(self.userID), users));
        file.close();
                
        file = open(User.fileName, 'w');
        for user in users:
            file.write(user + '\n');
        file.close();
        
        #Then, delete the phone book for this user
        if path.isfile(self.name + '.txt'):
            remove(self.name + '.txt');
        
        print('The account associated with', self.name, 'has been deleted');
    
    @staticmethod
    def fromDataString(string):
        if string.strip() == '': #Occurs at the last line (a dummy user is returned)
            return User(userID = 0000, name = '', password = '');
        else:
            contents = string.split(':');
            return User(userID = int(contents[0]), name = contents[1], password = contents[2]);
        
    def toDataString(self):
        return str(self.userID) + ':' + self.name + ':' + self.password + '\n';