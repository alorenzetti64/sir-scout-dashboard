import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="SIR 25-26", layout="wide")

ASSETS = Path("assets")
LOGO_PATH = ASSETS / "logo.png"

def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")

# --- CSS: scoreboard look ---
st.markdown(
    """
    <style>
      .stApp { background: #000000; }

      section.main > div { padding-top: 18px; }

      /* Header 25 - logo - 26 */
      .topbar{
        display:flex;
        align-items:center;
        justify-content:space-between;
        margin: 6px auto 22px auto;
        max-width: 820px;
      }
      .year{
        font-size: 64px;
        font-weight: 800;
        letter-spacing: 4px;
        color: #bfe6ff;
        text-shadow: 0 0 12px rgba(80,180,255,0.55);
        width: 140px;
        text-align:center;
        line-height: 1;
      }
      .logo-wrap{
        flex: 1;
        display:flex;
        justify-content:center;
        align-items:center;
        gap: 12px;
      }
      .logo-img{ max-height: 70px; }

      /* Scoreboard panel */
      .board{
        max-width: 820px;
        margin: 0 auto;
        padding: 22px 22px 16px 22px;
        border: 1px solid rgba(255,255,255,0.22);
        border-radius: 18px;
        background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
        box-shadow:
          0 0 18px rgba(120,200,255,0.08),
          inset 0 0 18px rgba(255,255,255,0.04);
      }
      .board-title{
        color: rgba(255,255,255,0.92);
        font-size: 14px;
        letter-spacing: 3px;
        text-transform: uppercase;
        opacity: 0.85;
        margin-bottom: 12px;
      }

      /* Streamlit buttons -> scoreboard links */
      div[data-testid="stButton"]{ margin: 0 !important; }
      div[data-testid="stButton"] > button[kind="secondary"]{
        width: 100% !important;
        background: transparent !important;
        border: none !important;
        padding: 10px 8px !important;
        margin: 0 !important;

        color: #ffffff !important;
        font-size: 26px !important;
        font-weight: 650 !important;
        text-align: left !important;
        justify-content: flex-start !important;

        letter-spacing: 0.5px !important;
        text-decoration: none !important;

        /* “LED” effect */
        text-shadow: 0 0 10px rgba(120,200,255,0.20);
        border-radius: 12px !important;
      }

      div[data-testid="stButton"] > button[kind="secondary"]:hover{
        background: rgba(120,200,255,0.10) !important;
        box-shadow: 0 0 16px rgba(120,200,255,0.18) !important;
        color: #cfefff !important;
      }

      /* row separator line */
      .sep{
        height: 1px;
        background: rgba(255,255,255,0.18);
        margin: 0;
      }

      .footerline{
        height: 1px;
        background: rgba(255,255,255,0.55);
        margin: 26px auto 0 auto;
        max-width: 820px;
        opacity: 0.65;
      }

      /* remove extra padding around widgets */
      .block-container { padding-bottom: 22px; }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header render ---
if LOGO_PATH.exists():
    b64 = img_to_base64(LOGO_PATH)
    logo_html = f'<img class="logo-img" src="data:image/png;base64,{b64}" />'
else:
    logo_html = '<div style="color:white;font-weight:800;letter-spacing:2px;">SIR SAFETY PERUGIA</div>'

st.markdown(
    f"""
    <div class="topbar">
      <div class="year">25</div>
      <div class="logo-wrap">{logo_html}</div>
      <div class="year">26</div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Scoreboard menu ---
items = [
    "Statistiche per Team",
    "Attacco - Dettaglio",
    "Stat Dett per Ruolo",
    "Linee SideOut & BreakPoint",
    "Dettaglio indici x tipo BT/Ric",
    "Indici x Ruolo",
    "Punti per set",
]

st.markdown('<div class="board">', unsafe_allow_html=True)
st.markdown('<div class="board-title">MENU</div>', unsafe_allow_html=True)

for i, label in enumerate(items):
    pressed = st.button(label, key=f"menu_{i}", use_container_width=True)
    if i < len(items) - 1:
        st.markdown('<div class="sep"></div>', unsafe_allow_html=True)
    if pressed:
        st.toast("Sezione in arrivo 🙂", icon="⏳")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown('<div class="footerline"></div>', unsafe_allow_html=True)
