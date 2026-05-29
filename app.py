import streamlit as st

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ChemGuide | Panduan Metode Analisis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 50%, #0a1628 100%);
        color: #e0e6f0;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1b2a 0%, #112240 100%);
        border-right: 1px solid #1e3a5f;
    }

    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stTextInput label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #a8c8f0 !important;
    }

    /* Header */
    .main-header {
        font-family: 'Space Mono', monospace;
        font-size: 2.4rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4fc3f7, #81d4fa, #b3e5fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.2rem;
    }

    .sub-header {
        color: #64b5f6;
        font-size: 0.95rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }

    /* Cards */
    .result-card {
        background: linear-gradient(135deg, #112240 0%, #0d1b35 100%);
        border: 1px solid #1e3a5f;
        border-left: 4px solid #4fc3f7;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }

    .result-card h3 {
        font-family: 'Space Mono', monospace;
        color: #4fc3f7;
        font-size: 0.8rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .result-card p {
        color: #cdd9f0;
        font-size: 1rem;
        line-height: 1.6;
        margin: 0;
    }

    .badge {
        display: inline-block;
        background: rgba(79, 195, 247, 0.15);
        border: 1px solid #4fc3f7;
        color: #4fc3f7;
        padding: 0.2rem 0.7rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-family: 'Space Mono', monospace;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }

    .badge-green {
        background: rgba(129, 199, 132, 0.15);
        border-color: #81c784;
        color: #81c784;
    }

    .badge-orange {
        background: rgba(255, 183, 77, 0.15);
        border-color: #ffb74d;
        color: #ffb74d;
    }

    .step-card {
        background: rgba(17, 34, 64, 0.8);
        border: 1px solid #1e3a5f;
        border-radius: 10px;
        padding: 1rem 1.5rem;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }

    .step-number {
        background: #4fc3f7;
        color: #0a0f1e;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.85rem;
        flex-shrink: 0;
        font-family: 'Space Mono', monospace;
    }

    .divider {
        border: none;
        border-top: 1px solid #1e3a5f;
        margin: 1.5rem 0;
    }

    .stat-box {
        background: linear-gradient(135deg, #112240, #0d1b35);
        border: 1px solid #1e3a5f;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }

    .stat-number {
        font-family: 'Space Mono', monospace;
        font-size: 1.8rem;
        color: #4fc3f7;
        font-weight: 700;
    }

    .stat-label {
        color: #64b5f6;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* Streamlit component overrides */
    .stSelectbox > div > div {
        background: #112240 !important;
        border: 1px solid #1e3a5f !important;
        color: #e0e6f0 !important;
        border-radius: 8px !important;
    }

    .stTextInput > div > div > input {
        background: #112240 !important;
        border: 1px solid #1e3a5f !important;
        color: #e0e6f0 !important;
        border-radius: 8px !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #1565c0, #1976d2) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.2s !important;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #1976d2, #42a5f5) !important;
        box-shadow: 0 4px 15px rgba(79, 195, 247, 0.3) !important;
    }

    h1, h2, h3 { color: #e0e6f0 !important; }
    p { color: #cdd9f0; }

    .search-result-item {
        background: rgba(17, 34, 64, 0.6);
        border: 1px solid #1e3a5f;
        border-radius: 8px;
        padding: 0.8rem 1.2rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
        transition: border-color 0.2s;
    }
    .search-result-item:hover {
        border-color: #4fc3f7;
    }
</style>
""", unsafe_allow_html=True)

# ─── Data Metode Analisis ──────────────────────────────────────────────────────
DATA = {
    "Air & Limbah": {
        "pH": {
            "metode": "SNI 06-6989.11-2004",
            "prinsip": "Pengukuran potensial ion H⁺ menggunakan elektroda gelas yang dikalibrasi dengan larutan buffer standar.",
            "alat": ["pH meter", "Elektroda gelas & referensi", "Beaker glass 100 mL", "Larutan buffer pH 4, 7, 10", "Aquades"],
            "prosedur": [
                "Kalibrasi pH meter dengan larutan buffer pH 4 dan 7",
                "Bilas elektroda dengan aquades, keringkan dengan tisu",
                "Celupkan elektroda ke dalam sampel (minimal 50 mL)",
                "Baca nilai pH setelah stabil (± 1 menit)",
                "Catat suhu pengukuran"
            ],
            "acuan": "SNI 06-6989.11-2004",
            "kategori": "Fisikokimia",
            "tingkat_kesulitan": "Mudah"
        },
        "COD": {
            "metode": "SNI 6989.2:2009 (Refluks Tertutup - Titrimetri)",
            "prinsip": "Oksidasi senyawa organik oleh K₂Cr₂O₇ berlebih dalam suasana asam kuat (H₂SO₄) dengan katalis Ag₂SO₄. Kelebihan dikromat dititrasi dengan FAS.",
            "alat": ["COD reaktor / block digester", "Tabung COD bertutup", "Buret 25 mL", "Erlenmeyer 250 mL", "Mikropipet", "Neraca analitik", "Pemanas"],
            "prosedur": [
                "Pipet 2,5 mL sampel ke dalam tabung COD",
                "Tambahkan 1,5 mL larutan K₂Cr₂O₇ dan 3,5 mL H₂SO₄ + Ag₂SO₄",
                "Tutup tabung, kocok perlahan, panaskan 150°C selama 2 jam",
                "Dinginkan, pindahkan ke erlenmeyer, tambahkan 1-2 tetes ferroin",
                "Titrasi dengan FAS 0,1 N hingga warna berubah hijau-biru → coklat kemerahan",
                "Hitung COD = (A-B) × N × 8000 / V sampel"
            ],
            "acuan": "SNI 6989.2:2009",
            "kategori": "Organik",
            "tingkat_kesulitan": "Menengah"
        },
        "BOD": {
            "metode": "SNI 6989.72:2009 (BOD₅ - Inkubasi 5 Hari)",
            "prinsip": "Pengukuran oksigen terlarut sebelum dan sesudah inkubasi 5 hari pada 20°C dalam gelap. Selisih DO merupakan nilai BOD.",
            "alat": ["Inkubator 20°C", "Botol winkler/BOD 300 mL", "DO meter atau set titrasi Winkler", "Pipet volumetrik", "Aerator"],
            "prosedur": [
                "Siapkan air pengencer (aerasi 1 jam, tambah buffer fosfat, MgSO₄, CaCl₂, FeCl₃)",
                "Isi 2 botol BOD: 1 untuk DO₀, 1 untuk DO₅",
                "Ukur DO awal (DO₀) dengan DO meter atau metode Winkler",
                "Inkubasi botol kedua pada 20°C, gelap, selama 5 hari",
                "Ukur DO akhir (DO₅)",
                "BOD₅ = (DO₀ – DO₅) × faktor pengenceran"
            ],
            "acuan": "SNI 6989.72:2009",
            "kategori": "Organik",
            "tingkat_kesulitan": "Menengah"
        },
        "TSS": {
            "metode": "SNI 06-6989.3-2004 (Gravimetri)",
            "prinsip": "Padatan tersuspensi disaring dengan kertas saring Whatman GF/C, dikeringkan pada 105°C, dan ditimbang.",
            "alat": ["Kertas saring Whatman GF/C 0,45 µm", "Perangkat filtrasi vakum", "Oven 105°C", "Desikator", "Neraca analitik 0,1 mg", "Cawan porselen"],
            "prosedur": [
                "Timbang kertas saring + cawan setelah dioven 105°C selama 1 jam (berat a)",
                "Saring sampel yang telah dikocok homogen (volume V mL)",
                "Oven kertas saring pada 105°C selama minimal 2 jam",
                "Dinginkan dalam desikator 15 menit, timbang (berat b)",
                "TSS (mg/L) = (b – a) × 1000 / V sampel (mL) × 1000"
            ],
            "acuan": "SNI 06-6989.3-2004",
            "kategori": "Fisikokimia",
            "tingkat_kesulitan": "Mudah"
        },
        "Nitrat (NO₃⁻)": {
            "metode": "SNI 6989.79:2011 (Spektrofotometri UV 220/275 nm)",
            "prinsip": "Nitrat menyerap sinar UV pada 220 nm. Gangguan bahan organik dikoreksi dengan pembacaan pada 275 nm.",
            "alat": ["Spektrofotometer UV-Vis", "Kuvet kuarsa", "Labu ukur 100 mL", "Kertas saring 0,45 µm", "Pipet volumetrik"],
            "prosedur": [
                "Saring sampel dengan kertas saring 0,45 µm",
                "Tambahkan 0,2 mL HCl 1N per 50 mL sampel untuk mengurangi gangguan",
                "Baca absorbansi pada λ 220 nm (A₂₂₀) dan 275 nm (A₂₇₅)",
                "Nilai terkoreksi = A₂₂₀ – 2 × A₂₇₅",
                "Buat kurva kalibrasi dari larutan standar KNO₃",
                "Tentukan konsentrasi dari persamaan regresi kurva kalibrasi"
            ],
            "acuan": "SNI 6989.79:2011",
            "kategori": "Anorganik",
            "tingkat_kesulitan": "Menengah"
        }
    },
    "Pangan & Minuman": {
        "Kadar Air": {
            "metode": "SNI 01-2891-1992 (Gravimetri - Oven 105°C)",
            "prinsip": "Air dalam bahan pangan diuapkan dengan pemanasan pada 105°C hingga bobot konstan. Selisih berat sebelum dan sesudah pemanasan merupakan kadar air.",
            "alat": ["Oven 105°C", "Desikator dengan silika gel", "Neraca analitik 0,1 mg", "Cawan porselen/aluminium", "Penjepit cawan"],
            "prosedur": [
                "Panaskan cawan kosong pada 105°C selama 1 jam, dinginkan dalam desikator, timbang (W₀)",
                "Timbang ± 5 gram sampel dalam cawan (W₁)",
                "Panaskan dalam oven 105°C selama 3-5 jam",
                "Dinginkan dalam desikator 30 menit, timbang (W₂)",
                "Ulangi pemanasan 1 jam hingga bobot konstan (selisih < 0,2 mg)",
                "Kadar Air (%) = (W₁ – W₂) / W₁ × 100%"
            ],
            "acuan": "SNI 01-2891-1992",
            "kategori": "Proksimat",
            "tingkat_kesulitan": "Mudah"
        },
        "Kadar Abu": {
            "metode": "SNI 01-2891-1992 (Pengabuan Kering 550°C)",
            "prinsip": "Bahan organik dioksidasi sempurna dalam tanur pada suhu 550°C. Residu yang tertinggal merupakan abu (mineral total).",
            "alat": ["Tanur (Muffle Furnace) 550°C", "Desikator", "Neraca analitik", "Cawan porselen", "Penjepit cawan", "Penangas air"],
            "prosedur": [
                "Timbang cawan kosong setelah dioven 105°C (W₀)",
                "Timbang ± 5 gram sampel dalam cawan (W₁)",
                "Arangkan di atas kompor/bunsen hingga tidak berasap",
                "Masukkan dalam tanur 550°C selama 4-6 jam hingga abu berwarna putih/abu-abu",
                "Matikan tanur, dinginkan hingga ± 200°C, pindahkan ke desikator",
                "Timbang setelah dingin (W₂). Kadar Abu (%) = (W₂ – W₀) / W₁ × 100%"
            ],
            "acuan": "SNI 01-2891-1992",
            "kategori": "Proksimat",
            "tingkat_kesulitan": "Mudah"
        },
        "Protein (Kjeldahl)": {
            "metode": "SNI 01-2891-1992 (Kjeldahl)",
            "prinsip": "Nitrogen dalam protein dikonversi menjadi NH₄⁺ melalui destruksi asam (H₂SO₄ pekat + katalis). NH₃ dilepaskan dengan NaOH, didestilasi, dan dititrasi dengan HCl standar.",
            "alat": ["Labu Kjeldahl 100 mL", "Unit destilasi Kjeldahl", "Set peralatan titrasi", "Pemanas Kjeldahl", "Labu destilat 250 mL", "Buret 25 mL"],
            "prosedur": [
                "Timbang ± 0,5 gram sampel dalam labu Kjeldahl",
                "Tambahkan 10 mL H₂SO₄ pekat + katalis (K₂SO₄ + CuSO₄)",
                "Destruksi hingga larutan jernih kehijauan (± 2 jam), dinginkan",
                "Pindahkan ke labu destilasi, tambahkan aquades dan 40% NaOH berlebih",
                "Destilasi, tampung distilat dalam labu berisi 25 mL H₃BO₃ + indikator",
                "Titrasi destilat dengan HCl 0,1 N. % N = (mL HCl × N × 14,01) / mg sampel × 100. % Protein = % N × faktor (6,25)"
            ],
            "acuan": "SNI 01-2891-1992",
            "kategori": "Proksimat",
            "tingkat_kesulitan": "Tinggi"
        },
        "Lemak (Soxhlet)": {
            "metode": "SNI 01-2891-1992 (Soxhlet - Ekstraksi Pelarut)",
            "prinsip": "Lemak diekstrak dari bahan pangan menggunakan pelarut nonpolar (n-heksan/petroleum eter) dalam alat Soxhlet secara kontinu. Pelarut diuapkan dan lemak ditimbang.",
            "alat": ["Alat Soxhlet lengkap", "Labu alas bulat 250 mL", "Kondensor", "Oven 105°C", "Desikator", "Neraca analitik", "n-Heksan/petroleum eter"],
            "prosedur": [
                "Timbang labu alas bulat bersih setelah dioven (W₀)",
                "Timbang ± 5 gram sampel kering dalam selongsong kertas saring (W₁)",
                "Rangkai alat Soxhlet, masukkan n-heksan ± 150-200 mL",
                "Ekstraksi selama 4-6 jam (sirkulasi minimal 6×)",
                "Uapkan pelarut dari labu dengan rotary evaporator atau oven",
                "Timbang labu + lemak (W₂). % Lemak = (W₂ – W₀) / W₁ × 100%"
            ],
            "acuan": "SNI 01-2891-1992",
            "kategori": "Proksimat",
            "tingkat_kesulitan": "Menengah"
        }
    },
    "Tanah & Pupuk": {
        "pH Tanah": {
            "metode": "SNI 03-3441-1994 (H₂O dan KCl 1N)",
            "prinsip": "Pengukuran pH suspensi tanah dalam air (pH aktual) dan dalam KCl 1N (pH potensial) menggunakan pH meter.",
            "alat": ["pH meter terkalibrasi", "Timbangan analitik", "Gelas beker 50 mL", "Pengaduk kaca", "Aquades", "Larutan KCl 1N", "Buffer pH 4 dan 7"],
            "prosedur": [
                "Timbang 10 gram tanah kering angin dalam beker",
                "Untuk pH H₂O: tambahkan 25 mL aquades, aduk 30 menit, diamkan 30 menit",
                "Untuk pH KCl: ulangi dengan 25 mL KCl 1N",
                "Kalibrasi pH meter dengan buffer pH 4 dan 7",
                "Celupkan elektroda ke suspensi, baca pH setelah stabil",
                "Interpretasi: masam (<5,5), netral (6,0-7,0), basa (>7,0)"
            ],
            "acuan": "SNI 03-3441-1994",
            "kategori": "Fisikokimia",
            "tingkat_kesulitan": "Mudah"
        },
        "Nitrogen Total (Kjeldahl)": {
            "metode": "SNI 2803:2012 (Kjeldahl)",
            "prinsip": "Nitrogen organik dan anorganik dalam tanah/pupuk dikonversi menjadi ammonium sulfat melalui destruksi. NH₃ didestilasi dan dititrasi untuk menentukan kadar N.",
            "alat": ["Labu Kjeldahl 100 mL", "Unit destilasi", "Peralatan titrasi lengkap", "Pemanas Kjeldahl", "Buret 25 mL", "Gelas ukur"],
            "prosedur": [
                "Timbang 0,5-1 gram sampel tanah/pupuk dalam labu Kjeldahl",
                "Tambahkan 10 mL H₂SO₄ pekat + katalis selenium/CuSO₄+K₂SO₄",
                "Destruksi hingga jernih (200°C → 370°C), ± 2-4 jam, dinginkan",
                "Encerkan, pindahkan ke labu destilasi, alkalisasi dengan NaOH 40%",
                "Destilasi, tampung dalam labu berisi H₃BO₃ + indikator campuran",
                "Titrasi dengan H₂SO₄ 0,05 N. % N = (mL × N × 14,01 × 100) / (mg sampel)"
            ],
            "acuan": "SNI 2803:2012",
            "kategori": "Makronutrien",
            "tingkat_kesulitan": "Tinggi"
        }
    },
    "Udara & Emisi": {
        "SO₂ (Pararosanilin)": {
            "metode": "SNI 19-7119.7-2005 (Spektrofotometri Pararosanilin)",
            "prinsip": "SO₂ dalam udara diserap larutan tetrakloromerkurat (TCM), bereaksi dengan formaldehid dan pararosanilin membentuk senyawa ungu yang diukur pada 548 nm.",
            "alat": ["Impinger 2 tabung", "Pompa vakum", "Flowmeter", "Spektrofotometer Vis", "Kuvet 1 cm", "Labu ukur 25 mL"],
            "prosedur": [
                "Isi impinger dengan 10 mL larutan penyerap TCM",
                "Sampling udara dengan laju 1 L/menit selama 30-60 menit",
                "Pindahkan larutan ke labu ukur 25 mL, tambahkan EDTA 0,1%",
                "Tambahkan 1 mL asam sulfamat, 3 mL formaldehid 0,2%, 5 mL pararosanilin",
                "Encerkan hingga tanda, diamkan 30 menit pada 22±2°C",
                "Baca absorbansi pada λ 548 nm, hitung konsentrasi dari kurva kalibrasi"
            ],
            "acuan": "SNI 19-7119.7-2005",
            "kategori": "Gas Anorganik",
            "tingkat_kesulitan": "Tinggi"
        }
    }
}

# ─── Helper Functions ──────────────────────────────────────────────────────────
def get_all_parameters():
    result = []
    for jenis, params in DATA.items():
        for param in params:
            result.append({"jenis": jenis, "parameter": param})
    return result

def get_difficulty_color(tingkat):
    if tingkat == "Mudah":
        return "badge-green"
    elif tingkat == "Menengah":
        return "badge-orange"
    else:
        return ""

def display_method_detail(info, param_name):
    st.markdown(f"""
    <div class="result-card">
        <h3>📋 Metode / Acuan</h3>
        <p>{info['metode']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-card">
        <h3>🔬 Prinsip Analisis</h3>
        <p>{info['prinsip']}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        alat_html = "".join([f'<span class="badge">{a}</span>' for a in info['alat']])
        st.markdown(f"""
        <div class="result-card">
            <h3>🧪 Alat & Bahan</h3>
            <p>{alat_html}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        diff_class = get_difficulty_color(info['tingkat_kesulitan'])
        st.markdown(f"""
        <div class="result-card">
            <h3>📊 Info Parameter</h3>
            <p>
                <span class="badge">Kategori: {info['kategori']}</span><br><br>
                <span class="badge {diff_class}">Kesulitan: {info['tingkat_kesulitan']}</span><br><br>
                <span class="badge">Acuan: {info['acuan']}</span>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📝 Prosedur Kerja")
    for i, step in enumerate(info['prosedur'], 1):
        st.markdown(f"""
        <div class="step-card">
            <div class="step-number">{i}</div>
            <p style="margin:0; color:#cdd9f0; padding-top:2px;">{step}</p>
        </div>
        """, unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧪 ChemGuide")
    st.markdown("<p style='color:#64b5f6; font-size:0.8rem;'>Panduan Metode Analisis Kimia</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1e3a5f'>", unsafe_allow_html=True)

    menu = st.radio("Navigasi", ["🔍 Cari Parameter", "📂 Browse per Jenis Sampel", "📊 Ringkasan Database"], label_visibility="collapsed")

    st.markdown("<hr style='border-color:#1e3a5f'>", unsafe_allow_html=True)

    # Stats
    total_param = sum(len(v) for v in DATA.values())
    total_jenis = len(DATA)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_param}</div>
            <div class="stat-label">Parameter</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_jenis}</div>
            <div class="stat-label">Jenis Sampel</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#4a6a9a; font-size:0.75rem; text-align:center;'>
    Politeknik AKA Bogor<br>Kimia Analitik 2026
    </p>
    """, unsafe_allow_html=True)

# ─── Main Content ──────────────────────────────────────────────────────────────
st.markdown('<p class="main-header">⚗️ ChemGuide</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistem Panduan Metode Analisis Kimia Analitik</p>', unsafe_allow_html=True)

# ── Menu 1: Cari Parameter ─────────────────────────────────────────────────────
if "Cari" in menu:
    st.markdown("### 🔍 Pencarian Parameter")
    keyword = st.text_input("Ketik nama parameter (contoh: pH, COD, protein...)", placeholder="Cari parameter analisis...")

    if keyword:
        all_params = get_all_parameters()
        hasil = [p for p in all_params if keyword.lower() in p['parameter'].lower()]

        if hasil:
            st.markdown(f"<p style='color:#64b5f6;'>Ditemukan <b>{len(hasil)}</b> hasil untuk '<b>{keyword}</b>'</p>", unsafe_allow_html=True)

            for h in hasil:
                info = DATA[h['jenis']][h['parameter']]
                diff_class = get_difficulty_color(info['tingkat_kesulitan'])
                if st.button(f"📌 {h['parameter']} — {h['jenis']}", key=f"btn_{h['jenis']}_{h['parameter']}"):
                    st.session_state['selected'] = (h['jenis'], h['parameter'])

            if 'selected' in st.session_state:
                jenis, param = st.session_state['selected']
                if jenis in DATA and param in DATA[jenis]:
                    st.markdown("<hr style='border-color:#1e3a5f'>", unsafe_allow_html=True)
                    st.markdown(f"## 📋 {param}")
                    st.markdown(f"<span class='badge'>Jenis Sampel: {jenis}</span>", unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)
                    display_method_detail(DATA[jenis][param], param)
        else:
            st.warning(f"Parameter '{keyword}' tidak ditemukan dalam database.")
    else:
        st.markdown("""
        <div style='background: rgba(17,34,64,0.6); border: 1px dashed #1e3a5f; border-radius:12px; padding:2rem; text-align:center; margin-top:1rem;'>
            <p style='color:#4a6a9a; font-size:1.1rem;'>🔎 Ketik nama parameter di atas untuk mulai pencarian</p>
            <p style='color:#4a6a9a; font-size:0.85rem;'>Tersedia: pH, COD, BOD, TSS, Nitrat, Kadar Air, Abu, Protein, Lemak, dan lainnya</p>
        </div>
        """, unsafe_allow_html=True)

# ── Menu 2: Browse ─────────────────────────────────────────────────────────────
elif "Browse" in menu:
    st.markdown("### 📂 Browse Berdasarkan Jenis Sampel")

    jenis_list = list(DATA.keys())
    jenis_icons = {"Air & Limbah": "💧", "Pangan & Minuman": "🍎", "Tanah & Pupuk": "🌱", "Udara & Emisi": "💨"}

    col1, col2 = st.columns([1, 2])
    with col1:
        selected_jenis = st.selectbox("Pilih Jenis Sampel:", jenis_list,
                                       format_func=lambda x: f"{jenis_icons.get(x, '🔬')} {x}")
    with col2:
        param_list = list(DATA[selected_jenis].keys())
        selected_param = st.selectbox("Pilih Parameter:", param_list)

    if selected_jenis and selected_param:
        info = DATA[selected_jenis][selected_param]
        st.markdown("<hr style='border-color:#1e3a5f'>", unsafe_allow_html=True)
        st.markdown(f"## {jenis_icons.get(selected_jenis,'🔬')} {selected_param}")
        st.markdown(f"<span class='badge'>Jenis Sampel: {selected_jenis}</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        display_method_detail(info, selected_param)

# ── Menu 3: Ringkasan ──────────────────────────────────────────────────────────
elif "Ringkasan" in menu:
    st.markdown("### 📊 Ringkasan Database Metode Analisis")

    for jenis, params in DATA.items():
        icon = {"Air & Limbah": "💧", "Pangan & Minuman": "🍎", "Tanah & Pupuk": "🌱", "Udara & Emisi": "💨"}.get(jenis, "🔬")
        with st.expander(f"{icon} {jenis} — {len(params)} Parameter"):
            table_data = []
            for param, info in params.items():
                table_data.append({
                    "Parameter": param,
                    "Metode/Acuan": info['acuan'],
                    "Kategori": info['kategori'],
                    "Tingkat Kesulitan": info['tingkat_kesulitan']
                })
            import pandas as pd
            df = pd.DataFrame(table_data)
            st.dataframe(df, use_container_width=True, hide_index=True)

