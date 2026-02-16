import streamlit as st
from pathlib import Path
import base64
import pandas as pd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="SIR 25-26", layout="wide")

ASSETS = Path("assets")
LOGO_PATH = ASSETS / "logo.png"

# ---------------------------
# HELPERS
# ---------------------------
def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")

@st.cache_data(show_spinner=False)
def load_matches():
    """
    Prova a caricare un file match 'leggero' per popolare i filtri.
    Se non c'è (es. su cloud), non esplode: torna DataFrame vuoto.
    """
    candidates = [
        Path("data/matches.csv"),
        Path("export/matches.csv"),
        Path("matches.csv"),
    ]
    for p in candidates:
        if p.exists():
            return pd.read_csv(p)
    return pd.DataFrame()

def init_filters():
    if "f_giornate" not in st.session_state:
        st.session_state.f_giornate = []
    if "f_squadre" not in st.session_state:
        st.session_state.f_squadre = []
    if "f_ruoli" not in st.session_state:
        st.session_state.f_ruoli = []

# ---------------------------
# STYLE (scoreboard-ish)
# ---------------------------
st.markdown(
    """
    <style>
      .stApp { background: #000000; }
      section.main > div { padding-top: 18px; }

      .topbar{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:28px;
        margin-top: 8px;
        margin-bottom: 6px;
      }
      .topnum{
        font-size: 64px;
        font-weight: 800;
        color: #cfe8ff;
        letter-spacing: 2px;
        text-shadow: 0 0 18px rgba(120,190,255,.35);
        line-height: 1;
      }
      .logoBox{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:12px;
        min-width: 260px;
      }
      .teamname{
        color:#eaeaea;
        font-weight:700;
        letter-spacing: 2px;
        font-size: 14px;
        text-transform: uppercase;
        text-align:center;
        margin-top: 6px;
      }

      .filterBox{
        border: 1px solid rgba(255,255,255,.18);
        border-radius: 16px;
        padding: 14px 14px 4px 14px;
        background: rgba(255,255,255,.03);
        margin: 14px auto 18px auto;
        max-width: 1100px;
      }

      .menuTitle{
        color: rgba(255,255,255,.55);
        font-size: 12px;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin: 14px 0 10px 0;
      }
      .menuItem{
        text-align:center;
        color:#f3f3f3;
        font-size: 22px;
        font-weight: 650;
        padding: 18px 10px;
        border-top: 1px solid rgba(255,255,255,.12);
      }
      .menuItem:last-child{
        border-bottom: 1px solid rgba(255,255,255,.12);
      }
      .hint{
        color: rgba(255,255,255,.55);
        font-size: 13px;
        text-align:center;
        margin-top: 10px;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# HEADER
# ---------------------------
logo_html = ""
if LOGO_PATH.exists():
    logo_b64 = img_to_base64(LOGO_PATH)
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:76px;" />'

st.markdown(
    f"""
    <div class="topbar">
      <div class="topnum">25</div>
      <div class="logoBox">
        {logo_html}
      </div>
      <div class="topnum">26</div>
    </div>
    <div class="teamname">SIR SAFETY PERUGIA</div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# FILTERS (HOME)
# ---------------------------
init_filters()
matches = load_matches()

# opzioni intelligenti se abbiamo matches, altrimenti fallback
if not matches.empty:
    giornate_opts = sorted(matches["match_id"].dropna().astype(str).unique().tolist()) if "match_id" in matches.columns else []
    squadre_opts = []
    if "home_team" in matches.columns:
        squadre_opts += matches["home_team"].dropna().astype(str).unique().tolist()
    if "visiting_team" in matches.columns:
        squadre_opts += matches["visiting_team"].dropna().astype(str).unique().tolist()
    squadre_opts = sorted(list(set(squadre_opts)))
else:
    giornate_opts = []
    squadre_opts = []

ruoli_opts = ["Setter", "Opposto", "Schiacciatore", "Centrale", "Libero"]

with st.container():
    st.markdown('<div class="filterBox">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        st.session_state.f_giornate = st.multiselect(
            "Seleziona giornate",
            options=giornate_opts,
            default=st.session_state.f_giornate,
            placeholder="(tutte)" if giornate_opts else "Dati non presenti sul cloud"
        )

    with c2:
        st.session_state.f_squadre = st.multiselect(
            "Seleziona squadre",
            options=squadre_opts,
            default=st.session_state.f_squadre,
            placeholder="(tutte)" if squadre_opts else "Dati non presenti sul cloud"
        )

    with c3:
        st.session_state.f_ruoli = st.multiselect(
            "Seleziona ruolo",
            options=ruoli_opts,
            default=st.session_state.f_ruoli,
            placeholder="(tutti)"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# piccolo riepilogo filtri (chiaro, da “cabina di comando”)
g = st.session_state.f_giornate
s = st.session_state.f_squadre
r = st.session_state.f_ruoli

st.markdown(
    f'<div class="hint">Filtri attivi → '
    f'Giornate: <b>{len(g) if g else "tutte"}</b> · '
    f'Squadre: <b>{len(s) if s else "tutte"}</b> · '
    f'Ruoli: <b>{", ".join(r) if r else "tutti"}</b>'
    f'</div>',
    unsafe_allow_html=True
)

# ---------------------------
# MENU (senza link per ora)
# ---------------------------
st.markdown('<div class="menuTitle">MENU</div>', unsafe_allow_html=True)

menu_items = [
    "Statistiche per Team",
    "Attacco - Dettaglio",
    "Stat Dett per Ruolo",
    "Linee SideOut & BreakPoint",
    "Dettaglio indici x tipo BT/Ric",
    "Indici x Ruolo",
    "Punti per set",
]

for item in menu_items:
    st.markdown(f'<div class="menuItem">{item}</div>', unsafe_allow_html=True)

st.markdown('<div class="hint">I filtri sono pronti. Nelle prossime sezioni li useremo per calcolare e mostrare i dati.</div>', unsafe_allow_html=True)
