import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("🔍 Spam Prediction")

st.write(
    "Enter your Email or SMS message below and check whether it is Spam or Ham."
)

message = st.text_area(
    "Message",
    height=200,
    placeholder="Type or paste your email/SMS here..."
)

if st.button("Predict", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message.")
    else:

        try:
            response = requests.post(
                API_URL,
                json={"text": message}
            )

            if response.status_code == 200:

                result = response.json()

                prediction = result["prediction"]
                confidence = round(
                    result["confidence"] * 100,
                    2
                )

                @st.dialog("Prediction Result")
                def show_result():

                    if prediction.lower() == "spam":
                        st.error(
                            f"🚨 SPAM DETECTED\n\nConfidence: {confidence}%"
                        )
                    else:
                        st.success(
                            f"✅ HAM (Safe Message)\n\nConfidence: {confidence}%"
                        )

                show_result()

            else:
                st.error("Prediction failed.")

        except Exception as e:
            st.error(f"Backend connection error: {e}")