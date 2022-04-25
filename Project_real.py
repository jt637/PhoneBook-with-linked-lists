import os
import itertools
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
        self.prev = None
class PhoneBook:
    def __init__(self): 
        self.head = None
        self.tail = None
    def push(self, data):        
        newNode = Node(data)      
        if(self.head == None):    
            self.head = self.tail = newNode      
            self.head.previous = None        
            self.tail.next = None                                   # O(n)
        else:                                       
            #New node will be added to the tail of the linked list
            self.tail.next = newNode     
            newNode.previous = self.tail    
            self.tail = newNode    
            self.tail.next = None 
    def search(self, value):    
        flag = False    
        #Node current will point to head    
        current = self.head    
        #Checks whether the list is empty    
        if(self.head == None):    
            print("List is empty")                                          # O(n)
            return    
        while(current != None):    
            #Compare value to be searched with each node in the list    
            if(current.data == value):    
                flag = True    
                break    
            current = current.next       
        if(flag):  
            print("Contact was found in the list: ")    
    def delete(self, key):    
        temp = self.head  
        if (temp is not None):
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
        while(temp is not None):  
            if temp.data == key:                                    # O(n)
                break
            prev = temp  
            temp = temp.next
        if(temp == None):  
            return
        prev.next = temp.next
        temp = None
    def printList(self):
        current = self.head
        if(self.head == None):
            print('list is empty')                                 # O(n)
            return
        while(current != None):
            print(current.data)
            current = current.next
#Driver Code
if __name__ == '__main__':
    pb = PhoneBook()
    n = 1
    fileIn = open('contacts.txt', 'r')
    for line in itertools.islice(fileIn, 1):
        pb.push(line)
        name = line
    for line in itertools.islice(fileIn, 2):
        pb.push(line)
        contact = line
    for line in itertools.islice(fileIn, 3):
        pb.push(line)
        emailid = line
    for line in itertools.islice(fileIn, 4):
        pb.push(line)
    for line in itertools.islice(fileIn, 5):
        pb.push(line)
    fileIn.close()
    while(n<100):
        print("Phone Book")
        print("1. Create a new Contact")
        print("2. Display Contacts")
        print("3. Search")
        print("4. Remove Contacts")
        choice=int(input("\nSelect an option: "))
        if(choice==1):
            file=open('contacts.txt', 'a')
            condition = 'y'
            while condition == 'y':
                name = input('Enter a contact ')
                num=input("Phone Number: ")
                email=input("Email: ")
                pb.push(name)
                pb.push(num)
                pb.push(email)
                file.write(name+'\n')
                file.write(num+'\n')
                file.write(email+'\n')
                file.write("------------------------------------"+'\n')
                condition=input("Do you want to enter another contact? y or n:  ")
            file.close()
        elif(choice==2):
            pb.printList()
        elif(choice==3):
            key = input('Who would you like to search for ')
            pb.search(key)
            file=open('contacts.txt', 'r')
            for line in file:
                if(key in line):
                    contact = file.readline()
                    emailid = file.readline()
                    print('Name : ' + key + '\n')
                    print('Contact Number : ' + contact + '\n')
                    print('Email ID : ' + emailid + '\n')
        elif(choice==4):
            key = input('Who would you like to delete? ')
            pb.delete(key)           
        condition = input("\nWould you like to continue? y or n: ")
        if condition == 'n':
            quit()
        n+=1
    
