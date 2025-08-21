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

## 📈 Performance

**Model Performance:**
- Validation Accuracy: ~66-68%
- Training Strategy: Transfer learning with data augmentation
- Inference Time: ~100-200ms per image (CPU)

## ⚕️ Clinical Applications

**Primary Use Cases:**
- **Screening Tool**: Initial assessment of suspicious lesions
- **Educational Platform**: Training for medical students and residents
- **Telemedicine**: Remote skin lesion evaluation
- **Research**: Baseline for comparative studies

**Important Disclaimers:**
- This system is for screening and educational purposes only
- Not intended to replace professional medical diagnosis
- Clinical decisions should always involve qualified healthcare providers
- Requires proper validation in clinical settings before deployment

## 📄 License

This project is intended for research and educational purposes. Please ensure compliance with medical device regulations and clinical validation requirements before any clinical deployment.

---

**Disclaimer**: This system is for research and educational purposes only. Not intended for clinical diagnosis without proper validation and regulatory approval.