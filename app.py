import streamlit as st
import random
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Vehicle AI Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ---------------- SESSION STATE INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "engine_temp" not in st.session_state:
    st.session_state.engine_temp = random.randint(70, 120)

if "battery_level" not in st.session_state:
    st.session_state.battery_level = random.randint(10, 100)

if "sensor_status" not in st.session_state:
    st.session_state.sensor_status = random.choice(["Working", "Failed"])

if "gps_status" not in st.session_state:
    st.session_state.gps_status = random.choice(["Active", "Lost"])


# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🔐 Secure Login - Vehicle Monitoring System")
    st.markdown("Enter credentials to access dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Username or Password")


# ---------------- DASHBOARD ----------------
def dashboard():

    st.title("🚗 AI-Based Self-Healing Autonomous Vehicle Monitoring System")

    col_logout, col_refresh = st.columns(2)

    with col_logout:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.rerun()

    with col_refresh:
        if st.button("🔄 Refresh Vehicle Data"):
            st.session_state.engine_temp = random.randint(70, 120)
            st.session_state.battery_level = random.randint(10, 100)
            st.session_state.sensor_status = random.choice(["Working", "Failed"])
            st.session_state.gps_status = random.choice(["Active", "Lost"])
            st.rerun()

    st.markdown("---")

    engine_temp = st.session_state.engine_temp
    battery_level = st.session_state.battery_level
    sensor_status = st.session_state.sensor_status
    gps_status = st.session_state.gps_status

    col1, col2 = st.columns(2)

    # Engine
    with col1:
        st.subheader("🔥 Engine Temperature")
        st.metric("Temperature (°C)", engine_temp)

        if engine_temp > 105:
            st.error("⚠ Critical Overheating Detected!")
            st.info("🔧 Auto Cooling System Activated")
        elif engine_temp > 95:
            st.warning("⚠ Temperature Rising - Predictive Risk")
        else:
            st.success("Engine Operating Normally")

    # Battery
    with col2:
        st.subheader("🔋 Battery Level")
        st.metric("Battery (%)", battery_level)

        if battery_level < 15:
            st.error("⚠ Critical Battery Level!")
            st.info("⚡ Emergency Power Mode Activated")
        elif battery_level < 30:
            st.warning("⚠ Battery Low")
            st.info("🔋 Energy Saving Mode Enabled")
        else:
            st.success("Battery Stable")

    st.markdown("---")

    # Sensor
    st.subheader("📡 Sensor Health Status")

    if sensor_status == "Failed":
        st.error("⚠ Sensor Failure Detected!")
        st.success("🔁 Backup Sensor Activated Successfully")
    else:
        st.success("All Sensors Working Properly")

    st.markdown("---")

    # GPS
    st.subheader("🛰 GPS Signal Status")

    if gps_status == "Lost":
        st.error("⚠ GPS Signal Lost!")
        st.success("📍 Switched to IMU-Based Navigation Mode")
    else:
        st.success("GPS Signal Active")

    st.markdown("---")

    # Graph
    st.subheader("📈 Engine Temperature Trend")

    temp_data = pd.DataFrame({
        "Time": range(10),
        "Temperature": [random.randint(70, 120) for _ in range(10)]
    })

    st.line_chart(temp_data.set_index("Time"))

    st.markdown("---")
    st.info("System running in Simulation Mode (IoT + AI Predictive + Self-Healing Enabled)")

    # ---------------- AI RISK SCORE ----------------
    st.markdown("---")
    st.subheader("🤖 AI Failure Risk Prediction")

    risk_score = 0

    if engine_temp > 100:
        risk_score += 30
    elif engine_temp > 90:
        risk_score += 15

    if battery_level < 15:
        risk_score += 30
    elif battery_level < 30:
        risk_score += 15

    if sensor_status == "Failed":
        risk_score += 25

    risk_score = min(risk_score, 100)

    st.metric("Failure Risk Score (%)", f"{risk_score}%")

    if risk_score < 30:
        st.success("🟢 Low Risk - Vehicle operating normally")
    elif risk_score < 60:
        st.warning("🟡 Medium Risk - Monitor closely")
    else:
        st.error("🔴 High Risk - Immediate maintenance required")


# ---------------- MAIN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()