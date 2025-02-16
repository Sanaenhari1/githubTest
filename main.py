from flask import Flask, render_template, request, send_file, url_for, jsonify, redirect, flash
from werkzeug.utils import secure_filename
from pydub import AudioSegment
from PIL import Image, ImageFilter, ImageOps
import os
import random
import pandas as pd
import plotly.graph_objects as go
import logging

# Configuration globale
UPLOAD_FOLDER = 'static/uploads'
MODIFIED_FOLDER = 'static/audio'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'flac', 'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config.update(
    SECRET_KEY='jawad',
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MODIFIED_FOLDER=MODIFIED_FOLDER
)

# Création des dossiers si non existants
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODIFIED_FOLDER, exist_ok=True)

# Configuration des logs
logging.basicConfig(level=logging.INFO)

# Vérification d'extension de fichier
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ======================== HOME PAGE ========================
@app.route('/')
def homepage():
    return render_template('home.html')

# ======================== ART GENERATOR ========================
def generate_random_shapes(n=50):
    shapes = [{
        "type": random.choice(["circle", "square", "triangle"]),
        "x": random.randint(50, 300),
        "y": random.randint(50, 300),
        "size": random.randint(30, 70),
        "color": f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
    } for _ in range(n)]
    return shapes

@app.route("/generate_shapes")
def generate_shapes_route():
    return jsonify(generate_random_shapes())

@app.route('/Art')
def Artpage():
    return render_template('Art.html')

# ======================== AUDIO EDITOR ========================
@app.route('/Audio', methods=['GET', 'POST'])
def Audiopage():
    if request.method == 'POST':
        try:
            # Téléchargement d'un fichier audio
            file = request.files.get('audio_file')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                audio = AudioSegment.from_file(filepath)
                original_filepath = os.path.join(app.config['MODIFIED_FOLDER'], f"original_{filename}")
                audio.export(original_filepath, format="mp3")

                return render_template('Audio.html', audio_url_original=f'uploads/{filename}', audio_url_modified=None)

            # Modification d'un fichier audio
            if 'apply_modification' in request.form:
                filename = request.form.get('filename')
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                if not os.path.exists(filepath):
                    flash('File not found!', 'error')
                    return redirect(url_for('Audiopage'))

                audio = AudioSegment.from_file(filepath)
                speed = float(request.form.get('speed', 1.0))
                volume = float(request.form.get('volume', 0))
                effects = request.form.get('effects', 'none')
                layer_audio = request.files.get('layer_audio')

                if speed != 1.0:
                    audio = audio.speedup(playback_speed=speed)
                if volume != 0:
                    audio += volume
                if effects == 'echo':
                    audio = audio.reverse()
                if layer_audio:
                    overlay_audio = AudioSegment.from_file(layer_audio)
                    audio = audio.overlay(overlay_audio)

                modified_filename = f"modified_{filename}"
                modified_filepath = os.path.join(app.config['MODIFIED_FOLDER'], modified_filename)
                audio.export(modified_filepath, format="mp3")

                return render_template('Audio.html', audio_url_original=f'uploads/{filename}', audio_url_modified=f'audio/{modified_filename}')

        except Exception as e:
            logging.error(f"Error: {e}")
            flash(f"An error occurred: {e}", 'error')
            return redirect(url_for('Audiopage'))

    return render_template('Audio.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/modified/<filename>')
def modified_file(filename):
    return send_file(os.path.join(app.config['MODIFIED_FOLDER'], filename))

# ======================== IMAGE EDITOR ========================
@app.route('/Image', methods=['GET', 'POST'])
def Imagepage():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or not allowed_file(file.filename):
            flash('Invalid file!', 'error')
            return redirect(url_for('Imagepage'))

        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)
        image = Image.open(original_path)

        effect = request.form.get('effect')
        if effect == 'grayscale':
            image = ImageOps.grayscale(image)
        elif effect == 'sepia':
            image = ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0A080')
        elif effect == 'invert':
            image = ImageOps.invert(image)
        elif effect == 'blur':
            image = image.filter(ImageFilter.BLUR)
        elif effect == 'pixelate':
            image = image.resize((image.width // 10, image.height // 10), Image.BILINEAR)
            image = image.resize((image.width * 10, image.height * 10), Image.NEAREST)

        processed_filename = f'processed_{filename}'
        processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        image.save(processed_path)

        return render_template('Image.html', 
                               original_image=f'static/uploads/{filename}', 
                               processed_image=f'static/uploads/{processed_filename}',
                               download_link=url_for('download_file', filename=processed_filename))

    return render_template('Image.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

# ======================== DATA VISUALIZATION ========================
@app.route('/Data_v1')
def Datapage():
    data = pd.read_csv("large_art_ecommerce_dataset.csv")

    size_values = data['Size'].unique()
    style_values = data['Style'].unique()
    Z = [[data[(data['Size'] == size) & (data['Style'] == style)]['Price ($)'].mean() for size in size_values] for style in style_values]

    fig = go.Figure(data=[go.Surface(z=Z, x=size_values, y=style_values, colorscale='Viridis')])
    fig.update_layout(
        scene=dict(xaxis_title='Size', yaxis_title='Style', zaxis_title='Price ($)'),
        title="3D Heatmap - Price vs. Size & Style",
        template='plotly_dark'
    )

    return render_template('Data.html', plot=fig.to_html(full_html=False))

# ======================== AUTHENTICATION ========================
@app.route('/LogIn')
def Loginpage():
    return render_template('LogIn.html')

@app.route('/register')
def registerpage():
    return render_template('register.html')

# ======================== MAIN EXECUTION ========================
if __name__ == '__main__':
    app.run(debug=True)
