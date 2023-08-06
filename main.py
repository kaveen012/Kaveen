#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#Admin panel--- Admin

def AdminPanel():
    while(True):
        print("                    ")
        print("Welcome to E-TEC BME")
        print("--------------------")
        print("1-Equipment management")
        print("2-Customer management")
        print("3-Approve/Reject repair")
        print("4-Repair completion")
        print("5-View Purchases")
        print("6-View Repairs")
        print("7-Reset system")
        print("8-Exit")
        print("                   ")
        opt=int(input("Enter your Choice [1/2/3/4/5/6/7/8]:"))
        if(opt<1 or opt>8):
            print("    ")
            print("Invalid option")
            print("Please try again")
        elif(opt==1):
            EquipmentMenu()
        elif(opt==2):
            CustomerMenu()
        elif(opt==3):
            ApproveReject()
        elif(opt==4):
            RepairCompletion()
        elif(opt==5):
            ViewPurchases()
        elif(opt==6):
            ViewRepair()
        elif(opt==7):
            Reset()
        elif(opt==8):
            break;

#-----------------------------------------------------------------------------------------------------------------------

#Equipment Menu----- Admin

def EquipmentMenu():
    while(True):
        print("    ")
        print("Manage Equipments --- Admin")
        print("---------------------------")
        print("1-Add equipments")
        print("2-Update equipments")
        print("3-Delete equipments")
        print("4-Search equipments")
        print("5-List equipments")
        print("6-Exit")
        print("    ")
        opt=int(input("Enter choice [1/2/3/4/5/6]:"))
        if (opt<1 or opt>6):
            print("    ")
            print("Invalid option")
            print("Please try again")
        elif(opt==1):
            addequipments()
        elif(opt==2):
            updateequipments()
        elif(opt==3):
            deleteequipments()
        elif(opt==4):
            searchequipment()
        elif(opt==5):
            listequipments()
        elif(opt==6):
            break;

#1-Add equipment to the system ----- Admin

def addequipments():
    file=open("Equipments.txt" , "a+")
    print("         ")
    print("Add equipments to the system --- Admin")
    print("--------------------------------------")
    Itemcode=input("Enter Item Code :")
    if (len(Itemcode) != 4):
        print("   ")
        print("Incorrect Length - Enter 4-digit code")
    else:
        print(" ")
        Equipmentname=input ("Enter device name :")
        EquipementQuantity =input("Enter quantity :")
        Manufacturer=input("Enter manufacturer :")
        Country=input("Enter Country of manufacturer :")
        Price= input ("Enter price :")
        file.writelines(Itemcode+","+Equipmentname+","+EquipementQuantity+","+Manufacturer+","+Country+","+Price+"\n")
        print(" ")
        print ("The device is save to the system")
    file.close()

#2-Update equipment in the System --- Admin

def updateequipments():
    file = open("Equipments.txt", "r")
    lines = file.readlines()
    file.close()
    print(" ")
    print("Update equipment details --- Admin")
    print("----------------------------------")
    searchkey = input("Enter device name :")
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
                print(" ")
                print("Item code\tDevice\t\t1Quantity\tManufacturer\tCountry\t\tPrice")
                print(Itemcode+"\t\t"+Equipmentname+"\t"+EquipementQuantity+"\t\t"+Manufacturer+"\t\t"+Country+"\t"+Price)
                print("Item code="+Itemcode)
                while (True):
                    print("  ")
                    print("What do you want to Update ?")
                    print("----------------------------")
                    print("1-Name")
                    print("2-Quantity ")
                    print("3-Price ")
                    print("4-Exit")
                    print("  ")
                    opt = int(input("Enter Choice :"))
                    if (opt < 1 or opt > 4):
                        print(" ")
                        print("Invalid option")
                        print(" Please try again")
                    elif (opt == 1):
                        Equipmentname=input("Enter new name of equipment :")
                    elif (opt == 2):
                        EquipementQuantity=input("Enter new quantity :")
                    elif (opt == 3):
                        Price= input("Enter new price :")
                    elif (opt == 4):
                        print(" ")
                        print("Back to the equipment menu")
                        return;
                    lines[index]=Itemcode+","+Equipmentname+","+EquipementQuantity+","+Manufacturer+","+Country+","+Price
                    file=open("Equipments.txt","w")
                    file.writelines(lines)
                    print("  ")
                    print("Device records updated")
                    file.close()
        index = index + 1
    if (found == False):
        print(" ")
        print("Device not found")

#3-Delete Equipemnt from the system --- admin

def deleteequipments():
    file = open("Equipments.txt", "r")
    lines = file.readlines()
    file.close()
    print(" ")
    print("Delete equipment details --- Admin")
    print("----------------------------------")
    searchkey = input("Enter Device name :")
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
                print(" ")
                print("Item code -", Itemcode )
                print("Device -",Equipmentname )
                print("Quantity -",EquipementQuantity)
                print("Manufacturer -",Manufacturer)
                print("Country of manufacturer -",Country)
                print("Equipment price -",Price)
                print(" ")
                lines.remove(lines[index])
                file=open("Equipments.txt","w")
                file.writelines(lines)
                print("The device was Removed from the system")
                file.close()
                return
        index = index + 1
    if (found == False):
        print(" ")
        print("Device not found")

#4-Search equipment in the system --- Admin

def searchequipment():
    file = open("Equipments.txt", "r")
    lines = file.readlines()
    file.close()
    print(" ")
    print("Search equipment details --- Admin")
    print("----------------------------------")
    searchkey = input("Enter device name :")
    index = 0
    found = False
    while (True):
        if (index == len(lines)):
            break;
        else:
            Line_parts = lines[index].split(",")
            if len(Line_parts) !=6:
                continue
            Itemcode= Line_parts[0]
            Equipmentname= Line_parts[1]
            EquipementQuantity= Line_parts[2]
            Manufacturer= Line_parts[3]
            Country = Line_parts[4]
            Price = Line_parts[5]
            if (searchkey == Equipmentname):
                found = True
                print(" ")
                print("Item code\tDevice\tQuantity\tManufacturer\tCountry\tPrice")
                print(Itemcode+"\t"+ Equipmentname +"\t"+ EquipementQuantity +"\t"+ Manufacturer +"\t"+ Country +"\t"+ Price)
        index = index + 1
    if (found == False):
        print(" ")
        print("Device not found")

#5-View list of equipment --- Admin

def listequipments():
    file=open("Equipments.txt","r")
    print("  ")
    print("List of Equipment")
    print("------------------")
    print(" ")
    print("Item code\tDevice\tQuantity\tManufacturer\tCountry\tPrice")
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
            print(Itemcode+"\t"+ Equipmentname +"\t"+ EquipementQuantity +"\t"+ Manufacturer +"\t"+ Country +"\t"+ Price)
    file.close()

# This code written by KaVeEn

#------------------------------------------------------------------------------------------------------------------------

#Customer Menu ------ Admin

def CustomerMenu():
    while(True):
        print("   ")
        print("Manage Customer --- Admin")
        print(" ------------------------")
        print("1-Add customers")
        print("2-Update customers")
        print("3-Delete customers")
        print("4-Search customers")
        print("5-List customers")
        print("6-Exit")
        print("       ")
        opt=int(input("Enter Choice [1/2/3/4/5/6]:"))
        if(opt<1 or opt>6):
            print("  ")
            print("Invalid option")
            print("Please try again")
        elif (opt==1):
            Addcustomer()
        elif (opt==2):
            Updatecustomer()
        elif (opt==3):
            Deletecustomer()
        elif (opt==4):
            searchcustomer()
        elif (opt==5):
            listcustomers()
        elif (opt==6):
            break;

#1-Add customer to the system --- Admin

def Addcustomer():
    file=open("Customers.txt","a+")
    print(" ")
    print("Register Customer --- Admin")
    print("---------------------------")
    nic = input ("Enter NIC number :")
    Cname=input("Enter name :")
    Cpw=input("Enter password :")
    Caddress=input("Enter address :")
    Contactno= input("Enter contact number :")
    file.writelines(nic+","+Cname+","+Cpw+","+Caddress+","+Contactno+"\n")
    print(" ")
    print ("Customer records saved to the system")
    file.close()

#2-Update customer in the system --- Admin

def Updatecustomer():
    file = open("Customers.txt", "r")
    lines = file.readlines()
    file.close()
    print(" ")
    print("Update customer details --- Admin")
    print("---------------------------------")
    searchkey = input("Enter customer NIC :")
    index = 0
    found = False
    while (True):
        if (index == len(lines)):
            break;
        else:
            Line_parts = lines[index].split(",")
            nic = Line_parts[0]
            Cname = Line_parts[1]
            Cpw=Line_parts[2]
            Caddress = Line_parts[3]
            Contactno = Line_parts[4]
            if (searchkey == nic):
                found = True
                print(" ")
                print("NIC\tCustomer\tAddress\tContact")
                print(nic +"\t"+Cname+"\t"+Caddress+"\t"+ Contactno)
                print("nic="+nic)
                while (True):
                    print(" ")
                    print("What do you want to Update ?")
                    print("----------------------------")
                    print("1-Name")
                    print("2-Address ")
                    print("3-Contact Number ")
                    print(" ")
                    print("4-Exit")
                    opt = int(input("Enter Choice :"))
                    if (opt < 1 or opt > 4):
                        print(" ")
                        print("Invalid option")
                        print(" Please try again")
                    elif (opt == 1):
                        Cname=input("Enter new name :")
                    elif (opt == 2):
                        Caddress=input("Enter new Address :")
                    elif (opt == 3):
                        Contactno=input("Enter new Contact number :")
                    elif (opt == 4):
                        return;
                    lines[index]=nic+","+Cname+","+Cpw+","+Caddress+","+Contactno
                    file=open("Customers.txt","w")
                    file.writelines(lines)
                    print(" ")
                    print("Customer record updated")
                    file.close()
            index = index + 1
        if (found == False):
            print(" ")
            print("Customer not found")

#3-Delete customer from th system --- Admin

def Deletecustomer():
    file=open("Customers.txt","r")
    lines=file.readlines()
    file.close()
    print(" ")
    print("Delete customer details --- Admin")
    print("---------------------------------")
    searchkey=input("Enter customer NIC :")
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
            if(searchkey==nic):
                found=True
                print("NIC -", nic)
                print("Name -", Cname)
                print("Address -", Caddress)
                print("Contact number -", Contactno)
                lines.remove(lines[index])
                file=open("Customers.txt","w")
                file.writelines(lines)
                print(" ")
                print("Customer Removed from the system")
                file.close()
                return
        index=index+1
    if(found==False):
        print(' ')
        print("Customer not found")

#4-Search customer in the system --- Admin

def searchcustomer():
    file=open("Customers.txt","r")
    lines=file.readlines()
    file.close()
    print(" ")
    print("Search customer details --- Admin")
    print("---------------------------------")
    searchkey=input("Enter customer NIC :")
    index=0
    found=False
    while(True):
        if(index==len(lines)):
            break;
        else:
            Line_parts=lines[index].split(",")
            if len(Line_parts)!=5:
                continue
            nic=Line_parts[0]
            Cname=Line_parts[1]
            Caddress=Line_parts[3]
            Contactno=Line_parts[4]
            if(searchkey==nic):
                found=True
                print("NIC\t\t\t\tCustomer\tAddress\t\t\t\t\tContact")
                print(nic+"\t"+Cname+"\t"+Caddress+"\t"+Contactno)
        index=index+1
    if(found==False):
        print(" ")
        print("Customer not found")

#5-View list of customers --- Admin

def listcustomers():
    file=open("Customers.txt","r")
    print(" ")
    print("List of Customers")
    print("-----------------")
    print(" ")
    print("NIC\t\t\t\tCustomer\tAddress\t\t\t\t\tContact")
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
            print(nic+"\t"+Cname+"\t\t"+Caddress+"\t\t\t"+Contactno)
    file.close()

#-----------------------------------------------------------------------------------------------------------------------

#Approve / Reject Cycle Repair---Admin Login

def ApproveReject():
    print("    ")
    print("Approve / Reject E-TEC BME - Admin Login")
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
                print(" ")
                print("Request ID  :", requestid)
                print("Item        :", Equipmentname)
                print("your problem :", Problem)
                print("Customer Name  :", Cname)
                print("Cost      :", cost)
                print("Status    :", status)
                print(" ")
                decission = input ("Do you Approve [Y/N] :")
                if (decission=="Y" or decission=="y"):
                    print("  ")
                    cost = input ("Enter cost estimate :")
                    status =("Approved")
                    print(" ")
                    print("Wait for customer respones")
                else:
                    status =("Rejected")
                    print(" ")
                    print("We can't do this")
                    cost= input("Reason :")
                    print(" ")
                    print("Thank you")


                # update file
                lines[index] = requestid+","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+str(status)
                # rewrite updated list to repair file
                file=open("Repairs.txt","w")
                file.writelines(lines)
                file.close()
        index = index + 1    # go to next record line in the list
    # End while
    if (found == False):
        print(" ")
        print("Incorrect search key")
        print("Please try again")

#-----------------------------------------------------------------------------------------------------------------------

#RepairCompletion --- Admin

def RepairCompletion():
    print("  ")
    print("Repair Completion --- Admin ")
    print("----------------------------")
    searchkey = input("Enter request Id as search key :")
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
                print(" ")
                print("Request ID  :", requestid)
                print("Item        :", Equipmentname)
                print("your problem :", Problem)
                print("Customer Name  :", Cname)
                print("Cost      :", cost)
                print("Status    :", status)
                print(" ")
                decission = input ("Do you Approve [Y/N] :")
                if (decission=="Y" or decission=="y"):
                    print(" ")
                    status =("Completed")
                    print(" ")
                    print("Ready to release")
                else:
                    status =("Still not")
                    print(" ")
                    print("Wait few days")
                # update file
                lines[index] = requestid+","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+str(status)
                # rewrite updated list to repair file
                file=open("Repairs.txt","w")
                file.writelines(lines)
                file.close()
        index = index + 1    # go to next record line in the list
    # End while
    if (found == False):
        print(" ")
        print("Incorrect search key")
        print("Please try again")





#-----------------------------------------------------------------------------------------------------------------------
#Vew all purchases data---Admin

def ViewPurchases():
    file=open("Purchase.txt","r")
    print(" ")
    print("List of Purchases")
    print("-----------------")
    print("ITEM\tEQUIPMENT\tQUANTITY\tAMOUNT\tDATE")
    print(" ")
    while(True):
        line=file.readline()
        if(line==""):
            break
        else:
            Line_parts=line.split(",")
            item = Line_parts[0]
            Equipmentname = Line_parts[1]
            qty = Line_parts[2]
            amt = Line_parts[3]
            date = Line_parts[4]
            print(item+"\t"+Equipmentname+"\t\t\t"+qty+"\t\t\t"+amt+"\t"+date)
    file.close()

# This code written by KaVeEn
#-----------------------------------------------------------------------------------------------------------------------

#view all repairs --- Admin

def ViewRepair():
        file = open("Repairs.txt", "r")
        print(" ")
        print("List of repairs")
        print("---------------")
        print("REQUEST ID\t\tDEVICE\t\t\t\t\tPROBLEM\t\t\tCUSTOMER\t\tCOST/REASON\t\tSTATUS")
        print(" ")
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
                print(requestid+"\t\t\t\t"+Equipmentname+"\t\t\t\t"+Problem+"\t\t"+Cname+"\t\t"+cost+"\t\t\t\t"+status)
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
    file.close()
    print(" ")
    print("all system data cleaned")


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#Customer Panel ---- Customer

def CustomerPanel():
    while(True):
        print("                    ")
        print("Welcome to E-TEC BME")
        print("--------------------")
        print("1-Purchase BME equipment")
        print("2-Submit BME repair request")
        print("3-Accept/Reject quotation")
        print("4-View repair status")
        print("5-Exit")
        print("                    ")
        opt=int(input("Enter choice[1/2/3/4/5]:"))
        if(opt<1 or opt>5):
            print("              ")
            print("Invalid option")
            print("Please try again")
        elif(opt==1):
            Purchase()
        elif(opt==2):
            Submitrequest()
        elif(opt==3):
            ApproveRejectquotes()
        elif(opt==4):
            Viewstatus()
        elif(opt==5):
            break;

#-----------------------------------------------------------------------------------------------------------------------


#1-Purchase BM equipement

def  Purchase():
    print(" ")
    print("Purchase E-TEC BME - Customer Login")
    print("-----------------------------------")
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
            Price = Line_parts[5].strip("\n").strip("LKR ")
            if (searchkey==Equipmentname):  # match found for search key
                found = True
                print("Item code\tEquipment\t\tManufacturer\t\tCountry\t\tPrice")
                print(Itemcode+"\t\t"+Equipmentname+"\t\t"+Manufacturer+"\t\t\t"+Country+"\t\t"+Price)
                print(" ")
                print("**** Purchase Details ****")
                print("--------------------------")
                qty = input("Enter purchase quantity :")
                creditno = input("Enter credit card number :")
                print(" ")
                print("----- Invoice -----")
                print("-------------------")
                import datetime
                date = datetime.datetime.now()
                print(" ")
                print("Date  :", date)
                print("Item code :", Itemcode)
                print("Equipement name :", Equipmentname)
                print("Unit Price :", Price)
                print("Sales Quantity :", qty)
                amt = int(qty) * int(Price)
                print("Amount :", amt)
                print("-----------------------")
                file = open("Purchase.txt", "a+")
                file.write(Itemcode+"," +Equipmentname+","+str(qty)+",LKR "+str(amt)+","+str(date)+"\n")
                print(" ")
                print("Purchase record saved to the system")
                file.close()
                return
        index = index + 1
    if (found == False):
        print(" ")
        print("Incorrect searchkey")
        print("Please try again")


#-----------------------------------------------------------------------------------------------------------------------

#2-Submit BME repair request

def Submitrequest():
    file = open("Repairs.txt", "r")
    lines = file.readlines()
    file.close()
    requestid = len(lines)+1
    print(" ")
    print("Submit Repair Request - Customer Login")
    print("--------------------------------------")
    print(" ")
    print("Repair request Id :", requestid)
    Equipmentname= input("Item Name  :")
    Problem= input("What is your problem :")
    Cname = input("Enter your name :")
    cost = "LKR 0"  # cost will be decided by admin later
    status = "Ongoing"
    file = open("Repairs.txt", "a+")
    file.writelines(str(requestid) +","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+status+"\n")
    print(" ")
    print("Repair request saved to the system")
    file.close()


#-----------------------------------------------------------------------------------------------------------------------

#3-Accept/Reject quation

def  ApproveRejectquotes():
    print(" ")
    print("Approve / Reject E-TEC BME Repair - Admin Login")
    print("-----------------------------------------------")
    searchkey = input("Enter request Id as search key :")
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
                print(" ")
                print("Request ID  :", requestid)
                print("Item        :", Equipmentname)
                print("your problem :", Problem)
                print("Customer Name  :", Cname)
                print("Cost      :", cost)
                print("Status    :", status)
                print(" ")
                decission = input ("Do you Approve [Y/N] :")
                if (decission=="Y" or decission=="y"):
                    status =("Approved by Customer")
                    print(" ")
                    print("Wait few days")
                else:
                    status =("Declined by Customer")
                    print(" ")
                    print("We Appreciate your response")
                # update file
                lines[index] = requestid+","+Equipmentname+","+Problem+","+Cname+","+str(cost)+","+str(status)
                # rewrite updated list to repair file
                file=open("Repairs.txt","w")
                file.writelines(lines)
                file.close()
        index = index + 1    # go to next record line in the list
    # End while
    if (found == False):
        print(" ")
        print("Incorrect Request ID")

# This code written by KaVeEn

#-----------------------------------------------------------------------------------------------------------------------

#-View status of Repair

def Viewstatus():
    file=open("Repairs.txt","r")
    lines=file.readlines()
    file.close()
    print(" ")
    print("Search status")
    print("-------------")
    searchkey=input("Enter Request Id :")
    index=0
    found=False
    while(True):
        if(index==len(lines)):
            break;
        else:
            Line_parts=lines[index].split(",")
            if len(Line_parts)!=6:
                continue
            requestid = Line_parts[0]
            Equipmentname = Line_parts[1]
            Problem = Line_parts[2]
            Cname = Line_parts[3]
            cost = Line_parts[4]
            status = Line_parts[5]
            if (searchkey ==requestid ):
                found = True
                print(" ")
                print("REQUEST_ID\tITEM\t\t\tPROBLEM\t\t\tCUSTOMER\t\tCOST/REASON\t\t\tSTATUS")
                print(requestid+"\t\t\t"+Equipmentname+"\t\t"+Problem+"\t\t"+Cname+"\t\t"+cost+"\t\t\t\t\t"+status)
        index=index+1
    if(found==False):
        print(" ")
        print("Incorrect Request Id")


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# start up Menu

print("**** Login Menu ****")
print("                    ")
print("Welcome to E-TEC BME")
print("--------------------")
print("1 - Admin Login")
print("2 - Customer Login")
print("3 - Exit")
print( "                   ")
opt = int(input("Enter Choice [1/2/3]:"))
if (opt == 1):
    print("                                    ")
    print("Welcome to E-TEC BME --- Admin login")
    print("------------------------------------")
    un = input("Enter username :")
    pw = input("Enter password :")
    if (un == "KaVeEn" and pw == "1234"):
        AdminPanel()
    else:
        print("                              ")
        print("Incorrect username or password")
        print("Please try again")

if (opt == 2):
    print("                                       ")
    print("Welcome to E-TEC BME --- Customer login")
    print("---------------------------------------")
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
            Contactno = Line_parts[4]
            if (un == name and pw == password):  # match found for search key
                found = True
                CustomerPanel()
        index = index + 1
    if (found == False):
        print("                              ")
        print("Incorrect username or password")
        print("Please try again")

if (opt == 3):
    print("           ")
    print("System Exit")
    print("Goodbye have a nice day")

