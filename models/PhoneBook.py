'''Performs operations on the phonebook'''
from models.Contact import Contact;
from os.path import isfile;

class PhoneBook:
    
    def __init__(self, user):
        self.user = user;
    
    def addContact(self):
        #Create the contact
        name = input('Enter first and last name of contact: ');
        address = input('Enter their physical address: ');
        phoneNumber = input('Enter their phone number: ');
        emailAddress = input('Enter their email address: ');
        
        contact = Contact(name = name, address = address, phoneNumber = phoneNumber, emailAddress = emailAddress);
        file = open(self.user.name + '.txt', 'a');
        file.write(contact.toDatabaseString());
        file.close();
        print('Contact saved successfully!');
        
    def deleteContact(self):
        
        name = input('Enter the name of the contact to delete: ');
            
        file = open(self.user.name + '.txt', 'r');
        contacts = file.read().split('\n');
        file.close();
                
        file = open(self.user.name + '.txt', 'w');
        for contact in contacts:
            if contact.split(':')[0] != name and contact != '':
                file.write(contact + '\n')
        file.close();
            
        print('Contact with name', name, 'removed from Phone Book');
    
    def viewPhoneBook(self):
        print('Here is a list of all the contacts in your Phone Book:');
        file = open(self.user.name + '.txt', 'r');
        contents = file.read();
        
        for line in contents.split('\n'):
            if line != '':
                contact = Contact.fromDataString(line);
                contact.displayContactInfo();
            
        file.close();
                
    def viewContact(self):
        
        if isfile(self.user.name + '.txt'):
            name = input('Enter the name of the contact: ');
            
            file = open(self.user.name + '.txt', 'r');
            contents = file.read();
            file.close();
            
            for line in contents.split('\n'):
                contact = Contact.fromDataString(line);
                
                if contact.name == name:
                    contact.displayContactInfo(announceContact = True);
                    exit();
            print('A contact with the name', name, 'could not be found. Add this contact to your PhoneBook and search again');

        else:
            print('You do not have any contacts in your PhoneBook. Add a contact to start');
            exit();
       
        