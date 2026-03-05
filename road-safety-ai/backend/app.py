from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_severity
import traceback

app = Flask(__name__)
# Enable CORS for dashboard integration
CORS(app)

@app.route('/', methods=['GET'])
def index():
    """Root route confirming the API is running."""
    return jsonify({
        "message": "Road Safety AI Backend Running"
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction Endpoint for Dashboard."""
    try:
        # 1. Receive JSON request
        input_data = request.get_json()
        
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400
            
        # 2. Pass input to predict_severity() from predict.py
        result = predict_severity(input_data)
        
        # 3. Return prediction result as JSON
        if result.get("status") == "success":
            return jsonify({
                "predicted_severity": result.get("predicted_severity")
            })
        else:
            return jsonify({
                "error": "Prediction Failed",
                "details": result.get("message")
            }), 500
            
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e), "trace": traceback.format_exc()}), 500

if __name__ == '__main__':
    # Step 4: Run locally
    print("Starting ML Backend Server. Accessible at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
