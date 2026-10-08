import streamlit as st
import os

# --- SAFE IMAGE LOADER ---
# Prevents the website from crashing if an image isn't uploaded yet
def load_image(image_path, caption_text):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption_text, use_container_width=True)
    else:
        st.info(f"📷 Image pending: Please upload `{image_path}` to the GitHub images folder.")

# --- PAGE SETUP ---
st.set_page_config(page_title="FIPI DUSC 2026-27", layout="wide")

st.title("FIPI Dibrugarh University Student Chapter")
st.subheader("Session 2026-27")
st.divider()

# --- CREATE TABS ---
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📅 Chapter Activities", "👥 Core Committee"])

# --- HOME TAB ---
with tab1:
    st.header("Welcome to FIPI DUSC")
    st.write("Bridging the gap between academia and the energy industry through technical excellence, innovation, and community outreach.")
    st.info("💡 **Admin Note:** To update this text or add new events, edit the `app.py` file on GitHub.")

# --- ACTIVITIES TAB ---
with tab2:
    st.header("Annual Activities & Evaluation")
    
    st.subheader("🎓 Academic Excellence")
    st.write("**IADC Well-Sharp University Examination:** The chapter proudly recognized members who successfully cleared the certification for the 2026–27 session, reflecting technical competence in well control principles. Achievers include Nirveek Goswami (86%), Abhishek Dutta (86%), Pratiksha Sonowal (85%), Aditi Gogoi (78%), Gargi Lahkar (75%), Arnavraj Baruah (74%), and Ipsita Deka (74%).")
    st.write("**Placement Achievement:** Two members, Abhishek Dutta (Finance Officer) and Arnavraj Baruah (HR Officer), were successfully recruited by Oil India Limited (OIL).")
    st.write("**FIPI DU SC x PETROGATE ACADEMY:** Organized the 'ALL-INDIA LEVEL UNLOCKING PE EXAM' free scholarship test on 8th August 2026 for GATE & ONGC PE aspirants.")
    load_image("images/petrogate.jpg", "Petrogate Academy Scholarship Test Poster")
    st.divider()

    st.subheader("💡 Innovations")
    st.write("Innovative works by the members. New ideas. New ideas for solving old problems. Student-led new initiatives etc.")
    st.write("*Status: To be updated.*")
    st.divider()

    st.subheader("⚙️ Technical Excellence")
    st.write("**Patent Published:** 'A PROCESS FOR REMEDIATION OF CRUDE-OIL CONTAMINATED WATER USING A PLANT-BASED ADSORBENT DERIVED FROM WATER HYACINTH (Eichhornia crassipes)'. Inventors: Ipsita Deka, Isfaqul Alam, Junayed Khan, Kasturi Bonia, Dr. Chayanika Borah, and Joyshree Barman.")
    load_image("images/patent.jpg", "Official Journal of The Patent Office Publication")
    
    st.write("**Geonova Competition:** Rock and Mineral Identification Competition ('Geonova') organized as part of Geology Week to enhance practical geological knowledge.")
    load_image("images/geonova.jpg", "Glimpses of Strata-Quest under Geonova")
    st.divider()

    st.subheader("🏭 Industry Orientation")
    st.write("**Industrial Visit to OIL, Duliajan:** 4th-semester B.Tech students visited the Water Supply Station (WSS) and Air Liquefaction Plant (ALP) on 7th May 2026.")
    st.write("**Well Logging Department Visit:** 2nd-semester M.Tech students undertook a one-day visit to the Well Logging Department of OIL on 28th April 2026 under Project SHARE, interacting with officials across Cased Hole, Open Hole, and Interpretation Sections.")
    load_image("images/oil_visit.jpg", "Industrial Visit to Well Logging Department, OIL India Limited")
    st.divider()

    st.subheader("🤝 Social Activities: Impact and Outreach")
    
    col_soc1, col_soc2 = st.columns(2)
    with col_soc1:
        st.write("**Visit to Prerona Children’s Home:** A pre-event of FIPI Energy Week 2026 (27th September 2026). The team spent time with the children and distributed food items and stationery.")
        load_image("images/prerona.jpg", "Visit to Prerona Children's Home")
        
        st.write("**Cleanliness Drive:** 'Code Green' drive conducted during Geology Week.")
        load_image("images/cleanliness.jpg", "Code Green Cleanliness Drive")

    with col_soc2:
        st.write("**Membership Drive:** Conducted at the Department of Geography on 25th September 2026 to brief students about FIPI's vision and Energy Week.")
        load_image("images/membership.jpg", "Membership Drive at Department of Geography")
        
        st.write("**Plantation Drive:** Organized on World Environment Day (5th June 2026) to promote green campus initiatives.")
        load_image("images/plantation.jpg", "World Environment Day Plantation Drive")
    st.divider()

    st.subheader("📊 Presentation Quality")
    st.write("Making structured presentation. Presenting within time limit, with good articulation, and effectively answering the questions of Jury.")
    st.write("*Status: To be updated.*")

# --- CORE COMMITTEE TAB ---
with tab3:
    st.header("Core Committee 2026-27")
    
    col_comm1, col_comm2 = st.columns(2)
    
    with col_comm1:
        st.write("### Advisory Board")
        st.write("- Dr. Deepjyoti Mech (Asst. Faculty Advisor)\n- Dr. Borkha Mech (Chief Faculty Advisor)\n- Dr. Himanta Borgohain (Asst. Faculty Advisor)")
        
        st.write("### Executive Leadership")
        st.write("- Nirveek Goswami (Secretary)\n- Gargi Lahkar (President)\n- Nabarun Chakraborty (Vice-President)")
        
        st.write("### Finance & Management")
        st.write("- Sparshan Bharadwaj (General Manager)\n- Abhishek Dutta (Finance Officer)\n- Hirok Jyoti Dutta (Chief Operational Officer)\n- Mridupawan Shandilya (General Manager)\n- Twinkle Bhuyan (Finance Officer)")
        
        st.write("### HR & Records")
        st.write("- Arnavraj Baruah (HR Officer)\n- Akashnil Borah (HR Officer)\n- Aditi Gogoi (Documentation Chief)\n- Spriha Hazarika (Documentation Head)\n- Bhargavjyoti Gogoi (Documentation Head)\n- Preeyam Choudhary (Documentation Head)\n- Abhinav Parasar (Documentation Head)")

    with col_comm2:
        st.write("### Creative & Outreach")
        st.write("- Ipsita Deka (Designing Chief)\n- Nibirh Hazarika (Designing Chief)\n- Biswajit Rajkhowa (Designing Head)\n- Tusti Chetia (Designing Head)\n- Jayed Hazarika (Membership Head)\n- Abhraneil Boruah (Membership Head)")
        
        st.write("### Industry, Tech & Culture")
        st.write("- Pratiksha Sonowal (Industrial & Communication Chairperson)\n- Roshan Kar (Industrial & Communication Chairperson)\n- Pankita Priyam Sarma (Industrial & Communication Chairperson)\n- Arindom Gogoi (Technical Head)\n- Shubharaj Sonowal (Technical Head)\n- Devleena Kalita (Cultural Head)\n- Manash Pratim Phukan (Cultural Head)")
        
        st.write("### Events, Media & Promotions")
        st.write("- Anisha Rahman (Event Management Head)\n- Debashish Sharma (Event Management Head)\n- Trishna Pegu (Social Media Manager)\n- Urmi Ghosh (Social Media Manager)\n- Anurag Thakur (Marketing Head)\n- Archan Nath (Marketing Head)")
