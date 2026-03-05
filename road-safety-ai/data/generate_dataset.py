import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Ensure the script is running with knowledge of where the data folder is
# The script will be inside the data/ folder
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'accidents.csv')

def generate_accidents_dataset(num_records=5000):
    print(f"Generating synthetic roadmap accident dataset with {num_records} records...")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate random dates over the past year
    start_date = datetime(2023, 1, 1)
    dates = [
        start_date + timedelta(
            days=np.random.randint(0, 365), 
            hours=np.random.randint(0, 24), 
            minutes=np.random.randint(0, 60)
        ) 
        for _ in range(num_records)
    ]
    
    # Generate realistic-looking Lat/Lon (e.g., around a fictional major city)
    latitudes = np.random.uniform(40.7, 40.9, num_records)
    longitudes = np.random.uniform(-74.1, -73.8, num_records)
    
    # Categorical features
    weather_conditions = np.random.choice(['Clear', 'Rain', 'Fog', 'Snow'], num_records, p=[0.5, 0.25, 0.15, 0.10])
    road_types = np.random.choice(['Highway', 'Intersection', 'City Street', 'Rural Road'], num_records, p=[0.25, 0.35, 0.30, 0.10])
    traffic_densities = np.random.choice(['Low', 'Medium', 'High', 'Congested'], num_records, p=[0.20, 0.40, 0.25, 0.15])
    vehicle_types = np.random.choice(['Car', 'Motorcycle', 'Truck', 'Bus'], num_records, p=[0.60, 0.20, 0.15, 0.05])
    
    # Simulate realistic accident severity based on conditions
    # 0: Minor, 1: Moderate, 2: Severe
    severities = []
    for w, t, r in zip(weather_conditions, traffic_densities, road_types):
        risk_score = 0
        
        # Bad weather increases risk
        if w in ['Rain', 'Fog']: risk_score += 1
        if w == 'Snow': risk_score += 2
        
        # High traffic increases risk of minor/moderate, but highway/intersection speed increases severe risk
        if t in ['High', 'Congested']: risk_score += 1
        if r in ['Highway', 'Intersection']: risk_score += 1
        
        # Decide severity probability based on risk score
        if risk_score >= 3:
            severity = np.random.choice([0, 1, 2], p=[0.2, 0.5, 0.3]) # More severe
        elif risk_score >= 1:
            severity = np.random.choice([0, 1, 2], p=[0.5, 0.4, 0.1]) # Moderate
        else:
            severity = np.random.choice([0, 1, 2], p=[0.8, 0.18, 0.02]) # Mostly minor
            
        severities.append(severity)

    # Create DataFrame
    df = pd.DataFrame({
        'timestamp': dates,
        'latitude': latitudes,
        'longitude': longitudes,
        'weather_condition': weather_conditions,
        'road_type': road_types,
        'traffic_density': traffic_densities,
        'vehicle_type': vehicle_types,
        'accident_severity': severities
    })
    
    # Sort by timestamp to simulate chronological data collection
    df = df.sort_values(by='timestamp').reset_index(drop=True)
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Dataset successfully created and saved to: {output_file}")
    print(f"Dataset Shape: {df.shape}")

if __name__ == "__main__":
    generate_accidents_dataset()
