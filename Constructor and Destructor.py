
class emp:
    def __init__(self): #constructor
        print('Employee object created')
    def __del__(self): #destructor
        print('Employee object is destroyed')

o1=emp()#object is created, call constructor automatically
del o1#object is destroyed,

# We use this code to delete a word from the web.