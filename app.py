import streamlit as st
from datetime import datetime, time, timezone, timedelta

# Page config
st.set_page_config(page_title="VIT Schedule", page_icon="⚡", layout="centered")

# --- MODERN GLASSMORPHISM STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(30, 27, 75, 0.9) 0%, rgba(10, 10, 15, 1) 90%);
        color: #f8fafc;
    }

    header, footer { visibility: hidden !important; }
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 520px !important;
    }

    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 12px 18px;
        margin-bottom: 20px;
    }
    .reg-pill {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: 700;
        font-size: 11px;
        padding: 4px 12px;
        border-radius: 20px;
        letter-spacing: 0.8px;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);
    }

    .class-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        transition: all 0.25s ease;
    }
    .class-card:hover {
        transform: translateY(-2px);
        border-color: rgba(168, 85, 247, 0.35);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    .card-active {
        border-left: 4px solid #10b981 !important;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%);
    }
    .card-next {
        border-left: 4px solid #f59e0b !important;
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%);
    }

    .time-badge {
        font-size: 11px;
        font-weight: 600;
        color: #94a3b8;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 8px;
    }
    .status-tag {
        font-size: 9px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 10px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .status-live { background: rgba(16, 185, 129, 0.2); color: #34d399; }
    .status-upcoming { background: rgba(245, 158, 11, 0.2); color: #fbbf24; }

    .course-title {
        font-size: 15px;
        font-weight: 600;
        color: #f1f5f9;
        margin-bottom: 12px;
        line-height: 1.35;
    }

    .chip-container {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }
    .chip {
        font-size: 11px;
        font-weight: 500;
        padding: 4px 10px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.05);
        color: #cbd5e1;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .chip-venue {
        color: #a5b4fc;
        background: rgba(99, 102, 241, 0.12);
        border-color: rgba(99, 102, 241, 0.2);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255, 255, 255, 0.03);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }
    .stTabs [data-baseweb="tab"] {
        height: 38px;
        border-radius: 10px;
        color: #94a3b8;
        font-weight: 600;
        border: none !important;
        padding: 0 16px;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    .stTabs [data-baseweb="tab-border"] { display: none; }
</style>
""", unsafe_allow_html=True)

# Timetable dataset
schedule = {
    "MON": [
        {"start": time(14, 55), "end": time(15, 45), "time": "02:55 PM - 03:45 PM", "name": "Applied Chemistry", "type": "ETH", "slot": "F2+TF2", "venue": "AB4-320"},
        {"start": time(15, 50), "end": time(16, 40), "time": "03:50 PM - 04:40 PM", "name": "Micro Economics", "type": "TH", "slot": "D2+TD2", "venue": "AB4-320"},
        {"start": time(16, 45), "end": time(17, 35), "time": "04:45 PM - 05:35 PM", "name": "Technical English Communication", "type": "ETH", "slot": "B2+TB2", "venue": "AB4-320"}
    ],
    "TUE": [
        {"start": time(9, 50), "end": time(11, 30), "time": "09:50 AM - 11:30 AM", "name": "Problem Solving Using Python", "type": "LO", "slot": "L9+L10+L25+L26", "venue": "AB1-206"},
        {"start": time(14, 0), "end": time(14, 50), "time": "02:00 PM - 02:50 PM", "name": "Technical English Communication", "type": "ETH", "slot": "B2+TB2", "venue": "AB4-320"},
        {"start": time(15, 50), "end": time(16, 40), "time": "03:50 PM - 04:40 PM", "name": "Multivariable Calculus and Diff. Equations", "type": "ETH", "slot": "E2+TE2", "venue": "AB4-320"}
    ],
    "WED": [
        {"start": time(8, 0), "end": time(9, 40), "time": "08:00 AM - 09:40 AM", "name": "Multivariable Calculus and Diff. Equations", "type": "ELA", "slot": "L13+L14", "venue": "AB1-505A"},
        {"start": time(15, 50), "end": time(16, 40), "time": "03:50 PM - 04:40 PM", "name": "Applied Chemistry", "type": "ETH", "slot": "F2+TF2", "venue": "AB4-320"},
        {"start": time(16, 45), "end": time(17, 35), "time": "04:45 PM - 05:35 PM", "name": "Micro Economics", "type": "TH", "slot": "D2+TD2", "venue": "AB4-320"}
    ],
    "THU": [
        {"start": time(9, 50), "end": time(11, 30), "time": "09:50 AM - 11:30 AM", "name": "Technical English Communication", "type": "ELA", "slot": "L21+L22", "venue": "AB1-404 A"},
        {"start": time(14, 0), "end": time(14, 50), "time": "02:00 PM - 02:50 PM", "name": "Micro Economics", "type": "TH", "slot": "D2+TD2", "venue": "AB4-320"},
        {"start": time(14, 55), "end": time(15, 45), "time": "02:55 PM - 03:45 PM", "name": "Technical English Communication", "type": "ETH", "slot": "B2+TB2", "venue": "AB4-320"},
        {"start": time(16, 45), "end": time(17, 35), "time": "04:45 PM - 05:35 PM", "name": "Multivariable Calculus and Diff. Equations", "type": "ETH", "slot": "E2+TE2", "venue": "AB4-320"}
    ],
    "FRI": [
        {"start": time(8, 0), "end": time(9, 40), "time": "08:00 AM - 09:40 AM", "name": "Problem Solving Using Python", "type": "LO", "slot": "L9+L10+L25+L26", "venue": "AB1-206"},
        {"start": time(11, 40), "end": time(13, 20), "time": "11:40 AM - 01:20 PM", "name": "Applied Chemistry", "type": "ELA", "slot": "L29+L30", "venue": "AB1-303"},
        {"start": time(14, 0), "end": time(14, 50), "time": "02:00 PM - 02:50 PM", "name": "Multivariable Calculus and Diff. Equations", "type": "ETH", "slot": "E2+TE2", "venue": "AB4-320"},
        {"start": time(16, 45), "end": time(17, 35), "time": "04:45 PM - 05:35 PM", "name": "Applied Chemistry", "type": "ETH", "slot": "F2+TF2", "venue": "AB4-320"}
    ]
}

# Standard Indian Standard Time (UTC+5:30) without external libraries
ist_zone = timezone(timedelta(hours=5, minutes=30))
now_ist = datetime.now(ist_zone)
current_time = now_ist.time()
weekday_names = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
today_str = weekday_names[now_ist.weekday()]

# Top Profile Bar
st.markdown(f"""
<div class="top-bar">
    <div>
        <div style="font-size: 11px; color: #94a3b8; letter-spacing: 0.5px; text-transform: uppercase;">VIT Timetable</div>
        <div style="font-size: 18px; font-weight: 700; color: #ffffff;">My Schedule</div>
    </div>
    <span class="reg-pill">26BAI1279</span>
</div>
""", unsafe_allow_html=True)

# Tabs
days = ["MON", "TUE", "WED", "THU", "FRI"]
tabs = st.tabs([f" {d} " for d in days])

for i, day in enumerate(days):
    with tabs[i]:
        classes = schedule[day]
        is_today = (day == today_str)
        found_next = False
        
        for item in classes:
            extra_class = ""
            status_tag = ""
            
            if is_today:
                if item["start"] <= current_time <= item["end"]:
                    extra_class = "card-active"
                    status_tag = '<span class="status-tag status-live">● Live Now</span>'
                elif current_time < item["start"] and not found_next:
                    extra_class = "card-next"
                    status_tag = '<span class="status-tag status-upcoming">Next Class</span>'
                    found_next = True
            
            st.markdown(f"""
            <div class="class-card {extra_class}">
                <div class="time-badge">
                    <span>⏱ {item['time']}</span>
                    {status_tag}
                </div>
                <div class="course-title">{item['name']}</div>
                <div class="chip-container">
                    <span class="chip chip-venue">📍 {item['venue']}</span>
                    <span class="chip">🏷 {item['slot']}</span>
                    <span class="chip">📘 {item['type']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
