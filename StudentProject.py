Names = []
RollNo = []
TotalMarks = []
Grades =  []

def addStudent():
    name =  input("Enter name of Student:")
    Names.append(name)

    rollNo = int(input("Enter roll number of Student :"))
    RollNo.append(rollNo)

    sumMarks = 0
    for i in range (7):
        marks = int(input("Enter marks of Subject "+str(i+1)+" : "))
        sumMarks += marks
    
    TotalMarks.append(sumMarks)
    percentage = (sumMarks/700)*100

    if(percentage>=90):
        Grades.append("A")
    elif(percentage>=80):
        Grades.append("B")
    elif(percentage>=70):
        Grades.append("C")
    else:
        Grades.append("F")
        
    print("Student added!")
    

def viewStudents():
    i = 0
    while i<len(Names):
        print(Names[i]," ",RollNo[i]," ",TotalMarks[i]," ",Grades[i])
        i = i+1

def searchStudent():
    rollN = int(input("Enter roll number you want to search :"))
    studentFound = False
    for num in RollNo:
        if(rollN ==  num):
            index = RollNo.index(num)
            print(Names[index]," ",RollNo[index]," ",TotalMarks[index]," ",Grades[index])
            studentFound = True
            break
    if(studentFound == False):
        print("Student not found!")


def updateStudent():
    rollN = int(input("Enter  roll number of student you want to update data  :"))
    studentFound = False
    for num in RollNo:
        if(rollN == num):
            index = RollNo.index(num)
            newName = input("Enter new Name :")
            Names[index] = newName
            newRNum = int(input("Enter new Roll Number :"))
            RollNo[index] = newRNum

            sumMarks = 0
            for i in range (7):
                marks = int(input("Enter marks of Subject "+str(i+1)+" : "))
                sumMarks += marks
    
            TotalMarks[index] = sumMarks
            percentage = (sumMarks/700)*100

            if(percentage>90):
                Grades[index] = "A"
            elif(percentage>80 and percentage<90):
                Grades[index] = "B"
            elif(percentage>70 and percentage<80):
                Grades[index] = "C"
            else:
                Grades[index] = "F"

            studentFound = True
            break
    if(studentFound == False):
        print("Student not found!")


def  deleteStudent():
    rollN =  int(input("Enter roll number of Student you want to delete : "))
    studentFound = False
    for num in RollNo:
        if(rollN == num):
            index = RollNo.index(num)
            Names.pop(index)
            RollNo.pop(index)
            TotalMarks.pop(index)
            Grades.pop(index)
            studentFound = True
            break
    if(studentFound == False):
        print("Student not found!")


def writeFile():
    with open("Students_info.txt","w")as file:
        i = 0
        while i<len(Names):
            file.write(Names[i]+" "+str(RollNo[i])+" "+str(TotalMarks[i])+" "+Grades[i]+"\n")
            i=i+1


def readFile():
    with open("Students_info.txt","r")as file:
        for line in file:
            data = line.split()
            Names.append(data[0])
            RollNo.append(int(data[1]))
            TotalMarks.append(int(data[2]))
            Grades.append(data[3])


readFile()
print("==== STUDENT MANAGMENT SYSTEM ====")
print("1) Add Student")
print("2) View Student")
print("3) Search Student")
print("4) Update Student")
print("5) Delete Student")
print("6) Exit")

while (True):
    choice = int(input("Enter choice:"))
    if(choice == 1):
        addStudent()
    elif(choice == 2):
        viewStudents()
    elif(choice == 3):
        searchStudent()
    elif(choice == 4):
        updateStudent()
    elif(choice == 5):
        deleteStudent()
    elif(choice == 6):
        writeFile()
        print("Exit")
        break
    else:
        print("Incorrect choice.Enter different one!")
        
        
        


        
    

        

            

              



        
        





 


    

