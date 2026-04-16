# 💧 Ripple Cost Calculator (Django + MySQL)

A web-based Ripple Cost Calculator built using Django and MySQL that analyzes how small cost changes impact the overall system.

---

## 🚀 Overview

This project calculates ripple cost effects, where a small change in base cost propagates through the system and affects the final cost. It demonstrates strong backend handling using Django with a MySQL database.

---

## ✨ Features

- 🔢 Dynamic ripple cost calculation
- ⚙️ Django-powered backend
- 🗄️ MySQL database integration
- 📊 Simple and clean UI
- 🔁 Form-based real-time processing

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL

---

## 📂 Project Structure

```
ripple_cost_calculator/
│── manage.py
│
├── calculator/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── templates/
│
├── ripple_cost_calculator/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Dnyaneshsasale/ripple-cost-calculator.git
cd ripple-cost-calculator
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment
- Windows:
```bash
venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure MySQL Database

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ripple_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Make sure MySQL server is running and database is created.

---

### 6. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 7. Start server
```bash
python manage.py runserver
```

---

### 8. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🧮 How It Works

1. User enters base cost  
2. Inputs ripple factor (%)  
3. Django processes input  
4. Final cost is calculated and displayed  

---

## 🧾 Example

- Base Cost: ₹1000  
- Ripple Factor: 20%  
- Output: ₹1200  

---

## 🎯 Future Improvements

- 📈 Graph visualization of ripple effects  
- 🔐 User authentication  
- 💾 Save calculation history  
- ☁️ Deployment on cloud  

## 👨‍💻 Author

**Dnyanesh Sasale**

---

## 📌 Note

This project is built using Django with MySQL for better scalability and real-world database handling.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
