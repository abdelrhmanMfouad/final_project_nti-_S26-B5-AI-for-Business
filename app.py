
import json
import joblib
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Blight Compliance Predictor",
    page_icon="🏠",
    layout="centered"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load(
        "best_blight_compliance_model.pkl"
    )


try:

    model = load_model()

except Exception as e:

    st.error("❌ Could not load the model.")

    st.code(str(e))

    st.info(
        """
        Make sure:

        • best_blight_compliance_model.pkl
          is in the same folder as app.py

        • All required packages are installed.

        • The model was trained with a compatible
          scikit-learn version.
        """
    )

    st.stop()


# ============================================================
# LOAD OPTIONS
# ============================================================

@st.cache_data
def load_options():

    with open(
        "options.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


try:

    options = load_options()

except Exception as e:

    st.error("❌ Could not load options.json.")

    st.code(str(e))

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("🏠 Blight Compliance Predictor")

st.write(
    """
    Use the property and ticket information below
    to predict whether the ticket is likely to be compliant.
    """
)

st.divider()


# ============================================================
# TICKET INFORMATION
# ============================================================

st.subheader("📋 Ticket Information")


col1, col2 = st.columns(2)


with col1:

    agency_name = st.selectbox(
        "Agency Name",
        options=options["agency_name"],
        index=None,
        placeholder="Search or select agency..."
    )

    city = st.selectbox(
        "City",
        options=options["city"],
        index=None,
        placeholder="Search or select city..."
    )


with col2:

    state = st.selectbox(
        "State",
        options=options["state"],
        index=None,
        placeholder="Search or select state..."
    )

    disposition = st.selectbox(
        "Disposition",
        options=options["disposition"],
        index=None,
        placeholder="Search or select disposition..."
    )


# ============================================================
# ADDRESS INFORMATION
# ============================================================

st.subheader("📍 Address Information")


col1, col2 = st.columns(2)


with col1:

    violation_street_number = st.number_input(
        "Violation Street Number",
        min_value=0.0,
        value=0.0,
        step=1.0
    )


with col2:

    mailing_address_str_number = st.number_input(
        "Mailing Address Street Number",
        min_value=0.0,
        value=0.0,
        step=1.0
    )


# ============================================================
# FINANCIAL INFORMATION
# ============================================================

st.subheader("💰 Financial Information")


col1, col2, col3 = st.columns(3)


with col1:

    fine_amount = st.number_input(
        "Fine Amount",
        min_value=0.0,
        value=100.0,
        step=10.0
    )


with col2:

    admin_fee = st.number_input(
        "Admin Fee",
        min_value=0.0,
        value=20.0,
        step=5.0
    )


with col3:

    state_fee = st.number_input(
        "State Fee",
        min_value=0.0,
        value=0.0,
        step=5.0
    )


col1, col2 = st.columns(2)


with col1:

    late_fee = st.number_input(
        "Late Fee",
        min_value=0.0,
        value=0.0,
        step=5.0
    )


with col2:

    discount_amount = st.number_input(
        "Discount Amount",
        min_value=0.0,
        value=0.0,
        step=5.0
    )


st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.subheader("🤖 Prediction")


predict_button = st.button(
    "🔮 Predict Compliance",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # CHECK REQUIRED STRING INPUTS
    # --------------------------------------------------------

    if (
        agency_name is None
        or city is None
        or state is None
        or disposition is None
    ):

        st.warning(
            "⚠️ Please select all required options before predicting."
        )

        st.stop()


    # --------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame({

        "agency_name": [
            agency_name
        ],

        "violation_street_number": [
            violation_street_number
        ],

        "mailing_address_str_number": [
            mailing_address_str_number
        ],

        "city": [
            city
        ],

        "state": [
            state
        ],

        "disposition": [
            disposition
        ],

        "fine_amount": [
            fine_amount
        ],

        "admin_fee": [
            admin_fee
        ],

        "state_fee": [
            state_fee
        ],

        "late_fee": [
            late_fee
        ],

        "discount_amount": [
            discount_amount
        ]

    })


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    try:

        prediction = model.predict(
            input_data
        )[0]


        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        probability = None

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_data
            )[0]

            # Probability of class 1
            if len(probabilities) > 1:

                probability = probabilities[1]


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.divider()

        st.subheader("📊 Prediction Result")


        if prediction == 1:

            st.success(
                "### ✅ Likely to Comply"
            )

        else:

            st.error(
                "### ❌ Likely Not to Comply"
            )


        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        if probability is not None:

            probability_percent = (
                probability * 100
            )


            if probability >= 0.75:

                risk = "Low"

            elif probability >= 0.50:

                risk = "Medium"

            else:

                risk = "High"


            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "Compliance Probability",
                    f"{probability_percent:.2f}%"
                )


            with col2:

                st.metric(
                    "Risk Level",
                    risk
                )


            st.write(
                "**Compliance Probability**"
            )

            st.progress(
                float(probability)
            )


            # ------------------------------------------------
            # RECOMMENDATION
            # ------------------------------------------------

            st.subheader("💡 Recommendation")


            if probability >= 0.75:

                st.info(
                    """
                    The model predicts a high probability
                    of compliance. Standard follow-up should
                    be sufficient.
                    """
                )

            elif probability >= 0.50:

                st.warning(
                    """
                    The model predicts a moderate probability
                    of compliance. Additional monitoring
                    may be useful.
                    """
                )

            else:

                st.error(
                    """
                    The model predicts a low probability
                    of compliance. Consider prioritizing
                    this ticket for follow-up.
                    """
                )


        # ----------------------------------------------------
        # INPUT SUMMARY
        # ----------------------------------------------------

        with st.expander(
            "🔎 View input data"
        ):

            st.dataframe(
                input_data,
                use_container_width=True,
                hide_index=True
            )


    except Exception as e:

        st.error(
            "❌ Prediction failed."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Blight Compliance Prediction • AI for Business Project"
)

