# Skin Cancer Classification System

A comprehensive deep learning-based system for automated skin cancer detection and classification using convolutional neural networks.

## 🔬 Project Overview

This project implements an end-to-end skin cancer classification system that can identify seven different types of skin lesions using deep learning. The system uses transfer learning with EfficientNetB3 architecture trained on the HAM10000 dataset and provides a user-friendly web interface for real-time predictions.

## 🎯 Key Features

- **7-Class Classification**: Melanoma, Nevus, Seborrheic Keratosis, Basal Cell Carcinoma, Actinic Keratosis, Benign Keratosis, Dermatofibroma
- **Deep Learning Model**: EfficientNetB3 with transfer learning from ImageNet
- **Web Interface**: Modern, responsive UI with drag-and-drop functionality
- **Real-time Predictions**: Instant classification with confidence scores
- **Clinical Focus**: Designed for medical screening and educational purposes

## 📊 Dataset

**HAM10000 Dataset**: 10,015 dermatoscopic images of pigmented skin lesions
- Multi-source collection from different institutions
- Ground truth based on histopathology, expert consensus, or confocal microscopy
- Covers the most common skin lesion types in clinical practice

## 🏗️ Model Architecture

```
EfficientNetB3 (Pre-trained on ImageNet)
├── GlobalAveragePooling2D
├── Dropout(0.3)
├── Dense(128, ReLU)
├── Dropout(0.2)
└── Dense(7, Softmax)
```

**Model Specifications:**
- Input Size: 224×224×3
- Parameters: ~12M
- Training: Transfer learning with frozen base model
- Optimization: Adam optimizer (lr=1e-4)
- Regularization: Dropout, Early Stopping, Learning Rate Reduction

## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.8
tensorflow >= 2.8.0
flask >= 2.0.0
opencv-python >= 4.5.0
```

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd skin-cancer-classification
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the interface**
   - Open your browser and navigate to `http://localhost:8000`
   - Upload a skin lesion image using drag-and-drop or file selection
   - Click "Predict" to get classification results

### API Usage

**Endpoint**: `POST /predict`

**Request Format**:
```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}
```

**Response Format**:
```json
{
  "predictions": [
    {"label": "Melanoma", "prob": 0.85},
    {"label": "Nevus", "prob": 0.10},
    {"label": "Basal Cell Carcinoma", "prob": 0.03},
    ...
  ]
}
```

## 📁 Project Structure

```
skin-cancer-classification/
├── app.py                      # Flask web application
├── interface.html              # Web interface
├── skin-cancer-cnn.ipynb      # Training notebook
├── best_model.h5               # Trained model weights
├── evaluation.png              # Training curves
├── prediction.png              # Sample predictions
├── SCIENTIFIC_DOCUMENTATION.md # Detailed scientific documentation
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

## 📈 Performance

**Model Performance:**
- Validation Accuracy: ~66-68%
- Training Strategy: Transfer learning with data augmentation
- Inference Time: ~100-200ms per image (CPU)

**Training Configuration:**
- Epochs: 30 (with early stopping)
- Batch Size: 16
- Data Split: 80% training, 20% validation
- Augmentation: Random flips and rotations

## 🖥️ Web Interface Features

- **Modern Design**: Clean, professional medical interface
- **Drag & Drop**: Intuitive image upload
- **Real-time Preview**: Immediate image visualization
- **Progress Bars**: Visual probability representation
- **Responsive**: Works on desktop and mobile devices
- **Clinical Information**: Architecture notes and usage guidelines


## ⚕️ Clinical Applications

**Primary Use Cases:**
- **Screening Tool**: Initial assessment of suspicious lesions
- **Educational Platform**: Training for medical students and residents
- **Telemedicine**: Remote skin lesion evaluation
- **Research**: Baseline for comparative studies


## 🛠️ Technical Details

**Core Technologies:**
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deep Learning**: TensorFlow/Keras
- **Image Processing**: OpenCV, PIL
- **Visualization**: Matplotlib, Seaborn

**System Requirements:**
- RAM: 8GB minimum, 16GB recommended
- Storage: 2GB for model and dependencies
- GPU: Optional for training, CPU sufficient for inference

## 🚀 Deployment

### Local Development
```bash
python app.py
# Access at http://localhost:8000
```

### Production Deployment
- Use WSGI server (Gunicorn, uWSGI)
- Configure reverse proxy (Nginx)
- Implement SSL/TLS encryption
- Set up monitoring and logging
- Consider GPU acceleration for high-volume inference

## 📝 Model Training

To retrain the model with new data:

1. **Prepare Dataset**: Organize images in HAM10000 format
2. **Run Training**: Execute `skin-cancer-cnn.ipynb`
3. **Evaluate Results**: Review training curves and validation metrics
4. **Update Model**: Replace `best_model.h5` with new weights

## 🏥 Clinical Validation

**Important**: This system requires proper clinical validation before deployment in healthcare settings. Consider:
- IRB approval for clinical studies
- Validation on diverse patient populations
- Integration with existing clinical workflows
- Regulatory compliance (FDA, CE marking, etc.)

## 📚 References

1. HAM10000 Dataset: Tschandl et al., Scientific Data 2018
2. EfficientNet: Tan & Le, ICML 2019
3. Dermatology AI: Esteva et al., Nature 2017
4. Clinical Validation: Haenssle et al., Annals of Oncology 2018



**Disclaimer**: This system is for research and educational purposes only. Not intended for clinical diagnosis without proper validation and regulatory approval.
