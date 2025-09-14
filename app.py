from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Put your real API key here:
API_KEY = "9045e3f0e0f24d35f07694f2e1d24555"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    try:
        if lat and lon:  # Location-based search
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        elif city:  # City-based search
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        else:
            return jsonify({"error": "Missing city or coordinates"})

        r = requests.get(url).json()
        f = requests.get(forecast_url).json()

        # Handle bad city names
        if r.get("cod") != 200:
            return jsonify({"error": r.get("message", "Invalid city or coordinates")})

        weather_data = {
            "city": r["name"],
            "temperature": r["main"]["temp"],
            "feels_like": r["main"]["feels_like"],
            "humidity": r["main"]["humidity"],
            "condition": r["weather"][0]["description"].title()
        }

        forecast_data = []
        for item in f.get("list", [])[:16]:  # next ~2 days (3h intervals)
            forecast_data.append({
                "time": item["dt_txt"],
                "temp": item["main"]["temp"],
                "condition": item["weather"][0]["description"].title()
            })

        return jsonify({"weather": weather_data, "forecast": forecast_data})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
