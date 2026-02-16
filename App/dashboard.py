import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="SIR 25-26", layout="wide")

ASSETS = Path("assets")
LOGO_PATH = ASSETS / "logo.png"

def img_to_base64(path):
    return base64.b64encode(path.read_bytes()).decode()

# --- CSS ---
st.markdown("""
<style>
.stApp { background:#000; color:white; }

.metric-box{
    border:1px solid rgba(255,255,255,0.2);
    border-radius:16px;
    padding:20px;
    text-align:center;
    background:rgba(255,255,255,0.03);
}

.metric-value{
    font-size:40px;
    font-weight:700;
    color:#cfefff;
}

.metric-label{
    font-size:14px;
    opacity:0.8;
    letter-spacing:1px;
}

.section-title{
    font-size:20px;
    margin-top:30px;
    margin-bottom:10px;
    opacity:0.9;
}

div[data-testid="stButton"] > button{
    background:transparent;
    border:none;
    color:white;
    font-size:24px;
    text-align:left;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
if LOGO_PATH.exists():
    logo = f'<img src="data:image/png;base64,{img_to_base64(LOGO_PATH)}" height="60">'
else:
    logo = "SIR SAFETY PERUGIA"

st.markdown(f"""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;">
<div style="font-size:60px;color:#bfe6ff;">25</div>
<div>{logo}</div>
<div style="font-size:60px;color:#bfe6ff;">26</div>
</div>
""", unsafe_allow_html=True)

# --- BLOCCO STATO SQUADRA ---
st.markdown('<div class="section-title">STATO SQUADRA</div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown('<div class="metric-box"><div class="metric-value">62%</div><div class="metric-label">SIDEOUT</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-box"><div class="metric-value">38%</div><div class="metric-label">BREAKPOINT</div></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-box"><div class="metric-value">+0.28</div><div class="metric-label">EFF ATTACCO</div></div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="metric-box"><div class="metric-value">11%</div><div class="metric-label">ERROR RATE</div></div>', unsafe_allow_html=True)

# --- TREND ---
st.markdown('<div class="section-title">TREND RECENTE</div>', unsafe_allow_html=True)
st.write("Grafico in arrivo")

# --- MENU ---
st.markdown('<div class="section-title">MENU</div>', unsafe_allow_html=True)

items = [
    "Statistiche per Team",
    "Attacco - Dettaglio",
    "Stat Dett per Ruolo",
    "Linee SideOut & BreakPoint",
    "Dettaglio indici x tipo BT/Ric",
    "Indici x Ruolo",
    "Punti per set",
]

for i,label in enumerate(items):
    st.button(label, key=i)
