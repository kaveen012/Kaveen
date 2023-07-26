from datetime import date
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


#Admin panel--- Admin

def AdminPanel():
    while(True):
        print("E-TEC BME System - Admin Login")
        print("1-Equipment Management")
        print("2-Customer Management")
        print("3-Approve/Reject Repair")
        print("4-Repair completion")
        print("5-View Purchases")
        print("6-View Repairs")
        print("7-Reset system")
        print("8-Exit")
        opt=int(input("Enter your Choice :"))
        if(opt<1 or opt>8):
            print("Invalid option")
        if(opt==1):
            EquipmentMenu()
        if(opt==2):
            CustomerMenu()
        if(opt==3):
            ApproveReject()
        if(opt==4):
            RepairCompletion()
        if(opt==5):
            ViewPurchases()
        if(opt==6):
            ViewRepair()
        if(opt==7):
            Reset()
        if(opt==8):
            break;

#-----------------------------------------------------------------------------------------------------------------------

#Equipment Menu----- Admin

def EquipmentMenu():
    while(True):
        print("Manage Equipments-Admin Login")
        print("1-Add Equipments")
        print("2-update Equipments")
        print("3-delete Equipments")
        print("4-search Equipments")
        print("5-list Equipments")
        print("6-exit")
        opt=int(input("Enter choice :"))
        if (opt<1 or opt>6):
            print("invalid option")
        if(opt==1):
            addequipments()
        if(opt==2):
            updateequipments()
        if(opt==3):
            deleteequipments()
        if(opt==4):
            searchequipment()
        if(opt==5):
            listequipments()
        if(opt==6):
            break;

#1-Add equipment to the system ----- Admin

def addequipments():
    file=open("Equipments.txt" , "a+")
    print("Add equipments to the system- Admin Login")
    print ("-----------------------------------------")
    Itemcode=input("Enter Item Code :")
    if (len(Itemcode) != 4):
        print("Incorrect Length - Enter 4 digit code")
    else:
        Equipmentname=input ("Enter Equipment name :")
        EquipementQuantity =input("Enter quantity:")
        Manufacturer=input("Enter manufacturer :")
        Country=input("Enter Country of manufacturer :")
        Price= input ("Enter price :")
        file.writelines(Itemcode+","+Equipmentname+","+EquipementQuantity+","+Manufacturer+","+Country+","+Price+"\n")
        print ("Equipment saved to the system ")
    file.close()

#2-Update equipment in the System --- Admin

def updateequipments():
    file = open("Equipments.txt", "r")
    lines = file.readlines()
    file.close()
    searchkey = input("Enter equipement name :")
    index = 0
    found = False
    while (True):
        if (index == len(lines)):
            break;
        else:
            Line_parts = lines[index].split(",")
            Itemcode= Line_parts[0]
            Equipmentname= Line_parts[1]
            EquipementQuantity= Line_parts[2]
            Manufacturer= Line_parts[3]
            Country = Line_parts[4]
            Price = Line_parts[5]
            if (searchkey == Equipmentname ):
                found = True
                print(Itemcode+ " " + Equipmentname + " " + EquipementQuantity + " " + Manufacturer +" "+Country+" "+Price)
                print("Item code="+Itemcode)
                Equipmentname=input("Enter new name of equipment :")
                EquipementQuantity=input("Enter new quantity :")
                Price= input("Enter new price :")
                lines[index]=Itemcode+","+Equipmentname+","+EquipementQuantity+","+Manufacturer+","+Country+","+Price+"\n"
                file=open("Equipments.txt","w")
                file.writelines(lines)
                print("Equipement records are updated")
                file.close()
        index = index + 1
    if (found == False):
        print("Equipment not found")

#3-Delete Equipemnt from the system --- admin

def deleteequipments():
    file = open("Equipments.txt", "r")
    lines = file.readlines()
    file.close()
    searchkey = input("Enter equipement name :")
    index = 0
    found = False
    while (True):
        if (index == len(lines)):
            break;
        else:
            Line_parts = lines[index].split(",")
            Itemcode= Line_parts[0]
            Equipmentname= Line_parts[1]
            EquipementQuantity= Line_parts[2]
            Manufacturer= Line_parts[3]
            Country = Line_parts[4]
            Price = Line_parts[5]
            if (searchkey == Equipmentname ):
                found = True
                print("Item code -", Itemcode )
                print("Equipment -",Equipmentname )
                print("Quantity -",EquipementQuantity)
                print("Manufacturer -",Manufacturer)
                print("Country of manufacturer -",Country)
                print("Equipment price -",Price)
                lines.remove(lines[index])
                file=open("Equipments.txt","w")
                file.writelines(lines)
                print("Equipement remove from the system")
                file.close()
        index = index + 1
    if (found == False):
        print("Equipment not found")

#4-Search equipment in the system --- Admin

def searchequipment():
    file = open("Equipments.txt", "r")
    lines = file.readlines()
    file.close()
    searchkey = input("Enter equipement name :")
    index = 0
    found = False
    while (True):
        if (index == len(lines)):
            break;
        else:
            Line_parts = lines[index].split(",")
            Itemcode= Line_parts[0]
            Equipmentname= Line_parts[1]
            EquipementQuantity= Line_parts[2]
            Manufacturer= Line_parts[3]
            Country = Line_parts[4]
            Price = Line_parts[5]
            if (searchkey == Equipmentname):
                found = True
                print(Itemcode+ " " + Equipmentname + " " + EquipementQuantity + " " + Manufacturer +" "+ Country +" "+Price)
        index = index + 1
    if (found == False):
        print("Equipment not found")

#5-View list of equipment --- Admin

def listequipments():
    file=open("Equipments.txt","r")
    print("List of Equipments")
    print ("-----------------")
    while(True):
        line=file.readline()
        if(line==""):
            break
        else:
            Line_parts = line.split(",")
            Itemcode= Line_parts[0]
            Equipmentname= Line_parts[1]
            EquipementQuantity= Line_parts[2]
            Manufacturer= Line_parts[3]
            Country = Line_parts[4]
            Price = Line_parts[5]
            print(Itemcode+ " " + Equipmentname + " " + EquipementQuantity + " " + Manufacturer +" "+ Country +" "+Price)
    file.close()



#------------------------------------------------------------------------------------------------------------------------

#Customer Menu ------ Admin

def CustomerMenu():
    while(True):
        print("Manage Customer -Admin login")
        print("1-Add customers")
        print("2-Update customers")
        print("3-Delete customers")
        print("4-Search customers")
        print("5-List customers")
        print("6-Exit")
        opt=int(input("Enter Choice :"))
        if(opt<1 or opt>6):
            print("Invalid option")
        if (opt==1):
            Addcustomer()
        if (opt==2):
            Updatecustomer()
        if (opt==3):
            Deletecustomer()
        if (opt==4):
            searchcustomer()
        if (opt==5):
            listcustomers()
        if (opt==6):
            break;

#1-Add customer to the system --- Admin

def Addcustomer():
    file=open("Customers.txt","a+")
    print("Register Customer - Admin Login")
    print ("-------- ----------------------")
    nic = input ("Enter NIC number :")
    Cname=input("Enter name :")
    Cpw=input("Enter password :")
    Caddress=input("Enter address :")
    Contactno= input("Enter contact number :")
    file.writelines(nic+","+Cname+","+Cpw+","+Caddress+","+Contactno+"\n")
    print ("Customer record saved to the system ")
    file.close()

#2-Update customer in the system --- Admin

def Updatecustomer():
    file = open("Customers.txt", "r")
    lines = file.readlines()
    file.close()
    searchkey = input("Enter customer name :")
    index = 0
    found = False
    while (True):
        if (index == len(lines)):
            break;
        else:
            Line_parts = lines[index].split(",")
            nic = Line_parts[0]
            Cname = Line_parts[1]
            Caddress = Line_parts[3]
            Contactno = Line_parts[4]
            if (searchkey == Cname):
                found = True
                print(nic + " " + Cname + " " + Caddress + " " + Contactno)
                print("nic="+nic)
                Cname=input("Enter new name :")
                Caddress=input("Enter new Address :")
                Contactno=input("Enter new Contact number :")
                lines[index]=nic+","+Cname+","+Caddress+","+Contactno+"\n"
                file=open("Customers.txt","w")
                file.writelines(lines)
                print("Customer record are updated")
                file.close()
        index = index + 1
    if (found == False):
        print("Customer not found")

#3-Delete customer from th system --- Admin

def Deletecustomer():
    file=open("Customers.txt","r")
    lines=file.readlines()
    file.close()
    searchkey=input("Enter customer name :")
    index=0
    found=False
    while(True):
        if(index==len(lines)):
            break;
        else:
            Line_parts=lines[index].split(",")
            nic=Line_parts[0]
            Cname=Line_parts[1]
            Caddress=Line_parts[3]
            Contactno=Line_parts[4]
            if(searchkey==Cname):
                found=True
                print("NIC -", nic)
                print("Name -", Cname)
                print("Address -", Caddress)
                print("Contact number -", Contactno)
                lines.remove(lines[index])
                file=open("Customers.txt","w")
                file.writelines(lines)
                print("Customer Remove from the system successfully")
                file.close()
        index=index+1
    if(found==False):
        print("Customer not found")

#4-Search customer in the system --- Admin

def searchcustomer():
    file=open("Customers.txt","r")
    lines=file.readlines()
    file.close()
    searchkey=input("Enter customer name :")
    index=0
    found=False
    while(True):
        if(index==len(lines)):
            break;
        else:
            Line_parts=lines[index].split(",")
            nic=Line_parts[0]
            Cname=Line_parts[1]
            Caddress=Line_parts[3]
            Contactno=Line_parts[4]
            if(searchkey==Cname):
                found=True
                print(nic+" "+Cname+" "+Caddress+" "+Contactno)
        index=index+1
    if(found==False):
        print("Customer not found")

#5-View list of customers --- Admin

def listcustomers():
    file=open("Customers.txt","r")
    print("List of Customers")
    print ("-----------------")
    while(True):
        line=file.readline()
        if(line==""):
            break
        else:
            Line_parts=line.split(",")
            nic = Line_parts[0]
            Cname = Line_parts[1]
            Caddress = Line_parts[3]
            Contactno = Line_parts[4]
            print(nic+"   "+Cname+"    "+Caddress+"   "+Contactno)
    file.close()

#-----------------------------------------------------------------------------------------------------------------------

#Approve / Reject Cycle Repair---Admin Login

def ApproveReject():
    print("Approve / Reject Cycle Repair - Admin Login")
    print("-------------------------------------------")
    searchkey = input("Enter request ID as search key :")
    file=open("Repairs.txt","r")
    lines=file.readlines()# store all repair records in a list called lines
    file.close()
    index = 0
    found = False
    while (True):
        if (index == len(lines)):   # end of list
            break;
        else:
            Line_parts=lines[index].split(",")
            requestid = Line_parts[0]
            Equipmentname = Line_parts[1]
            Problem = Line_parts[2]
            Cname = Line_parts[3]
            cost = Line_parts[4]
            status = Line_parts[5]
            if (searchkey==requestid):  # match found for search key
                found = True
                print("Request ID  :", requestid)
                print("Item        :", Equipmentname)
                print("your problem :", Problem)
                print("Customer Name  :", Cname)
                print("Cost      :", cost)
                print("Status    :", status)
                decission = input ("Do you Approve [Y/N] :")
                if (decission=="Y" or decission=="y"):
                    cost = input ("Enter cost estimate :")
                    status =("Approved")
                else:
                    status =("Rejected")
                    cost= input("Reason :")

                # update file
                lines[index] = requestid+","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+str(status)
                # rewrite updated list to repair file
                file=open("Repairs.txt","w")
                file.writelines(lines)
                file.close()
        index = index + 1    # go to next record line in the list
    # End while
    if (found == False):
        print("Incorrect search key")

#-----------------------------------------------------------------------------------------------------------------------

#RepairCompletion --- Admin

def RepairCompletion():
    print("Approve / Reject Cycle Repair - Admin Login")
    print("-------------------------------------------")
    searchkey = input("Enter request ID as search key :")
    file=open("Repairs.txt","r")
    lines=file.readlines()# store all repair records in a list called lines
    file.close()
    index = 0
    found = False
    while (True):
        if (index == len(lines)):   # end of list
            break;
        else:
            Line_parts=lines[index].split(",")
            requestid = Line_parts[0]
            Equipmentname = Line_parts[1]
            Problem = Line_parts[2]
            Cname = Line_parts[3]
            cost = Line_parts[4]
            status = Line_parts[5]
            if (searchkey==requestid):  # match found for search key
                found = True
                print("Request ID  :", requestid)
                print("Item        :", Equipmentname)
                print("your problem :", Problem)
                print("Customer Name  :", Cname)
                print("Cost      :", cost)
                print("Status    :", status)
                decission = input ("Do you Approve [Y/N] :")
                if (decission=="Y" or decission=="y"):
                    status =("Approved")
                else:
                    status =("Rejected")
                # update file
                lines[index] = requestid+","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+str(status)
                # rewrite updated list to repair file
                file=open("Repairs.txt","w")
                file.writelines(lines)
                file.close()
        index = index + 1    # go to next record line in the list
    # End while
    if (found == False):
        print("Incorrect search key")






#-----------------------------------------------------------------------------------------------------------------------
#Vew all purchases data---Admin

def ViewPurchases():
    file=open("Purchase.txt","r")
    print("List of Purchases")
    print("-----------------")
    print("ITEM    DESCRIPTION    QUANTITY     AMOUNT      DATE")
    while(True):
        line=file.readline()
        if(line==""):
            break
        else:
            Line_parts=line.split(",")
            item = Line_parts[0]
            description = Line_parts[1]
            qty = Line_parts[2]
            amt = Line_parts[3]
            date = Line_parts[4]
            print(item+"      "+description+"      "+qty+"      "+amt+"      "+date)
    file.close()


#-----------------------------------------------------------------------------------------------------------------------

#view all repairs --- Admin

def ViewRepair():
        file = open("Repairs.txt", "r")
        print("List of repairs")
        print("---------------")
        while (True):
            line = file.readline()
            if (line == ""):
                break
            else:
                Line_parts = line.split(",")
                requestid = Line_parts[0]
                Equipmentname= Line_parts[1]
                Problem = Line_parts[2]
                Cname = Line_parts[3]
                cost=Line_parts[4]
                status=Line_parts[5]
                print(requestid + "   " + Equipmentname + "    " + Problem  + "   " + Cname +"   " + cost +" "+status)
        file.close()

#-----------------------------------------------------------------------------------------------------------------------

#Reset all data fields

def  Reset():
    file=open("Equipments.txt","w")
    file.close()
    file=open("Repairs.txt","w")
    file.close()
    file=open("Customers.txt","w")
    file.close()
    file=open("Purchase.txt","w")
    print("all system data are cleaned")
    file.close()

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#Customer Panel ---- Customer

def CustomerPanel():
    while(True):
        print("****Customer transactions Customer login ****")
        print("1-Purchase BME equipment")
        print("2-Submit BME repair request")
        print("3-Accept/Reject quotation")
        print("4-View repair status")
        print("5-Exit")
        opt=int(input("Enter choice[1/2/3/4]:"))
        if(opt<1 or opt>4):
            print("Invalid option")
        if(opt==1):
            Purchase()
        if(opt==2):
            Submitrequest()
        if(opt==3):
            ApproveRejectquotes()
        if(opt==4):
            Viewstatus()
        if(opt==5):
            break;

#-----------------------------------------------------------------------------------------------------------------------


#1-Purchase BM equipement

def  Purchase():
    print("Purchase Cycles - Customer Login")
    print("--------------------------------")
    searchkey=input("Enter equipment name as search key :")
    file=open("Equipments.txt","r")
    lines=file.readlines()# store all cycle records in a list called lines
    file.close()
    index = 0
    found = False
    while (True):
        if (index == len(lines)):   # end of list
            break;
        else:
            Line_parts=lines[index].split(",")
            Itemcode= Line_parts[0]
            Equipmentname= Line_parts[1]
            Manufacturer= Line_parts[3]
            Country = Line_parts[4]
            Price = Line_parts[5]
            if (searchkey==Equipmentname):  # match found for search key
                found = True
        print(Itemcode + " " + Equipmentname + " " + " " + Manufacturer + " " + Country + " " + Price)
        index = index + 1
    if (found == False):
        print("Incorrect search key")
    else:
        print("**** Purchase Details ****")
        qty = input("Enter purchase quantity ")
        creditno = input("Enter credit card number ")
        print("----- Invoice --------")
        import datetime
        date=datetime.datetime.now()

        print("Date  :", date)
        print("Item code :", Itemcode)
        print("Equipement name :", Equipmentname)
        print("Unit Price :", Price)
        print("Sales Quantity :", qty)
        amt = int(qty) * int(Price)
        print("Amount :", amt)
        print("-----------------------")
        file=open("Purchase.txt","a+")
        file.writelines(Itemcode+","+Equipmentname+","+","+str(qty)+","+str(amt)+","+str(date)+"\n")
        print("Purchase record saved")
        file.close()

#-----------------------------------------------------------------------------------------------------------------------

#2-Submit BME repair request

def Submitrequest():
    print("Submit Repair Request - Customer Login")
    print("--------------------------------------")
    file = open("Repairs.txt", "r")
    lines = file.readlines()
    file.close()
    requestid = len(lines) + 1
    print("Repair request ID :", requestid)
    Equipmentname= input("Item Name  :")
    Problem= input("What is your problem :")
    Cname = input("Enter your name :")
    cost = "0"  # cost will be decided by admin later
    status = "ongoing"
    file = open("Repairs.txt", "a+")
    file.writelines(str(requestid) + "," + Equipmentname + "," + Problem + "," + Cname + "," + cost + "," + status + "\n")
    print("Repair request saved")
    file.close()

#-----------------------------------------------------------------------------------------------------------------------

#3-Accept/Reject quation

def  ApproveRejectquotes():
    print("Approve / Reject Quotation    Repair -Customer ")
    print("-------------------------------------------")
    searchkey = input("Enter request ID as search key :")
    file=open("Repairs.txt","r")
    lines=file.readlines()# store all repair records in a list called lines
    file.close()
    index = 0
    found = False
    while (True):
        if (index == len(lines)):   # end of list
            break;
        else:
            Line_parts=lines[index].split(",")
            requestid = Line_parts[0]
            Equipmentname = Line_parts[1]
            Problem = Line_parts[2]
            Cname = Line_parts[3]
            cost = Line_parts[4]
            status = Line_parts[5]
            if (searchkey==requestid):  # match found for search key
                found = True
                print("Request ID  :", requestid)
                print("Item        :", Equipmentname)
                print("your problem :", Problem)
                print("Customer Name  :", Cname)
                print("Cost      :", cost)
                print("Status    :", status)
                decission = input ("Do you Approve [C/c] :")
                if (decission=="C" or decission=="c"):
                    status =("Completed")
                else:
                    status =("Still not")
                # update file
                lines[index] = requestid+","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+str(status)
                # rewrite updated list to repair file
                file=open("Repairs.txt","w")
                file.writelines(lines)
                file.close()
        index = index + 1    # go to next record line in the list
    # End while
    if (found == False):
        print("Incorrect search key")

#-----------------------------------------------------------------------------------------------------------------------

#-View status of Repair

def Viewstatus():
    file = open("Repairs.txt", "r")
    print( "List of Repairs")
    print("---------------")
    print("REQUEST_ID     ITEM      PROBLEM     CUSTOMER        COST/Reason      STATUS")
    while (True):
        line = file.readline()
        if (line == ""):
            break
        else:
            Line_parts = line.split(",")
            requestid = Line_parts[0]
            Equipmentname = Line_parts[1]
            Problem = Line_parts[2]
            Cname = Line_parts[3]
            cost = Line_parts[4]
            status = Line_parts[5]

            print (requestid + "              " + Equipmentname + "         " + Problem + "          " + Cname + "          "+ cost + "       " + status)
    file.close()

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# start up Menu

print("*** Login Menu ****")
print("1 - Admin Login")
print("2 - Customer Login")
print("3 - Exit")
opt = int(input("Enter Choice [1/2/3]:"))
if (opt == 1):
    un = input("Enter username :")
    pw = input("Enter password :")
    if (un == "K" and pw == "1"):
        print("Hello""welocme")
        AdminPanel()
    else:
        print("Incorrect user name or password")
if (opt == 2):
    un = input("Enter username :")
    pw = input("Enter password :")
    file = open("Customers.txt", "r")
    lines = file.readlines()  # store all customer records in a list called lines
    file.close()
    index = 0
    found = False
    while (True):
        if (index == len(lines)):  # end of list
            break;
        else:
            Line_parts = lines[index].split(",")
            nic = Line_parts[0]
            name = Line_parts[1]
            password = Line_parts[2]
            address = Line_parts[3]
            contactno = Line_parts[4]
            if (un == name and pw == password):  # match found for search key
                found = True
                CustomerPanel()
        index = index + 1
    if (found == False):
        print("Incorrect username or password")

if (opt == 3):
    print("System Exit")
