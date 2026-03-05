import os
import joblib
import pandas as pd

# Load artifacts
# We use absolute paths derived from the script's location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, 'models', 'risk_model.pkl')
scaler_path = os.path.join(base_dir, 'models', 'scaler.pkl')
encoders_path = os.path.join(base_dir, 'models', 'label_encoders.pkl')

try:
    risk_model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    label_encoders = joblib.load(encoders_path)
    
    # Target mapping from the Indian Dataset LabelEncoder
    # The classes were ['Fatal', 'Minor', 'Serious'] mapped to [0, 1, 2] alphabetically by LabelEncoder
    severity_mapping = {0: 'Fatal', 1: 'Minor', 2: 'Serious'}
except Exception as e:
    print(f"Error loading artifacts: {e}")

def predict_severity(input_data: dict) -> dict:
    """
    Takes a dict of features, scales and predicts the accident severity risk.
    """
    try:
        # Expected feature columns from the scaler
        expected_features = scaler.feature_names_in_
        
        # Create a dictionary to hold cleaned input
        processed_data = {}
        
        for feature in expected_features:
            # Get the value provided by user, or fallback to a default
            val = input_data.get(feature, None)
            
            # If the feature is categorical, we must encode it
            if feature in label_encoders:
                # If user didn't provide a value, fallback to the most common (mode from encoder classes)
                if val is None or str(val) not in label_encoders[feature].classes_:
                    val = label_encoders[feature].classes_[0]
                # Encode
                processed_data[feature] = label_encoders[feature].transform([str(val)])[0]
            else:
                # Numeric Feature
                if val is None:
                    processed_data[feature] = 0 # Default fallback
                else:
                    try:
                        processed_data[feature] = float(val)
                    except ValueError:
                        processed_data[feature] = 0.0

        # Convert to DataFrame in the exact feature order
        df = pd.DataFrame([processed_data], columns=expected_features)
        
        # Scale Features
        X_scaled = scaler.transform(df)
        
        # Predict
        prediction_num = risk_model.predict(X_scaled)[0]
        
        # Decode prediction mapping
        predicted_severity = severity_mapping.get(int(prediction_num), str(prediction_num))

        return {
            "predicted_severity": predicted_severity,
            "status": "success"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
