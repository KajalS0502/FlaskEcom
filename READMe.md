# Flask E-commerce Application (Modified Version) 

📦 A Flask-based E-commerce web application featuring user authentication, cart management, admin controls, and integrated payment gateways like Razorpay.

> ⚠️ This is a **modified version** of an original project by [Monish247](https://hub.docker.com/r/monish247/ecommerce_python_image) and [Frost-Codes](https://github.com/Frost-Codes/Flask-Ecommerce).  
> Licensed under the MIT License.

---

## 🛍️ Features

- 👤 Customer authentication (sign up, sign in, password reset)
- 🔎 Product search and view
- 🛒 Add to cart & checkout functionality
- 💳 Payment gateway integration (Razorpay)
- 🧑‍💼 Admin dashboard for managing:
  - Product stock
  - Order status
- 📄 SQLite backend for storage

---

## 🧰 Tech Stack

- Python 3.8+
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- Razorpay API
- HTML, CSS, Bootstrap (Frontend)

---

## 🛠️ My Modifications

- ✅ Refactored code structure into a `website/` package
- ✅ Customized UI styling
- ✅ Added Razpayment modules
- ✅ Updated `README.md` and cleaned dependencies
- ✅ Integrated Flask authentication and form validation

---

## 🚀 Running Locally

```bash
git clone https://github.com/KajalS0502/FlaskEcom.git
cd FlaskEcom

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python main.py
```
Visit http://127.0.0.1:5000 to use the app.

---
## 📦 Docker Image (From Original Project)

From the original image published by Monish247 — useful if you want to deploy with Docker.

```bash
docker pull monish247/ecommerce_python_image:latest  
docker run -itd -p 8034:80 monish247/ecommerce_python_image:latest
```

---
## 🧾 Requirements

See requirements.txt in this repo for all dependencies.

---
## 📌 Credits

This project is based on:

- [Frost-Codes/Flask-Ecommerce](https://github.com/Frost-Codes/Flask-Ecommerce)  
- [monish247/ecommerce_python_image](https://hub.docker.com/r/monish247/ecommerce_python_image)

Both are licensed under the MIT License and reused here with minor changes.

---
## 🙋‍♀️ About Me
Hi! I'm Kajal Singh (@KajalS0502). I'm learning Flask, backend development, and how to integrate third-party services like payment gateways.

Feel free to fork this repo or connect if you'd like to collaborate or give feedback.