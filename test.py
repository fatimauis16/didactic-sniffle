import os
import sys
os.system("cls")
print("""
   ____       _     _              ____                  _   _       _       _ 
  / ___| ___ | | __| | ___ _ __   |  _ \ ___  ___  ___  | | | | ___ | |_ ___| |
 | |  _ / _ \| |/ _` |/ _ \ '_ \  | |_) / _ \/ __|/ _ \ | |_| |/ _ \| __/ _ \ |
 | |_| | (_) | | (_| |  __/ | | | |  _ < (_) \__ \  __/ |  _  | (_) | ||  __/ |
  \____|\___/|_|\__,_|\___|_| |_| |_| \_\___/|___/\___| |_| |_|\___/ \__\___|_|
""")
try:
    print("Installing required modules...")
    os.system("pip3 install  -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location mysql-connector-python")
    os.system("pip3 install  -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location datetime")
    os.system("pip3 install  -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location tabulate")
except:
    sys.exit("Error installing modules")

try:
    print("Importing required modules...")
    import random
    import datetime
    import mysql.connector as m
    from tabulate import tabulate
except:
    sys.exit("Error importing modules")

try:
    print("Connecting to database...")
    con = m.connect(host='localhost', user='root', password='root')
    if con.is_connected():
        print('Successfully connected')
except:
    sys.exit("Error connecting to database")

try:
    print("Creating database...")
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hostel")
    cursor.execute("USE hostel")
    cursor.execute("CREATE TABLE IF NOT EXISTS customer(id BIGINT PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL, phno BIGINT NOT NULL, addr VARCHAR(255) NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS booking(custid BIGINT NOT NULL, bookid BIGINT NOT NULL, checkin DATE NOT NULL, checkout DATE NOT NULL, room_type VARCHAR(35) NOT NULL, price INT NOT NULL, phno BIGINT NOT NULL, status VARCHAR(35) NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS payment(bookid BIGINT PRIMARY KEY NOT NULL, phno BIGINT NOT NULL, mode VARCHAR(255) NOT NULL, amnt BIGINT NOT NULL)")
except:
    sys.exit("Error creating database")

roomno = []


def booking():
    print("BOOKING ROOMS")
    while True:
        name = input("Name: ")
        phno = int(input("Phone No: "))
        addr = input("Address: ")
        chk_in = input("Check-in date (dd/mm/yyyy): ").split('/')
        chk_out = input("Check-out date (dd/mm/yyyy): ").split('/')
        if datetime.datetime(int(chk_out[2]), int(chk_out[1]), int(chk_out[0])) < datetime.datetime(int(chk_in[2]), int(chk_in[1]), int(chk_in[0])):
            print("Check-out date must be greater than Check-in date")
            break
        
        print("\n----*SELECT ROOM TYPE*----")
        print("1. Standard Non-AC - Rs. 3500")
        print("2. Standard AC - Rs. 4000")
        print("3. 3-Bed Non-AC - Rs. 4500")
        print("4. 3-Bed AC - Rs. 5000")
        
        ch = int(input("> "))    

        if ch==1:
            print("Room Type - Standard Non-AC")        
            print("Price - 3500")
            room = "Standard Non-AC"
            price = 3500

        elif ch==2:
            print("Room Type - Standard AC")
            print("Price - 4000")
            room = "Standard AC"
            price = 4000

        elif ch==3:
            print("Room Type - 3-Bed Non-AC")
            print("Price - 4500")
            room = "3-Bed Non-AC"
            price = 4500

        elif ch==4:
            print("Room Type - 3-Bed AC")
            print("Price - 5000")
            room = "3-Bed AC"
            price = 5000
                
        #generating random room numbers and customer id
        rn = random.randint(1, 50) + 300
        roomno.append(rn)
        cursor.execute("SELECT id FROM customer WHERE phno = %s", (phno,))
        data = cursor.fetchall()
        if data:
            cid = data[0][0]
            exists = True
        else:
            cid = random.randint(1, 9999999999)
            exists = False
        bid = random.randint(1, 9999999999)
            
        #checking if room numbers are customer ids are not already alloted
        if rn in roomno:
            rn = random.randint(1, 50) + 400
        
        in_date = '-'.join(str(i) for i in chk_in[::-1])
        out_date = '-'.join(str(i) for i in chk_out[::-1])
        status = "Unpaid"
        print("Room number:", rn)
        print("Customer ID:", cid)
        print("Booking ID:", bid)
        if exists == False:
            cursor.execute("INSERT INTO customer VALUES(%s, %s, %s, %s)", (cid, name, phno, addr))
            con.commit()
        cursor.execute("INSERT INTO booking VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (cid, bid, in_date, out_date, room, price, phno, status))
        con.commit()
        print("Room Booked Successfully!!")
        break

#ROOMS INFO
def Rooms_Info():
    print("""
---------------------- HOTEL ROOMS INFO -----------------------

STANDARD NON-AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water.\n
STANDARD NON-AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water + Window/Split AC.\n
3-Bed NON-AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1
Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water.\n
3-Bed AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 
1 Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water + Window/Split AC.\n\n
""")
    
#ROOM SERVICES
def Room_Services():
    print("         ------ ROOM SERVICES ------")
    print("1. Swimming Pool\n2. Airport Shuttle\n3. Fitness Centre\n4. Spa and Wellness Centre\n5. Non-Smoking Rooms")


# PAYMENT FUNCTION
def payment():
    ph = int(input("Phone Number: "))      
    cursor.execute("SELECT * from booking WHERE phno = %s AND status = 'Unpaid'", (ph,))
    rs = cursor.fetchall()
    
    if rs == []:
        print("Unpaid bookings not found")

    else:
        cursor.execute("SELECT * FROM customer WHERE id = %s", (rs[0][0],))
        rss = cursor.fetchall()
        name = rss[0][1]
        phone = rss[0][2]
        address = rss[0][3]

        print("Payment")
        print("-------------------------------")
        print("MODE OF PAYMENT")

        print("1. Credit / Debit Card")
        print("2. Paytm / PhonePe")
        print("3. UPI")
        x = int(input("> ")) 
        
        day = (rs[-1][3] - rs[-1][2]).days
        amount = rs[-1][5] * day
        print("Amount to be paid: ", amount)
        
        if x == 1:
            mode = "Credit / Debit Card"
            print("Enter Card Details")
            input("Card Number: ")
            input("CVV: ")
            input("Expiry Date: ")
            input("Name on Card: ")
        
        elif x == 2:
            mode = "Paytm / PhonePe"
            print("Enter Paytm / PhonePe Details")
            input("Phone Number: ")
            input("UPI ID: ")

        elif x == 3:
            mode = "UPI"
            print("Enter UPI Details")
            input("UPI ID: ")
            input("Phone Number: ")

        print("\n\n --------------------------------")
        print("           Hotel GOLDEN ROSE")
        print(" --------------------------------")
        print("              Bill")
        print(" --------------------------------")
        print(" Name: ", name,"\t\n Phone No.: ", phone,"\t\n Address: ",address,"\t")
        print("\n Check-In: ", rs[-1][2],"\t\n Check-Out: ", rs[-1][3],"\t")
        print("\n Room Type: ", rs[-1][4],"\t\n Room Charges: ", amount,"\t")
        print(" --------------------------------")
        print("\n Total Amount: ", amount,"\t")
        cursor.execute("INSERT INTO payment VALUES(%s, %s, %s, %s)", (rs[0][1], phone, mode, amount))
        con.commit()
        cursor.execute("UPDATE booking SET status = 'Paid' WHERE phno = %s and bookid = %s", (phone, rs[0][1]))
        con.commit()
        print(" --------------------------------")
        print("          Thank You")
        print("          Visit Again :)")
        print(" --------------------------------\n")

                     

def Record():# checks if any record exists or not
    cursor.execute("SELECT name, customer.phno, addr, checkin, checkout, room_type, price FROM customer, booking WHERE customer.id = booking.custid")
    data = cursor.fetchall()
    if data:
        data.insert(0, ["Name", "Phone No.", "Address", "Check-In", "Check-Out", "Room Type", "Price"])
        print("        *** HOTEL RECORD ***\n")
        print(tabulate(data, tablefmt="grid", disable_numparse=True, colalign='center'))
        print()
    else:
        print("No Records Found")

def hostel_rules():
    print("         ------ RULES TO BE FOLLOWED ------")
    print("1.Cancellation and prepayment policies vary according to accommodation type")
    print("2.Refundable damage deposit:A damage deposit of AED 100 is required on arrival. This will be collected as a cash payment. You should be reimbursed on check-out. Your deposit will be refunded in full in cash, subject to an inspection of the property.")
    print("3.Children are not allowed\nExtra bed policies:\nThere is no capacity for extra beds at this property")
    print("4.Age restriction:\nThe minimum age for check-in is 18")
    print("5.Pets:\nPets are not allowed.")
    choice=input("do u accept all the rules?yes or no:")
    if choice=='yes':
        pass
    else:
        exit 


def main():
    while True:
        print("\t\t\t\t\t\t WELCOME TO GOLDEN ROSE HOSTEL \n")
        print("1 Booking")
        print("2 Rooms Info")
        print("3 Room Service")
        print("4 Payment")
        print("5 Hostel rules")
        print("6 Record")
        print("0 Exit")
        
        ch=int(input("> "))

        if ch==1:
            print(" ")
            booking()
        
        elif ch==2:
            print(" ")
            Rooms_Info()
        
        elif ch==3:
            print(" ")
            Room_Services()
        
        elif ch==4:
            print(" ")
            payment()
            
        elif ch==5:
            print(" ")
            hostel_rules()
        
        elif ch==6:
            print(" ")
            Record()

        else:
            print("Exiting...")
            exit()


main()
