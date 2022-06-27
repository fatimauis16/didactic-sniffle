import random
import datetime
import mysql.connector as m
con=m.connect(host='localhost',user='root',password='root',database='hostel')
if con.is_connected():
    print('successfully connected')
else:
    print('error')
cursor=con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(Username VARCHAR(10)PRIMARY KEY NOT NULL,Password VARCHAR(11)NOT NULL,No_of_Members CHAR(2)NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS BOOKING(Checkin_Date CHAR(10) PRIMARY KEY NOT NULL,Checkout_Date CHAR(10)NOT NULL,Room_Type VARCHAR(35)NOT NULL,Price CHAR(35)NOT NULL,Phone_No CHAR(11)NOT NULL)")
#cursor.execute("CREATE TABLE IF NOT EXISTS FILTERS(Budget_Per_Night CHAR(3)NOT NULL,Meals CHAR(3)NOT NULL,Property_Type CHAR(2)NOT NULL,Bed_Preference CHAR(2)NOT NULL,Cancellation_policy CHAR(2)NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS PAYMENT(Phone_no CHAR(11),Mode_of_payment CHAR(11)NOT NULL)")
#global list allows to modify values outside the

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

i = 0

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
#date used in booking       
def date(d):
    if c[2]>2021 and c[2]<=2022:
        if c[1]!=0 and c[1]<=12:
            if c[1]==2 and c[0]!=0 and c[0]<=31:
                pass
            else:
                print("Invalid date\n")
def Booking():
    #booking
    global i
    print("BOOKING ROOMS")
    print("")
    while True:
        n=str(input("Name:"))
        ph_no=int(input("Phone No:"))
        a=str(input("Address:"))
    # checks if any field is not empty
        if name!="" and phone!="" and add!="":
            name.append(n)
            add.append(a)
            phone_no.append(ph_no)
            break
        else:
            print("\t Name,Phone_No and Address *this field is required* ")
    #check in
        chk_in=str(input("Check-In: "))
        checkin_date.append(chk_in)
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        #date(ci)
    #check out
        chk_out=str(input("Check-Out: "))
        checkout_date.append(chk_out)
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
    #check in and check out date should be proper
        if co[1]<ci[1] and co[2]<ci[2] and co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
            print("\n\tError Found\n\t please make sure Check-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        else:
            pass
          
        date(co)
        d1=datetime.datetime(ci[2],ci[1],ci[0])
        d2=datetime.datetime(co[2],co[1],co[0])
        d=(d2-d1).days
        day.append(d)
        
        #rooms
        print("----*SELECT ROOM TYPE*----")
        print(" 1. Standard Non-AC")
        print(" 2. Standard AC")
        print(" 3. 3-Bed Non-AC")
        print(" 4. 3-Bed AC")
        print(("\t\tPress 0 for Room Prices"))
        
        ch=int(input("->"))
          
        #input for rooms and its prices
        if ch==0:
            print(" 1. Standard Non-AC - Rs. 3500")
            print(" 2. Standard AC - Rs. 4000")
            print(" 3. 3-Bed Non-AC - Rs. 4500")
            print(" 4. 3-Bed AC - Rs. 5000")
            
            ch=int(input("=>"))
            if ch==1:
                room.append('Standard Non-AC')
                print("Room Type- Standard Non-AC")  
                price.append(2500)
                print("Price- 3500")
        elif ch==2:
                room.append('Standard AC')
                print("Room Type- Standard AC")
                price.append(3500)
                print("Price- 4000")
        elif ch==3:
                room.append('3-Bed Non-AC')
                print("Room Type- 3-Bed Non-AC")
                price.append(4500)
                print("Price- 4500")
        elif ch==4:
                room.append('3-Bed AC')
                print("Room Type- 3-Bed AC")
                price.append(5500)
                print("Price- 5000")
        else:
            print("Please Try Again!!")
            
        #generating random room numbers and customer id
        rn=random.randrange(20)+300
        cid=random.randrange(20)+10
        
        #checking if room numbers are customer ids are not already alloted
       ''' while rn in roomno or cid in customer_id:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
        record.append(0)
        payment.append(0)
       if p1 not in phno:
            phno.append(p1)'''
       # ROOMS INFO 
def Rooms_Info():
    print("         ------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()
# PAYMENT FUNCTION             
'''def Payment():
      
    ph=str(input("Phone Number: "))
    global i
    f=0
      
    for n in range(0,i):
        if ph==phone_no[n] :
              
            # checks if payment is
            # not already done
             if payment[name]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                   
                print("  1- Credit/Debit Card")
                print("  2- Paytm/PhonePe")
                print("  3- Using UPI")
                print("  4- Cash")
                x=int(input("-> "))
                print("\n  Amount: ",(price[n]*day[n])+rc[n])
                print("\n            Pay For AnCasa")
                print("  (y/n)")
                ch=str(input("->"))
                '''
