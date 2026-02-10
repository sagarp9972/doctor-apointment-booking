# 🏥 MedBook - Smart Doctor Appointment Booking System

A beautiful and interactive doctor appointment booking application built with Streamlit and powered by Google's Gemini AI for intelligent recommendations and emergency assistance.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 🤖 AI-Powered Intelligence
- **Smart Doctor Recommendations**: Get personalized doctor suggestions based on symptoms, age, and gender using Gemini AI
- **Emergency AI Assistant**: Real-time emergency guidance and first-aid advice
- **Intelligent Symptom Analysis**: AI analyzes your symptoms to recommend the right specialist

### 📅 Appointment Management
- **Easy Booking**: Book appointments with your preferred doctors in just a few clicks
- **Real-time Slot Availability**: View and select available time slots
- **Appointment Tracking**: View all your booked appointments in one place
- **Cancel & Reschedule**: Manage your appointments with ease
- **Confirmation System**: Instant booking confirmations via SMS and Email (simulated)

### 🗺️ Hospital Navigation
- **Interactive Floor Plans**: Visual representation of hospital departments using Plotly
- **Department Locator**: Find any department with room numbers and contact details
- **Parking Information**: Complete parking and facility information
- **Operating Hours**: Department-wise timing information

### 🚨 24/7 Emergency Services
- **Emergency Button**: Quick access to emergency services
- **Ambulance Dispatch**: One-click ambulance calling (simulated)
- **Emergency Hotlines**: All important emergency contact numbers
- **AI Emergency Guidance**: Immediate first-aid advice for emergency situations
- **Hospital Location**: GPS coordinates and address information

### 🎨 Modern UI/UX
- **Beautiful Design**: Gradient backgrounds and modern styling
- **Responsive Layout**: Works on all screen sizes
- **Interactive Cards**: Hover effects and smooth animations
- **Professional Theme**: Medical-themed color scheme
- **Easy Navigation**: Intuitive menu system with icons

## 🚀 Demo

The application includes 5 main sections:

1. **🏠 Home**: Dashboard with statistics and featured services
2. **📅 Book Appointment**: AI-powered doctor booking system
3. **📋 My Appointments**: View and manage your bookings
4. **🗺️ Hospital Navigation**: Interactive hospital maps and directions
5. **🚨 Emergency**: 24/7 emergency services and AI assistance

## 📥 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/medbook-appointment-system.git
cd medbook-appointment-system
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install packages manually:

```bash
pip install streamlit pandas google-generativeai plotly streamlit-option-menu
```

### Step 4: Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key (you'll need this to run the app)

## 🎯 Usage

### Running the Application

```bash
streamlit run doctor_appointment_app.py
```

Or use:

```bash
python -m streamlit run doctor_appointment_app.py
```

The application will open automatically in your default browser at `http://localhost:8501`

### First-Time Setup

1. Enter your Gemini API Key in the sidebar
2. The API key will be stored in the session (you'll need to re-enter it when you restart the app)
3. Start booking appointments!

## ⚙️ Configuration

### API Key Configuration

Enter your Gemini API key in the sidebar of the application. The key is used for:
- AI doctor recommendations
- Emergency situation analysis
- Symptom evaluation

### Customizing Doctors

Edit the `doctors_data` in the code to add/modify doctors:

```python
st.session_state.doctors_data = [
    {
        "name": "Dr. Sarah Johnson",
        "specialty": "Cardiology",
        "rating": 4.9,
        "experience": "15 years",
        "fee": 150,
        "available_slots": ["09:00", "10:30", "14:00", "15:30"]
    },
    # Add more doctors...
]
```

## 📁 Project Structure

```
medbook-appointment-system/
│
├── doctor_appointment_app.py    # Main application file
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
│
└── assets/                      # (Optional) Images and resources
    └── screenshots/             # Application screenshots
```

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **Google Gemini AI** | AI-powered recommendations |
| **Plotly** | Interactive visualizations and maps |
| **Pandas** | Data manipulation |
| **streamlit-option-menu** | Navigation menu |
| **Python 3.7+** | Core programming language |

## 🎨 Features in Detail

### Available Specialties
- ❤️ Cardiology
- 🧠 Neurology
- 👨 Dermatology
- 🦴 Orthopedics
- 👶 Pediatrics
- 🤰 Gynecology

### Doctor Information Includes
- Name and specialty
- Years of experience
- Patient ratings (out of 5 stars)
- Consultation fees
- Available time slots
- Contact information

### Appointment Details
- Patient information (name, phone, email)
- Doctor and specialty
- Date and time
- Consultation fee
- Booking status
- Booking timestamp

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

## 📝 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Email/SMS notification system
- [ ] Payment gateway integration
- [ ] Doctor availability calendar
- [ ] Patient medical history
- [ ] Prescription management
- [ ] Video consultation feature
- [ ] Multi-language support
- [ ] Admin dashboard
- [ ] Analytics and reporting

## 🐛 Known Issues

- Appointments are stored in session state (lost on browser refresh)
- SMS/Email confirmations are simulated
- No authentication system currently

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Google Gemini AI for intelligent recommendations
- Streamlit team for the amazing framework
- Plotly for interactive visualizations
- The open-source community

## 📞 Support

For support, email your.email@example.com or open an issue in the GitHub repository.

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repo if you find it helpful!

</div>
