from flask import Flask, request, jsonify
from get_pred_on_single_video import Predictor

app = Flask(__name__)

pred = Predictor()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    output = pred.get_final_labels_in_video(data['url'])
    print(output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000)
