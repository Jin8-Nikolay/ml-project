from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/callback-endpoint", methods=['POST'])
def callback_endpoint():
    data = request.form
    audio_url = data.get('audio_url')

    return jsonify({
        'audio_url': audio_url
    })


@app.route("/get-songs", methods=['GET'])
def get_songs():
    search = request.args.get('search')
    callback_url = request.args.get('callback_url')

    audio_file_url = f'http://127.0.0.1:5000/static/gimn-lyuftvafe-st.mp3'

    files = {'file': ('gimn-lyuftvafe-st.mp3', requests.get(audio_file_url).content)}
    data = {'audio_url': audio_file_url}

    print("Data:", data)

    response = requests.post(callback_url, files=files, data=data)

    print("Callback Response:", response.text)

    return jsonify({'message': 'Audio file processed. Callback sent successfully.'})


if __name__ == "__main__":
    app.run(debug=True)
