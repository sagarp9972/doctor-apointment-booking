import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import time

# Configure page
st.set_page_config(
    page_title="MedBook - Doctor Appointment System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .doctor-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .doctor-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .emergency-btn {
        background: linear-gradient(45deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .success-message {
        background: linear-gradient(90deg, #56ab2f, #a8e6cf);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'appointments' not in st.session_state:
    st.session_state.appointments = []
if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = ""
if 'doctors_data' not in st.session_state:
    st.session_state.doctors_data = [
        {"name": "Dr. Sarah Johnson", "specialty": "Cardiology", "rating": 4.9, "experience": "15 years", "fee": 150, "available_slots": ["09:00", "10:30", "14:00", "15:30"]},
        {"name": "Dr. Michael Chen", "specialty": "Neurology", "rating": 4.8, "experience": "12 years", "fee": 180, "available_slots": ["08:30", "11:00", "13:30", "16:00"]},
        {"name": "Dr. Emily Davis", "specialty": "Dermatology", "rating": 4.7, "experience": "10 years", "fee": 120, "available_slots": ["09:30", "11:30", "14:30", "16:30"]},
        {"name": "Dr. James Wilson", "specialty": "Orthopedics", "rating": 4.9, "experience": "18 years", "fee": 160, "available_slots": ["08:00", "10:00", "13:00", "15:00"]},
        {"name": "Dr. Lisa Rodriguez", "specialty": "Pediatrics", "rating": 4.8, "experience": "14 years", "fee": 140, "available_slots": ["09:00", "11:00", "14:00", "16:00"]},
        {"name": "Dr. David Kim", "specialty": "Gynecology", "rating": 4.6, "experience": "16 years", "fee": 170, "available_slots": ["08:30", "10:30", "13:30", "15:30"]}
    ]

# Gemini AI Configuration
def configure_gemini():
    if st.session_state.gemini_api_key:
        try:
            genai.configure(api_key=st.session_state.gemini_api_key)
            return True
        except:
            return False
    return False

# AI-powered doctor recommendation
def get_ai_recommendation(symptoms, age, gender):
    if not configure_gemini():
        return "Please configure your Gemini API key to get AI recommendations."
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        Based on the following patient information:
        - Symptoms: {symptoms}
        - Age: {age}
        - Gender: {gender}
        
        Recommend the most appropriate medical specialist from these options:
        - Cardiology
        - Neurology  
        - Dermatology
        - Orthopedics
        - Pediatrics
        - Gynecology
        
        Provide a brief explanation (2-3 sentences) for your recommendation.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error getting AI recommendation: {str(e)}"

# Emergency assistance
def get_emergency_guidance(symptoms):
    if not configure_gemini():
        return "Please configure your Gemini API key for emergency assistance."
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        EMERGENCY MEDICAL GUIDANCE:
        Patient reports: {symptoms}
        
        Provide immediate first aid advice and determine urgency level (High/Medium/Low).
        Include when to call emergency services.
        Keep response concise but comprehensive.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error getting emergency guidance: {str(e)}"

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏥 MedBook - Smart Hospital System</h1>
    <p>Your Health, Our Priority - Book appointments with ease</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for API key
with st.sidebar:
    st.header("🔑 Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password", value=st.session_state.gemini_api_key)
    if api_key != st.session_state.gemini_api_key:
        st.session_state.gemini_api_key = api_key
    
    if st.session_state.gemini_api_key:
        st.success("✅ API Key Configured")
    else:
        st.warning("⚠️ Please enter your Gemini API key for AI features")

# Navigation menu
selected = option_menu(
    menu_title=None,
    options=["🏠 Home", "📅 Book Appointment", "📋 My Appointments", "🗺️ Hospital Navigation", "🚨 Emergency"],
    icons=["house", "calendar-plus", "list-task", "map", "exclamation-triangle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#667eea", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#667eea"},
    },
)

# Home Page
if selected == "🏠 Home":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">👨‍⚕️ Doctors</h3>
            <h2>50+</h2>
            <p>Specialist Doctors</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">🏥 Departments</h3>
            <h2>15</h2>
            <p>Medical Departments</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">⭐ Rating</h3>
            <h2>4.8</h2>
            <p>Patient Satisfaction</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">📅 Appointments</h3>
            <h2>{}</h2>
            <p>Booked Today</p>
        </div>
        """.format(len(st.session_state.appointments)), unsafe_allow_html=True)
    
    st.markdown("### 🔥 Featured Services")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🤖 **AI Doctor Recommendations** - Get personalized doctor suggestions based on your symptoms")
    
    with col2:
        st.success("⚡ **Quick Booking** - Book appointments in just a few clicks")
    
    with col3:
        st.warning("🚨 **24/7 Emergency** - Round-the-clock emergency assistance")

# Book Appointment Page
elif selected == "📅 Book Appointment":
    st.header("📅 Book Your Appointment")
    
    # AI Recommendation Section
    with st.expander("🤖 Get AI Doctor Recommendation", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            symptoms = st.text_area("Describe your symptoms:", placeholder="e.g., chest pain, headache, skin rash...")
            age = st.number_input("Age:", min_value=1, max_value=120, value=30)
        with col2:
            gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
            
        if st.button("Get AI Recommendation 🔍"):
            if symptoms and st.session_state.gemini_api_key:
                with st.spinner("Analyzing symptoms..."):
                    recommendation = get_ai_recommendation(symptoms, age, gender)
                st.success("**AI Recommendation:**")
                st.write(recommendation)
    
    # Booking Form
    col1, col2 = st.columns(2)
    
    with col1:
        patient_name = st.text_input("👤 Patient Name:", placeholder="Enter your full name")
        phone = st.text_input("📱 Phone Number:", placeholder="+91 9876543210")
        email = st.text_input("📧 Email:", placeholder="patient@email.com")
        
    with col2:
        appointment_date = st.date_input("📅 Appointment Date:", 
                                       min_value=datetime.now().date(),
                                       max_value=datetime.now().date() + timedelta(days=30))
        specialty = st.selectbox("🏥 Select Department:", 
                               ["Cardiology", "Neurology", "Dermatology", "Orthopedics", "Pediatrics", "Gynecology"])
        
    # Doctor selection based on specialty
    available_doctors = [doc for doc in st.session_state.doctors_data if doc["specialty"] == specialty]
    
    if available_doctors:
        st.markdown("### 👨‍⚕️ Available Doctors")
        
        for idx, doctor in enumerate(available_doctors):
            with st.container():
                st.markdown(f"""
                <div class="doctor-card">
                    <h4>{doctor['name']}</h4>
                    <p><strong>Specialty:</strong> {doctor['specialty']} | <strong>Experience:</strong> {doctor['experience']}</p>
                    <p><strong>Rating:</strong> {'⭐' * int(doctor['rating'])} {doctor['rating']} | <strong>Fee:</strong> ₹{doctor['fee']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    selected_doctor = st.checkbox(f"Select {doctor['name']}", key=f"doc_{idx}")
                with col2:
                    if selected_doctor:
                        time_slot = st.selectbox(f"Available Time Slots:", 
                                               doctor['available_slots'], 
                                               key=f"slot_{idx}")
                
                if selected_doctor and st.button(f"Book with {doctor['name']}", key=f"book_{idx}"):
                    if patient_name and phone and email:
                        appointment = {
                            "id": len(st.session_state.appointments) + 1,
                            "patient_name": patient_name,
                            "phone": phone,
                            "email": email,
                            "doctor": doctor['name'],
                            "specialty": doctor['specialty'],
                            "date": appointment_date.strftime("%Y-%m-%d"),
                            "time": time_slot,
                            "fee": doctor['fee'],
                            "status": "Confirmed",
                            "booking_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        st.session_state.appointments.append(appointment)
                        
                        st.markdown("""
                        <div class="success-message">
                            ✅ Appointment Booked Successfully!<br>
                            You will receive a confirmation SMS and Email shortly.
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Show booking details
                        st.info(f"""
                        **Booking Details:**
                        - Patient: {patient_name}
                        - Doctor: {doctor['name']}
                        - Date: {appointment_date}
                        - Time: {time_slot}
                        - Fee: ₹{doctor['fee']}
                        """)
                    else:
                        st.error("Please fill in all patient details!")

# My Appointments Page
elif selected == "📋 My Appointments":
    st.header("📋 My Appointments")
    
    if st.session_state.appointments:
        # Statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Appointments", len(st.session_state.appointments))
        with col2:
            confirmed = len([apt for apt in st.session_state.appointments if apt['status'] == 'Confirmed'])
            st.metric("Confirmed", confirmed)
        with col3:
            total_fee = sum([apt['fee'] for apt in st.session_state.appointments])
            st.metric("Total Fee", f"₹{total_fee}")
        
        # Appointments list
        st.markdown("### 📅 Upcoming Appointments")
        
        for apt in st.session_state.appointments:
            with st.container():
                col1, col2, col3 = st.columns([3, 2, 1])
                
                with col1:
                    st.markdown(f"""
                    **🏥 {apt['doctor']}** - {apt['specialty']}  
                    📅 {apt['date']} at {apt['time']}  
                    👤 Patient: {apt['patient_name']}
                    """)
                
                with col2:
                    st.markdown(f"""
                    💰 Fee: ₹{apt['fee']}  
                    📱 {apt['phone']}  
                    ✅ Status: {apt['status']}
                    """)
                
                with col3:
                    if st.button("Cancel", key=f"cancel_{apt['id']}"):
                        st.session_state.appointments = [a for a in st.session_state.appointments if a['id'] != apt['id']]
                        st.experimental_rerun()
                
                st.divider()
    else:
        st.info("No appointments booked yet. Book your first appointment!")
        if st.button("Book Appointment Now"):
            st.session_state.selected = "📅 Book Appointment"

# Hospital Navigation Page
elif selected == "🗺️ Hospital Navigation":
    st.header("🗺️ Hospital Navigation")
    
    # Hospital floor plan
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏥 Interactive Floor Plan")
        
        # Create a simple floor plan using plotly
        fig = go.Figure()
        
        # Add rooms
        rooms = [
            {"name": "Reception", "x": [0, 2], "y": [0, 1], "color": "lightblue"},
            {"name": "Emergency", "x": [2, 4], "y": [0, 1], "color": "red"},
            {"name": "Cardiology", "x": [0, 2], "y": [1, 2], "color": "lightgreen"},
            {"name": "Neurology", "x": [2, 4], "y": [1, 2], "color": "lightyellow"},
            {"name": "Pharmacy", "x": [0, 1], "y": [2, 3], "color": "lightcoral"},
            {"name": "Lab", "x": [1, 3], "y": [2, 3], "color": "lightgray"},
            {"name": "Cafeteria", "x": [3, 4], "y": [2, 3], "color": "lightpink"}
        ]
        
        for room in rooms:
            fig.add_shape(
                type="rect",
                x0=room["x"][0], y0=room["y"][0],
                x1=room["x"][1], y1=room["y"][1],
                fillcolor=room["color"],
                line=dict(color="black", width=2)
            )
            
            # Add room labels
            fig.add_annotation(
                x=(room["x"][0] + room["x"][1]) / 2,
                y=(room["y"][0] + room["y"][1]) / 2,
                text=room["name"],
                showarrow=False,
                font=dict(size=12, color="black")
            )
        
        fig.update_layout(
            title="Ground Floor - Main Building",
            xaxis=dict(range=[-0.5, 4.5], showgrid=True),
            yaxis=dict(range=[-0.5, 3.5], showgrid=True),
            width=600,
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Quick Navigation")
        
        department = st.selectbox("Select Department:", 
                                ["Reception", "Emergency", "Cardiology", "Neurology", 
                                 "Dermatology", "Orthopedics", "Pediatrics", "Pharmacy", "Lab"])
        
        # Department information
        dept_info = {
            "Reception": {"floor": "Ground Floor", "room": "101", "phone": "+91-11-2345-6789"},
            "Emergency": {"floor": "Ground Floor", "room": "102-105", "phone": "+91-11-2345-9999"},
            "Cardiology": {"floor": "First Floor", "room": "201-205", "phone": "+91-11-2345-6701"},
            "Neurology": {"floor": "First Floor", "room": "206-210", "phone": "+91-11-2345-6702"},
            "Dermatology": {"floor": "Second Floor", "room": "301-303", "phone": "+91-11-2345-6703"},
            "Orthopedics": {"floor": "Second Floor", "room": "304-308", "phone": "+91-11-2345-6704"},
            "Pediatrics": {"floor": "Third Floor", "room": "401-405", "phone": "+91-11-2345-6705"},
            "Pharmacy": {"floor": "Ground Floor", "room": "110", "phone": "+91-11-2345-6706"},
            "Lab": {"floor": "Ground Floor", "room": "111-113", "phone": "+91-11-2345-6707"}
        }
        
        if department in dept_info:
            info = dept_info[department]
            st.info(f"""
            **📍 {department}**  
            🏢 Floor: {info['floor']}  
            🚪 Room: {info['room']}  
            📞 Phone: {info['phone']}
            """)
        
        st.markdown("### 🚗 Parking Information")
        st.success("🅿️ **Free Parking Available**")
        st.write("- Ground Level: 2-wheeler parking")
        st.write("- Basement 1: Car parking")
        st.write("- Basement 2: Ambulance bay")
        
        st.markdown("### 🕐 Hospital Hours")
        st.write("- **OPD:** 8:00 AM - 8:00 PM")
        st.write("- **Emergency:** 24/7")
        st.write("- **Pharmacy:** 24/7")
        st.write("- **Lab:** 6:00 AM - 10:00 PM")

# Emergency Page
elif selected == "🚨 Emergency":
    st.markdown("""
    <div style="background: linear-gradient(45deg, #ff6b6b, #ee5a52); padding: 2rem; border-radius: 15px; text-align: center; color: white; margin-bottom: 2rem;">
        <h1>🚨 EMERGENCY SERVICES</h1>
        <h3>24/7 Emergency Care Available</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🆘 Emergency Contacts")
        
        if st.button("🚨 CALL AMBULANCE NOW", type="primary", use_container_width=True):
            st.success("🚑 Ambulance dispatched! ETA: 8-12 minutes")
            st.info("**Emergency Team Notified**\nStay calm and wait for medical assistance.")
        
        st.markdown("""
        **📞 Emergency Hotlines:**
        - 🚑 Ambulance: **102**
        - 🏥 Hospital Emergency: **+91-11-2345-9999**
        - 🚨 General Emergency: **112**
        - 🚓 Police: **100**
        - 🚒 Fire: **101**
        """)
        
        st.markdown("### 📍 Hospital Location")
        st.success("""
        **MedBook Hospital**  
        123 Health Street, Medical District  
        New Delhi - 110001  
        
        **GPS Coordinates:**  
        Lat: 28.6139, Long: 77.2090
        """)
    
    with col2:
        st.markdown("### 🤖 AI Emergency Assistant")
        
        emergency_symptoms = st.text_area(
            "Describe the emergency situation:",
            placeholder="e.g., severe chest pain, difficulty breathing, unconscious person..."
        )
        
        if st.button("Get Emergency Guidance 🔍"):
            if emergency_symptoms and st.session_state.gemini_api_key:
                with st.spinner("Analyzing emergency situation..."):
                    guidance = get_emergency_guidance(emergency_symptoms)
                
                st.markdown("### 🚨 Emergency Guidance")
                st.warning(guidance)
                
                st.error("""
                **⚠️ IMPORTANT REMINDERS:**
                - If life-threatening, call ambulance immediately
                - Don't leave the patient alone
                - Keep airways clear
                - Apply pressure to bleeding wounds
                - Stay calm and follow medical guidance
                """)
            else:
                st.warning("Please describe the symptoms and ensure API key is configured.")
        
        st.markdown("### 🏥 Emergency Departments")
        st.info("""
        **Available 24/7:**
        - ❤️ Cardiac Emergency
        - 🧠 Stroke Unit  
        - 🦴 Trauma Center
        - 👶 Pediatric Emergency
        - 🤰 Maternity Emergency
        - 🧪 Poison Control
        """)

# Footer
st.markdown("""
---
<div style="text-align: center; color: #666; padding: 2rem;">
    <h4>🏥 MedBook Hospital System</h4>
    <p>Your Health, Our Priority | Available 24/7</p>
    <p>📞 Emergency: +91-11-2345-9999 | 📧 info@medbook.hospital</p>
</div>
""", unsafe_allow_html=True)