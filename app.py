from flask import Flask, render_template, send_file, request
import numpy as np
import matplotlib.pyplot as plt
import io
import cv2
import pandas as pd
from pydub import AudioSegment

app = Flask(__name__)

# 📌 PAGE D'ACCUEIL
@app.route('/')
def home():
    return render_template("index.html")

# 🎨 GÉNÉRATION D'ART AVEC MATPLOTLIB
@app.route('/generate')
def generate_art():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('black')
    
    for _ in range(100):
        x, y = np.random.rand(2)
        color = np.random.rand(3,)
        size = np.random.rand(1) * 100
        ax.scatter(x, y, s=size * 500, c=[color])
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

# 📊 VISUALISATION DE DONNÉES
@app.route('/data')
def data_visualization():
    data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        'Value': np.random.randint(1, 100, 5)
    })
    
    fig, ax = plt.subplots()
    ax.bar(data['Day'], data['Value'], color=['red', 'blue', 'green', 'yellow', 'purple'])
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

# 🖼️ MANIPULATION D'IMAGES AVEC OPENCV
@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, buf = cv2.imencode('.png', img_gray)
    return send_file(io.BytesIO(buf), mimetype='image/png')

# 🎵 EFFET AUDIO AVEC PYDUB
@app.route('/audio')
def modify_audio():
    audio = AudioSegment.from_file("static/sample.mp3")
    reversed_audio = audio.reverse()
    reversed_audio.export("static/reversed.mp3", format="mp3")
    return send_file("static/reversed.mp3", mimetype="audio/mp3")

# 🚀 LANCER LE SERVEUR
if __name__ == '__main__':
    app.run(debug=True)


