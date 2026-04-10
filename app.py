import streamlit as st
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# =========================
# 🔑 LOAD API KEY
# =========================
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# =========================
# 📚 LOAD KNOWLEDGE BASE
# =========================
try:
    with open("sgbv.txt", "r", encoding="utf-8") as f:
        knowledge = f.read()
except:
    knowledge = "SGBV is abuse based on gender."

# =========================
# 🎯 SYSTEM PROMPT
# =========================
system_prompt = f"""
You are a professional SGBV chatbot.

- Be calm and supportive
- Do not blame users
- Give clear answers
- Guide users to PHC

Knowledge:
{knowledge}
"""

# =========================
# 🎨 PAGE SETUP
# =========================
st.set_page_config(page_title="SGBV Support System", layout="wide")

# =========================
# 🌄 BACKGROUND FUNCTION
# =========================
def set_bg(image):
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# =========================
# 🌙 DARK MODE DEFAULT
# =========================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

def set_theme():
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        .stApp { color: white; }
        .stButton>button { background-color: #262730; color: white; border-radius: 10px; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp { color: black; }
        .stButton>button { background-color: white; color: black; border-radius: 10px; }
        </style>
        """, unsafe_allow_html=True)

set_theme()

mode = "☀️ Light Mode" if st.session_state.dark_mode else "🌙 Dark Mode"

# =========================
# 📂 SIDEBAR
# =========================
with st.sidebar:
    try:
        st.image("assets/logo.png", width=100)
    except:
        pass

    st.title("SGBV Support")
    st.caption("Powered by Atlas Initiative")

    if st.button(mode):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.markdown("---")

    if st.button("🏠 Home"):
        st.session_state.page = "home"
        st.rerun()

    if st.button("🤖 Chatbot"):
        st.session_state.page = "chatbot"
        st.rerun()

    if st.button("📘 Rights"):
        st.session_state.page = "rights"
        st.rerun()

    if st.button("🚨 Emergency"):
        st.session_state.page = "emergency"
        st.rerun()

    if st.button("📍 Help"):
        st.session_state.page = "help"
        st.rerun()

    if st.button("🎓 Training"):
        st.session_state.page = "training"
        st.rerun()
        
st.markdown("---")
st.markdown("### 👨‍💻 Developer")
st.markdown("**Raywise Creativity**")
st.markdown("[Visit Website](https://raywisecreativity.netlify.app/)")
# =========================
# PAGE STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================
# 🏠 HOME PAGE (WITH IMAGES)
# =========================
if st.session_state.page == "home":
    set_bg("assets/bg_home.jpg")

    st.markdown("## 🧭 Choose a Service")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/chatbot.png", use_container_width=True)
        if st.button("🤖 Open Chatbot", use_container_width=True):
            st.session_state.page = "chatbot"
            st.rerun()

        st.image("assets/rights.png", use_container_width=True)
        if st.button("📘 Know Your Rights", use_container_width=True):
            st.session_state.page = "rights"
            st.rerun()

        st.image("assets/emergency.png", use_container_width=True)
        if st.button("🚨 Emergency", use_container_width=True):
            st.session_state.page = "emergency"
            st.rerun()

    with col2:
        st.image("assets/help.png", use_container_width=True)
        if st.button("📍 Find Help", use_container_width=True):
            st.session_state.page = "help"
            st.rerun()

        st.image("assets/training.png", use_container_width=True)
        if st.button("🎓 Training", use_container_width=True):
            st.session_state.page = "training"
            st.rerun()

# =========================
# 💬 CHATBOT PAGE
# =========================
elif st.session_state.page == "chatbot":
    set_bg("assets/bg_chat.jpg")

    try:
        st.image("assets/chatbot_banner.png", use_container_width=True)
    except:
        pass

    st.markdown("## 💬 SGBV Support Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello 👋, I’m here to support you."}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your question...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""

            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                )

                reply = response.choices[0].message.content

                # 🔥 Smooth typing (character-based)
                for i in range(len(reply)):
                    full_response = reply[:i+1]
                    placeholder.markdown(full_response + "▌")
                    time.sleep(0.005)

                placeholder.markdown(full_response)

            except Exception as e:
                full_response = f"⚠️ Error: {e}"
                placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

import streamlit as st

# Helper for background
def set_bg(url):
    # Fixed: Use unsafe_allow_html=True instead of unsafe_content_as_template [cite: 58, 60]
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"

# =========================
# 📘 RIGHTS PAGE
# =========================
if st.session_state.page == "rights":
    set_bg("assets/bg_rights.png")  # Updated to .png
    st.title("📘 Know Your Rights")
    st.subheader("The VAPP Act (2015) & Your Protection")
    
    st.markdown("""
    Under Nigerian law, specifically the **Violence Against Persons (Prohibition) Act**:
    * **Broad Definition of Violence:** Violence includes physical, sexual, emotional, psychological, and economic harm. 
    * **Marital Rights:** Consent is required in all sexual relations; marital rape is explicitly a crime. 
    * **Gender Equality:** Both women and men can be survivors under the law. 
    * **Prohibited Practices:** Female Genital Mutilation (FGM) and forceful ejection from home are illegal. 
    * **Survivor Rights:** You have a legal right to medical care, protection, and legal remedies.
    """)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# =========================
# 🚨 EMERGENCY
# =========================
elif st.session_state.page == "emergency":
    set_bg("assets/bg_emergency.png")  # Updated to .png
    st.title("🚨 Emergency Contacts")
    
    st.markdown("### **Immediate Response (Lagos & Ogun)**")
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("**Lagos State (DSVA)**")
        st.write("📞 **08000 333 333** (Toll-Free)")
    
    with col2:
        st.error("**National & Ogun**")
        st.write("📞 **112 / 767** (General Emergency)")
        st.write("📞 **0800 72 73 2255** (National SGBV Line)")

    st.warning("**Safety Tip:** If sexual assault has occurred, visit a SARC or PHC immediately to preserve evidence. ")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# =========================
# 📍 FIND HELP
# =========================
elif st.session_state.page == "help":
    set_bg("assets/bg_help.png")  # Updated to .png
    st.title("📍 Find Support Services")
    
    st.markdown("""
    ### **Where to Go**
    * **Primary Health Centres (PHCs):** These are the primary gateways for health and psychosocial referrals. 
    * **Sexual Assault Referral Centres (SARC):** Specialized centers for clinical and forensic support. 
    * **Champions:** Trusted community members who connect survivors to formal support systems. 
    * **ELITE Project:** Provides assistance in urban and peri-urban informal settlements.
    """)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# =========================
# 🎓 TRAINING
# =========================
elif st.session_state.page == "training":
    set_bg("assets/bg_training.png")
    st.title("🎓 SGBV Training")
    
    st.markdown("""
    ### **What is SGBV ?**
    SGBV stands for Sexual and Gender-Based Violence. it is defined as any harmful act perpetrated against a person’s will that is rooted in socially constructed gender roles, power differences, and inequality.
    
    **Your Core Competencies:**
    * **Psychological First Aid:** Active listening and providing emotional support. 
    * **Safe Disclosures:** Managing the safe receipt of trauma disclosures. 
    * **Referral Navigation:** Connecting survivors to PHC-centered pathways. 
    * **Confidentiality:** Protecting survivor privacy and autonomy. 

    **Important Boundaries:**
    * ❌ **NOT investigators** who gather evidence. 
    * ❌ **NOT counsellors** who provide therapy. 
    * ❌ **NOT mediators** who resolve disputes. 
    """)

    st.divider()
    st.subheader("📝 Training Scenarios")
    st.info("Use these local context examples to practice identifying SGBV in the community.")

    # Organizing scenarios into expanders for better UI
    with st.expander("Sexual Violence Scenarios"):
        st.write("""
        * **Rape:** Forced sex by a husband (marital rape) or assault by a neighbor.
        * **Exploitation:** A landlord demanding sex for rent or a teacher for grades.
        * **Harassment:** Unwanted touching in markets or on buses.
        * **Tech-Abuse:** Sharing private images or online harassment.
        """)

    with st.expander("Physical Violence Scenarios"):
        st.write("""
        * **Domestic Aggression:** Beating a wife for coming home late.
        * **High-Risk Indicators:** Choking or strangulation (strong predictor of lethal violence).
        * **Weapons:** Use of belts, sticks, cutlasses, or bottles.
        * **Confinement:** Locking someone in a room or tying them up.
        """)

    with st.expander("Emotional & Economic Scenarios"):
        st.write("""
        * **Emotional:** Constant insults, gaslighting, or preventing contact with family.
        * **Economic:** Taking a partner's earnings or destroying their business stock.
        * **Denial:** Refusing money for food or rent as a form of punishment.
        """)

    with st.expander("Harmful Traditional Practices"):
        st.write("""
        * **Marriage:** Forced marriage of girls under 18 or as a debt settlement.
        * **Widowhood:** Forcing a widow to shave her head or marry a relative.
        * **Other:** Female Genital Mutilation (FGM) and breast ironing.
        """)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()
# =========================
# 💬 WHATSAPP FLOAT BUTTON
# =========================
st.markdown("""
<a href="https://wa.me/2348086815767" target="_blank">
<img src="https://img.icons8.com/color/70/000000/whatsapp--v1.png"
style="position:fixed;bottom:20px;right:20px;"/>
</a>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px;'>
        Developed by <b>Raywise Creativity</b> 🚀 <br>
        🌐 <a href="https://raywisecreativity.netlify.app/" target="_blank">
        https://raywisecreativity.netlify.app/
        </a>
    </div>
    """,
    unsafe_allow_html=True
)