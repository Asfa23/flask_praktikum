from flask import Flask, redirect, url_for, request, render_template, send_file, jsonify
import math
import json
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# -------------------------------------------------------------------------------------

@app.route('/cv')
def bio():
    return render_template('cv.html')

# -------------------------------------------------------------------------------------

@app.route('/calculator', methods = ['GET','POST'])
def hitung():
    if request.method == "GET":
        return render_template('sqrt.html')
    elif request.method == "POST":
        number = int(request.form['angka'])
        hasil = math.sqrt(number)
        hasil = str(hasil)
        return f"akar dari {number} adalah {hasil}"

# -------------------------------------------------------------------------------------

@app.route('/csvtojson') 
def csvtojson():
    return render_template('ubah_json.html')

@app.route('/convert', methods = ['GET', 'POST'])
def convert():
    if request.method == 'POST':
        f = request.files['berkas']
        f.save(f.filename)

    data = {}

    with open(f.filename, 'r', encoding="utf-8") as csvFile: 
        csvReader = csv.DictReader(csvFile)
        for i, rows in enumerate(csvReader):
            data[i] = rows

    with open('array.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

    return send_file('array.json', as_attachment=True) 

# -------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)