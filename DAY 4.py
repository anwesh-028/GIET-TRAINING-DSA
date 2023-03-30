#Linear search in python
def linearSearch(array, n, x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1

array = [2,4,0,1,9]
x = 1 #input
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index:", result)


#Binary search in python
def binarySearch(array, x, low, high):
    while low<=high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present in index :" + str(result))
else:
    print("Element not found")



#A python class that represent an indivisual node in binary tree
class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val= item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->",end=' ')
def preorder(root):
    if root:
        print (str(root.val)+ "->", end= ' ')
        preorder (root.left)
        preorder (root.right)
root=Node(1)
root.left=Node(2) 
root.right = Node (3) 
root.left.left=Node(4)
root.left.right=Node(5)
print ("Inorder traversal ")
inorder(root)
print ("\npreorder traversal ")
preorder(root)
print ("\nposterder traversal ")
postorder(root)



#binary search tree norder traversal
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        return node
    
def minvaluenode(node):
    current=node
    while(current.left is not None):
        current = current.left
    return current

def deletenode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deletenode(root.left,key)
    elif(key > root.key):
        root.right = deletenode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root=None
            return temp
        temp = minvaluenode(root.right)
        root.key = temp.key
        root.right = deletenode(root.right,temp.key)
    return root

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("Inorder trversal:", end=' ')
inorder(root)
print("\n Delete 10")


#Compartment Question
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg
class Compartment:
    def __init__(self,compartment_name,no_of_passengers,total_seats):
        self.__compartment_name=compartment_name
        self.__no_of_passengers=no_of_passengers
        self.__total_seats=total_seats
        
    def get_compartment_name(self):
        return self.__compartment_name
    
    def get_no_of_passengers(self):
        return self.__no_of_passengers
    
    def get_total_seats(self):
        return self.__total_seats
        
class Train:
    def __init__(self,train_name,compartment_list): 
        self.__train_name=train_name 
        self.__compartment_list=compartment_list
    
    def get_train_name(self):
        return self.__train_name
    def get_compartment_list(self):
        return self.__compartment_list
    def count_compartments(self):
        temp = self.__compartment_list.get_head()
        count=0
        while(temp):
            count+=1
            temp=temp.get_next()
        return count
    def check_vacancy(self):
        count=0
        temp=self.__compartment_list.get_head()
        while(temp):
            per= (temp.get_data().get_total_seats() - temp.get_data().get_no_of_passengers())/temp.get_data().get_total_seats()
            if per>0.5:
                count+=1
            temp=temp.get_next()
        return count
    
#Use different values for compartment and test your program    
compartment1=Compartment("SL",250,400)   
compartment2=Compartment("2AC",125,280)   
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
compartment_list=LinkedList()
compartment_list.add(compartment1)
compartment_list.add(compartment2)
compartment_list.add(compartment3)
compartment_list.add(compartment4)
compartment_list.add(compartment5)
train1=Train("Shatabdi",compartment_list)
count=train1.count_compartments()
print("The number of compartments in the train:",count)
vacancy_count=train1.check_vacancy()
print("The number of compartments which have more than 50% vacancy:",vacancy_count)

