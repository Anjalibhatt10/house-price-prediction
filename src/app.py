import streamlit as st
import joblib
import pandas as pd
from pathlib import Path


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# =========================================================
# LOAD MODEL
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = 1

if "price" not in st.session_state:
    st.session_state.price = None


# =========================================================
# PAGE 1 - WELCOME
# =========================================================

if st.session_state.page == 1:

    st.write("")
    st.write("")
    st.title("🏠 House Price Predictor")

    st.write("### Welcome! 👋")

    st.write(
        "Predict an estimated house price using "
        "Machine Learning."
    )

    st.write("")
    st.write("")
    
    st.write("**A Machine Learning Project by Anjali Bhatt**")

    st.write("Python • Scikit-learn • Streamlit")

    st.write("")
    st.write("")

    if st.button(
        "🚀 Let's Start",
        use_container_width=True
    ):
        st.session_state.page = 2
        st.rerun()


# =========================================================
# PAGE 2 - HOUSE DETAILS
# =========================================================

elif st.session_state.page == 2:

    st.title("🏡 House Details")

    st.write(
        "Enter the details below to estimate the house price."
    )

    st.write("")

    col1, col2 = st.columns(2)


    # -------------------------
    # LEFT COLUMN
    # -------------------------

    with col1:

        medinc = st.number_input(
            "Median Income ($10,000s)",
            min_value=0.0,
            value=4.0,
            step=0.1
        )

        house_age = st.number_input(
            "House Age (years)",
            min_value=0.0,
            value=20.0,
            step=1.0
        )

        ave_rooms = st.number_input(
            "Average Rooms per Household",
            min_value=0.0,
            value=5.0,
            step=0.1
        )

        ave_bedrms = st.number_input(
            "Average Bedrooms per Household",
            min_value=0.0,
            value=1.0,
            step=0.1
        )


    # -------------------------
    # RIGHT COLUMN
    # -------------------------

    with col2:

        population = st.number_input(
            "Block Population",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

        ave_occup = st.number_input(
            "Average Occupancy",
            min_value=0.0,
            value=3.0,
            step=0.1
        )

        latitude = st.number_input(
            "Latitude",
            value=35.0,
            step=0.1
        )

        longitude = st.number_input(
            "Longitude",
            value=-119.0,
            step=0.1
        )


    st.write("")


    # -------------------------
    # PREDICT BUTTON
    # -------------------------

    if st.button(
        "🔮 Predict House Price",
        use_container_width=True
    ):

        input_data = pd.DataFrame({
            "MedInc": [medinc],
            "HouseAge": [house_age],
            "AveRooms": [ave_rooms],
            "AveBedrms": [ave_bedrms],
            "Population": [population],
            "AveOccup": [ave_occup],
            "Latitude": [latitude],
            "Longitude": [longitude]
        })


        # Make prediction
        prediction = model.predict(input_data)


        # Convert model output to dollars
        price = prediction[0] * 100000


        # Save prediction
        st.session_state.price = price


        # Go to result page
        st.session_state.page = 3
        st.rerun()


    st.write("")

    # Back button
    if st.button("← Back to Welcome"):
        st.session_state.page = 1
        st.rerun()


# =========================================================
# PAGE 3 - RESULT
# =========================================================

elif st.session_state.page == 3:

    st.title("✨ Prediction Complete")

    st.write("")

    st.subheader("🏠 Estimated House Price")

    st.write("")

    st.metric(
        label="Predicted Price",
        value=f"${st.session_state.price:,.2f}"
    )

    st.write("")

    st.write(
        "This estimate is based on the property details "
        "you provided."
    )

    st.write("")
    st.write("")


    # -------------------------
    # TRY AGAIN
    # -------------------------

    if st.button(
        "🔄 Try Again",
        use_container_width=True
    ):
        st.session_state.page = 2
        st.session_state.price = None
        st.rerun()


    # -------------------------
    # HOME
    # -------------------------

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):
        st.session_state.page = 1
        st.session_state.price = None
        st.rerun()