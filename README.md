# 🌾 Farm Market – Django-Based Digital Platform for Farmers  

![License](https://img.shields.io/badge/license-MIT-green)  
![Python](https://img.shields.io/badge/python-3.9%2B-blue)  
![Django](https://img.shields.io/badge/django-4.x-darkgreen)  
![ML](https://img.shields.io/badge/ML-Crop%20Prediction-orange)  

## 📌 Overview  
**Farm Market** is a Django-based web platform that empowers farmers by connecting them directly with buyers. It provides a **digital marketplace**, **crop price transparency**, and **AI-powered crop prediction** to help farmers make data-driven decisions.  

This project aims to:  
- Enable **direct selling** of crops without middlemen  
- Provide **real-time market price updates**  
- Offer **AI-powered crop recommendation** based on soil nutrients  
- Support farmers and buyers with a **user-friendly platform**  

---

## ✨ Features  

### 👨‍🌾 Farmers  
- Register/Login with farmer role  
- Upload crop details (name, price, quantity, image)  
- Get **crop prediction** using ML (`model.pkl`, `minmaxscaler.pkl`)  
- View live crop prices  
- Manage uploaded crops & sales  

### 🛒 Buyers  
- Register/Login with buyer role  
- Browse and search available crops  
- Directly purchase crops from farmers  
- Track order history  

### ⚙️ Admin  
- Manage users (Farmers & Buyers)  
- Approve/Reject crop listings  
- Monitor transactions (future Razorpay integration)  
- Dashboard for analytics  

---

## 🧠 AI/ML Integration  
- **Crop Recommendation System**  
  - Input: Soil nutrients (N, P, K, pH, temperature, etc.)  
  - Output: Suggested crop for better yield  
  - Model Files:  
    - `model.pkl` – trained ML model  
    - `minmaxscaler.pkl` – normalization model  

---

## 🛠️ Tech Stack  
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (dev) → PostgreSQL/MySQL (production)  
- **ML Model:** Scikit-learn (Pickle format)  
- **Authentication:** Django Auth with custom roles  
- **Payment Gateway (planned):** Razorpay  

---

## 🚀 Getting Started  

### 🔧 Prerequisites  
- Python 3.9+  
- pip  
- Virtual environment (recommended)  

### ⚙️ Installation  

```bash
# Clone the repository
git clone https://github.com/your-username/farm-market.git
cd farm-market

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

Now open 👉 `http://127.0.0.1:8000/`  

---

## 📂 Project Structure  

```
farm_market/
│── farm_market/        # Main Django project
│── marketplace/        # App for farmer-buyer interactions
│── templates/          # HTML templates
│── static/             # CSS, JS, images
│── ml_models/          # ML model files (model.pkl, scaler.pkl)
│── manage.py           # Django manager
│── requirements.txt    # Dependencies
```

---

## 📸 Screenshots  
 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/add653b4-025e-4ec7-aa9c-ede962f1d20e" />

---

## 📈 Roadmap  
- ✅ Role-based authentication (Farmer/Buyer)  
- ✅ Crop prediction using ML  
- 🔄 Payment integration (Razorpay/UPI)  
- 🔄 Weather-based crop suggestion  
- 🔄 Mobile-friendly responsive UI  
- 🔄 Multi-language support (regional languages)  
- 🔄 Analytics dashboard for farmers  

---

## 🤝 Contributing  
Contributions are welcome!  
1. Fork the repo  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m 'Add new feature'`)  
4. Push to branch (`git push origin feature-name`)  
5. Open a Pull Request  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 👨‍💻 Author  
**Rakesh Kumar Mishra**  
- 💼 Core Member, Robotics Club Coding Team (2024-25)  
- 🌍 Passionate about AI, ML, and Full-Stack Development  
- 📫 Reach me: [LinkedIn](#) | [Email](#)  

---

⚡ With **Farm Market**, we aim to **digitally empower farmers**, create **fair trade opportunities**, and bring **technology-driven growth** to agriculture.  
