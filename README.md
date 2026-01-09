# 🏥 Insurance Premium Prediction System

A full-stack machine learning application that predicts insurance premium categories (Low, Medium, High) based on user demographics, lifestyle factors, and financial information. Built with FastAPI backend and Streamlit frontend.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Real-time Predictions**: Get instant insurance premium category predictions
- **Interactive UI**: User-friendly Streamlit interface with visual feedback
- **RESTful API**: FastAPI backend for easy integration with other services
- **Probability Distribution**: See confidence scores and class probabilities
- **Visual Analytics**: Bar charts and metrics for better understanding
- **Health Check Endpoint**: Monitor API status and model version
- **Input Validation**: Pydantic schemas for robust data validation

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **scikit-learn**: Machine learning model training and prediction
- **Uvicorn**: ASGI server for running FastAPI

### Frontend
- **Streamlit**: Python library for creating interactive web applications
- **Requests**: HTTP library for API communication

### Machine Learning
- **scikit-learn**: Model training and prediction
- **pandas**: Data manipulation and preprocessing
- **numpy**: Numerical computing

## 📁 Project Structure

```
insurance_premium_prediction/
│
├── app.py                      # FastAPI application entry point
├── frontend.py                 # Streamlit frontend application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
│
├── config/
│   └── city_tier.py           # City tier configuration mapping
│
├── model/
│   ├── predict.py             # Prediction logic and model loading
│   └── model.pkl              # Trained ML model (pickle file)
│
└── schema/
    ├── user_input.py          # Pydantic schema for input validation
    └── prediction_response.py # Pydantic schema for API response
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/pratikbugade01/FastAPI_Project.git
cd insurance_premium_prediction
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv myenv
myenv\Scripts\activate

# On macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Application

#### 1. Start the FastAPI Backend
Open a terminal and run:
```bash
# Activate virtual environment first
myenv\Scripts\activate  # Windows
# source myenv/bin/activate  # macOS/Linux

# Start the API server
uvicorn app:app --reload
```
The API will be available at `http://127.0.0.1:8000`

#### 2. Start the Streamlit Frontend
Open a new terminal and run:
```bash
# Activate virtual environment first
myenv\Scripts\activate  # Windows
# source myenv/bin/activate  # macOS/Linux

# Start Streamlit
streamlit run frontend.py
```
The frontend will open automatically in your browser at `http://localhost:8501`

### Using the Application

1. **Enter User Details**:
   - Age
   - Weight (kg)
   - Height (m)
   - Annual Income (LPA)
   - Smoking status
   - City
   - Occupation

2. **Click "Predict Premium Category"**

3. **View Results**:
   - Premium category (Low/Medium/High) with color coding
   - Confidence score with progress bar
   - Probability distribution across all categories
   - Visual bar chart

## 🔌 API Endpoints

### 1. Home
```http
GET /
```
Returns a welcome message.

**Response:**
```json
{
  "message": "This is a Insurance_premium_prediction API"
}
```

### 2. Health Check
```http
GET /health
```
Check API status and model information.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "model_loaded": true
}
```

### 3. Predict Premium
```http
POST /predict
```
Predict insurance premium category based on user input.

**Request Body:**
```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 12.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": {
    "predicted_category": "Low",
    "confidence": 0.47,
    "class_probabilities": {
      "High": 0.08,
      "Low": 0.47,
      "Medium": 0.45
    }
  }
}
```

## 🤖 Model Information

The prediction model considers the following features:
- **BMI**: Calculated from weight and height
- **Age Group**: Categorized age ranges
- **Lifestyle Risk**: Derived from smoking status
- **City Tier**: Metropolitan/Tier-1/Tier-2/Tier-3 classification
- **Income (LPA)**: Annual income in lakhs
- **Occupation**: Job category

### Supported Occupations
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

## 📊 Screenshots

<!-- Add screenshots here -->
*Coming soon: Add screenshots of the Streamlit interface and API documentation*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Pratik Bugade**
- GitHub: [@pratikbugade01](https://github.com/pratikbugade01)

## 🙏 Acknowledgments

- FastAPI documentation and community
- Streamlit team for the amazing framework
- scikit-learn contributors

---

**Note**: Make sure both the FastAPI server and Streamlit app are running simultaneously for the application to work properly.
