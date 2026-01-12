import streamlit as st
import requests

API_URL = "http://13.62.18.68:8000/predict" 

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

#input fields

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()['response']
            
            # Display prediction result in a visually appealing way
            st.markdown("---")
            st.markdown("### 🎯 Prediction Results")
            
            # Main prediction with colored badge
            category = result['predicted_category']
            confidence = result['confidence']
            
            if category == 'Low':
                st.success(f"### ✅ Premium Category: **{category}**")
            elif category == 'Medium':
                st.warning(f"### ⚠️ Premium Category: **{category}**")
            else:
                st.error(f"### 🔴 Premium Category: **{category}**")
            
            # Confidence score with progress bar
            st.metric(label="Confidence Score", value=f"{confidence:.1%}")
            st.progress(confidence)
            
            # Class probabilities
            st.markdown("#### 📊 Probability Distribution")
            probs = result['class_probabilities']
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="🟢 Low", value=f"{probs['Low']:.1%}")
            with col2:
                st.metric(label="🟡 Medium", value=f"{probs['Medium']:.1%}")
            with col3:
                st.metric(label="🔴 High", value=f"{probs['High']:.1%}")
            
            # Visual bar chart
            st.bar_chart(probs)
        
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")