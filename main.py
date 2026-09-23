patients = []

def selectChoice():
    print('''
1.	Add Patient
2.	View All Patients
3.	Search Patient
4.	Search by Disease
5.	Show Emergency Patients
6.	Update Doctor
7.	Discharge Patient
8.	Patient Statistics
9.	Search by Doctor
10.	Exit
''')
    choice = int(input("Your Choice: "))

    if(choice == 1):
        addPatient()
    elif choice == 2:
        viewAllPatients()
    elif choice == 3:
        searchPatient()    
    elif choice == 4:
        searchByDisease()
    elif choice == 5:
        showEmergencyPatients()
    elif choice == 6:
        updateDoctor()
    elif choice == 7:
        Discharge()
    elif choice == 8:
        Statistic()
    elif choice == 9:
        searchByDoctor()
    elif choice == 10:
        return

def addPatient():
    arr = []
    patient_name = input("Enter Patient Name: ")
    count = 0
    for i in range(len(patients)):
        if(patients[i][0] == patient_name):
            print("Patient Already Exists.")
            selectChoice()
            count += 1
            return
    if count == 0:
        arr.append(patient_name)
        arr.append(input("Enter Disease: ")) 
        arr.append(input("Enter Emergency Status: ")) 
        arr.append(input("Enter Doctor Name: ")) 
        patients.append(arr)
    selectChoice()

def viewAllPatients():
    for i in range(len(patients)):
        print(i+1, "Patient Name: ", patients[i][0], "\n  Disease:", patients[i][1], "\n  Status:", patients[i][2], "\n  Doctor Assigned:", patients[i][3],"\n" )

    selectChoice()
        
def searchPatient():
    name = input("Enter Patients Name: ")
    count = 0
    for i in range(len(patients)):
        if(patients[i][0] == name):
            print("")
            print("Patient Name:", patients[i][0])
            print("Disease:", patients[i][1]) 
            print("Status:", patients[i][2])
            print("Doctor:", patients[i][3])
            count+=1
            return
    if count == 0:
        print("No Patient Found with this Name.")
    
    selectChoice()

def searchByDisease():
    disease = input("Enter Disease: ")
    count = 0
    for i in range(len(patients)):
        if(patients[i][1] == disease):
            print(i+1, "Patient Name:", patients[i][0], "\nDisease:", patients[i][1], "\nStatus:", patients[i][2], "\nDoctor:", patients[i][3])
            count += 1
    if count == 0:
        print("No Patients Found with this Disease.")

    selectChoice()

def showEmergencyPatients():
    count = 0
    for i in range(len(patients)):
        if(patients[i][2] == "Emergency"):
            print("Patient Name:", patients[i][0], ", Disease:", patients[i][1], ", Status:", patients[i][2], ", Doctor:", patients[i][3])
            count += 1
    if count == 0:
        print("No Emergency Patients Found.")

    selectChoice()

def updateDoctor():
    Patient=input("Enter Patient Name:")
    count=0
    for i in range(len(patients)):
        if(patients[i][0]== Patient):
            Doctor_name=input("Enter Doctor Name:")
            patients[i][3]=Doctor_name
            count += 1
    if count == 0:
        print("No Patient Found with this Name.")

    selectChoice()

def Discharge():
    Patient=input("Enter Patient Name:")
    count=0
    for i in range(len(patients)):
        if(patients[i][0]==Patient):
            temp=patients[i]
            patients.remove(temp)
            count += 1
            break
    if count == 0:
        print("No Patient Found with this Name.")
    selectChoice()

def Statistic():
    Patient=input("Enter Patient Name:")
    count=0
    for i in range(len(patients)):
        if(patients[i][0]==Patient):
            print("Name:",patients[i][0])
            print("Disease:",patients[i][1])
            print("Status:",patients[i][2])
            print("Doctor Name:",patients[i][3])
            count += 1
    if count == 0:
        print("No Patient Found with this Name.")
    selectChoice()

def searchByDoctor():
    Doctor=input("Enter Doctor Name:")
    count=0
    for i in range(len(patients)):
        if(patients[i][3]==Doctor):
            print("Name:",patients[i][0])
            print("Disease:",patients[i][1])
            print("Status:",patients[i][2])
            print("Doctor Name:",patients[i][3])
            count+=1
    
    if count == 0:
        print("No Patients Found for this Doctor.")
    
    selectChoice()

selectChoice()