# Fertilizer Prediction Model

A machine learning model package for predicting fertilizer.

## Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/PagnaMMA/fertilizer-recommendation-model-package.git
```

## Usage
```python
from fertilizer_model import FertilizerPredictor

# Initialize the predictor
predictor = FertilizerPredictor()

# Make predictions
features = [30.0, 200.0, 7.0, 0.70, 75.0, 85.0, 70.0, 'Alkaline Soil', 'wheat']  # Example features
prediction = predictor.predict_fertilizer(features)
print(f"Predicted fertilizer: {prediction}")
```

## Model Details

- Model type: [Gradient Boosting]
- Features: [Temperature, Rainfall, PH, Moisture, Nitrogen, Potassium,
         Phosphorous, Soil_Type, Crop]
- Target: fertilizer

## Version History

- 0.1.0: Initial release
```

## Step 9: Create `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db