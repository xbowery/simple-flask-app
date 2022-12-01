from flask import Flask, render_template, request

app = Flask(__name__)

def convert_height(height, unit):
    if unit == "meters":
        height = round(float(height) * 3.281, 2)
        unit = "feet"
    elif unit == "feet":
        height = round(float(height) / 3.281, 2)
        unit = "meters"

    return height, unit

@app.route('/', methods=['POST', 'GET'])
def height():
    if request.method == 'POST':
        if (len(request.form) != 2):
            error = "Invalid input - Please choose a unit type."
            return render_template('height_converter.html', error=error)

        height = request.form['height']
        unit = request.form['unit']

        if (height == ''):
            error = "Invalid input - Please enter an input for height."
            return render_template('height_converter.html', error=error)

        height, unit = convert_height(height, unit)
        return render_template('height_converter.html', height=height, unit=unit)
    else:
        return render_template('height_converter.html')