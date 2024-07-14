from flask import Flask, request, jsonify, send_file, render_template
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    tts = gTTS(text)
    tts.save('output.mp3')

    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
