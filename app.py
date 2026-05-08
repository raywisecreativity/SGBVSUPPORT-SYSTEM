
import streamlit as st
import time
import os
import base64 

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="700px">
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

from dotenv import load_dotenv
from openai import OpenAI

# =========================
# SESSION STATE INIT (FIXED)
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "messages" not in st.session_state:
    st.session_state.messages = []
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
# 🎨 THEME (FULL CONTROL)
# =========================
def set_theme():
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        .stApp {background-color:#0E1117;color:white;}
        section[data-testid="stSidebar"] {background-color:#161A23;}
        .stButton>button {
            background:#262730;color:white;border-radius:10px;border:none;
        }
        </style>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <style>
        /* MAIN APP */
        .stApp {
            background-color:#F5F7FA;
            color:black;
        }

        /* ✅ SIDEBAR BACKGROUND */
        section[data-testid="stSidebar"] {
            background-color:#FFFFFF !important;
        }

        /* ✅ FORCE ALL SIDEBAR TEXT TO BLACK */
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] div {
            color: black !important;
        }

        /* ✅ BUTTON TEXT */
        section[data-testid="stSidebar"] .stButton>button {
            color: black !important;
        }

        /* ✅ CHAT TEXT */
        .stChatMessage p {
            color: black !important;
        }

        /* ✅ CHAT INPUT */
        textarea {
            color: black !important;
            background-color: white !important;
        }

        /* NORMAL BUTTONS */
        .stButton>button {
            background:white;
            color:black;
            border-radius:10px;
            border:1px solid #ccc;
        }
        
        /* DOWNLOAD BUTTON FIX */
.stDownloadButton>button {
    background-color: #E3F2FD !important;  /* light blue */
    color: black !important;
    border-radius: 10px;
    border: 1px solid #ccc;
}
        </style>
        """, unsafe_allow_html=True)


set_theme()
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

    # ✅ FIXED DARK MODE BUTTON (PUT HERE)
    if st.button("🌙 Toggle Dark Mode"):
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
# =========================
# 🏠 HOME PAGE (PROFESSIONAL GRID)
# =========================
if st.session_state.page == "home":
    set_bg("assets/bg_home.jpg")

    st.markdown("## 🧭 Choose a Service")

    # =========================
    # CUSTOM CARD CSS
    # =========================
    st.markdown("""
    <style>
    .service-card {
        background: rgba(255,255,255,0.08);
        padding: 10px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 15px;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .service-card img {
        width: 100%;
        height: 140px;
        object-fit: cover;
        border-radius: 12px;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }

    /* MOBILE RESPONSIVE */
    @media (max-width: 768px) {
        .service-card {
            height: 220px;
        }

        .service-card img {
            height: 120px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # 3 COLUMNS
    # =========================
    col1, col2, col3 = st.columns(3)

    # =========================
    # COLUMN 1
    # =========================
    with col1:

        st.markdown("""
        <div class="service-card">
            <img src="data:image/png;base64,{}">
        </div>
        """.format(
            base64.b64encode(open("assets/chatbot_banner.png", "rb").read()).decode()
        ), unsafe_allow_html=True)

        if st.button("🤖 Chatbot", key="chatbot"):
            st.session_state.page = "chatbot"
            st.rerun()

        st.markdown("""
        <div class="service-card">
            <img src="data:image/png;base64,{}">
        </div>
        """.format(
            base64.b64encode(open("assets/help.jpg", "rb").read()).decode()
        ), unsafe_allow_html=True)

        if st.button("📍 Help", key="help"):
            st.session_state.page = "help"
            st.rerun()

    # =========================
    # COLUMN 2
    # =========================
    with col2:

        st.markdown("""
        <div class="service-card">
            <img src="data:image/png;base64,{}">
        </div>
        """.format(
            base64.b64encode(open("assets/right.jpg", "rb").read()).decode()
        ), unsafe_allow_html=True)

        if st.button("📘 Rights", key="rights"):
            st.session_state.page = "rights"
            st.rerun()

        st.markdown("""
        <div class="service-card">
            <img src="data:image/png;base64,{}">
        </div>
        """.format(
            base64.b64encode(open("assets/training.jpg", "rb").read()).decode()
        ), unsafe_allow_html=True)

        if st.button("🎓 Training", key="training"):
            st.session_state.page = "training"
            st.rerun()

    # =========================
    # COLUMN 3
    # =========================
    with col3:

        st.markdown("""
        <div class="service-card">
            <img src="data:image/png;base64,{}">
        </div>
        """.format(
            base64.b64encode(open("assets/emergency.jpg", "rb").read()).decode()
        ), unsafe_allow_html=True)

        if st.button("🚨 Emergency", key="emergency"):
            st.session_state.page = "emergency"
            st.rerun()
        
        
        
        
        
            # CHATBOT SESSION

elif st.session_state.page == "chatbot":
    set_bg("assets/bg_chat.jpg")

    st.title("💬 SGBV Support Chat")

    # ✅ Banner fix
    try:
        st.image("assets/chatbot_banner.png", use_container_width=True)
    except:
        st.warning("⚠️ Chatbot banner not found")

    # ✅ Ensure first message
    if len(st.session_state.messages) == 0:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Hello 👋, I’m here to support you with any questions."
        })

    # Display messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input
    user_input = st.chat_input("Type your question...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )

            reply = response.choices[0].message.content

            for i in range(len(reply)):
                full_response = reply[:i+1]
                placeholder.markdown(full_response + "▌")
                time.sleep(0.005)

            placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()



# # Helper for background
# def set_bg(url):
#     # Fixed: Use unsafe_allow_html=True instead of unsafe_content_as_template [cite: 58, 60]
#     st.markdown(f"""
#     <style>
#     .stApp {{
#         background-image: url("{url}");
#         background-size: cover;
#         background-position: center;
#     }}
#     </style>
#     """, unsafe_allow_html=True)

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

 # ✅ DOWNLOAD BUTTON
    with open("assets/Violence-Against-Persons-Prohibition-Act-2015-1.pdf", "rb") as file:
        st.download_button(
            "📥 Download Violence-Against-Persons-Prohibition-Act-2015-1.pdf",
            file,
            file_name="Violence-Against-Persons-Prohibition-Act-2015-1.pdf"
        )
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# =========================
# 🚨 EMERGENCY PAGE
# =========================
elif st.session_state.page == "emergency":
    set_bg("assets/bg_emergency.png")
    st.title("🚨 Emergency Contacts")

    # =========================
    # Lagos DSVA
    # =========================
    st.markdown("## 🛑 Lagos State SGBV Support")

    st.info("""
Lagos State has a well-established Domestic and Sexual Violence Agency (DSVA) that provides 24/7 support, rescue, and referral services for survivors of abuse and violence.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.error("Lagos State DSVA Toll-Free Line")
        st.write("📞 0-8000-333-333 (24/7)")

    with col2:
        st.error("National Emergency Lines")
        st.write("📞 112")
        st.write("📞 767")
        st.write("📞 0800 7273 2255")

    st.success("Always report to the nearest PHC, SARC, or hospital immediately after any incident.")

    # =========================
    # Lagos SARC Centres
    # =========================
    st.markdown("""
### ATLAS Initiative
📍 Block 4 Suru Ibeshe Garden Estate, Owode-Ibeshe,Ikorodu.Lagos
 
📞 +2348078072911

📧  safeguard@atlas.org.ng , atlasinitiativenigeria@gmail.com

---
### Mirabel Centre (SARC)
📍 Lagos State University Teaching Hospital (LASUTH), Ikeja  
📞 0815 577 0000 | 0818 724 3468 | 0701 349 1769  

---

### Idera Centre (SARC)
📍 Alimosho General Hospital, Igando  
📞 0815 047 3831 | 0905 589 1612  

---

### WARIF Centre (SARC)
📍 Yaba, Lagos  
📞 Toll-Free: 0800 921 00009  
📞 Helpline: 0809 210 0009  

---

### Community Women's Rights Foundation (CWRF)
📞 Helpline: 0809 210 0009
""")

    # =========================
    # Ogun State Support
    # =========================
    st.markdown("## 🌿 Ogun State SGBV Support")

    st.info("""
Ogun State has expanded Sexual Assault Referral Centres (SARCs) across major zones to support survivors of violence.
    """)

    st.write("📞 Ogun State GBV Toll-Free Lines:")
    st.write("0800 000 0666")
    st.write("0800 000 0555")

    st.markdown("""
## 🌿 Ogun State SARC Locations

Specialized Sexual Assault Referral Centres (SARCs) provide **medical, psychological, and legal support** for survivors.

---

### 🏥 Sagamu SARC
📍 Olabisi Onabanjo University Teaching Hospital (OOUTH), Sagamu  
📞 0800 0000 555  
💬 WhatsApp: 0807 129 0703  
📧 Email: ogsarc21@gmail.com  

---

### 🏥 Ilaro SARC
📍 Ilaro Safe Centre, Block 2–8, Oba Olugbenle Palace Way, Adjacent Recreation Club, Ilaro, Ogun State  
📞 0800 0000 077  
📧 Email: ilarosafecentre@gmail.com  

---

### 🏥 Ijebu-Ode SARC
📍 Ijebu-Ode Safe Centre, Igneba Road, Off Elebute, Ijebu-Ode, Ogun State  
📞 0800 0000 088  
📧 Email: ogunstatesarcijebuode@gmail.com  

---

### 🏥 Abeokuta SARC (Asero)
📍 Beside Juvenile Home, Asero Garage, Abeokuta  
📞 0800 0000 099  
📧 Email: sarcasero@gmail.com  

---
""")

    # =========================
    # National Support
    # =========================
    st.markdown("## 🇳🇬 National & Child Protection Support")

    st.write("📞 Federal GBV Helpline: 0800 72 73 2255")
    st.write("📞 Child Helpline (Cece Yara): 0800 800 8001")

    # =========================
    # Safety Warning
    # =========================
    st.warning("""
🚨 If you are in immediate danger:
Call 112 or go to the nearest hospital, PHC, or police station immediately.
""")
# =========================
# 📍 HELP
# =========================
elif st.session_state.page == "help":
    set_bg("assets/bg_help.png")
    st.title("📍 Find Help")

    st.markdown("## 📄 Help Documents")

    # ✅ DOCUMENT 1
    with open("assets/Primary Health Centers in Lagos State.docx", "rb") as file:
        st.download_button(
            label="📥 Download Primary Health Centers in Lagos State",
            data=file,
            file_name="Primary Health Centers in Lagos State.docx"
        )

    # ✅ DOCUMENT 2
    with open("assets/Primary Health Centers in Ogun State.docx", "rb") as file:
        st.download_button(
            label="📥 Download Primary Health Centers in Ogun State",
            data=file,
            file_name="Primary Health Centers in Ogun State.docx"
        )

    # ✅ STATE SELECT
    state = st.selectbox("Select State", ["Lagos", "Ogun"])

    # 🔥 ADD YOUR FULL LAGOS PHC LIST HERE
    lagos_phcs = [
  {"lga": "Alimosho LGA", "ward": "Alabata", "name": "Akowonjo PHC", "address": "100 Akowonjo Road, Vulganider B/S"},
  {"lga": "Alimosho LGA", "ward": "Oguntaade Bameke", "name": "Orisunbare PHC", "address": "20 Ejigbo Road, Orisunmibare, Shasha"},

  {"lga": "Agbado Oke Odo LCDA", "ward": "Agbado Okeodo", "name": "Oke Odo PHC", "address": "Ekoro Okeodo Road, Okeodo Abule Egba"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Ajasa/Amikanle", "name": "Surulere PHC", "address": "3 Faith Rescue by Command Secondary School"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Ajasa/Amikanle", "name": "Amikanle PHC", "address": "2/5 Fadipe Street, Agbado"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Ajasa/Amikanle", "name": "Ikola PHC", "address": "Ikola Street"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Abule Egba", "name": "Olota PHC", "address": "Olaloto Street, Abule Egba"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Aboru", "name": "Aboru PHC", "address": "Yisa Street, Babalola Bus Stop"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Aboru", "name": "Tinubu PHC", "address": "Along Agbelekale Road"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Aboru", "name": "Ogundimu PHC", "address": "22 Awotedu Street"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Alagbado/Alakuko", "name": "Agbado PHC", "address": "Old Ota Road"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Agbele", "name": "Agbele PHC", "address": "12 Manner Street"},
  {"lga": "Agbado Oke Odo LCDA", "ward": "Oki", "name": "Oki PHC", "address": "Iperun-Akisan Street, Old Ota Road"},

  {"lga": "Ayobo Ipaja LCDA", "ward": "Ipaja", "name": "Ipaja PHC", "address": "Ayobo Road, Igbo-Gbila Bus Stop"},
  {"lga": "Ayobo Ipaja LCDA", "ward": "Bada", "name": "Cele/Apata PHC", "address": "4 Bethel Street"},
  {"lga": "Ayobo Ipaja LCDA", "ward": "Baruwa", "name": "Baruwa PHC", "address": "Progressive Estate"},
  {"lga": "Ayobo Ipaja LCDA", "ward": "Ayobo", "name": "Ishefun PHC", "address": "Camp David Road"},
  {"lga": "Ayobo Ipaja LCDA", "ward": "Ayobo", "name": "Ayobo PHC", "address": "Anisere Durojaiye Street"},

  {"lga": "Egbe Idimu LCDA", "ward": "Isheri Olofin", "name": "Isheri Olofin PHC", "address": "LASU/Isheri Road"},
  {"lga": "Egbe Idimu LCDA", "ward": "Idimu", "name": "Helen Aderonke Memorial PHC", "address": "Beside Olorunfunmi Secondary School"},
  {"lga": "Egbe Idimu LCDA", "ward": "Egbe Agodo", "name": "Agodo PHC", "address": "6 Adeyinka Street"},

  {"lga": "Ejigbo LCDA", "ward": "Fadu", "name": "Ejigbo PHC", "address": "38 Lafenwa Street"},
  {"lga": "Ejigbo LCDA", "ward": "Ailegun", "name": "Iyana Ejigbo PHC", "address": "Iyana Ejigbo Bus Stop"},
  {"lga": "Ejigbo LCDA", "ward": "Ifoshi", "name": "Ona Iwamimo PHC", "address": "Ona Iwamimo Street"},
  {"lga": "Ejigbo LCDA", "ward": "Jakande", "name": "Jakande PHC", "address": "Oja Bus Stop"},

  {"lga": "Igando Ikotun LCDA", "ward": "Ijegun", "name": "Ijegun PHC", "address": "Kudeyibu Street"},
  {"lga": "Igando Ikotun LCDA", "ward": "Ikotun", "name": "Foundation PHC", "address": "Ikotun Idimu Road"},
  {"lga": "Igando Ikotun LCDA", "ward": "Egan", "name": "Egan PHC", "address": "Akesan Bus Stop"},
  {"lga": "Igando Ikotun LCDA", "ward": "Isheri Oshun", "name": "Isheri Oshun PHC", "address": "Last Bus Stop"},

  {"lga": "Mosan Okunola LCDA", "ward": "Okunola", "name": "Rauf Aregbesola PHC", "address": "Okunola Road"},

  {"lga": "Oriade LCDA", "ward": "Agboju", "name": "Agboju PHC", "address": "Baruwa Bus Stop"},
  {"lga": "Oriade LCDA", "ward": "Satellite", "name": "Satellite PHC", "address": "Learning Field Road"},
  {"lga": "Oriade LCDA", "ward": "Ibeshe", "name": "Ibeshe PHC", "address": "Beside Police Station"},
  {"lga": "Oriade LCDA", "ward": "Kirikiri", "name": "Kirikiri PHC", "address": "In front of Female Prison"},

  {"lga": "Agege LGA", "ward": "Keke", "name": "Sango PHC", "address": "Balogun Road"},
  {"lga": "Agege LGA", "ward": "Isale Oja", "name": "Iloro PHC", "address": "Olufeso Street"},
  {"lga": "Agege LGA", "ward": "Dopeemu", "name": "Dopeemu PHC", "address": "Shitta Street"},
  {"lga": "Agege LGA", "ward": "Sango", "name": "Ajegunle Health Post", "address": "Ajigbotinu Street"},

  {"lga": "Ifako Ijaiye LGA", "ward": "Ifako Coker", "name": "Ifako PHC", "address": "Ajilete Street"},
  {"lga": "Ifako Ijaiye LGA", "ward": "Iju Ishaga", "name": "Iju PHC", "address": "Ladipo Avenue"},
  {"lga": "Ifako Ijaiye LGA", "ward": "Iju Obawole", "name": "Obawole PHC", "address": "Asabi Taiwo Street"},
  {"lga": "Ifako Ijaiye LGA", "ward": "Ogundimu", "name": "Ogundimu PHC", "address": "Kayode Street"},

  {"lga": "Kosofe LGA", "ward": "Mende", "name": "Mende PHC", "address": "Bode Oluwo Street"},
  {"lga": "Kosofe LGA", "ward": "Ogudu", "name": "Ogudu PHC", "address": "Ogudu Road"},
  {"lga": "Kosofe LGA", "ward": "Orile Oworo", "name": "Oworo PHC", "address": "Gbenga Asabi Street"}
]

    ogun_phcs = [
  {"lga": "Abeokuta North LGA", "ward": "", "name": "Odeda Local Government Health Clinic", "address": ""},
  {"lga": "Abeokuta North LGA", "ward": "", "name": "Ikeye Health Centre", "address": ""},

  {"lga": "Abeokuta South LGA", "ward": "", "name": "Family Health Centre Health Center", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Ijaye Health Centre Health Center", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Saraki Health Center", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Oke Ijemo Health Post", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Iyabo Morenike Healthcare and Birth Home", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Keesi Primary Health Centre", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Itoko Health Center", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Kugba Health Centre", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "OOUTH Annex Health Center", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Abule Oloni Health Centre", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Oba Gbadebo Health Facility", "address": ""},
  {"lga": "Abeokuta South LGA", "ward": "", "name": "Igbore Health Centre", "address": ""},

  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Ife Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Ijoko Health Post", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Iroko/Aparadija Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Iloye Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Olorunsogo Iloye Health Post", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Sango Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Owode Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Ewupe Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Otun Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Ota Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Ilo Awela Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Osinachi Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Ijoko Primary Health Center", "address": ""},
  {"lga": "Ado-Odo/Ota LGA", "ward": "", "name": "Iju Health Center", "address": ""},

  {"lga": "Yewa North LGA", "ward": "", "name": "Family Health Centre Ibile", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Primary Health Center Idofoi", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Isa Ope Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Igan Okoto Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Ilujoda/Iboro Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Imasai Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Joga Orile Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Igbogila Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Eggua Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Ijoun Health Center", "address": ""},
  {"lga": "Yewa North LGA", "ward": "", "name": "Afon Health Center", "address": ""},

  {"lga": "Ijebu North LGA", "ward": "", "name": "Oke Agbo Health Center", "address": ""},
  {"lga": "Ijebu North LGA", "ward": "", "name": "Oru Awa Ilaporu Health Center", "address": ""},

  {"lga": "Ifo LGA", "ward": "", "name": "Robiyan Health Center", "address": ""},

  {"lga": "Ijebu Ode LGA", "ward": "", "name": "Iwade Isale Health Centre", "address": ""},

  {"lga": "Ijebu North-East LGA", "ward": "", "name": "Oke Eri Community PHC", "address": ""},

  {"lga": "Imeko Afon LGA", "ward": "", "name": "Ilara PHC", "address": ""},
  {"lga": "Imeko Afon LGA", "ward": "", "name": "Primary Health Care Center Ilara", "address": ""},
  {"lga": "Imeko Afon LGA", "ward": "", "name": "Agberiodo Primary Health Center", "address": ""},
  {"lga": "Imeko Afon LGA", "ward": "", "name": "Imeko/Dende Primary Health Center", "address": ""},
  {"lga": "Imeko Afon LGA", "ward": "", "name": "Idofa Health Clinic", "address": ""},

  {"lga": "Ikenne LGA", "ward": "", "name": "Ago Ilara Health Centre", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Ilishan PHC", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Ago Ilara PHC", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Iregun Health Center", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Imobido Health Center", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Irolu PHC", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Ogere PHC", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Ikenne Health Center", "address": ""},
  {"lga": "Ikenne LGA", "ward": "", "name": "Iperu PHC", "address": ""},

  {"lga": "Odeda LGA", "ward": "", "name": "Engr Adisa Adeyinka Primary Healthcare Centre", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Baale Ogunbayo Health Clinic", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Odeda Primary Health Centre", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Orile Ilugun Health Centre", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Primary Health Centre Obete", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Opeji Local Council Area Health Centre", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Osiele Primary Health Centre", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Primary Health Centre Obantoko", "address": ""},
  {"lga": "Odeda LGA", "ward": "", "name": "Primary Health Clinic Emulu", "address": ""}
]

    data = lagos_phcs if state == "Lagos" else ogun_phcs

    lga = st.selectbox("Select LGA", list(set([d["lga"] for d in data])))

    for phc in [d for d in data if d["lga"] == lga]:
        st.success(f"{phc['name']} - {phc['address']}")
# =========================
# 🎓 TRAINING
# =========================


elif st.session_state.page == "training":
    set_bg("assets/bg_training.png")
    st.title("🎓 SGBV Training")


    # ✅ DOWNLOAD BUTTON
    with open("assets/SGBV Champions manual_20260119_072455_0000.pdf", "rb") as file:
        st.download_button(
            "📥 Download Training Manual",
            file,
            file_name="SGBV Champions manual_20260119_072455_0000.pdf"
        )
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