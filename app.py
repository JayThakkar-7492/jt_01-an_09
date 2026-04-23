import streamlit as st
from datetime import datetime
import pandas as pd
import time

# --- CONFIGURATION ---
# Setting the target to May 1st, 2026
TARGET_DATE = pd.Timestamp("2026-05-01 00:00:00").tz_localize('Asia/Kolkata')
TITLE = "Milte hain bahut jaldi!🫶"
VALID_USER = "Nanugolu"
VALID_PASS = "2201200403092004"

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if st.session_state["authenticated"]:
        return True

    st.title("🔒 Private Access")
    user_input = st.text_input("User ID", key="user_login")
    pass_input = st.text_input("Password", type="password", key="pass_login")
    
    if st.button("Login"):
        if user_input == VALID_USER and pass_input == VALID_PASS:
            st.session_state["authenticated"] = True
            st.rerun() 
        else:
            st.error("Invalid User ID or Password")
    return False

def show_timer():
    st.set_page_config(page_title="Countdown", layout="centered")
    
    # CSS for the UI
    st.markdown("""
        <style>
        .timer-card {
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            padding: 40px;
            border-radius: 25px;
            color: #4a4a4a;
            text-align: center;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
        }
        .title { font-size: 28px; font-weight: bold; margin-bottom: 20px; }
        .time-display { font-size: 40px; font-weight: 800; color: #ff5e62; font-family: monospace; }
        </style>
    """, unsafe_allow_html=True)

    # This container will be updated every second
    placeholder = st.empty()

    while True:
        # Get current time in India
        now = pd.Timestamp.now(tz='Asia/Kolkata')
        diff = TARGET_DATE - now

        if diff.total_seconds() <= 0:
            placeholder.markdown(f"""
                <div class="timer-card">
                    <div class="title">{TITLE}</div>
                    <div class="time-display">The Wait is Over! ❤️</div>
                </div>
            """, unsafe_allow_html=True)
            break
        
        # Math to get Days, Hours, Minutes, Seconds
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Update the display
        placeholder.markdown(f"""
            <div class="timer-card">
                <div class="title">{TITLE}</div>
                <div class="time-display">
                    {days}d {hours:02d}h {minutes:02d}m {seconds:02d}s
                </div>
                <div style="margin-top:10px; opacity:0.7;">until May 01, 2026</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Wait 1 second before the next update
        time.sleep(1)

if __name__ == "__main__":
    if check_password():
        show_timer()
