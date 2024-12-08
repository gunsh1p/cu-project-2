from flask import Flask, render_template, request

from weather_api import get_weather_by_city, get_location_key, check_bad_weather
import config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather-api", methods=["GET"])
def weather():
    city_name = request.args.get("city")
    weather_data = get_weather_by_city(get_location_key(city_name))
    if weather_data:
        return {
            "status": "success",
            "data": weather_data
        }, 200
    else:
        return {
            "status": "error",
            "message": "Не удалось получить данные о погоде"
        }, 404


@app.route("/check-weather", methods=["POST"])
def check_weather():
    start_city = request.form.get("start_city").strip()
    end_city = request.form.get("end_city").strip()

    if not start_city or not end_city:
        error = "Пожалуйста, заполните оба поля."
        return render_template("index.html", error=error)

    try:
        start_weather = get_weather_by_city(start_city)
        end_weather = get_weather_by_city(end_city)

        start_weather["conditions"] = check_bad_weather(*start_weather.values())
        end_weather["conditions"] = check_bad_weather(*end_weather.values())

        return render_template(
            'result.html',
            start_city=start_city,
            end_city=end_city,
            start_weather=start_weather,
            end_weather=end_weather
        )

    except ValueError as e:
        error = "Упс. Город не найден. Проверьте ввод."
    except Exception as e:
        error = "Ошибка подключения к API. Повторите попытку позже."

    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
