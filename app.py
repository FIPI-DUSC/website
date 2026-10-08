import streamlit as st
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="FIPI DUSC 2026-27", layout="wide", page_icon="🛢️")

# --- SAFE IMAGE STYLING ---
# This ensures images don't stretch and look out of proportion
st.markdown("""
<style>
img {
    border-radius: 8px;
    max-height: 450px;
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

# --- IMAGE LOADER ---
def load_image(image_path, caption_text=""):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption_text)

# --- HEADER ---
st.title("FIPI Dibrugarh University Student Chapter")
st.subheader("Session 2026-27")
st.divider()

# --- CREATE 4 TABS (R&D Cell Restored) ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📅 Chapter Activities", "👥 Core Committee", "🔬 R&D Cell"])

# --- HOME TAB ---
with tab1:
    st.header("Welcome to FIPI DUSC")
    st.write("Bridging the gap between academia and the energy industry through technical excellence, innovation, and community outreach.")

# --- ACTIVITIES TAB ---
with tab2:
    st.header("Annual Activities & Evaluation")
    
    st.subheader("🎓 Academic Excellence")
    st.write("**IADC Well-Sharp University Examination:** The chapter proudly recognized members who successfully cleared the certification for the 2026–27 session, reflecting technical competence in well control principles. Achievers include Nirveek Goswami (86%), Abhishek Dutta (86%), Pratiksha Sonowal (85%), Aditi Gogoi (78%), Gargi Lahkar (75%), Arnavraj Baruah (74%), and Ipsita Deka (74%).")
    st.write("**Placement Achievement:** Two members, Abhishek Dutta (Finance Officer) and Arnavraj Baruah (HR Officer), were successfully recruited by Oil India Limited (OIL).")
    st.write("**FIPI DU SC x PETROGATE ACADEMY:** Organized the 'ALL-INDIA LEVEL UNLOCKING PE EXAM' free scholarship test on I see exactly what happened, and I apologize. I tried to get too fancy with the design by putting the committee members into drop-down menus (which hid their names) and adding custom styling that clashed. I also completely missed putting the R&D Cell back in! 

Let's strip away the overly complicated design and return to a clean, native Streamlit layout where absolutely everything is immediately visible on the screen. 

Here is the fully corrected code.

### How to fix it immediately:
1. Go back to your `app.py` file on GitHub and click the pencil icon to edit.
2. Delete everything in the file.
3. Paste the corrected code below.
4. Click **Commit changes**. (Streamlit will refresh automatically in about 30 seconds).

```python
import streamlit as st
import os

# --- SAFE IMAGE LOADER ---
def load_image(image_path, caption_text):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption_text, use_container_width=True)
    else:
        st.info(f"📷 Image pending: Upload `{image_path}` to GitHub.")

# --- PAGE SETUP ---
st.set_page_config(page_title="FIPI DUSC 2026-27", layout="wide", page_icon="🛢️")

st.title("FIPI Dibrugarh University Student Chapter")
st.subheader("Session 2026-27")
st.divider()

# --- CREATE TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📅 Chapter Activities", "👥 Core Committee", "🔬 R&D Cell"])

# --- HOME TAB ---
with tab1:
    st.header("Welcome to FIPI DUSC")
    st.write("Bridging the gap between academia and the energy industry through technical excellence, innovation, and community outreach.")
    st.info("💡 **Admin Note:** To update this text or add new events, edit the `app
