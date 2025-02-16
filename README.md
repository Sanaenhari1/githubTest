# EdioArt - Multi-Functional Gallery Web Application 🎨🎵📊
EdioArt is a feature-rich Flask-based web application that serves as an interactive gallery for various creative functionalities, including random art generation, audio processing, data visualization, and image editing.

🚀 Features
🏡 Homepage: A visually engaging landing page that highlights the app’s core functionalities.


🎨 Art Generator: Generates random artistic patterns and fractals.


🔊 Audio Processing: Upload, modify (adjust speed, volume, effects), and download audio files.


📊 Data Visualization: Displays interactive data plots to analyze trends and insights.


🖼 Image Editor: Upload images and apply filters like grayscale, sepia, invert, blur, and pixelate.


🔐 User Authentication: Includes login and registration pages (can be extended for full authentication).


📩 Contact Page: Allows users to send inquiries or feedback.


# 📑 Table of Contents

1.Prerequisites

2.Installation

3.Setup Instructions

4.Running the Application

5.Application Routes

6.Dependencies and Tools

7.Troubleshooting

8.Contact

# ⚙️ Prerequisites

Ensure you have the following installed:

Git → Version control for cloning repositories.

Python 3.7+ → Required for Flask and dependencies.

pip → Python package installer.

FFmpeg → Required for audio processing with Pydub (Download FFmpeg).

# installation

# Clone the repository
git clone https://github.com/Sanaenhari1/EdioArt.git
cd EdioArt

1️⃣ Create a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

2️⃣ Install Required Packages
pip install -r requirements.txt

# ⚙️ Setup Instructions

📌 Install the necessary libraries manually if needed:

pip install Flask Flask-WTF pandas numpy matplotlib seaborn plotly PIL pydub pygame Werkzeug
# 📂 Directory Structure
📂 EdioArt/
│-- 📂 static/uploads/       # Stores uploaded images and audio files.
│-- 📂 static/modified/      # Stores processed audio files.
│-- 📂 templates/            # HTML templates for Flask.
│-- 📄 app.py                # Main Flask application.
│-- 📄 requirements.txt       # Dependencies.


# 🔑 Configuration


Secret Key: app.config['SECRET_KEY'] = 'Sanae'
Upload Paths: app.config['UPLOAD_FOLDER'], app.config['MODIFIED_FOLDER']
Ensure FFmpeg is correctly installed for audio processing.
# 🚀 Running the Application
python app.py

The application will run on http://127.0.0.1:5000/. Open this in your browser.
.

# 🌍 Application Routes
Route	Description
/ or /home	-->Homepage
/Art	-->Random art generator
/Audio	-->Upload, modify, and download audio
/Data	-->Data visualization
/Image	-->Image processing and effects
/upload	-->Handles image uploads
/download/<filename>	-->Downloads processed images
/LogIn	-->User login
/register	-->User registration
/Contact	-->Contact form
/generate_shapes	-->API for random shapes

# 📦 Dependencies and Tools
The application relies on the following:

.Flask → Web framework.
.Matplotlib & Seaborn → Data visualization.
.Pandas & NumPy → Data manipulation.
.Pillow (PIL) → Image processing.
.Pydub & FFmpeg → Audio processing.
.Werkzeug → Secure file handling.
.Pygame → Graphics and sound processing.
.Plotly → Interactive charts.

# 🔧 Troubleshooting
🛑 Missing Dependencies
Run:
pip install -r requirements.txt

🛑 FFmpeg Issues
Ensure FFmpeg is installed and available in system PATH.
verify installation

ffmpeg -version


🛑 Port Conflicts
If port 5000 is in use, run the app on a different port:

python app.py --port 8000


🛑 File Permissions
Ensure the uploads and modified directories have the correct write permissions.
# 📬 Contact

For any inquiries or issues, please reach out via:
📧 Email: nhari.sanae@etu.uae.ac.ma
