from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        app.logger.error('No text provided')
        return jsonify({'error': 'No text provided'}), 400

    try:
        tts = gTTS(text)
        tts.save('output.mp3')
        app.logger.info('Audio file generated successfully')
        return send_file('output.mp3', as_attachment=True)
    except Exception as e:
        app.logger.error(f'Error generating audio file: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
