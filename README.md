# 🚚 QuickMove Operations Workflow Management System

A web-based Operations Workflow Management System built using **Python, Django, Bootstrap, and SQLite** to streamline and standardize customer relocation operations.

This project was developed as part of the **AI Ops Engineer Hiring Assignment** for **StampMyVisa**.

---

# 🔑 Demo Credentials

Use the following credentials to access the application.

**Username:** `admin`

**Password:** `admin`

> These credentials are provided for evaluation purposes.

---

# 🌐 Live Demo

https://quickmoveops.onrender.com

---

# 📌 Project Overview

QuickMove coordinates end-to-end customer relocations across multiple cities.

Traditionally, operations were managed using WhatsApp groups, Google Sheets, and emails, making it difficult to:

- Track relocation progress
- Monitor pending work
- Prioritize urgent relocations
- Identify high-risk cases
- Maintain standardized workflows

This application provides a centralized Operations Workflow Management System where Operations Executives can manage every relocation from a single dashboard.

---

# ✨ Features

## 📊 Dashboard

- Total Relocations
- Active Relocations
- Completed Relocations
- Pending Tasks
- Recent Relocations
- Operations Summary
- Relocation Risk Indicator

---

## 🚚 Relocation Management

- Create New Relocation
- View Relocation Details
- Customer Information Management
- Move Status Tracking

---

## ✅ Automated Workflow Generation

Whenever a new relocation is created, the system automatically generates a standardized workflow consisting of **10 operational tasks**.

The generated workflow includes:

- Apartment Search
- Property Finalization
- Rental Agreement
- Packers & Movers Booking
- Electricity Setup
- Internet Setup
- Water Connection
- Gas Connection
- Documentation
- Move Completion

This eliminates manual task creation and ensures consistency across all relocations.

---

## 📋 Workflow Tracking

Operations Executives can:

- View workflow tasks
- Update task status
- Track workflow completion
- Monitor progress percentage

---

## 📅 Operations Queue

The Operations Queue automatically categorizes relocations into:

- Today's Relocations
- Upcoming Relocations (Next 7 Days)
- Future Relocations

This helps Operations Executives prioritize daily work.

---

## ⚠️ Relocation Risk Assessment

Each relocation is automatically classified as:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

Risk is calculated using:

- Pending workflow tasks
- Days remaining until move date

This enables Operations Managers to identify relocations requiring immediate attention.

---

## 📈 Analytics

Analytics dashboard built using **Chart.js**

Displays:

- Planning Relocations
- In Progress Relocations
- Completed Relocations

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Django | Backend Framework |
| SQLite | Database |
| HTML5 | Frontend |
| Bootstrap 5 | UI Framework |
| CSS3 | Styling |
| Chart.js | Analytics |
| Render | Deployment |

---

# 📂 Project Structure

```
quickmoveops/
│
├── operations/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── quickmove/
│
├── manage.py
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/adityagws45/quickmoveops.git
```

### Navigate into Project

```bash
cd quickmoveops
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```

---

# 💼 Business Impact

This solution standardizes relocation operations by:

- Eliminating manual workflow creation
- Improving operational visibility
- Standardizing relocation processes
- Tracking workflow progress
- Prioritizing relocations using an Operations Queue
- Identifying high-risk relocations
- Supporting better operational decision-making

---

# 📸 Application Modules

- Dashboard
- New Relocation
- Relocation Details
- Workflow Management
- Operations Queue
- Analytics Dashboard

---

# 🎯 Future Enhancements

- User Authentication & Role-Based Access
- Vendor Management
- WhatsApp & Email Notifications
- SLA Monitoring
- REST API Integration
- AI-Based Vendor Recommendation
- AI-Powered Delay Prediction
- Multi-City Vendor Database

---

# 👨‍💻 Developed By

**Aditya Gawas**

📧 Email: *your-email@example.com*

🔗 LinkedIn: https://linkedin.com/in/aditya-gawas-b785bb257/

💻 GitHub: https://github.com/adityagws45

---

# 📄 License

This project was developed as part of the **AI Ops Engineer Hiring Assignment** for **StampMyVisa** and is intended for evaluation purposes only.
