class Library:
    def __init__(self, list, name):#list=L,name="Let's Upgrow"
        self.blist=list#blist=L
        self.name=name#name="Let's Upgrow"
        self.Ldict={}#keep record of lent books
    def disp(self):
        print("We have following books in our library", self.name)
        for b in self.blist:
            print(b)
    def Lbook (self, uname, bname): #ovi, Harry Potter, (k1:v,k2:v1)
        if bname not in self.Ldict.keys():
            self.Ldict.update({bname: uname}) #Harry Potter:ovi, Harry Potter: Luqman
            print("You can take the book now")
        else:
            print("book is already being used by", self.Ldict[bname]) #ovi
    def abook(self, bname):
        self.blist.append(bname) #Pride & Prejudice
        print("Book is added")
    def rbook (self, bname):
        self.Ldict.pop(bname)
        print("Your book returned successfully")

if __name__=='__main__':
    L=['Python for Kids', "Computer Science", "Harry Potter", "Magic of thinking big", "Rich Dad Poor Dad", "Java"]
    #Pride & Prejudice 
    
