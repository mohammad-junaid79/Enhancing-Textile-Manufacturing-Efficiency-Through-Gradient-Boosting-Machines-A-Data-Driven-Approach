from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('gradient_boosting_model.pkl')

# Home route for rendering the form
@app.route('/')
def index():
    return render_template('index.html')

# Predict route for handling form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure all 28 features are being extracted from the form
        features = [
            float(request.form['TOTAL_LENGTH']),
            float(request.form['THEORY_LENGTH']),
            float(request.form['WARPTOTAL']),
            float(request.form['YA_RN_SPEC_DEN_IM']),
            float(request.form['YARN_SPEC_FIBERBASE']),
            float(request.form['DEN_IM']),
            float(request.form['FIBERBASE']),
            float(request.form['UNITWEIGHT']),
            float(request.form['GRANULARITY']),
            float(request.form['WARPLENGTH']),
            float(request.form['WARPSTRIP']),
            float(request.form['SIZINGLENGTH']),
            float(request.form['WARPSPEED']),
            float(request.form['WARPPRES']),
            float(request.form['SSTENSION']),
            float(request.form['WARPTENSION']),
            float(request.form['HYDRATENSION']),
            float(request.form['SIZINGSPEED']),
            float(request.form['SIZINGBPRES']),
            float(request.form['SIZINGATENSION']),
            float(request.form['SIZINGBTENSION']),
            float(request.form['CONSISTENCY']),
            float(request.form['DENSITY']),
            float(request.form['BEAMSPEED']),
            float(request.form['BEAMATENSION']),
            float(request.form['BEAMBTENSION']),
            float(request.form['BEAMTENSION']),
            float(request.form['WEAVEBTENSION'])
        ]

        # Convert features to numpy array
        input_data = np.array(features).reshape(1, -1)

        # Make the prediction
        prediction = model.predict_proba(input_data)[0][1]  # Predict probability for class 1

        # Return the prediction in the HTML page
        return render_template('index.html', prediction=f'{prediction:.4f}')

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)