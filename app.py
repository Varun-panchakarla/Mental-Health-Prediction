from flask import Flask, render_template, request, jsonify, url_for
import numpy as np
import pickle

app = Flask(__name__)

# === Optional: Load your trained model if available ===
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# === LANDING PAGE ===
@app.route('/')
def index():
    """
    Displays the landing (index) page.
    """
    return render_template('index.html')


# === MAIN FORM PAGE ===
@app.route('/form')
def form_page():
    """
    Displays the main depression test form.
    """
    return render_template('main.html')


# === PREDICTION ENDPOINT ===
@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles incoming JSON data from frontend,
    processes it, and returns depression prediction.
    """
    try:
        data = request.get_json()
        answers = data.get('answers', [])

        if not answers:
            return jsonify({'error': 'No answers received'}), 400

        # Convert to NumPy array for model processing
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
        return jsonify({'error': str(e)}), 500


# === RUN SERVER ===
if __name__ == '__main__':
    app.run(debug=True, port=5000)
