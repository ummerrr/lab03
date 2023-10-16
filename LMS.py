class book :
    def __init__(self,bookNo,name,author):
        self.serialNo = bookNo
        self.bookname = name
        self.author = author
        self.issuestatus= False
class LMS:
    def __init__(self):
        self.bookstore=[]
        self.users = {}
        self.Books_serial_NO = 1
        self.mainMenu()
    def createAccount(self,username,password):
        self.users[username] = password
    def addBook(self,name,author):
        bookEntry = book(self.Books_serial_NO,name,author)
        self.Books_serial_NO+=1
        self.bookstore.append(bookEntry)
    def removeBook(self,serialNo):
        for book in self.bookstore:
            if book.serialNo == serialNo:
                self.bookstore.remove(book)
                print("Book has been removed the store:)")
                break
    def checkin(self,serailNo):
        for book in self.bookstore:
            if book.serialNo == serailNo:
                book.issuestatus = False
                break
    def login(self,username,password):
        if username in self.users and self.users[username]==password:
            return True
        return False
    def display(self):
        for book in self.bookstore:
            print(f"Book serial N0: {book.serialNo}     Book Name:{book.name}\n Book Author :{book.author}")
    def checkout(self,serialno):
        for book in self.bookstore:
            if book.serialNo == serialno:
                if bool.issuestatus == True:
                    print("Book is already Issued")
                else:
                    book.issuestatus =True
                    print("Book is issued to you")
            

    def mainMenu(self):
        while True:
            print("Welcome to Ashraf LMS0\nUse Following commands to perform tasks.")
            while True:
                task = input("1.Login      2.Create an account      3.Quit")
                if task =="1":
                    username=input("Enter username")
                    password = input("Enter Password")
                    if self.login(username,password):
                        print("Welcome",username)
                        while True:
                            task2 = input("1.Issue a Book      2.Return a book     3.Display_Books       4.Logout ")
                            if task2=="1":
                                self.isuseBook()
                            elif task2=="2":
                                self.checkin(input("Enter Book serial No:"))
                            elif task2 =="3":
                                self.display()
                            elif task2=="4":
                                break
                            else:
                                print("Enter correct command please:)")
                    else:
                        print("Incorrect credentials")
                elif task =="2":
                    self.createAccount(input("Enter username"),input("Enter Password"))
                elif task=="3":
                    break
                else:
                    print("Enter correct command please:)")
LMS()
