# 📚 School Management System

## 📋 About the Project

This system was developed as a project for the **Software Project** course at the **Federal University of Alagoas (UFAL)**, taught by Professor Dr. **Baldoino Fonseca dos Santos Neto**.

The system manages a school environment, supporting three user roles:

- 👨‍🎓 Students  
- 👨‍🏫 Staff (Teachers)  
- 👪 Guardians (Parents or Legal Representatives)

Developed by student **Zilderlan Naty dos Santos**.

---

## ✨ Features Implemented

- ✅ Registration for students, staff, and guardians (with name and password)  
- 🔐 Secure login by user type (student, staff, guardian)  
- 📝 Personalized menu for each profile  
- ⏰ Attendance registration (**restricted to staff**)  
- 📊 Grade assignment and consultation  
- 📚 Distribution and viewing of class materials  
- 🗓️ Exam scheduling and viewing  
- 🎯 Extracurricular activity tracking  
- 💰 **Monthly payment processing (restricted to guardians)**  
- 🚌 School transport tracking (available to guardians)  
- 👀 Detailed student report viewable by the guardian  
- 📆 Class schedule and group management  
- 🧠 Intelligent error messages and validations for invalid or missing data  

---

## ⚠️ Rules and Restrictions

- 📅 Dates must follow the format `DD/MM/YYYY`  
- 🔢 **Only students** are assigned IDs, used by staff and guardians to link  
- 🔒 Passwords are plain text (no encryption)  
- 🚫 Only staff can register attendance and manage academic information  
- 👪 Guardians must provide a valid **student ID** when registering  
- 💾 All data is stored **in memory only** — nothing is saved permanently  
- ❌ If no materials, grades, or exams are available, the system notifies the user with a message and a visual symbol (ASCII)

---

## 🛠️ How to Run the Project

1. Install **Python 3.6+** ([Download here](https://www.python.org/downloads/))  
2. Clone or download the repository  
3. Place the files `escola.py` and `main.py` in the same directory  
4. Run the system by opening a terminal in the project folder and typing:

   ```bash
   python main.py
