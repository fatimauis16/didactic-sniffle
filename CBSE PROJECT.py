import datetime
import mysql.connector as m
con=m.connect(host='localhost',user='root',password='root',database='hostel')
if con.is_connected():
    print('successfully connected')
else:
    print('error')
cursor=con.cursor()
con.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(Username VARCHAR(10)PRIMARY KEY NOT NULL,Password VARCHAR(11)NOT NULL,No_of_Members CHAR(2)NOT NULL)")
con.execute("CREATE TABLE IF NOT EXISTS BOOKING(Checkin_Date CHAR(10) PRIMARY KEY NOT NULL,Checkout_Date CHAR(10)NOT NULL,Room_Type VARCHAR(35)NOT NULL,Price CHAR(35)NOT NULL,Phone_No CHAR(11)NOT NULL)")
con.execute("CREATE TABLE IF NOT EXISTS FILTERS(Budget_Per_Night CHAR(3)NOT NULL,Meals CHAR(3)NOT NULL,Property_Type CHAR(2)NOT NULL,Bed_Preference CHAR(2)NOT NULL,Cancellation_policy CHAR(2)NOT NULL)")
con.execute("CREATE TABLE IF NOT EXISTS PAYMENT(Phone_no CHAR(11),Mode_of_payment CHAR(11)NOT NULL,)")
con.execute("CREATE TABLE IF NOT EXISTS RECORD()")
'''#global list allows to modify values outside the 
name=[]
phone_no=[]
address=[]
checkin_date=[]
checkout_date=[]
room=[]
price=[]
record=[]
payment=[]
roomno=[]
customer_id=[]
day=[]
def Home():
    print("\t\t\t\t\t\t WELCOME TO GOLDEN ROSE HOSTEL \n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room Service\n")
    print("\t\t\t 4 Payment\n")
    print("\t\t\t 5 Hostel rules\n")
    print("\t\t\t 6 Record\n")
    print("\t\t\t 0 Exit\n")
    
    ch=int(input("=>"))
    if ch==1:
        print(" ")
        Booking()
      
    elif ch==2:
        print(" ")
        Rooms_Info()
      
    elif ch==3:
        print(" ")
        Room_service()
      
    elif ch==4:
        print(" ")
        Payment()
        
    elif ch==5:
        print(" ")
        Hostel_rules()
      
    elif ch==6:
        print(" ")
        Record()
    else:
        exit()
        
def date(d):
    if c[2]>2021 and c[2]<=2022:
        if c[1]!=0 and c[1]<=12:
            if c[1]==2 and c[0]!=0 and c[0]<=31:
                pass
            else:
                print("Invalid date\n")'''

                

                        
    
    

    
