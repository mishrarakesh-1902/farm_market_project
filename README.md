# 🌾 Farm Market - AI Powered Platform for Farmers

[![Deployed on Render](https://img.shields.io/badge/Live-Demo-brightgreen)](https://farm-market-project-8.onrender.com/)
[![Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django)](https://www.djangoproject.com/)


## 🧭 Overview

**Farm Market** is a Django-based web platform designed to empower farmers through technology. It connects farmers directly with buyers, provides crop and yield predictions using AI models, and promotes transparency in agricultural trade.

> 🌱 *Built with the mission of digitalizing Indian agriculture and making smart farming accessible.*

---

## ✨ Key Features

- 👨‍🌾 **Farmer & Buyer Registration/Login**  
  Secure authentication system with role-based access.

- 📈 **AI-Powered Predictions**  
  - **Crop Prediction** based on soil data  
  - **Yield Prediction** for informed decisions

- 🛒 **Direct Selling Marketplace**  
  Farmers can list their crops; buyers can view and purchase directly.

- 📊 **Real-time Market Dashboard**  
  Easy navigation of all listings, prices, and user accounts.

- 🧠 **ML Integration**  
  Uses pre-trained `.pkl` models (`model.pkl` & `minmaxscaler.pkl`) for crop recommendations.

---

## 🛠 Tech Stack

| Layer        | Technologies Used                              |
|--------------|-------------------------------------------------|
| 💻 Frontend   | HTML, CSS, Bootstrap                           |
| ⚙️ Backend    | Django (Python)                                |
| 🧠 AI Models  | Scikit-learn (`.pkl` files)                    |
| 🗃 Database   | SQLite (Development), compatible with PostgreSQL |
| 🌐 Deployment | Render (Free Tier Hosting)                     |

---

## 🚀 Getting Started

### 1. Clone the Repository
```base
git clone https://github.com/mishrarakesh-1902/farm_market_project.git
cd farm_market_project
```
---
 ## Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

 ##  Install Dependencies
 ```
pip install -r requirements.txt
```
## Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Run the Server
```
python manage.py runserver
```
---
## Project Structure
```
farm_market_project/
│
├── farm_market/           # Main Django App
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/             # HTML Templates
├── static/                # CSS, JS, images
├── ML_Models/             # model.pkl, scaler.pkl
├── media/                 # Uploaded crop images
├── db.sqlite3             # Dev database
├── manage.py
└── requirements.txt
```
---
## 📸 Screenshots
![image](https://github.com/user-attachments/assets/8eb508de-bba5-4aad-8c7a-a110482e4760)
![image](https://github.com/user-attachments/assets/2897ae6f-1b31-4a94-80fa-96299ff10fb4)
![image](https://github.com/user-attachments/assets/649dddcf-dec8-43d9-95d9-9073fbd3d522)
![image](https://github.com/user-attachments/assets/b06b29a3-2378-44a4-841e-2b9b4bcaeed2)

---

## 🙋‍♂️ Author
Rakesh Kumar Mishra
📧 mishrarakeshkumar766@gmail.com
🔗 [GitHub](https://github.com/mishrarakesh-1902)
🔗 [LinkedIn](https://www.linkedin.com/in/rakesh-kumar-b64934284/)

Let me know if you'd like help adding screenshots, a Hindi version, or badges like GitHub stars or contributors.








