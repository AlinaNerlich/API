from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        location = request.form.get("location")
        api_key = "2b9b192a3fd2926952d5abd3b15aac0f"
        weather_url = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric&lang=de ".format(location, api_key)
        weather_data = requests.get(url=weather_url)
    if weather_data:
        return render_template("index.html", weather_data=weather_data.json())
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
