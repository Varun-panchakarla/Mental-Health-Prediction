from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# === Optional: Load your trained model if available ===
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        answers = data['answers']

        # Convert answers to numeric array
        features = np.array(answers, dtype=float).reshape(1, -1)

        # === MOCK LOGIC (replace with model.predict(features)) ===
        total = np.sum(features)
        if total <= 10:
            result = "Not Depressed"
        elif total <= 15:
            result = "Mildly Depressed"
        elif total <= 20:
            result = "Depressed"
        else:
            result = "Critically Depressed"

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
