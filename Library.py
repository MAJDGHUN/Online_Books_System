
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import LibBksDatabase
import AMAZONDB
import sqlite3
import main
from main import no_pages

#tkinter standard Python interface to the Tk GUI toolkit.
#sqlite database "LibBksDatabase.py" the main database of users
#sqlite database "AMAZONDB.py" for amazon results 
#C library that provides a lightweight disk-based database
# scraping code "main.py" 
#no_pages parameter from scraping code "main.py"


#class inherits from the Frame container widget
#function to delegate the creation of the user interface to the initUI method.
#Here I put the Frame widget, accessed via the self attribute to the Tk root window.It is expanded in both directions.
#the __init__ constructor method we call the constructor of our inherited class
class Library:
    
    #self is a class level identifier. When you type self.root = Tk() 
    # it means in this class it will create a class level variable root and initialize it with Tk() object 
    # and whenever you want to access this variable in the class you will call it with self.root like self.root.title()
    def __init__(self,root):
        self.root = root
        self.root.title("Online Library")
        #The geometry method sets a size for the window and positions it on the screen
        self.root.geometry("1350x850+0+0")
        
        #A string such as "hello" is just a data type
        #StringVar() allows you to easily track tkinter variables and see if they have been read, overwritten
        # String variabels - tkinter
        BT= StringVar()
        BA= StringVar()
        BR= StringVar()
        BPD= StringVar()
        BP= StringVar()
        BI= StringVar()
        BC= StringVar()
      
    #=========================Function Declaration=======================================
    ##Calling exits and acts my messsage box
        def iExit():
            iExit= tkinter.messagebox.askyesno("Online Library","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
    ##ClearData Fun
        def ClearData():
            self.txtBT.delete(0,END)
            self.txtBA.delete(0,END)
            self.txtBR.delete(0,END)
            self.txtBPD.delete(0,END)
            self.txtBP.delete(0,END)
            self.txtBI.delete(0,END)
            self.txtBC.delete(0,END)
            
         
    ##AddData Function
        def addData():
            if(len(BT.get())!=0):
                ###LibBksDarabase (my DB)--addDataRec(The Function on my DB)
                LibBksDatabase.addDataRec(BT.get(),BA.get(),BR.get(),BPD.get(), \
                    BP.get(),BI.get(),BC.get())

                booklist.delete(0,END)
                booklist.insert(END,(BT.get(),BA.get(),BR.get(),BPD.get(), \
                    BP.get(),BI.get(),BC.get()))
            
        ##Display Data Function
        def DisplayData():
            booklist.delete(0,END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END,row)
        ##Selected Book Data Function
        def SelectedBook(event):
            global sb
            searchbk= booklist.curselection() [0]
            sb= booklist.get(searchbk)

            self.txtBT.delete(0,END)
            self.txtBT.insert(END,sb[1])
            self.txtBA.delete(0,END)
            self.txtBA.insert(END,sb[2])
            self.txtBR.delete(0,END)
            self.txtBR.insert(END,sb[3])
            self.txtBPD.delete(0,END)
            self.txtBPD.insert(END,sb[4])
            self.txtBP.delete(0,END)
            self.txtBP.insert(END,sb[5])
            self.txtBI.delete(0,END)
            self.txtBI.insert(END,sb[6])
            self.txtBC.delete(0,END)
            self.txtBC.insert(END,sb[7])

        ##Selected Book Data Function(Amazon DB)
        #Return the indices of currently selected item.
        def SelectedBook2(event):
            global sb2
            searchbk2= booklistAm.curselection() [0]
            sb2= booklistAm.get(searchbk2)

            self.txtBT.delete(0,END)
            self.txtBT.insert(END,sb2[0])
            self.txtBA.delete(0,END)
            self.txtBA.insert(END,sb2[1])
            self.txtBR.delete(0,END)
            self.txtBR.insert(END,sb2[2])
            self.txtBPD.delete(0,END)
            self.txtBPD.insert(END,sb2[3])
            self.txtBP.delete(0,END)
            self.txtBP.insert(END,sb2[4])
            self.txtBI.delete(0,END)
            self.txtBI.insert(END,sb2[5])
            self.txtBC.delete(0,END)
            self.txtBC.insert(END,sb2[6])
        ##DELETE DATA  from DB
        def DELETDATA():
            if(len(BT.get())!=0):
                LibBksDatabase.deletRec(sb[0])
                ClearData()
                DisplayData()

        ##Search DATA  in DB
        def searchDATABASE():
            booklist.delete(0,END)
            for row in LibBksDatabase.SEARCHdata(BT.get(),BA.get(),BR.get(),BPD.get(), \
                        BP.get(),BI.get(),BC.get()):
                booklist.insert(END,row)

        ##Update DATA of DB
        def Update():
            if(len(BT.get())!=0):
                LibBksDatabase.dataupdate(sb[0],BT.get(),BA.get(),BR.get(),BPD.get(), \
                        BP.get(),BI.get(),BC.get())

            


            
        
        ##Display AMAZON Data 
        def AMAData():
           

            main.get_data(no_pages)
            booklistAm.delete(0,END)
            for row in AMAZONDB.viewData():
                booklistAm.insert(END,row)
            
            #con=sqlite3.connect("Amazonbooks.db")
            #cur= con.cursor()
            #cur.execute("SELECT * FROM Amazonbooks")
            #rows = cur.fetchall()
            #con.close
            #return rows

        




##########################################################################################################################################
##########################################################################################################################################
    #=========================Frame CREATION==================================
        #The Grid geometry manager puts the widgets in a 2-dimensional table.
        #padx >>External padding, horizontally
        #pady >>External padding, vertically
        #The relief=RIDG style of a widget refers to certain simulated 3-D effects around the outside of the widget

        MainFrame = Frame(self.root) 
        MainFrame.grid()

        BRFrame = Frame(MainFrame, bg="Cadet blue", padx=40, bd=2, pady=8, relief=RIDGE)
        BRFrame.pack(side=TOP) 

        self.lblBR= Label(BRFrame, font=('arial', 44, 'bold'), text="\tOnline Library\t")
        self.lblBR.grid(sticky=W)

        ButtonFrame= Frame(MainFrame, bd=2, width=1550, height=30, padx=0, pady=0, bg="Cadet blue", relief=RIDGE)
        ButtonFrame.pack(side=TOP) 

        FrameDetail= Frame(MainFrame, width=1350, height=50, padx=20, bd=0, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM) 

        DataFram= Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE)
        DataFram.pack(side=BOTTOM) 

        DataFramLEFT= LabelFrame(DataFram, bd=1, width=800, height=300, padx=20, pady=70, relief=RIDGE, 
        font=('arial', 12, 'bold'),text="\tBooks info:", bg="Cadet blue" )
        DataFramLEFT.pack(side=LEFT)

        DataFramRIGHT= LabelFrame(DataFram, bd=1, width=450, height=300, padx=20, pady=3, relief=RIDGE, 
        font=('arial', 12, 'bold'),text="\tBook Details:", bg="Cadet blue")
        DataFramRIGHT.pack(side=RIGHT)

      

#=========================Widget CREATION, Data Entry==================================
        self.lblBT= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2, bg="Cadet blue")
        self.lblBT.grid(row=0, column=0, sticky=W)
        self.txtBT = Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BT, width=25)
        self.txtBT.grid(row=0, column=1)
        

        self.lblBA= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2, bg="Cadet blue")
        self.lblBA.grid(row=0, column=2, sticky=W)
        self.txtBA = Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BA, width=25)
        self.txtBA.grid(row=0, column=3)
        


        self.lblBR= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="Rating:", padx=2, pady=2, bg="Cadet blue")
        self.lblBR.grid(row=1, column=0, sticky=W)
        self.txtBR = Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BR, width=25)
        self.txtBR.grid(row=1, column=1)


        self.lblBPD= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="Publish Date:", padx=2, pady=2, bg="Cadet blue")
        self.lblBPD.grid(row=1, column=2, sticky=W)
        self.txtBPD= Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BPD, width=25)
        self.txtBPD.grid(row=1, column=3)

        self.lblBP= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="Price:", padx=2, pady=2, bg="Cadet blue")
        self.lblBP.grid(row=2, column=0, sticky=W)
        self.txtBP= Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BP, width=25)
        self.txtBP.grid(row=2, column=1)

        self.lblBI= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="ISBN:", padx=2, pady=2, bg="Cadet blue")
        self.lblBI.grid(row=2, column=2, sticky=W)
        self.txtBI= Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BI, width=25)
        self.txtBI.grid(row=2, column=3)

        self.lblBC= Label(DataFramLEFT, font=('arial', 12, 'bold'), text="Bookcase:", padx=2, pady=2, bg="Cadet blue")
        self.lblBC.grid(row=3, column=0, sticky=W)
        self.txtBC= Entry(DataFramLEFT, font=('arial', 12, 'bold'), textvariable=BC, width=25)
        self.txtBC.grid(row=3, column=1)

        
 

#=========================List Books====================================

        scrollbar = Scrollbar(DataFramRIGHT)
        scrollbar.grid(row=0, column=0, sticky='ns')
        booklist = Listbox(DataFramRIGHT, width =45, height=12,font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>', SelectedBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)
#=========================Buttons====================================
        self.btnAddData = Button(ButtonFrame, text='Amazon',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=AMAData)
        self.btnAddData.grid(row=0, column=0)

        self.btnAddData = Button(ButtonFrame, text='Add Data',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=1)

        self.btnDisplayData = Button(ButtonFrame, text='Display Data',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=2)

        self.btnClearData = Button(ButtonFrame, text='Clear Data',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=ClearData)
        self.btnClearData.grid(row=0, column=3)

        self.btnDeleteData = Button(ButtonFrame, text='Delete Data',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=DELETDATA)
        self.btnDeleteData.grid(row=0, column=4)

        self.btnUpdatData = Button(ButtonFrame, text='Updat Data',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=Update)
        self.btnUpdatData.grid(row=0, column=5)

        self.btnSearchData = Button(ButtonFrame, text='Search Data',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command=searchDATABASE)
        self.btnSearchData.grid(row=0, column=6)

        self.btnExit = Button(ButtonFrame, text='Exit',font=('arial', 12, 'bold'),height =2, width=15, bd=4, command =iExit)
        self.btnExit.grid(row=0, column=7)
   ######Amazon area#######
   #######Amazon Frame
        AMFrame= Frame(MainFrame,height=100, padx=1, pady=1, bg="Cadet blue", relief=RIDGE)
        AMFrame.pack(side=TOP)    
        DataFramDown= LabelFrame(AMFrame, bd=1, width=1000, height=300, padx=20, pady=3, relief=RIDGE, 
        font=('arial', 12, 'bold'),text="Amazon Search:", bg="Cadet blue")
        DataFramDown.pack(side=BOTTOM)
        #===List Books (Amazon)====
        scrollbarAm = Scrollbar(DataFramDown)
        scrollbarAm.grid(row=0, column=0, sticky='ns')
        booklistAm = Listbox(DataFramDown, width =100, height=15,font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        booklistAm.bind('<<ListboxSelect>>', SelectedBook2)
        booklistAm.grid(row=0, column=0, padx=8)
        scrollbarAm.config(command=booklistAm.yview)

        #################################
        #################################

     
        

#Tk is the class which we use to create the root window 
if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()