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
cursor.execute("CREATE TABLE IF NOT EXISTS BOOKING(Checkin_Date CHAR(12) PRIMARY KEY NOT NULL,Checkout_Date CHAR(12)NOT NULL,Room_Type VARCHAR(35)NOT NULL,Price CHAR(35)NOT NULL,Phone_No CHAR(11)NOT NULL)")
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
def customer():
    while True:
        username=input('enter your username')
        password=int(input('enter password'))
        members=int(input('enter number of members'))
def date(d):
    if d[2]>'2021' and d[2]<='2022':
        if d[1]!=0 and d[1]<='12':
            if d[1]==2 and d[0]!=0 and d[0]<='31':
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
        if n!="" and ph_no!="" and a!="":
            name.append(n)
            address.append(a)
            phone_no.append(ph_no)
            break
        else:
            print("\t Name,Phone_No and Address *this field is required* ")
    #check in
    chk_in=str(input("Check-In: "))
    checkin_date.append(chk_in)
    '''chk_in[0]=int(chk_in[0])
    chk_in[1]=int(chk_in[1])
    chk_in[2]=int(chk_in[2])'''
        #date(ci)
    #check out
    chk_out=str(input("Check-Out: "))
    checkout_date.append(chk_out)
    '''co[0]=int(co[0])
    co[1]=int(co[1])
    co[2]=int(co[2])'''
    #check in and check out date should be proper
    if  chk_out[1]<chk_in[1] and  chk_out[2]<chk_in[2] and  chk_out[1]==chk_in[1] and  chk_out[2]>=chk_in[2] and  chk_out[0]<=chk_in[0]:
        print("\n\tError Found\n\t please make sure Check-Out date must fall after Check-In\n")
        name.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Booking()
    else:
        pass
          
    '''date(chk_out)
    d1=datetime.datetime(int(chk_in[2]),int(chk_in[1]),int(chk_in[0]))
    d2=datetime.datetime(int(chk_out[2]),int(chk_out[1]),int(chk_out[0]))
    d=(d2-d1).days
    day.append(d)'''
        
        #rooms
    print("----*SELECT ROOM TYPE*----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print(("\t\tPress 0 for Room Prices"))
        
    ch=int(input("=>"))
          
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
        while rn in roomno or cid in customer_id:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
        record.append(0)
        payment.append(0)
        if ph_no not in phno:
            phno.append(p1)
       #ROOMS INFO
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
    n=int(input("0-BACK\n =>"))
    if n==0:
        Home()
    else:
        exit()
#ROOM SERVICES
def Room_Services():
    print("         ------ ROOM SERVICES ------")
    print("1.swimming pool\n2. Airport shuttle\n3.Fitness centre\nSpa and wellness centre\nNon-smoking rooms")
    print("")
# PAYMENT FUNCTION
def Payment():
      
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
                x=int(input("=> "))
                print("\n  Amount: ",(price[n]*day[n])+record[n])
                print("\n        PAY FOR GOLDEN ROSE ")
                print("  (y/n)")
                ch=str(input("=>"))
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("           Hotel GOLDEN ROSE")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]*day[n])+record[n],"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n,0)
                    custid.insert(n,0)
                      
             else:
                  
                for j in range(n+1,i):
                    if ph==phno[j] :
                        if p[j]==0:
                            pass
                          
                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n") 
    if f==0:    
        print("Invalid Customer Id")
          
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
def Record():# checks if any record exists or not
    if phno!=[]:
        print("        *** HOTEL RECORD ***\n")
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------")
          
        for n in range(0,i):
            print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
          
        print("----------------------------------------------------------------------------------------------------------------------")
      
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
          
    else:
        exit()
Home()     
