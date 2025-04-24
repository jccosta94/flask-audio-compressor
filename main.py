from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Audio Compressor is running!"

@app.route('/compress', methods=['POST'])
def compress_audio():
    input_file = request.files['file']
    input_path = '/tmp/input'
    output_path = '/tmp/output.mp3'

    input_file.save(input_path)

    subprocess.run([
        'ffmpeg', '-y', '-i', input_path,
        '-ac', '1', '-ar', '16000', '-b:a', '32k',
        output_path
    ])

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
