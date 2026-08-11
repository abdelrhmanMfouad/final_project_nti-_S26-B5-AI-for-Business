
import streamlit as st
import pandas as pd
import numpy as np
import joblib



st.set_page_config(
    page_title="Blight Compliance AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

.stApp {
    background: #f5f7fb;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}


/* HERO */

.hero {
    background: linear-gradient(
        135deg,
        #111827 0%,
        #1f2937 50%,
        #374151 100%
    );

    padding: 38px 42px;
    border-radius: 24px;
    margin-bottom: 28px;
    color: white;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.12);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    margin: 0 0 8px 0;
}

.hero p {
    font-size: 17px;
    color: #d1d5db;
    margin: 0;
}


/* CARDS */

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.05);

    margin-bottom: 20px;
}

.card-title {
    font-size: 21px;
    font-weight: 750;
    color: #111827;
    margin-bottom: 5px;
}

.card-subtitle {
    font-size: 14px;
    color: #6b7280;
}


/* RESULT */

.result-card {
    padding: 32px;
    border-radius: 22px;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.success-card {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
}

.warning-card {
    background: #fffbeb;
    border: 1px solid #fde68a;
}

.danger-card {
    background: #fef2f2;
    border: 1px solid #fecaca;
}

.probability {
    font-size: 50px;
    font-weight: 850;
    margin: 10px 0;
}

.result-title {
    font-size: 26px;
    font-weight: 800;
}

.result-text {
    font-size: 15px;
    color: #4b5563;
}


/* RISK BADGES */

.risk-low {
    display: inline-block;
    padding: 7px 18px;
    border-radius: 30px;
    background: #d1fae5;
    color: #065f46;
    font-weight: 700;
}

.risk-medium {
    display: inline-block;
    padding: 7px 18px;
    border-radius: 30px;
    background: #fef3c7;
    color: #92400e;
    font-weight: 700;
}

.risk-high {
    display: inline-block;
    padding: 7px 18px;
    border-radius: 30px;
    background: #fee2e2;
    color: #991b1b;
    font-weight: 700;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #111827;
}

section[data-testid="stSidebar"] * {
    color: white;
}


/* BUTTON */

.stButton > button {
    width: 100%;
    border-radius: 13px;
    padding: 13px 20px;

    font-size: 16px;
    font-weight: 700;

    border: none;

    background: #111827;
    color: white;

    transition: 0.2s;
}

.stButton > button:hover {
    background: #374151;
    transform: translateY(-1px);
}


/* METRICS */

[data-testid="stMetric"] {
    background: white;
    padding: 18px;

    border-radius: 15px;
    border: 1px solid #e5e7eb;

    box-shadow:
        0 4px 15px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)


MODEL_PATH = "best_blight_compliance_model.pkl"


@st.cache_resource
def load_model():

    return joblib.load(
        MODEL_PATH
    )


try:

    model = load_model()

except Exception as e:

    st.error(
        "❌ Could not load the model."
    )

    st.code(
        str(e)
    )

    st.info(
        """
        Make sure that:

        • best_blight_compliance_model.pkl
          is in the same folder as app.py

        • The required Python packages
          are installed.

        • The sklearn version is compatible
          with the version used to train the model.
        """
    )

    st.stop()



with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px 0 25px 0;
        ">

            <div style="font-size:55px;">
                🏠
            </div>

            <h2 style="margin:0;">
                Blight AI
            </h2>

            <p style="color:#9ca3af;">
                Compliance Prediction
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 🤖 About the Model")

    st.write(
        """
        This Machine Learning system predicts
        whether a property maintenance ticket
        is likely to be compliant.
        """
    )

    st.markdown("---")

    st.markdown("### 📊 Prediction")

    st.write(
        """
        The system provides:

        • Compliance prediction
        • Probability score
        • Risk level
        • Business recommendation
        """
    )

    st.markdown("---")

    st.caption(
        "AI for Business Project"
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <h1>
            🏠 Blight Compliance AI
        </h1>

        <p>
            AI-powered property maintenance
            compliance prediction system
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TOP METRICS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Problem Type",
        "Classification"
    )


with col2:

    st.metric(
        "Target",
        "Compliance"
    )


with col3:

    st.metric(
        "AI Output",
        "Probability"
    )


st.markdown("<br>", unsafe_allow_html=True)



st.markdown(
    """
    <div class="card">

        <div class="card-title">
            🎯 Ticket Information
        </div>

        <div class="card-subtitle">
            Enter the information about the
            property maintenance ticket.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)



col1, col2 = st.columns(2)


with col1:

    agency_name = st.text_input(
        "Agency Name",
        placeholder="Example: Department of Public Works"
    )


with col2:

    disposition = st.text_input(
        "Disposition",
        placeholder="Enter disposition"
    )



col1, col2 = st.columns(2)


with col1:

    city = st.text_input(
        "City",
        value="Detroit"
    )


with col2:

    state = st.text_input(
        "State",
        value="MI"
    )




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



st.markdown(
    """
    <div class="card">

        <div class="card-title">
            💰 Financial Information
        </div>

        <div class="card-subtitle">
            Enter ticket-related financial values.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


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

with st.expander(
    "🔎 View submitted information"
):

    st.dataframe(
        input_data,
        use_container_width=True,
        hide_index=True
    )



st.markdown("<br>", unsafe_allow_html=True)


predict_button = st.button(
    "🔮 Predict Compliance"
)



if predict_button:

    try:

        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]


        probability_percent = (
            probability * 100
        )



        if probability >= 0.75:

            risk = "LOW RISK"

            risk_class = "risk-low"

            card_class = "success-card"

            recommendation = """
            The model estimates a high probability
            of compliance.

            Standard monitoring and follow-up should
            be sufficient.
            """


        elif probability >= 0.50:

            risk = "MEDIUM RISK"

            risk_class = "risk-medium"

            card_class = "warning-card"

            recommendation = """
            The model estimates a moderate probability
            of compliance.

            Additional monitoring may be useful.
            """


        else:

            risk = "HIGH RISK"

            risk_class = "risk-high"

            card_class = "danger-card"

            recommendation = """
            The model estimates a low probability
            of compliance.

            This ticket may require higher-priority
            follow-up.
            """


        if prediction == 1:

            result_title = (
                "Likely to Comply"
            )

        else:

            result_title = (
                "Likely Not to Comply"
            )


        st.markdown(
            f"""
            <div class="result-card {card_class}">

                <div class="result-title">
                    {result_title}
                </div>

                <div class="probability">
                    {probability_percent:.1f}%
                </div>

                <div class="result-text">
                    Compliance Probability
                </div>

                <br>

                <span class="{risk_class}">
                    {risk}
                </span>

            </div>
            """,
            unsafe_allow_html=True
        )



        st.markdown(
            "### 📊 Compliance Probability"
        )

        st.progress(
            float(probability)
        )



        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    💡 Business Recommendation
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            recommendation
        )


        st.markdown(
            "### 📋 Prediction Details"
        )


        result_df = pd.DataFrame({

            "Metric": [
                "Prediction",
                "Probability",
                "Risk Level"
            ],

            "Result": [
                result_title,
                f"{probability_percent:.2f}%",
                risk
            ]

        })


        st.dataframe(
            result_df,
            use_container_width=True,
            hide_index=True
        )


        with st.expander(
            "🤖 Model Output"
        ):

            st.write(
                "Raw prediction:",
                prediction
            )

            st.write(
                "Probability:",
                probability
            )


    except Exception as e:

        st.error(
            "❌ Prediction failed."
        )

        st.exception(e)

        st.warning(
            """
            Check that the input columns in this app
            exactly match the columns used to train
            the Pipeline.
            """
        )


st.markdown(
    """
    <br><br>

    <div style="
        text-align:center;
        color:#9ca3af;
        padding:25px;
        font-size:13px;
    ">

        <b>Blight Compliance AI</b><br>

        Machine Learning • AI for Business

    </div>
    """,
    unsafe_allow_html=True
)


