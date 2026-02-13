import streamlit as st
import joblib
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Crop Yield Predictor", page_icon="🌾")

# 2. Loading the Pipeline
@st.cache_resource
def load_model():
    return joblib.load("crop_yield_model.pkl")

model = load_model()

# 3. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Prediction", "History", "Dataset Info", "Settings"])

if page == "Prediction":
    st.title("🌾 Crop Yield Prediction")
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            crop = st.selectbox("Crop Type", options=["Maize", "Rice", "Cassava", "Wheat", "Sorghum"])
            area = st.number_input("Area (Hectares)", min_value=0.1, value=1.0, step=0.1)
            rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=1200.0)
            temp = st.number_input("Temperature (°C)", value=28.0)
            
        with col2:
            humidity = st.slider("Humidity (%)", 0, 100, 75)
            sunlight = st.number_input("Sunlight Hours", min_value=0.0, max_value=24.0, value=7.5)
            soil_ph = st.slider("Soil pH", 0.0, 14.0, 6.5)
            
        st.write("**Soil Nutrients**")
        n_col, p_col, k_col = st.columns(3)
        n = n_col.number_input("N", value=80.0)
        p = p_col.number_input("P", value=45.0)
        k = k_col.number_input("K", value=60.0)

        submit = st.form_submit_button("Predict Yield")

    if submit:
        # Create input DataFrame
        input_df = pd.DataFrame([{
            "rainfall_mm": rainfall,
            "temperature_c": temp,
            "humidity_percent": humidity,
            "soil_ph": soil_ph,
            "nitrogen": n,
            "phosphorus": p,
            "potassium": k,
            "sunlight_hours": sunlight,
            "area_hectares": area,
            "crop_type": crop
        }])

        prediction = model.predict(input_df)[0]
        
        st.success(f"### Estimated Yield: **{prediction:.2f} tonnes**")
        
        # Save to session state for the 'History' page
        if 'history' not in st.session_state:
            st.session_state['history'] = []
        st.session_state['history'].append({"Crop": crop, "Yield": round(prediction, 2)})

elif page == "History":
    st.title("📜 Prediction History")
    if 'history' in st.session_state and st.session_state['history']:
        st.table(pd.DataFrame(st.session_state['history']))
    else:
        st.info("No predictions made yet.")

elif page == "Dataset Info":
    st.title("📊 Dataset & Model Metrics")
    st.write("The model was trained on `crop_yield_data.csv`.")
    st.metric("Model Accuracy ($R^2$)", "0.79")
    st.metric("RMSE", "0.53")

elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("App version: 1.0.0")