# 📚 Student Management System (Python)

## 🌟 Overview
A command-line Student Management System built using Python.  
It allows users to manage student records using a menu-driven interface with persistent file storage.

The system performs full CRUD operations and automatically calculates Total Marks, Percentage, and Grade.

---

## ⚙ Features
✔ Add Student Record (7 Subjects)  
✔ View All Students  
✔ Search Student by Roll Number  
✔ Update Student Data  
✔ Delete Student Record  
✔ Automatic Total Marks Calculation (out of 700)  
✔ Percentage Calculation  
✔ Grade System  
✔ File Handling (Save & Load Data)  
✔ Persistent Storage using `Students_info.txt`  
✔ Auto-load data on start  
✔ Auto-save data on exit  

---

## 🧠 How It Works
The system uses 4 parallel lists:

- Names[]
- RollNo[]
- TotalMarks[]
- Grades[]

Each student enters marks for 7 subjects.

### Calculations:
- Total Marks = Sum of 7 subjects
- Percentage = (TotalMarks / 700) × 100
- Grade is assigned based on percentage

---

## 🎯 Grade System
| Percentage | Grade |
|------------|-------|
| ≥ 90       | A     |
| ≥ 80       | B     |
| ≥ 70       | C     |
| < 70       | F     |

---

## 🗂 File Handling
File used: `Students_info.txt`

✔ Data is loaded when program starts (`readFile()`)  
✔ Data is saved when program exits (`writeFile()`)  
✔ Each record is stored as:

Name RollNo TotalMarks Grade

Example:
Ali 101 650 A  
Ahmed 102 590 B  

---

## 📸 Program Flow
Start Program → Load File Data → Show Menu → User Selects Option → Perform Operation (Add/View/Search/Update/Delete) → Exit → Save Data

---

## 🖥 Menu Options
1) Add Student  
2) View Students  
3) Search Student  
4) Update Student  
5) Delete Student  
6) Exit  

---

## 🚀 How to Run
Step 1: Install Python (3.x)

Step 2: Clone Repository
```bash
git clone https://github.com/nomi40/Student-Management-System-Python.git

Step 3: Open Folder

Step 4: Run Program

python main.py


🧩 Technologies Used

Python
Lists (Data Structures)
File Handling (read/write)
Loops & Conditionals
Command Line Interface (CLI)


🔍 Functions Used in Code
addStudent()

Adds student, takes 7 subject marks, calculates total, percentage, grade

viewStudents()

Displays all students

searchStudent()

Searches student by roll number

updateStudent()

Updates name, roll number, marks and recalculates everything

deleteStudent()

Deletes student from all lists

writeFile()

Saves data into file

readFile()

Loads data from file

🔮 Future Improvements

✔ Database Integration (SQLite / MySQL)
✔ GUI Version (Tkinter / PyQt)
✔ Input Validation
✔ Login System
✔ OOP Version Upgrade

👨‍💻 Author
Noman Ahmed

⭐ Summary

This project demonstrates:
✔ CRUD operations
✔ File handling persistence
✔ Menu-driven system
✔ Real-world student management logic
