'''The entry point of the program'''
from methods.methods import firstCommand;

def main():
    try:
        firstCommand();
    except Exception as obj:
        print(obj);
    
main();      
    