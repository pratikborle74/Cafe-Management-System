# ☕ Cafe Management System

A **Python-based CLI application** for managing cafe operations, including **customer orders, menu management, and revenue tracking**.

## 📌 Features
### **Customer Side**
✅ **Customer Registration** (Name, Email, Phone, Address)  
✅ **Place Orders** (Coffee, Tea, Desserts, Burgers, Pizzas)  
✅ **View Order Summary** (Total bill calculation)  

### **Admin Side**
✅ **Menu Management** (Add & Remove items)  
✅ **View All Products** (Coffee, Tea, Desserts, etc.)  
✅ **View All Customers**  
✅ **Price Distribution Visualization** (Histogram using Matplotlib)  
✅ **Revenue Analysis** (Total revenue per customer)  

---

## 🏗️ Project Structure
```
Cafe-Management-System/
│── data/                   # Stores CSV files for customers, menu, and orders
│   ├── customers.csv
│   ├── coffee_menu.csv
│   ├── tea_menu.csv
│   ├── desserts_menu.csv
│   ├── burgers_menu.csv
│   ├── pizzas_menu.csv
│── src/                    # Source code directory
│   ├── cafe_management.py  # Main Python script
│── docs/                   # Documentation files (if needed)
│── README.md               # Project documentation
│── requirements.txt        # Dependencies
│── .gitignore              # Exclude unnecessary files
│── LICENSE                 # Project license
```

---

## 🚀 Installation & Usage
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/pratikborle74/Cafe-Management-System.git
cd Cafe-Management-System
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
```sh
python src/cafe_management.py
```

---

## 📊 Data Visualization (Admin)
The system provides **graphical insights** using `matplotlib`:
- **Price Distribution:** Histogram of item prices  
- **Revenue Per Customer:** Bar chart showing total spending per customer  

---

## 📜 Requirements
- **Python 3.x**
- **pandas**
- **matplotlib**

Install dependencies using:
```sh
pip install -r requirements.txt
```

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Feel free to **fork** this repository and submit pull requests.  
For major changes, please open an issue first.

---

## 👤 Author  
**Pratik Borle**  
📧 Email: [pratikborle64@gmail.com](mailto:pratikborle64@gmail.com)  
🔗 GitHub: [pratikborle74](https://github.com/pratikborle74)  

---
