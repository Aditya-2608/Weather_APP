# 🌦 Weather + AQI Dashboard

A simple **Flask + HTML/JS frontend** project that shows live **Weather, Forecast, and Air Quality Index (AQI)** with animations.  
Perfect starter project to showcase on **GitHub / LinkedIn / Resume**.  

---

## ✨ Features
- 🔍 Search by **city name**  
- 📍 Detect **current location** using browser geolocation  
- 🌦 Live **weather conditions** (temp, feels-like, humidity, condition)  
- 📅 **Forecast** (scrollable horizontal cards with animations)  
- 🌫 **Air Quality Index (AQI)** with health advice  
- 🎨 Animated weather icons (Lottie)  
- 💡 **Tip of the day** based on conditions  

---

## 🛠 Tech Stack
- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)  
- **Frontend**: HTML, CSS, JavaScript (or TypeScript if you prefer)  
- **Animations**: [Lottie](https://airbnb.io/lottie/)  
- **API**: [OpenWeather API](https://openweathermap.org/api)  

---

## ⚙️ Setup & Run

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/weather-aqi-dashboard.git
   cd weather-aqi-dashboard

2. **Install dependencies**
    ```bash
    pip install flask requests

3. **Get your OpenWeather API key**
  * Sign up at [OpenWeather](https://openweathermap.org/api)

  * Replace "your_api_key_here" in app.py with your key.

4. **Project structure**
    ```bash
    weather-aqi-dashboard/
    ├── static/
    │   ├── animations/       # Lottie JSON files (sunny.json, rainy.json, etc.)
    │   └── style.css         # (if you separate CSS)
    ├── templates/
    │   └── index.html        # Frontend
    ├── app.py                # Flask backend
    ├── README.md             # Project docs

5. **Run the Flask app**
    ```bash
    python app.py

6. **Open the app in your browser**
    ```bash
    http://127.0.0.1:5000/