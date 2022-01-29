#==================================== SUM ============================
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]

S = sum(album_ratings)
print(S)

#==================================== SORTED ========================
sorted_A = sorted(album_ratings)
print("Album ratings are:", sorted_A)

#================================= MAKE FUNCTIONS ==================
def add1(a):
    """
    Documentation:
    This function adds 1 to the input number
    """

    b=a+1
    return b

def Mult(a,b):
    """
    Documentation:
    This function multiplies the two input numbers
    """
    d = a*b
    return d

help(add1)
c = add1(5)
print("Result of the function add1 =", c)

help(Mult)
d = Mult(5,6)
print("Result of the function Mult =", d)

def div(a,b):
    return(a/b)

c = div(2, 5)

print("The result is:", c)

#=======================Arguments packed in a tuple ===============================
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

#=======================Arguments packed in a dictionary======================
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    
##################################
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList



