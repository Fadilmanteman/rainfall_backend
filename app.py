from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return "Backend Flask aktif!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Tidak ada file yang diunggah'
    file = request.files['file']
    if file.filename == '':
        return 'File tidak memiliki nama'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return f"File berhasil diunggah: {filepath}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
