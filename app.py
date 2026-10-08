import streamlit as st
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="FIPI DUSC | 2026–27",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SAFE HTML RENDERER
# ============================================================
def render(html_str):
    """Safely strips spaces to prevent Streamlit from creating raw code blocks."""
    cleaned_html = "\n".join(line.strip() for line in html_str.split("\n") if line.strip())
    st.markdown(cleaned_html, unsafe_allow_html=True)

# ============================================================
# HIGH CONTRAST PROFESSIONAL CSS
# ============================================================
render("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #0F172A;        /* Deep Slate Navy */
        --navy-light: #1E293B;  
        --teal: #0F766E;        /* Industrial Teal */
        --gold: #EA580C;        /* Sharp Corporate Orange/Gold */
        --bg-gray: #F1F5F9;     /* Cool Gray for high contrast background */
        --white: #FFFFFF;
        --text-main: #0F172A;
        --text-muted: #475569;
        --border-color: #CBD5E1;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* High contrast background */
    .stApp {
        background-color: var(--bg-gray);
        color: var(--text-main);
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    header[data-testid="stHeader"] { background: transparent; }
    footer { visibility: hidden; }

    /* HERO SECTION */
    .hero {
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        padding: 50px 48px;
        margin-bottom: 30px;
        background: linear-gradient(135deg, var(--navy) 0%, #1E3A8A 100%);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        color: white;
        border-bottom: 5px solid var(--gold);
    }
    .hero-title {
        margin: 0; color: white !important; font-size: clamp(2.2rem, 4vw, 4rem) !important;
        line-height: 1.1; font-weight: 800; letter-spacing: -1px;
    }
    .hero-highlight { color: #FACC15; }
    .hero-subtitle {
        max-width: 800px; margin-top: 15px; color: #E2E8F0 !important;
        font-size: 1.1rem; line-height: 1.6; font-weight: 400;
    }
    .hero-bottom { display: flex; gap: 12px; margin-top: 25px; flex-wrap: wrap; }
    .hero-pill {
        display: inline-flex; align-items: center; padding: 8px 16px; border-radius: 6px;
        background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2);
        color: white; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;
    }

    /* SECTION HEADERS */
    .section-title {
        display: flex; align-items: center; gap: 12px; margin-top: 30px; margin-bottom: 10px;
        padding-bottom: 10px; border-bottom: 2px solid var(--border-color);
    }
    .section-icon {
        width: 45px; height: 45px; border-radius: 8px; display: flex; align-items: center; justify-content: center;
        background: var(--navy); color: white; font-size: 1.3rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .section-name { margin: 0; font-size: 1.6rem; font-weight: 800; color: var(--navy); text-transform: uppercase; letter-spacing: -0.5px;}
    .section-desc { margin: 0 0 25px 0; color: var(--text-muted); font-size: 0.95rem; font-weight: 500;}

    /* KPI CARDS (Top Stats) */
    .kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 15px 0 35px 0; }
    .kpi-card {
        background: var(--white); border: 1px solid var(--border-color); border-left: 6px solid var(--gold);
        border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .kpi-icon { font-size: 1.5rem; margin-bottom: 10px; color: var(--navy); }
    .kpi-number { font-size: 2.2rem; font-weight: 800; color: var(--navy); line-height: 1; }
    .kpi-label { margin-top: 5px; color: var(--text-muted); font-size: 0.85rem; font-weight: 700; text-transform: uppercase; }

    /* GENERAL CARDS */
    .info-card {
        background: var(--white); border: 1px solid var(--border-color); border-top: 5px solid var(--teal);
        border-radius: 8px; padding: 25px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .info-card-title { color: var(--navy); font-weight: 800; font-size: 1.15rem; margin-bottom: 10px; text-transform: uppercase; }
    .info-card-text { color: var(--text-main); line-height: 1.6; font-size: 0.95rem; }
    .tag {
        display: inline-block; padding: 4px 10px; margin: 5px 5px 0 0; border-radius: 4px;
        background: #F1F5F9; border: 1px solid var(--border-color); color: var(--navy); font-size: 0.75rem; font-weight: 700;
    }

    /* ACHIEVEMENT CARDS (For text inside tabs) */
    .achievement {
        background: var(--white); border: 1px solid var(--border-color); border-left: 5px solid var(--teal);
        border-radius: 6px; padding: 20px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .achievement strong { color: var(--navy); font-size: 1.05rem; }
    .achievement p { margin: 8px 0 0 0; color: var(--text-main); line-height: 1.6; font-size: 0.95rem; }
    .achievement.gold { border-left-color: var(--gold); background-color: #FFFBEB; }

    /* IMAGES */
    div[data-testid="stImage"] {
        border-radius: 8px; overflow: hidden; border: 1px solid var(--border-color);
        background: var(--white); box-shadow: 0 4px 6px rgba(0,0,0,0.05); padding: 5px;
    }
    div[data-testid="stImage"] img { border-radius: 4px; object-fit: cover; }

    /* CORE COMMITTEE MEMBERS */
    .member-section {
        background: var(--white); border: 1px solid var(--border-color); border-top: 5px solid var(--navy);
        border-radius: 8px; padding: 25px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .member-section-title {
        font-size: 1.2rem; font-weight: 800; color: var(--navy); margin-bottom: 15px;
        padding-bottom: 10px; border-bottom: 2px solid var(--bg-gray); text-transform: uppercase;
    }
    .member { display: flex; align-items: center; gap: 15px; padding: 12px 0; border-bottom: 1px solid var(--bg-gray); }
    .member:last-child { border-bottom: none; }
    .member-avatar {
        width: 40px; height: 40px; min-width: 40px; border-radius: 6px; display: flex; align-items: center; justify-content: center;
        background: var(--bg-gray); border: 1px solid var(--border-color); color: var(--navy); font-weight: 800; font-size: 0.85rem;
    }
    .member-info { display: flex; flex-direction: column; }
    .member-name { color: var(--navy); font-size: 0.95rem; font-weight: 700; }
    .member-role { color: var(--text-muted); font-size: 0.8rem; margin-top: 2px; font-weight: 600; text-transform: uppercase; }

    /* R&D BANNER */
    .rd-banner {
        border-radius: 12px; padding: 35px; color: white; background: var(--navy);
        border-bottom: 5px solid var(--teal); box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2); margin-bottom: 30px;
    }
    .rd-banner h3 { color: white !important; margin-bottom: 12px; font-size: 1.8rem; text-transform: uppercase; }
    .rd-banner p { color: #E2E8F0; max-width: 850px; line-height: 1.6; font-size: 1.05rem; }
    .rd-chip {
        display: inline-block; margin-top: 15px; margin-right: 10px; padding: 6px 12px; border: 1px solid var(--teal);
        background: rgba(15, 118, 110, 0.2); border-radius: 4px; font-size: 0.8rem; font-weight: 700; color: #CCFBF1; text-transform: uppercase;
    }

    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px; background: var(--border-color); padding: 5px; border-radius: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px; padding: 0 20px; border-radius: 6px; color: var(--navy); font-weight: 700; background: var(--white); border: 1px solid transparent;
    }
    .stTabs [aria-selected="true"] {
        background: var(--navy) !important; color: white !important; border-color: var(--navy);
    }

    /* FOOTER */
    .footer {
        margin-top: 50px; padding: 30px; border-top: 2px solid var(--border-color);
        text-align: center; color: var(--text-muted); font-size: 0.85rem; background: var(--white); border-radius: 8px;
    }
    .footer strong { color: var(--navy); font-size: 1rem; }

</style>
""")

# ============================================================
# HELPERS
# ============================================================
def load_image(image_path, caption_text):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption_text, use_container_width=True)
    else:
        render(f"""
        <div class="info-card" style="text-align:center; padding:30px 20px; border-top: 5px solid #EA580C;">
            <div style="font-size:2rem; color: #EA580C;">⚠️</div>
            <div style="font-weight:800; color:var(--navy); margin-top:10px; text-transform:uppercase;">Image Not Found</div>
            <div style="font-size:0.9rem; color:var(--text-main); margin-top:5px;">
                Looking for exact file: <br><code style="background:#F1F5F9; padding:2px 5px; color:#EA580C;">{image_path}</code>
            </div>
        </div>
        """)

def section_header(icon, title, description=""):
    desc_html = f"<div class='section-desc'>{description}</div>" if description else ""
    render(f"""
    <div class="section-title">
        <div class="section-icon">{icon}</div>
        <div class="section-name">{title}</div>
    </div>
    {desc_html}
    """)

def achievement_card(title, text, gold=False):
    extra = "gold" if gold else ""
    render(f"""
    <div class="achievement {extra}">
        <strong>{title}</strong>
        <p>{text}</p>
    </div>
    """)

def initials(name):
    parts = name.split()
    return (parts[0][0] + parts[-1][0]).upper() if len(parts) >= 2 else name[:2].upper()

def member_section(title, members):
    html = f"""<div class="member-section"><div class="member-section-title">{title}</div>"""
    for name, role in members:
        html += f"""
        <div class="member">
            <div class="member-avatar">{initials(name)}</div>
            <div class="member-info">
                <div class="member-name">{name}</div>
                <div class="member-role">{role}</div>
            </div>
        </div>
        """
    html += "</div>"
    render(html)

# ============================================================
# HERO
# ============================================================
render("""
<div class="hero">
    <div class="hero-content">
        <h1 class="hero-title">FIPI Dibrugarh University <span class="hero-highlight">Student Chapter</span></h1>
        <div class="hero-subtitle">
            Bridging academia and the energy industry through technical excellence, innovation, research, industrial exposure and community engagement.
        </div>
        <div class="hero-bottom">
            <div class="hero-pill">Session 2026–27</div>
            <div class="hero-pill">Dibrugarh University</div>
            <div class="hero-pill">Energy • Technology • Innovation</div>
        </div>
    </div>
</div>
""")

# ============================================================
# TABS
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs(["HOME OVERVIEW", "CHAPTER ACTIVITIES", "CORE COMMITTEE", "RESEARCH & DEVELOPMENT"])

# ============================================================
# HOME
# ============================================================
with tab1:
    render("""
    <div class="kpi-grid">
        <div class="kpi-card"><div class="kpi-icon">🏆</div><div class="kpi-number">7</div><div class="kpi-label">IADC Well-Sharp Achievers</div></div>
        <div class="kpi-card"><div class="kpi-card" style="border:none; padding:0; box-shadow:none;"><div class="kpi-icon">🎯</div><div class="kpi-number">2</div><div class="kpi-label">OIL Placements</div></div></div>
        <div class="kpi-card"><div class="kpi-card" style="border:none; padding:0; box-shadow:none;"><div class="kpi-icon">🔬</div><div class="kpi-number">1</div><div class="kpi-label">Patent Published</div></div></div>
        <div class="kpi-card"><div class="kpi-card" style="border:none; padding:0; box-shadow:none;"><div class="kpi-icon">🌱</div><div class="kpi-number">4+</div><div class="kpi-label">Social Initiatives</div></div></div>
    </div>
    """)

    section_header("⚡", "Strategic Focus Areas", "The four pillars shaping the FIPI DUSC operational structure.")
    f1, f2, f3, f4 = st.columns(4)
    with f1: render("""<div class="info-card"><div class="info-card-title">Academic Excellence</div><div class="info-card-text">Supporting students through technical learning, professional certifications, and competitive academic initiatives.</div></div>""")
    with f2: render("""<div class="info-card"><div class="info-card-title">Industry Orientation</div><div class="info-card-text">Connecting students with real-world petroleum, energy, and industrial operations through guided exposure.</div></div>""")
    with f3: render("""<div class="info-card"><div class="info-card-title">Research & Innovation</div><div class="info-card-text">Encouraging student-led research, technical projects, patents, and emerging energy technologies.</div></div>""")
    with f4: render("""<div class="info-card"><div class="info-card-title">Social Impact</div><div class="info-card-text">Promoting responsible energy awareness, environmental sustainability, and dedicated community engagement.</div></div>""")

# ============================================================
# CHAPTER ACTIVITIES
# ============================================================
with tab2:
    # ACADEMIC EXCELLENCE
    section_header("🎓", "Academic Excellence", "Demonstrating technical and academic commitment.")
    c_a1, c_a2 = st.columns([1.7, 1], gap="large")
    with c_a1:
        achievement_card("IADC Well-Sharp University Examination", "The chapter proudly recognized members who successfully cleared the certification for the 2026–27 session. Achievers include Nirveek Goswami (86%), Abhishek Dutta (86%), Pratiksha Sonowal (85%), Aditi Gogoi (78%), Gargi Lahkar (75%), Arnavraj Baruah (74%), and Ipsita Deka (74%).")
        achievement_card("Placement Achievement", "Two members, Abhishek Dutta (Finance Officer) and Arnavraj Baruah (HR Officer), were successfully recruited by Oil India Limited (OIL).", gold=True)
        achievement_card("FIPI DU SC × PETROGATE ACADEMY", "Organized the 'ALL-INDIA LEVEL UNLOCKING PE EXAM' free scholarship test on 8th August 2026 for GATE & ONGC PE aspirants.")
    with c_a2: load_image("images/petrogate.jpg", "Petrogate Academy Scholarship Test")

    # INNOVATIONS
    section_header("💡", "Innovations", "Student-led ideas solving energy and engineering challenges.")
    render("""<div class="info-card"><div class="info-card-title">Emerging Student Innovations</div><div class="info-card-text">Innovative works by the members. New ideas. New approaches for solving old problems. Student-led new initiatives and technical solutions.</div><div style="margin-top:15px;"><span class="tag">Innovation</span><span class="tag">Problem Solving</span><span class="tag">Student Projects</span></div></div>""")

    # TECHNICAL EXCELLENCE
    section_header("⚙️", "Technical Excellence", "Research, competitions, and technical accomplishments.")
    c_t1, c_t2 = st.columns([1.7, 1], gap="large")
    with c_t1:
        achievement_card("Patent Published", "“A Process for Remediation of Crude-Oil Contaminated Water Using a Plant-Based Adsorbent Derived from Water Hyacinth (Eichhornia crassipes).” Inventors: Ipsita Deka, Isfaqul Alam, Junayed Khan, Kasturi Bonia, Dr. Chayanika Borah, and Joyshree Barman.", gold=True)
        achievement_card("Geonova Competition", "Rock and Mineral Identification Competition (“Geonova”) organized as part of Geology Week to enhance practical geological knowledge.")
    with c_t2:
        img1, img2 = st.columns(2)
        with img1: load_image("images/patent.jpg", "Patent Publication")
        with img2: load_image("images/geonova.jpg", "Geonova Competition")

    # INDUSTRY ORIENTATION
    section_header("🏭", "Industry Orientation", "Hands-on exposure to operating facilities and petroleum professionals.")
    c_i1, c_i2 = st.columns([1.7, 1], gap="large")
    with c_i1:
        achievement_card("Industrial Visit to OIL, Duliajan", "4th-semester B.Tech students visited the Water Supply Station (WSS) and Air Liquefaction Plant (ALP) on 7th May 2026.")
        achievement_card("Well Logging Department Visit", "2nd-semester M.Tech students undertook a one-day visit to the Well Logging Department of OIL on 28th April 2026 under Project SHARE, interacting with officials across Cased Hole, Open Hole, and Interpretation Sections.")
    with c_i2: load_image("images/oil_visit.jpg", "Industrial Visit to Oil India Limited")

    # SOCIAL ACTIVITIES
    section_header("🤝", "Social Activities & Outreach", "Community engagement and sustainability initiatives.")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        render("""<div class="info-card-title" style="margin-bottom:8px; font-size:0.95rem;">Prerona Children's Home</div>""")
        load_image("images/prerona.jpg", "Pre-event of FIPI Energy Week")
    with s2:
        render("""<div class="info-card-title" style="margin-bottom:8px; font-size:0.95rem;">Cleanliness Drive</div>""")
        load_image("images/cleanliness.jpg", "Code Green Drive")
    with s3:
        render("""<div class="info-card-title" style="margin-bottom:8px; font-size:0.95rem;">Membership Drive</div>""")
        load_image("images/membership.jpg", "Department of Geography")
    with s4:
        render("""<div class="info-card-title" style="margin-bottom:8px; font-size:0.95rem;">Plantation Drive</div>""")
        load_image("images/plantation.jpg", "World Environment Day")

    # PRESENTATION QUALITY
    section_header("📊", "Presentation Quality", "Clear communication and structured delivery.")
    render("""<div class="info-card"><div class="info-card-title">Evaluation Focus</div><div class="info-card-text">Making structured presentations, presenting within the prescribed time limit, demonstrating good articulation, and effectively answering questions from the jury.</div><div style="margin-top:15px;"><span class="tag">Structure</span><span class="tag">Time Management</span><span class="tag">Communication</span><span class="tag">Technical Depth</span></div></div>""")

# ============================================================
# CORE COMMITTEE
# ============================================================
with tab3:
    section_header("👥", "Core Committee 2026–27", "The leadership structure of FIPI Dibrugarh University Student Chapter.")
    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        member_section("Advisory Board", [("Dr. Deepjyoti Mech", "Asst. Faculty Advisor"), ("Dr. Borkha Mech", "Chief Faculty Advisor"), ("Dr. Himanta Borgohain", "Asst. Faculty Advisor")])
        member_section("Executive Leadership", [("Nirveek Goswami", "Secretary"), ("Gargi Lahkar", "President"), ("Nabarun Chakraborty", "Vice-President")])
        member_section("Finance & Management", [("Sparshan Bharadwaj", "General Manager"), ("Abhishek Dutta", "Finance Officer"), ("Hirok Jyoti Dutta", "Chief Operational Officer"), ("Mridupawan Shandilya", "General Manager"), ("Twinkle Bhuyan", "Finance Officer")])
        member_section("HR & Records", [("Arnavraj Baruah", "HR Officer"), ("Akashnil Borah", "HR Officer"), ("Aditi Gogoi", "Documentation Chief"), ("Spriha Hazarika", "Documentation Head"), ("Bhargavjyoti Gogoi", "Documentation Head"), ("Preeyam Choudhary", "Documentation Head"), ("Abhinav Parasar", "Documentation Head")])

    with col_right:
        member_section("Creative & Outreach", [("Ipsita Deka", "Designing Chief"), ("Nibirh Hazarika", "Designing Chief"), ("Biswajit Rajkhowa", "Designing Head"), ("Tusti Chetia", "Designing Head"), ("Jayed Hazarika", "Membership Head"), ("Abhraneil Boruah", "Membership Head")])
        member_section("Industry, Technology & Culture", [("Pratiksha Sonowal", "Industrial & Communication Chairperson"), ("Roshan Kar", "Industrial & Communication Chairperson"), ("Pankita Priyam Sarma", "Industrial & Communication Chairperson"), ("Arindom Gogoi", "Technical Head"), ("Shubharaj Sonowal", "Technical Head"), ("Devleena Kalita", "Cultural Head"), ("Manash Pratim Phukan", "Cultural Head")])
        member_section("Events, Media & Promotions", [("Anisha Rahman", "Event Management Head"), ("Debashish Sharma", "Event Management Head"), ("Trishna Pegu", "Social Media Manager"), ("Urmi Ghosh", "Social Media Manager"), ("Anurag Thakur", "Marketing Head"), ("Archan Nath", "Marketing Head")])

# ============================================================
# R&D CELL
# ============================================================
with tab4:
    render("""
    <div class="rd-banner">
        <h3>🔬 Research & Development Cell</h3>
        <p>Cultivating a research-oriented culture, encouraging interdisciplinary technical work, and creating opportunities for students to explore emerging technologies in petroleum and energy engineering.</p>
        <span class="rd-chip">Research</span><span class="rd-chip">Innovation</span><span class="rd-chip">Technical Projects</span><span class="rd-chip">Interdisciplinary Work</span>
    </div>
    """)

    rd1, rd2 = st.columns(2, gap="large")
    with rd1: member_section("Advisory Board", [("Dr. Borkha Mech", "Director"), ("Dr. Deepjyoti Mech", "Director")])
    with rd2: member_section("R&D Core Team", [("Abhishek Dutta", "Chief Coordinator"), ("Arnavraj Baruah", "Technical Lead"), ("Roshan Kar", "Technical Lead"), ("Nirveek Goswami", "Finance Manager"), ("Akashnil Borah", "Finance Manager")])

    section_header("🚀", "R&D Vision", "Turning student ideas into structured technical initiatives.")
    v1, v2, v3 = st.columns(3)
    with v1: render("""<div class="info-card"><div class="info-card-title">Research Culture</div><div class="info-card-text">Encourage students to identify engineering problems, conduct literature reviews and develop technically sound solutions.</div></div>""")
    with v2: render("""<div class="info-card"><div class="info-card-title">Technical Projects</div><div class="info-card-text">Promote simulation, experimentation, data analysis and prototype development across energy disciplines.</div></div>""")
    with v3: render("""<div class="info-card"><div class="info-card-title">Research Outcomes</div><div class="info-card-text">Transform promising student projects into papers, patents, competitions and industry-relevant solutions.</div></div>""")

# ============================================================
# FOOTER
# ============================================================
render("""
<div class="footer">
    <strong>FIPI Dibrugarh University Student Chapter</strong><br>Session 2026–27 · Dibrugarh University<br><br>Petroleum Engineering • Research • Industry • Innovation
</div>
""")
