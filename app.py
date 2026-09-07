import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Time Table", layout="centered")

# Custom Dark Mode styling
st.markdown("""
<style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    .header-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .badge {
        background-color: #2a2a3c;
        color: #a5b4fc;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
    }
    .card {
        background-color: #1e1e24;
        border: 1px solid #2a2a32;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .time {
        font-size: 13px;
        font-weight: 600;
        color: #d4d4d8;
        margin-bottom: 6px;
    }
    .title {
        font-size: 16px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .meta {
        font-size: 13px;
        color: #a1a1aa;
    }
</style>
""", unsafe_allow_html=True)

# Timetable Data
schedule = {
    "MON": [
        {"time": "02:55 PM - 03:45 PM", "name": "Applied Chemistry - ETH", "venue": "F2+TF2 - AB4-320"},
        {"time": "03:50 PM - 04:40 PM", "name": "Micro Economics - TH", "venue": "D2+TD2 - AB4-320"},
        {"time": "04:45 PM - 05:35 PM", "name": "Technical English Communication - ETH", "venue": "B2+TB2 - AB4-320"}
    ],
    "TUE": [
        {"time": "09:50 AM - 11:30 AM", "name": "Problem Solving Using Python - LO", "venue": "L9+L10+L25+L26 - AB1-206"},
        {"time": "02:00 PM - 02:50 PM", "name": "Technical English Communication - ETH", "venue": "B2+TB2 - AB4-320"},
        {"time": "03:50 PM - 04:40 PM", "name": "Multivariable Calculus and Differential Equations - ETH", "venue": "E2+TE2 - AB4-320"}
    ],
    "WED": [
        {"time": "08:00 AM - 09:40 AM", "name": "Multivariable Calculus and Differential Equations - ELA", "venue": "L13+L14 - AB1-505A"},
        {"time": "03:50 PM - 04:40 PM", "name": "Applied Chemistry - ETH", "venue": "F2+TF2 - AB4-320"},
        {"time": "04:45 PM - 05:35 PM", "name": "Micro Economics - TH", "venue": "D2+TD2 - AB4-320"}
    ],
    "THU": [
        {"time": "09:50 AM - 11:30 AM", "name": "Technical English Communication - ELA", "venue": "L21+L22 - AB1-404 A"},
        {"time": "02:00 PM - 02:50 PM", "name": "Micro Economics - TH", "venue": "D2+TD2 - AB4-320"},
        {"time": "02:55 PM - 03:45 PM", "name": "Technical English Communication - ETH", "venue": "B2+TB2 - AB4-320"},
        {"time": "04:45 PM - 05:35 PM", "name": "Multivariable Calculus and Differential Equations - ETH", "venue": "E2+TE2 - AB4-320"}
    ],
    "FRI": [
        {"time": "08:00 AM - 09:40 AM", "name": "Problem Solving Using Python - LO", "venue": "L9+L10+L25+L26 - AB1-206"},
        {"time": "11:40 AM - 01:20 PM", "name": "Applied Chemistry - ELA", "venue": "L29+L30 - AB1-303"},
        {"time": "02:00 PM - 02:50 PM", "name": "Multivariable Calculus and Differential Equations - ETH", "venue": "E2+TE2 - AB4-320"},
        {"time": "04:45 PM - 05:35 PM", "name": "Applied Chemistry - ETH", "venue": "F2+TF2 - AB4-320"}
    ]
}

# Header Section
st.markdown("""
<div class="header-box">
    <h2 style="margin: 0;">Time Table</h2>
    <span class="badge">26BAI1279</span>
</div>
""", unsafe_allow_html=True)

# Select Current Day by Default
days = ["MON", "TUE", "WED", "THU", "FRI"]
today_index = datetime.today().weekday()
default_index = today_index if today_index < 5 else 0

selected_day = st.radio(
    label="Select Day",
    options=days,
    index=default_index,
    horizontal=True,
    label_visibility="collapsed"
)

# Display Classes
for item in schedule[selected_day]:
    st.markdown(f"""
    <div class="card">
        <div class="time">{item['time']}</div>
        <div class="title">{item['name']}</div>
        <div class="meta">{item['venue']}</div>
    </div>
    """, unsafe_allow_html=True)
