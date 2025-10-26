from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = None
    unit = "metric"

    if request.method == "POST":
        unit = request.form["unit"]

        if unit == "metric":
            weight = float(request.form["weight_kg"])
            height_cm = float(request.form["height_cm"])
            height_m = height_cm / 100
            bmi = round(weight / (height_m ** 2), 2)

        elif unit == "imperial":
            weight_lb = float(request.form["weight_lb"])
            height_ft = float(request.form["height_ft"])
            height_in = float(request.form["height_in"])
            total_height_in = height_ft * 12 + height_in
            bmi = round((weight_lb / (total_height_in ** 2)) * 703, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi, category=category, unit=unit)

if __name__ == "__main__":
    app.run(debug=True)
