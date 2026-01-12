# 🏥 Insurance Premium Prediction System

A full-stack machine learning application that predicts insurance premium categories (Low, Medium, High) based on user demographics, lifestyle factors, and financial information. Built with FastAPI backend and Streamlit frontend.

## 🌐 Live Demo

- **Frontend (Streamlit)**: [https://insurance-premium-prediction-website.streamlit.app/](https://insurance-premium-prediction-website.streamlit.app/)
- **Backend API (AWS EC2)**: `http://13.62.18.68:8000`
- **API Documentation**: `http://13.62.18.68:8000/docs` (FastAPI Swagger UI)

## 📋 Table of Contents
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
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

### Deployment
- **AWS EC2**: Backend API hosting (Ubuntu server)
- **Streamlit Community Cloud**: Frontend deployment
- **Docker**: Containerization (optional)

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    End User                             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│          Streamlit Frontend                             │
│    (Streamlit Community Cloud)                          │
│    https://insurance-premium-prediction-website         │
│           .streamlit.app/                               │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ HTTP POST /predict
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│          FastAPI Backend                                │
│          (AWS EC2 Instance)                             │
│          http://13.62.18.68:8000                        │
│                                                          │
│  ┌──────────────┐      ┌──────────────┐                │
│  │  Pydantic    │      │   ML Model   │                │
│  │  Validation  │─────▶│  (Pickle)    │                │
│  └──────────────┘      └──────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
insurance_premium_prediction/
│
├── app.py                      # FastAPI application entry point
├── frontend.py                 # Streamlit frontend application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration for containerization
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
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

## 🚀 Deployment

This application is deployed and accessible online:

### Frontend Deployment (Streamlit Community Cloud)

The Streamlit frontend is deployed on **Streamlit Community Cloud** and accessible at:
**[https://insurance-premium-prediction-website.streamlit.app/](https://insurance-premium-prediction-website.streamlit.app/)**

**Deployment Steps:**
1. Push code to GitHub repository
2. Sign in to [share.streamlit.io](https://share.streamlit.io) with GitHub
3. Select repository and branch
4. Set main file as `frontend.py`
5. Deploy automatically

**Requirements for Streamlit Cloud:**
- `requirements.txt` with all dependencies
- Public GitHub repository
- Python 3.8+ compatible code

### Backend Deployment (AWS EC2)

The FastAPI backend is hosted on **AWS EC2** (Ubuntu instance) and accessible at:
**`http://13.62.18.68:8000`**

**Deployment Steps:**

1. **Launch EC2 Instance**
   ```bash
   # Amazon Linux 2 or Ubuntu Server
   # Instance type: t2.micro (free tier eligible)
   # Security Group: Allow HTTP (80), Custom TCP (8000)
   ```

2. **SSH into EC2 Instance**
   ```bash
   ssh -i your-key.pem ubuntu@13.62.18.68
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv -y
   ```

4. **Clone Repository**
   ```bash
   git clone https://github.com/pratikbugade01/FastAPI_Project.git
   cd FastAPI_Project
   ```

5. **Setup Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Run FastAPI Server**
   ```bash
   # For testing
   uvicorn app:app --host 0.0.0.0 --port 8000
   
   # For production (using screen or tmux)
   screen -S fastapi
   uvicorn app:app --host 0.0.0.0 --port 8000
   # Detach: Ctrl+A then D
   ```

7. **Optional: Setup as Systemd Service**
   ```bash
   sudo nano /etc/systemd/system/fastapi.service
   ```
   
   Add:
   ```ini
   [Unit]
   Description=FastAPI Insurance Prediction API
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/FastAPI_Project
   Environment="PATH=/home/ubuntu/FastAPI_Project/venv/bin"
   ExecStart=/home/ubuntu/FastAPI_Project/venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000

   [Install]
   WantedBy=multi-user.target
   ```
   
   Enable and start:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable fastapi
   sudo systemctl start fastapi
   sudo systemctl status fastapi
   ```

### Docker Deployment (Optional)

Build and run using Docker:

```bash
# Build image
docker build -t insurance-prediction-api .

# Run container
docker run -d -p 8000:8000 insurance-prediction-api
```

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

### City Tier Classification
- **Tier 1**: Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune
- **Tier 2**: Jaipur, Chandigarh, Indore, Lucknow, Patna, and 40+ other cities
- **Tier 3**: All other cities

## 📊 Screenshots

### Live Application
Visit the live app: [https://insurance-premium-prediction-website.streamlit.app/](https://insurance-premium-prediction-website.streamlit.app/)

### Features in Action:
- Interactive input form with real-time validation
- Color-coded premium category predictions (🟢 Low, 🟡 Medium, 🔴 High)
- Confidence scores with visual progress bars
- Probability distribution across all categories
- Responsive bar charts for visual analysis

## 🔒 Security Note

**Important**: The current deployment uses HTTP. For production use, consider:
- Setting up HTTPS with SSL/TLS certificates (Let's Encrypt)
- Using AWS Application Load Balancer with HTTPS
- Implementing API authentication (API keys, JWT tokens)
- Setting up CORS policies appropriately
- Using environment variables for sensitive configuration

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
- AWS for cloud infrastructure
- Streamlit Community Cloud for free hosting

## 📫 Contact

For questions, suggestions, or issues, please:
- Open an issue on GitHub
- Contact: [GitHub @pratikbugade01](https://github.com/pratikbugade01)

---

**Note**: 
- The live application is available at [https://insurance-premium-prediction-website.streamlit.app/](https://insurance-premium-prediction-website.streamlit.app/)
- Backend API hosted on AWS EC2: `http://13.62.18.68:8000`
- For local development, make sure both the FastAPI server and Streamlit app are running simultaneously
