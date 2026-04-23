import streamlit as st
from datetime import datetime
import pandas as pd

# --- CONFIGURATION ---
TARGET_DATETIME = "2026-05-01T00:00:00"
TITLE = "Milte hain bahut jaldi!🫶"
VALID_USER = "Nanugolu"
VALID_PASS = "2201200403092004"

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        return True

    st.title("🔒 Private Access")
    # Using unique keys to prevent Streamlit widget errors
    user_input = st.text_input("User ID", key="user_login_final")
    pass_input = st.text_input("Password", type="password", key="pass_login_final")
    
    if st.button("Login"):
        if user_input == VALID_USER and pass_input == VALID_PASS:
            st.session_state["authenticated"] = True
            st.rerun() 
        else:
            st.error("Invalid User ID or Password")
    return False

def show_timer():
    st.set_page_config(page_title="Countdown", layout="centered")
    
    # CSS to make it look beautiful on Android
    st.markdown("""
        <style>
        .timer-card {
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            padding: 30px;
            border-radius: 20px;
            color: #4a4a4a;
            text-align: center;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .title { font-size: 24px; font-weight: bold; margin-bottom: 15px; }
        #live-timer {
            font-size: 38px;
            font-weight: 800;
            color: #ff5e62;
            font-family: 'monospace';
            background: rgba(255,255,255,0.3);
            padding: 10px;
            border-radius: 10px;
        }
        .footer-label { font-size: 16px; margin-top: 15px; opacity: 0.8; }
        </style>
    """, unsafe_allow_html=True)

    # The HTML and the Live Script
    st.markdown(f"""
        <div class="timer-card">
            <div class="title">{TITLE}</div>
            <div id="live-timer">00:00:00:00</div>
            <div class="footer-label">until May 01, 2026</div>
        </div>

        <script>
        function startCountdown() {{
            const target = new Date("{TARGET_DATETIME}").getTime();
            
            const timerInterval = setInterval(function() {{
                // Get current time in IST
                const nowUTC = new Date().getTime();
                const offset = 5.5 * 60 * 60 * 1000; // IST is UTC+5.5
                const nowIST = nowUTC + (new Date().getTimezoneOffset() * 60000) + offset;
                
                const diff = target - nowIST;

                if (diff <= 0) {{
                    document.getElementById("live-timer").innerHTML = "00:00:00:00";
                    clearInterval(timerInterval);
                    return;
                }}

                const d = Math.floor(diff / (1000 * 60 * 60 * 24));
                const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                const s = Math.floor((diff % (1000 * 60)) / 1000);

                // Add leading zeros for a cleaner look
                const display = 
                    (d < 10 ? "0"+d : d) + "d " + 
                    (h < 10 ? "0"+h : h) + "h " + 
                    (m < 10 ? "0"+m : m) + "m " + 
                    (s < 10 ? "0"+s : s) + "s";
                
                document.getElementById("live-timer").innerHTML = display;
            }}, 1000);
        }}
        startCountdown();
        </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    if check_password():
        show_timer()
