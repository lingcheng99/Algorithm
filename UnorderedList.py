#Refer to http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
#With added functions of append(),index(),insert(),pop()

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self,item):
        current=self.head
        while current.getNext()!=None:
            current=current.getNext()
        temp=Node(item)
        current.setNext(temp)
        
    def index(self,item):
        current=self.head
        position=0
        while current.getData()!=item and current.getNext()!=None:
            current=current.getNext()
            position+=1
        if current.getData()==item:
            return position
        else:
            return 'Not found'
        
    def insert(self,pos,item):
        if pos==0:
            self.add(item)
            return
        current=self.head
        location=1
        while current.getNext()!=None and location!=pos:
            current=current.getNext()
            location+=1
        temp=Node(item)
        after=current.getNext()
        current.setNext(temp)
        temp.setNext(after)
        
    def pop(self,pos):
        current=self.head
        if pos==0:
            self.head=current.getNext()
            return        
        location=1
        while current.getNext()!=None and location!=pos:
            current=current.getNext()
            location+=1
        after=current.getNext().getNext()
        current.setNext(after)
