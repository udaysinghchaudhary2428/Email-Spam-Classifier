import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:

    st.markdown("<br>", unsafe_allow_html=True)

    # Center the image
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/2092/2092663.png",
            width=150
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="text-align:center;">
            🛡️ Spam Shield
        </h2>

        <p style="
            text-align:center;
            font-size:18px;
            color:#D1D5DB;
        ">
            Detect spam emails and SMS messages instantly.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

# ---------------- CSS ---------------- #
with open("Static/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- MAIN CONTENT ---------------- #

st.markdown(
    """
    <h1 class="main-title">
        📧 Email Spam Classifier
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="sub-title">
        Protect your inbox from unwanted spam messages
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns([2, 1])

# ---------------- LEFT SECTION ---------------- #

with col1:

    st.markdown("""
    ## Why do we need Spam Detection?

    Every day millions of emails and SMS messages are exchanged across the world.

    Many of these messages contain:

    - 🚨 Fraudulent Offers
    - 🎣 Phishing Attempts
    - 🎁 Fake Lottery Messages
    - 🦠 Malware Links
    - 📢 Promotional Spam

    Spam detection systems use Machine Learning techniques to automatically classify incoming messages as **Spam** or **Ham (Legitimate Message)**.

    ## Benefits

    ✅ Protects users from scams

    ✅ Saves time by filtering unwanted messages

    ✅ Improves email security

    ✅ Reduces phishing attacks

    ✅ Enhances user experience
    """)

# ---------------- RIGHT SECTION ---------------- #

with col2:

    st.info(
        """
        ### 📌 Project Features

        - ML-based Spam Detection
        - Email & SMS Support
        - Confidence Score
        - Fast Predictions
        - User Friendly Interface
        """
    )

st.success("👉 Open the Prediction page from the sidebar.")