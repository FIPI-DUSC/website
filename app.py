import streamlit as st
import os
import textwrap

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
# CUSTOM CSS
# ============================================================
st.markdown(textwrap.dedent(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #071A2B;
        --navy-2: #0B2740;
        --blue: #123E63;
        --teal: #0F766E;
        --teal-light: #14B8A6;
        --gold: #F59E0B;
        --gold-light: #FBBF24;
        --white: #FFFFFF;
        --bg: #F4F8FB;
        --text: #1F2937;
        --muted: #64748B;
        --border: #DCE6EE;
        --card: #FFFFFF;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 5%, rgba(20,184,166,0.07), transparent 22%),
            radial-gradient(circle at 92% 8%, rgba(245,158,11,0.06), transparent 20%),
            linear-gradient(180deg, #F8FBFD 0%, #F3F7FA 100%);
        color: var(--text);
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hide default Streamlit top decoration */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    footer {
        visibility: hidden;
    }

    h1, h2, h3, h4 {
        color: var(--navy) !important;
        font-weight: 800 !important;
    }

    p {
        color: var(--text);
    }

    /* ========================================================
       HERO SECTION
       ======================================================== */

    .hero {
        position: relative;
        overflow: hidden;
        border-radius: 26px;
        padding: 46px 48px;
        margin-bottom: 28px;

        background:
            linear-gradient(
                120deg,
                rgba(7,26,43,1) 0%,
                rgba(11,39,64,0.98) 50%,
                rgba(15,118,110,0.95) 100%
            );

        box-shadow:
            0 18px 45px rgba(7,26,43,0.18),
            inset 0 1px 0 rgba(255,255,255,0.08);

        color: white;
    }

    .hero::before {
        content: "";
        position: absolute;
        width: 360px;
        height: 360px;
        border-radius: 50%;
        top: -180px;
        right: -90px;
        background: rgba(20,184,166,0.16);
        filter: blur(2px);
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 240px;
        height: 240px;
        border-radius: 50%;
        bottom: -150px;
        left: -70px;
        background: rgba(245,158,11,0.12);
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .hero-kicker {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 13px;
        margin-bottom: 16px;

        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 999px;

        background: rgba(255,255,255,0.07);
        color: #D5FFFA;

        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .hero-title {
        margin: 0;
        color: white !important;
        font-size: clamp(2rem, 4vw, 3.7rem) !important;
        line-height: 1.05;
        letter-spacing: -1.8px;
    }

    .hero-highlight {
        color: var(--gold-light);
    }

    .hero-subtitle {
        max-width: 820px;
        margin-top: 16px;
        color: rgba(255,255,255,0.82) !important;
        font-size: 1.05rem;
        line-height: 1.75;
    }

    .hero-bottom {
        display: flex;
        gap: 12px;
        margin-top: 28px;
        flex-wrap: wrap;
    }

    .hero-pill {
        display: inline-flex;
        align-items: center;
        padding: 9px 14px;
        border-radius: 10px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.09);
        color: white;
        font-size: 0.82rem;
        font-weight: 600;
    }

    /* Petroleum graphic */
    .hero-graphic {
        position: absolute;
        right: 45px;
        bottom: 25px;
        width: 245px;
        height: 130px;
        opacity: 0.9;
        z-index: 1;
    }

    .rig {
        position: absolute;
        right: 45px;
        bottom: 5px;
        width: 90px;
        height: 110px;
        border-left: 3px solid rgba(255,255,255,0.45);
        border-right: 3px solid rgba(255,255,255,0.45);
        transform: skew(-9deg);
    }

    .rig::before {
        content: "";
        position: absolute;
        top: 0;
        left: -4px;
        width: 96px;
        border-top: 3px solid rgba(255,255,255,0.45);
    }

    .rig::after {
        content: "";
        position: absolute;
        left: 42px;
        top: 0;
        height: 110px;
        border-left: 2px dashed rgba(255,255,255,0.32);
    }

    .pipeline {
        position: absolute;
        left: 0;
        bottom: 15px;
        width: 190px;
        height: 10px;
        border-radius: 999px;
        background: linear-gradient(
            90deg,
            rgba(255,255,255,0.12),
            rgba(20,184,166,0.75),
            rgba(245,158,11,0.8)
        );
        box-shadow: 0 0 15px rgba(20,184,166,0.3);
    }

    /* ========================================================
       SECTION HEADERS
       ======================================================== */

    .section-title {
        display: flex;
        align-items: center;
        gap: 13px;
        margin-top: 18px;
        margin-bottom: 8px;
    }

    .section-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;

        background:
            linear-gradient(135deg, var(--navy), var(--teal));

        color: white;
        font-size: 1.15rem;

        box-shadow:
            0 7px 18px rgba(7,26,43,0.14);
    }

    .section-name {
        margin: 0;
        font-size: 1.55rem;
        font-weight: 800;
        color: var(--navy);
    }

    .section-desc {
        margin: 0 0 20px 55px;
        color: var(--muted);
        font-size: 0.9rem;
    }

    /* ========================================================
       KPI CARDS
       ======================================================== */

    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin: 12px 0 30px 0;
    }

    .kpi-card {
        position: relative;
        overflow: hidden;
        background: white;
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 22px;

        box-shadow: 0 7px 20px rgba(15,23,42,0.055);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 13px 30px rgba(15,23,42,0.09);
    }

    .kpi-card::after {
        content: "";
        position: absolute;
        right: -35px;
        top: -35px;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background: rgba(20,184,166,0.07);
    }

    .kpi-icon {
        font-size: 1.45rem;
        margin-bottom: 8px;
    }

    .kpi-number {
        font-size: 1.9rem;
        font-weight: 800;
        color: var(--navy);
    }

    .kpi-label {
        margin-top: 3px;
        color: var(--muted);
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* ========================================================
       CARDS
       ======================================================== */

    .info-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 22px;
        height: 100%;
        box-shadow: 0 6px 18px rgba(15,23,42,0.045);
    }

    .info-card-title {
        color: var(--navy);
        font-weight: 800;
        font-size: 1.05rem;
        margin-bottom: 9px;
    }

    .info-card-text {
        color: #475569;
        line-height: 1.7;
        font-size: 0.9rem;
    }

    .tag {
        display: inline-block;
        padding: 5px 9px;
        margin: 4px 4px 0 0;
        border-radius: 7px;
        background: #E7F7F4;
        color: #0F5E57;
        font-size: 0.72rem;
        font-weight: 700;
    }

    /* ========================================================
       ACHIEVEMENT CARDS
       ======================================================== */

    .achievement {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FCFD 100%);
        border: 1px solid var(--border);
        border-left: 4px solid var(--teal);
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 13px;
        box-shadow: 0 5px 15px rgba(15,23,42,0.045);
    }

    .achievement strong {
        color: var(--navy);
    }

    .achievement p {
        margin: 6px 0 0 0;
        color: #475569;
        line-height: 1.65;
        font-size: 0.88rem;
    }

    /* Gold achievement */
    .achievement.gold {
        border-left-color: var(--gold);
    }

    /* ========================================================
       IMAGE CARDS
       ======================================================== */

    .image-caption {
        font-size: 0.78rem;
        font-weight: 700;
        color: var(--navy);
        margin-top: 6px;
    }

    div[data-testid="stImage"] {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid var(--border);
        background: white;
        box-shadow: 0 7px 20px rgba(15,23,42,0.08);
    }

    div[data-testid="stImage"] img {
        border-radius: 15px;
        object-fit: cover;
    }

    /* ========================================================
       MEMBER CARDS
       ======================================================== */

    .member-section {
        background: white;
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;

        box-shadow: 0 6px 18px rgba(15,23,42,0.045);
    }

    .member-section-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: var(--navy);
        margin-bottom: 15px;
        padding-bottom: 11px;
        border-bottom: 1px solid #E8EEF3;
    }

    .member {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 0;
        border-bottom: 1px solid #F0F4F7;
    }

    .member:last-child {
        border-bottom: none;
    }

    .member-avatar {
        width: 34px;
        height: 34px;
        min-width: 34px;
        border-radius: 50%;

        display: flex;
        align-items: center;
        justify-content: center;

        background: linear-gradient(135deg, var(--navy), var(--teal));
        color: white;
        font-weight: 800;
        font-size: 0.75rem;
    }

    .member-info {
        display: flex;
        flex-direction: column;
    }

    .member-name {
        color: var(--navy);
        font-size: 0.86rem;
        font-weight: 700;
    }

    .member-role {
        color: var(--muted);
        font-size: 0.72rem;
        margin-top: 2px;
    }

    /* ========================================================
       R&D SPOTLIGHT
       ======================================================== */

    .rd-banner {
        border-radius: 22px;
        padding: 28px;
        color: white;

        background:
            linear-gradient(
                135deg,
                #071A2B 0%,
                #0C3C5D 60%,
                #0F766E 100%
            );

        box-shadow: 0 15px 35px rgba(7,26,43,0.16);
        margin-bottom: 22px;
    }

    .rd-banner h3 {
        color: white !important;
        margin-bottom: 8px;
    }

    .rd-banner p {
        color: rgba(255,255,255,0.78);
        max-width: 850px;
        line-height: 1.7;
    }

    .rd-chip {
        display: inline-block;
        margin-top: 8px;
        margin-right: 7px;
        padding: 6px 10px;
        border: 1px solid rgba(255,255,255,0.14);
        background: rgba(255,255,255,0.07);
        border-radius: 8px;
        font-size: 0.72rem;
        font-weight: 700;
    }

    /* ========================================================
       INFO BOX / ADMIN NOTE
       ======================================================== */

    .admin-note {
        border: 1px solid #CFE7E4;
        border-radius: 15px;
        padding: 16px 18px;
        background: #EFFAF8;
        color: #155E59;
        margin-top: 10px;
    }

    /* ========================================================
       TABS
       ======================================================== */

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255,255,255,0.82);
        padding: 8px;
        border: 1px solid var(--border);
        border-radius: 15px;

        box-shadow:
            0 6px 18px rgba(15,23,42,0.045);

        backdrop-filter: blur(10px);
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        padding: 0 17px;
        border-radius: 10px;
        color: #64748B;
        font-weight: 700;
    }

    .stTabs [aria-selected="true"] {
        background:
            linear-gradient(135deg, var(--navy), var(--teal)) !important;

        color: white !important;
        box-shadow: 0 5px 14px rgba(7,26,43,0.18);
    }

    /* ========================================================
       DIVIDER
       ======================================================== */

    hr {
        border: none !important;
        border-top: 1px solid #DCE6EE !important;
        margin: 30px 0 !important;
    }

    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        margin-top: 40px;
        padding: 25px;
        border-top: 1px solid var(--border);
        text-align: center;
        color: #7A8794;
        font-size: 0.78rem;
    }

    .footer strong {
        color: var(--navy);
    }

    /* ========================================================
       RESPONSIVE
       ======================================================== */

    @media (max-width: 900px) {
        .hero {
            padding: 32px 28px;
        }

        .hero-graphic {
            display: none;
        }

        .kpi-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 600px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            border-radius: 19px;
            padding: 28px 22px;
        }

        .hero-title {
            font-size: 2rem !important;
        }

        .hero-subtitle {
            font-size: 0.9rem;
        }

        .kpi-grid {
            grid-template-columns: 1fr 1fr;
            gap: 9px;
        }

        .kpi-card {
            padding: 15px;
        }

        .kpi-number {
            font-size: 1.5rem;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 0 9px;
            font-size: 0.72rem;
        }
    }

    </style>
    """
), unsafe_allow_html=True)

# ============================================================
# HELPERS
# ============================================================

def load_image(image_path, caption_text):
    """
    Safely loads an image from the local project directory.
    """
    if os.path.exists(image_path):
        st.image(
            image_path,
            caption=caption_text,
            use_container_width=True
        )
    else:
        st.markdown(textwrap.dedent(
            f"""
            <div class="info-card" style="text-align:center; padding:35px 20px;">
                <div style="font-size:2rem;">📷</div>
                <div style="font-weight:700; color:#071A2B; margin-top:6px;">
                    Image Pending
                </div>
                <div style="font-size:0.76rem; color:#64748B; margin-top:4px;">
                    Add <code>{image_path}</code> to the GitHub repository.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)


def section_header(icon, title, description=""):
    st.markdown(textwrap.dedent(
        f"""
        <div class="section-title">
            <div class="section-icon">{icon}</div>
            <div class="section-name">{title}</div>
        </div>
        {"<div class='section-desc'>" + description + "</div>" if description else ""}
        """
    ), unsafe_allow_html=True)


def achievement_card(title, text, gold=False):
    extra_class = "gold" if gold else ""
    st.markdown(textwrap.dedent(
        f"""
        <div class="achievement {extra_class}">
            <strong>{title}</strong>
            <p>{text}</p>
        </div>
        """
    ), unsafe_allow_html=True)


def initials(name):
    parts = name.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    return name[:2].upper()


def member_section(title, members):
    html = f"""
    <div class="member-section">
        <div class="member-section-title">{title}</div>
    """

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

    st.markdown(textwrap.dedent(html), unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown(textwrap.dedent(
    """
    <div class="hero">
        <div class="hero-content">

            <div class="hero-kicker">
                🛢️ FIPI STUDENT CHAPTER
            </div>

            <h1 class="hero-title">
                FIPI Dibrugarh University
                <span class="hero-highlight">Student Chapter</span>
            </h1>

            <div class="hero-subtitle">
                Bridging academia and the energy industry through
                technical excellence, innovation, research,
                industrial exposure and community engagement.
            </div>

            <div class="hero-bottom">
                <div class="hero-pill">📚 Session 2026–27</div>
                <div class="hero-pill">🎓 Dibrugarh University</div>
                <div class="hero-pill">⚡ Energy • Technology • Innovation</div>
            </div>

        </div>

        <div class="hero-graphic">
            <div class="pipeline"></div>
            <div class="rig"></div>
        </div>
    </div>
    """
), unsafe_allow_html=True)

# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🏠  Home",
        "📅  Chapter Activities",
        "👥  Core Committee",
        "🔬  R&D Cell",
    ]
)

# ============================================================
# HOME
# ============================================================

with tab1:

    section_header(
        "🏠",
        "Welcome to FIPI DUSC",
        "A student-driven platform connecting petroleum education, industry exposure and innovation."
    )

    st.markdown(textwrap.dedent(
        """
        <div class="info-card">
            <div class="info-card-title">
                Building the next generation of energy professionals
            </div>
            <div class="info-card-text">
                The FIPI Dibrugarh University Student Chapter works to create
                meaningful opportunities for students through technical
                activities, industrial interaction, academic initiatives,
                research, innovation and social outreach.
            </div>

            <div style="margin-top:14px;">
                <span class="tag">Petroleum Engineering</span>
                <span class="tag">Industry Interaction</span>
                <span class="tag">Research</span>
                <span class="tag">Innovation</span>
                <span class="tag">Leadership</span>
            </div>
        </div>
        """
    ), unsafe_allow_html=True)

    # --------------------------------------------------------
    # KPI SECTION
    # --------------------------------------------------------

    st.markdown(textwrap.dedent(
        """
        <div class="kpi-grid">

            <div class="kpi-card">
                <div class="kpi-icon">🏆</div>
                <div class="kpi-number">7</div>
                <div class="kpi-label">IADC Well-Sharp Achievers</div>
            </div>

            <div class="kpi-card">
                <div class="kpi-icon">🎯</div>
                <div class="kpi-number">2</div>
                <div class="kpi-label">OIL Placement Achievements</div>
            </div>

            <div class="kpi-card">
                <div class="kpi-icon">🔬</div>
                <div class="kpi-number">1</div>
                <div class="kpi-label">Patent Published</div>
            </div>

            <div class="kpi-card">
                <div class="kpi-icon">🌱</div>
                <div class="kpi-number">4+</div>
                <div class="kpi-label">Community Initiatives</div>
            </div>

        </div>
        """
    ), unsafe_allow_html=True)

    # --------------------------------------------------------
    # FOCUS AREAS
    # --------------------------------------------------------

    section_header(
        "⚡",
        "Our Focus",
        "Four pillars shaping the chapter's activities."
    )

    focus1, focus2, focus3, focus4 = st.columns(4)

    with focus1:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.8rem;">🎓</div>
                <div class="info-card-title">Academic Excellence</div>
                <div class="info-card-text">
                    Supporting students through technical learning,
                    certifications, competitions and academic initiatives.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)

    with focus2:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.8rem;">🏭</div>
                <div class="info-card-title">Industry Orientation</div>
                <div class="info-card-text">
                    Connecting students with real-world petroleum,
                    energy and industrial operations.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)

    with focus3:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.8rem;">🔬</div>
                <div class="info-card-title">Research & Innovation</div>
                <div class="info-card-text">
                    Encouraging student-led research, technical projects,
                    patents and emerging technologies.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)

    with focus4:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.8rem;">🌱</div>
                <div class="info-card-title">Social Impact</div>
                <div class="info-card-text">
                    Promoting responsible energy awareness,
                    sustainability and community engagement.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(textwrap.dedent(
        """
        <div class="admin-note">
            💡 <strong>Admin Note:</strong>
            To update chapter information, activities or committee data,
            edit the corresponding sections of <code>app.py</code>
            and commit the changes to GitHub.
        </div>
        """
    ), unsafe_allow_html=True)


# ============================================================
# CHAPTER ACTIVITIES
# ============================================================

with tab2:

    section_header(
        "📅",
        "Annual Activities & Evaluation",
        "Highlights from the FIPI DUSC 2026–27 session."
    )

    # --------------------------------------------------------
    # ACADEMIC EXCELLENCE
    # --------------------------------------------------------

    section_header(
        "🎓",
        "Academic Excellence",
        "Achievements that demonstrate technical and academic commitment."
    )

    col_a1, col_a2 = st.columns([1.7, 1], gap="large")

    with col_a1:

        achievement_card(
            "IADC Well-Sharp University Examination",
            "The chapter proudly recognized members who successfully cleared "
            "the certification for the 2026–27 session. Achievers include "
            "Nirveek Goswami (86%), Abhishek Dutta (86%), Pratiksha Sonowal "
            "(85%), Aditi Gogoi (78%), Gargi Lahkar (75%), Arnavraj Baruah "
            "(74%), and Ipsita Deka (74%)."
        )

        achievement_card(
            "Placement Achievement",
            "Two members, Abhishek Dutta (Finance Officer) and Arnavraj Baruah "
            "(HR Officer), were successfully recruited by Oil India Limited (OIL).",
            gold=True
        )

        achievement_card(
            "FIPI DU SC × PETROGATE ACADEMY",
            "Organized the 'ALL-INDIA LEVEL UNLOCKING PE EXAM' free scholarship "
            "test on 8th August 2026 for GATE & ONGC PE aspirants."
        )

    with col_a2:
        load_image(
            "images/petrogate.jpg",
            "Petrogate Academy Scholarship Test"
        )

    st.divider()

    # --------------------------------------------------------
    # INNOVATIONS
    # --------------------------------------------------------

    section_header(
        "💡",
        "Innovations",
        "Student-led ideas aimed at solving existing energy and engineering challenges."
    )

    st.markdown(textwrap.dedent(
        """
        <div class="info-card">
            <div class="info-card-title">
                Emerging Student Innovations
            </div>
            <div class="info-card-text">
                Innovative works by the members. New ideas. New approaches
                for solving old problems. Student-led new initiatives and
                technical solutions.
            </div>

            <div style="margin-top:15px;">
                <span class="tag">Innovation</span>
                <span class="tag">Problem Solving</span>
                <span class="tag">Student Projects</span>
            </div>

            <div style="margin-top:15px; color:#94A3B8; font-style:italic;">
                Status: To be updated.
            </div>
        </div>
        """
    ), unsafe_allow_html=True)

    st.divider()

    # --------------------------------------------------------
    # TECHNICAL EXCELLENCE
    # --------------------------------------------------------

    section_header(
        "⚙️",
        "Technical Excellence",
        "Research, competitions and technical accomplishments."
    )

    col_t1, col_t2 = st.columns([1.7, 1], gap="large")

    with col_t1:

        achievement_card(
            "Patent Published",
            "“A Process for Remediation of Crude-Oil Contaminated Water Using "
            "a Plant-Based Adsorbent Derived from Water Hyacinth "
            "(Eichhornia crassipes).” Inventors: Ipsita Deka, Isfaqul Alam, "
            "Junayed Khan, Kasturi Bonia, Dr. Chayanika Borah, and Joyshree Barman.",
            gold=True
        )

        achievement_card(
            "Geonova Competition",
            "Rock and Mineral Identification Competition (“Geonova”) "
            "organized as part of Geology Week to enhance practical "
            "geological knowledge."
        )

    with col_t2:

        img1, img2 = st.columns(2)

        with img1:
            load_image(
                "images/patent.jpg",
                "Patent Publication"
            )

        with img2:
            load_image(
                "images/geonova.jpg",
                "Geonova Competition"
            )

    st.divider()

    # --------------------------------------------------------
    # INDUSTRY ORIENTATION
    # --------------------------------------------------------

    section_header(
        "🏭",
        "Industry Orientation",
        "Hands-on exposure to operating facilities and petroleum-industry professionals."
    )

    col_i1, col_i2 = st.columns([1.7, 1], gap="large")

    with col_i1:

        achievement_card(
            "Industrial Visit to OIL, Duliajan",
            "4th-semester B.Tech students visited the Water Supply Station (WSS) "
            "and Air Liquefaction Plant (ALP) on 7th May 2026."
        )

        achievement_card(
            "Well Logging Department Visit",
            "2nd-semester M.Tech students undertook a one-day visit to the "
            "Well Logging Department of OIL on 28th April 2026 under Project SHARE, "
            "interacting with officials across Cased Hole, Open Hole, and "
            "Interpretation Sections."
        )

    with col_i2:
        load_image(
            "images/oil_visit.jpg",
            "Industrial Visit to Oil India Limited"
        )

    st.divider()

    # --------------------------------------------------------
    # SOCIAL ACTIVITIES
    # --------------------------------------------------------

    section_header(
        "🤝",
        "Social Activities & Outreach",
        "Community engagement and sustainability initiatives driven by chapter members."
    )

    s1, s2, s3, s4 = st.columns(4)

    social_data = [
        ("Prerona Children's Home", "images/prerona.jpg", "Pre-event of FIPI Energy Week"),
        ("Cleanliness Drive", "images/cleanliness.jpg", "Code Green Drive"),
        ("Membership Drive", "images/membership.jpg", "Department of Geography"),
        ("Plantation Drive", "images/plantation.jpg", "World Environment Day"),
    ]

    columns = [s1, s2, s3, s4]

    for col, (title, path, caption) in zip(columns, social_data):
        with col:
            st.markdown(textwrap.dedent(
                f"""
                <div class="info-card-title" style="margin-bottom:8px;">
                    {title}
                </div>
                """
            ), unsafe_allow_html=True)
            load_image(path, caption)

    st.divider()

    # --------------------------------------------------------
    # PRESENTATION QUALITY
    # --------------------------------------------------------

    section_header(
        "📊",
        "Presentation Quality",
        "Clear communication, structured delivery and effective response to jury questions."
    )

    st.markdown(textwrap.dedent(
        """
        <div class="info-card">
            <div class="info-card-title">
                Evaluation Focus
            </div>

            <div class="info-card-text">
                Making structured presentations, presenting within the
                prescribed time limit, demonstrating good articulation,
                and effectively answering questions from the jury.
            </div>

            <div style="margin-top:15px;">
                <span class="tag">Structure</span>
                <span class="tag">Time Management</span>
                <span class="tag">Communication</span>
                <span class="tag">Technical Depth</span>
            </div>

            <div style="margin-top:15px; color:#94A3B8; font-style:italic;">
                Status: To be updated.
            </div>
        </div>
        """
    ), unsafe_allow_html=True)


# ============================================================
# CORE COMMITTEE
# ============================================================

with tab3:

    section_header(
        "👥",
        "Core Committee 2026–27",
        "The leadership and functional structure of FIPI Dibrugarh University Student Chapter."
    )

    left_col, right_col = st.columns(2, gap="large")

    # --------------------------------------------------------
    # LEFT
    # --------------------------------------------------------

    with left_col:

        member_section(
            "Advisory Board",
            [
                ("Dr. Deepjyoti Mech", "Asst. Faculty Advisor"),
                ("Dr. Borkha Mech", "Chief Faculty Advisor"),
                ("Dr. Himanta Borgohain", "Asst. Faculty Advisor"),
            ]
        )

        member_section(
            "Executive Leadership",
            [
                ("Nirveek Goswami", "Secretary"),
                ("Gargi Lahkar", "President"),
                ("Nabarun Chakraborty", "Vice-President"),
            ]
        )

        member_section(
            "Finance & Management",
            [
                ("Sparshan Bharadwaj", "General Manager"),
                ("Abhishek Dutta", "Finance Officer"),
                ("Hirok Jyoti Dutta", "Chief Operational Officer"),
                ("Mridupawan Shandilya", "General Manager"),
                ("Twinkle Bhuyan", "Finance Officer"),
            ]
        )

        member_section(
            "HR & Records",
            [
                ("Arnavraj Baruah", "HR Officer"),
                ("Akashnil Borah", "HR Officer"),
                ("Aditi Gogoi", "Documentation Chief"),
                ("Spriha Hazarika", "Documentation Head"),
                ("Bhargavjyoti Gogoi", "Documentation Head"),
                ("Preeyam Choudhary", "Documentation Head"),
                ("Abhinav Parasar", "Documentation Head"),
            ]
        )

    # --------------------------------------------------------
    # RIGHT
    # --------------------------------------------------------

    with right_col:

        member_section(
            "Creative & Outreach",
            [
                ("Ipsita Deka", "Designing Chief"),
                ("Nibirh Hazarika", "Designing Chief"),
                ("Biswajit Rajkhowa", "Designing Head"),
                ("Tusti Chetia", "Designing Head"),
                ("Jayed Hazarika", "Membership Head"),
                ("Abhraneil Boruah", "Membership Head"),
            ]
        )

        member_section(
            "Industry, Technology & Culture",
            [
                ("Pratiksha Sonowal", "Industrial & Communication Chairperson"),
                ("Roshan Kar", "Industrial & Communication Chairperson"),
                ("Pankita Priyam Sarma", "Industrial & Communication Chairperson"),
                ("Arindom Gogoi", "Technical Head"),
                ("Shubharaj Sonowal", "Technical Head"),
                ("Devleena Kalita", "Cultural Head"),
                ("Manash Pratim Phukan", "Cultural Head"),
            ]
        )

        member_section(
            "Events, Media & Promotions",
            [
                ("Anisha Rahman", "Event Management Head"),
                ("Debashish Sharma", "Event Management Head"),
                ("Trishna Pegu", "Social Media Manager"),
                ("Urmi Ghosh", "Social Media Manager"),
                ("Anurag Thakur", "Marketing Head"),
                ("Archan Nath", "Marketing Head"),
            ]
        )


# ============================================================
# R&D CELL
# ============================================================

with tab4:

    st.markdown(textwrap.dedent(
        """
        <div class="rd-banner">
            <h3>🔬 Research & Development Cell</h3>

            <p>
                The R&D Cell is focused on cultivating a research-oriented
                culture, encouraging interdisciplinary technical work and
                creating opportunities for students to explore emerging
                technologies in petroleum and energy engineering.
            </p>

            <span class="rd-chip">Research</span>
            <span class="rd-chip">Innovation</span>
            <span class="rd-chip">Technical Projects</span>
            <span class="rd-chip">Interdisciplinary Work</span>
        </div>
        """
    ), unsafe_allow_html=True)

    rd1, rd2 = st.columns(2, gap="large")

    with rd1:

        member_section(
            "Advisory Board",
            [
                ("Dr. Borkha Mech", "Director"),
                ("Dr. Deepjyoti Mech", "Director"),
            ]
        )

    with rd2:

        member_section(
            "R&D Core Team",
            [
                ("Abhishek Dutta", "Chief Coordinator"),
                ("Arnavraj Baruah", "Technical Lead"),
                ("Roshan Kar", "Technical Lead"),
                ("Nirveek Goswami", "Finance Manager"),
                ("Akashnil Borah", "Finance Manager"),
            ]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    section_header(
        "🚀",
        "R&D Vision",
        "Turning student ideas into structured technical initiatives."
    )

    v1, v2, v3 = st.columns(3)

    with v1:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.7rem;">🧠</div>
                <div class="info-card-title">Research Culture</div>
                <div class="info-card-text">
                    Encourage students to identify engineering problems,
                    conduct literature reviews and develop technically
                    sound solutions.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)

    with v2:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.7rem;">⚙️</div>
                <div class="info-card-title">Technical Projects</div>
                <div class="info-card-text">
                    Promote simulation, experimentation, data analysis
                    and prototype development across petroleum and
                    energy disciplines.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)

    with v3:
        st.markdown(textwrap.dedent(
            """
            <div class="info-card">
                <div style="font-size:1.7rem;">🏆</div>
                <div class="info-card-title">Research Outcomes</div>
                <div class="info-card-text">
                    Transform promising student projects into papers,
                    patents, competitions and industry-relevant solutions.
                </div>
            </div>
            """
        ), unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown(textwrap.dedent(
    """
    <div class="footer">
        <strong>FIPI Dibrugarh University Student Chapter</strong>
        <br>
        Session 2026–27 · Dibrugarh University
        <br><br>
        Petroleum Engineering • Research • Industry • Innovation
    </div>
    """
), unsafe_allow_html=True)
