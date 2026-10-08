import streamlit as st
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="FIPI DUSC 2026-27", layout="wide", page_icon="🛢️")

# --- UI UPGRADES (CSS INJECTION) ---
st.markdown("""
<style>
/* Soft background color for the whole site */
.stApp {
    background-color: #f8fafc;
}
/* Deep blue headers */
h1, h2, h3 {
    color: #1e3a8a !important;
}
/* Fix image proportions, add rounded corners and shadows */
img {
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    max-height: 400px; /* Prevents images from getting too tall */
    object-fit: cover; /* Prevents stretching */
}
/* Make the tabs look like clean, elevated cards */
.stTabs [data-baseweb="tab-list"] {
    background-color: white;
    padding: 10px 20px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    gap: 20px;
}
/* Style the info boxes */
.stAlert {
    border-radius: 10px;
    border-left: 5px solid #f97316; /* Orange accent */
}
</style>
""", unsafe_allow_html=True)

# --- SAFE IMAGE LOADER ---
def load_image(image_path, caption_text):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption_text, use_container_width=True)
    else:
        st.info(f"📷 Image pending: Upload `{image_path}` to GitHub.")

# --- HEADER ---
st.title("FIPI Dibrugarh University Student Chapter")
st.subheader("Session 2026-27")
st.divider()

# --- CREATE TABS ---
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📅 Chapter Activities", "👥 Core Committee"])

# --- HOME TAB ---
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Welcome to FIPI DUSC")
        st.write("Bridging the gap between academia and the energy industry through technical excellence, innovation, and community outreach.")
        st.info("💡 **Admin Note:** To update this text or add new events, edit the `app.py` file on GitHub.")

# --- ACTIVITIES TAB ---
with tab2:
    st.header("Annual Activities & Evaluation")
    
    st.subheader("🎓 Academic Excellence")
    col_acad_text, col_acad_img = st.columns([3, 2])
    with col_acad_text:
        st.write("**IADC Well-Sharp University Examination:** The chapter proudly recognized members who successfully cleared the certification for the 2026–27 session, reflecting technical competence in well control principles. Achievers include Nirveek Goswami (86%), Abhishek Dutta (86%), Pratiksha Sonowal (85%), Aditi Gogoi (78%), Gargi Lahkar (75%), Arnavraj Baruah (74%), and Ipsita Deka (74%).")
        st.write("**Placement Achievement:** Two members, Abhishek Dutta (Finance Officer) and Arnavraj Baruah (HR Officer), were successfully recruited by Oil India Limited (OIL).")
        st.write("**FIPI DU SC x PETROGATE ACADEMY:** Organized the 'ALL-INDIA LEVEL UNLOCKING PE EXAM' free scholarship test on 8th August 2026 for GATE & ONGC PE aspirants.")
    with col_acad_img:
        load_image("images/petrogate.jpg", "Petrogate Academy Scholarship Test")
    st.divider()

    st.subheader("⚙️ Technical Excellence")
    col_tech_text, col_tech_img = st.columns([3, 2])
    with col_tech_text:
        st.write("**Patent Published:** 'A PROCESS FOR REMEDIATION OF CRUDE-OIL CONTAMINATED WATER USING A PLANT-BASED ADSORBENT DERIVED FROM WATER HYACINTH (Eichhornia crassipes)'. Inventors: Ipsita Deka, Isfaqul Alam, Junayed Khan, Kasturi Bonia, Dr. Chayanika Borah, and Joyshree Barman.")
        st.write("**Geonova Competition:** Rock and Mineral Identification Competition ('Geonova') organized as part of Geology Week to enhance practical geological knowledge.")
    with col_tech_img:
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            load_image("images/patent.jpg", "Patent Publication")
        with col_t2:
            load_image("images/geonova.jpg", "Geonova Competition")
    st.divider()

    st.subheader("🏭 Industry Orientation")
    col_ind_text, col_ind_img = st.columns([3, 2])
    with col_ind_text:
        st.write("**Industrial Visit to OIL, Duliajan:** 4th-semester B.Tech students visited the Water Supply Station (WSS) and Air Liquefaction Plant (ALP) on 7th May 2026.")
        st.write("**Well Logging Department Visit:** 2nd-semester M.Tech students undertook a one-day visit to the Well Logging Department of OIL on 28th April 2026 under Project SHARE, interacting with officials across Cased Hole, Open Hole, and Interpretation Sections.")
    with col_ind_img:
        load_image("images/oil_visit.jpg", "Industrial Visit to OIL India Limited")
    st.divider()

    st.subheader("🤝 Social Activities: Impact and Outreach")
    st.write("Community engagement and green initiatives driven by our chapter members.")
    
    # Using a 4-column grid for social activity photos so they stay compact
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        load_image("images/prerona.jpg", "Visit to Prerona Children's Home")
    with col_s2:
        load_image("images/cleanliness.jpg", "Code Green Cleanliness Drive")
    with col_s3:
        load_image("images/membership.jpg", "Membership Drive")
    with col_s4:
        load_image("images/plantation.jpg", "Plantation Drive")
    st.divider()

    col_pending1, col_pending2 = st.columns(2)
    with col_pending1:
        st.subheader("💡 Innovations")
        st.write("*Status: To be updated.*")
    with col_pending2:
        st.subheader("📊 Presentation Quality")
        st.write("*Status: To be updated.*")

# --- CORE COMMITTEE TAB ---
with tab3:
    st.header("Core Committee 2026-27")
    
    # Using st.expander creates clean drop-down menus instead of an endless wall of text
    with st.expander("🎓 Advisory Board", expanded=True):
        st.write("- Dr. Deepjyoti Mech (Asst. Faculty Advisor)\n- Dr. Borkha Mech (Chief Faculty Advisor)\n- Dr. Himanta Borgohain (Asst. Faculty Advisor)")
        
    with st.expander("⭐ Executive Leadership", expanded=True):
        st.write("- Nirveek Goswami (Secretary)\n- Gargi Lahkar (President)\n- Nabarun Chakraborty (Vice-President)")
        
    with st.expander("💼 Finance & Management"):
        st.write("- Sparshan Bharadwaj (General Manager)\n- Abhishek Dutta (Finance Officer)\n- Hirok Jyoti Dutta (Chief Operational Officer)\n- Mridupawan Shandilya (General Manager)\n- Twinkle Bhuyan (Finance Officer)")
        
    with st.expander("🗂️ HR & Records"):
        st.write("- Arnavraj Baruah (HR Officer)\n- Akashnil Borah (HR Officer)\n- Aditi Gogoi (Documentation Chief)\n- Spriha Hazarika (Documentation Head)\n- Bhargavjyoti Gogoi (Documentation Head)\n- Preeyam Choudhary (Documentation Head)\n- Abhinav Parasar (Documentation Head)")

    with st.expander("🎨 Creative & Outreach"):
        st.write("- Ipsita Deka (Designing Chief)\n- Nibirh Hazarika (Designing Chief)\n- Biswajit Rajkhowa (Designing Head)\n- Tusti Chetia (Designing Head)\n- Jayed Hazarika (Membership Head)\n- Abhraneil Boruah (Membership Head)")
        
    with st.expander("⚙️ Industry, Tech & Culture"):
        st.write("- Pratiksha Sonowal (Industrial & Communication Chairperson)\n- Roshan Kar (Industrial & Communication Chairperson)\n- Pankita Priyam Sarma (Industrial & Communication Chairperson)\n- Arindom Gogoi (Technical Head)\n- Shubharaj Sonowal (Technical Head)\n- Devleena Kalita (Cultural Head)\n- Manash Pratim Phukan (Cultural Head)")
        
    with st.expander("📸 Events, Media & Promotions"):
        st.write("- Anisha Rahman (Event Management Head)\n- Debashish Sharma (Event Management Head)\n- Trishna Pegu (Social Media Manager)\n- Urmi Ghosh (Social Media Manager)\n- Anurag Thakur (Marketing Head)\n- Archan Nath (Marketing Head)")
