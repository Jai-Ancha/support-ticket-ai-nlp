import streamlit as st
import requests

# ---------------------------
# EC2 API Endpoint
# ---------------------------
API_URL = "http://13.232.43.36:8000/predict"


# ---------------------------
# Streamlit UI Config
# ---------------------------
st.set_page_config(page_title="Support Ticket AI", layout="centered")

st.title("🎫 Support Ticket AI Routing System (Cloud Version)")
st.write("Enter a support issue description to classify category and priority using AWS deployment.")

user_input = st.text_area(
    "Describe your issue (please provide detailed explanation for better accuracy):",
    height=150
)


if st.button("Analyze Ticket"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            response = requests.post(
                API_URL,
                params={"ticket": user_input}
            )

            if response.status_code == 200:
                result = response.json()

                predicted_tag = result["predicted_tag"]
                predicted_priority = result["predicted_priority"]

                st.success("Prediction Complete ✅")

                # ===== Issue Category =====
                st.subheader("📌 Predicted Issue Category")
                st.write(f"**{predicted_tag}**")

                # ===== Priority =====
                st.subheader("⚡ Priority Assessment")
                st.write(f"**{predicted_priority.upper()}**")

            else:
                st.error("Error from API. Please try again.")

        except Exception as e:
            st.error("Unable to connect to cloud API.")
            st.exception(e)
