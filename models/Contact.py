'''The phone book class for phone book instances'''

class Contact:
    
    def __init__(self, name, phoneNumber, emailAddress, address):
        self.name = name;
        self.address = address;
        self.phoneNumber = phoneNumber;
        self.emailAddress = emailAddress;
        
    def toDatabaseString(self): 
        return self.name + ':' + self.phoneNumber + ':' + self.emailAddress + ':' + self.address + '\n';
    
    @staticmethod
    def fromDataString(content):
        
        if content == '':
            return Contact(name = '', phoneNumber = '', emailAddress = '', address = '');
        else:
            data = content.split(':');
            return Contact(name = data[0], phoneNumber = data[1], emailAddress = data[2], address = data[3]);        
        
    def displayContactInfo(self, announceContact = False):
        if announceContact:print('The contact information for', self.name, 'is as follows:');
        print('Name: ', self.name, ', Phone Number: ', self.phoneNumber, ', Email address: ', self.emailAddress, ', Physical address: ', self.address, sep = '');
        