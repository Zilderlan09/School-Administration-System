# 📚 School Administration System

## 📋 About the Project

This system was developed as a project for the **Software Project** course at the **Federal University of Alagoas (UFAL)**, taught by Professor Dr. **Baldoino Fonseca dos Santos Neto**.

It is a terminal-based school management system designed to support:

- 👨‍🎓 Students  
- 👨‍🏫 Staff (Teachers)  
- 👪 Guardians  

Developed by student **Zilderlan Naty dos Santos**.

---

## ✨ Features Implemented

- ✅ Registration for students, staff, and guardians (with name and password)  
- 🔐 Secure login by user type (student, staff, guardian)  
- 📝 Personalized menus for each profile  
- ⏰ Attendance registration **restricted to teachers only**  
- 📊 Grade entry and consultation  
- 📚 Material sharing and consultation  
- 🗓️ Exam scheduling  
- 🎯 Extracurricular activity records  
- 🚌 Simulated tracking of school transportation  
- 💰 Tuition payment processing  
- 📆 Management of class schedules  
- 👀 Detailed consultation for students and guardians  
- ❌ Clear error messages and alerts for invalid or missing data  

---

## ⚠️ Rules and Restrictions

- 📅 Dates must be entered in the format `DD/MM/YYYY`  
- 🔢 Only students have numerical IDs  
- 🔒 Passwords are stored in plain text (no encryption)  
- 🚫 Only staff can register attendance and perform administrative actions  
- 👪 To register a guardian, you must provide the ID of an existing student  
- 💾 Data is stored **only in memory** and will be lost when the program is closed  
- ⚠️ Invalid input generates an error message and prompts retry  

---

## 🛠️ How to Run on Another Computer

1. Install **Python 3.6+** 👉 [Download here](https://www.python.org/downloads/)  
2. Download the files `system.py` and `main.py` and place them in the same folder  
3. Open the terminal (or command prompt) in the project folder  
4. Run the program with the command:  
   ```bash
   python main.py
