"""
Mechanical Engineering PhD Portfolio - Streamlit Application
Dr. Alex Rivers | Advanced Thermal Systems, Robotics & Multiphysics Modeling
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import io
import os

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dr. Devarsh M. Vispute | Mechanical Engineering PhD",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# CUSTOM CSS: SOBER, ACADEMIC & PROFESSIONAL STYLING
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Color Tokens */
    :root {
        --brand-primary: #1a2a3a;
        --brand-secondary: #4a5a6a;
        --brand-accent: #2c4a6f;
        --bg-subtle: #f8f9fa;
        --border-color: #e2e8f0;
    }

    /* Base Typography */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #1e293b;
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', Georgia, serif;
        color: #1a2a3a;
        font-weight: 700;
        letter-spacing: -0.01em;
    }

    /* Hero section styling */
    .hero-container {
        padding: 1.5rem 0 2rem 0;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 2rem;
    }

    .badge-phd {
        display: inline-block;
        background-color: #f1f5f9;
        color: #1a2a3a;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        text-transform: uppercase;
        border: 1px solid #cbd5e1;
        margin-bottom: 0.75rem;
    }

    .hero-tagline {
        font-size: 1.15rem;
        color: #475569;
        line-height: 1.6;
        max-width: 900px;
    }

    /* Project card styling */
    .project-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .project-card:hover {
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    }

    .tag-chip {
        display: inline-block;
        background-color: #f8fafc;
        color: #334155;
        border: 1px solid #e2e8f0;
        font-size: 0.75rem;
        font-family: 'JetBrains Mono', monospace;
        padding: 0.2rem 0.55rem;
        border-radius: 6px;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }

    /* Publication row styling */
    .pub-item {
        border-left: 3px solid #1a2a3a;
        padding: 0.75rem 0 0.75rem 1.25rem;
        margin-bottom: 1.25rem;
        background: #fbfcfd;
        border-radius: 0 8px 8px 0;
    }
    .pub-title {
        font-weight: 600;
        font-size: 1rem;
        color: #0f172a;
        margin-bottom: 0.25rem;
    }
    .pub-meta {
        font-size: 0.85rem;
        color: #64748b;
    }

    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-family: 'Playfair Display', serif;
        color: #1a2a3a !important;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# PORTFOLIO DATA STRUCTURE (CUSTOMIZE HERE)
# -----------------------------------------------------------------------------
BIO_DATA = {
    "name": "Dr. Devarsh M. Vispute",
    "title": "Ph.D. in Mechanical Engineering",
    "affiliation": "Postdoctoral Research Associate | Carnegie Mellon University",
    "email": "devarsh.vispute@gmail.com",
    "location": "Pittsburgh, PA, USA",
    "linkedin": "https://www.linkedin.com/in/devarshvispute/",
    "scholar": "https://scholar.google.com/citations?hl=en&user=59rywrIAAAAJ",
    "github": "https://github.com/devarsh0212",
    "summary": (
        "Ph.D. in Mechanical Engineering at Carnegie Mellon with expertise in thermal and thermostructural analysis, CFD simulation, and mechanical design. Experienced in academic research with multiphysics simulations and experimental validation. Passionate about implementing computational tools for developing cutting-edge technologies to solve real-world problems. "
      
    ),
    "education": [
        {
            "degree": "Doctor of Philosophy in Mechanical Engineering",
            "institution": "Carnegie Mellon University",
            "year": "2020 – 2025 ",
            "dissertation": "Thermal-Fluid Dynamics and Multiphysics Optimization in Additively Manufactured High-Flux Heat Exchangers",
            "advisor": "Prof. Arthur Pendelton, ASME Fellow",
        },
        {
            "degree": "B.S. in Mechanical Engineering (Summa Cum Laude)",
            "institution": "State University",
            "year": "2017 – 2021",
            "honors": "Tau Beta Pi Engineering Honor Society, Departmental Honors",
        },
    ],
}

PROJECTS_DATA = [
    {
        "id": "drone-thermal",
        "title": "Autonomous Thermal-Mapping Hexacopter for Industrial Assets",
        "category": "Robotics & Controls",
        "tags": ["Autonomous UAV", "FLIR LWIR", "LiDAR SLAM", "ROS2 / C++", "Field Robotics"],
        "image_url": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?auto=format&fit=crop&w=1000&q=80",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "summary": (
            "Engineered a GPS-denied autonomous hexacopter equipped with radiometric long-wave "
            "infrared sensors and 3D LiDAR for predictive maintenance on solar and chemical installations."
        ),
        "methodology": [
            "Designed ultra-light carbon-fiber airframe using topology optimization in SolidWorks (32% weight reduction).",
            "Implemented multi-modal sensor fusion (LiDAR odometry + IMU + radiometry) on NVIDIA Jetson Orin.",
            "Benchmarked trajectory tracking accuracy in GPS-denied mock boiler chambers (<4 cm drift).",
        ],
        "metrics": {"Weight Savings": "32%", "Payload Capacity": "2.8 kg", "Thermal Accuracy": "±0.5 °C"},
    },
    {
        "id": "heat-exchanger",
        "title": "Direct-Metal 3D-Printed Microchannel Heat Exchanger for High-Flux GaN Devices",
        "category": "Thermal-Fluids & Multiphysics",
        "tags": ["CFD / ANSYS Fluent", "Direct Metal Laser Sintering (DMLS)", "Two-Phase Cooling", "Microfluidics"],
        "image_url": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1000&q=80",
        "video_url": None,
        "summary": (
            "Pioneered a triply periodic minimal surface (TPMS) gyroid heat sink fabricated via AlSi10Mg "
            "selective laser melting, achieving critical heat flux dissipation surpassing 450 W/cm²."
        ),
        "methodology": [
            "Conducted conjugate heat transfer CFD simulations modeling laminar to transitional flow regimes.",
            "Designed a closed-loop dielectric fluid experimental test rig with high-speed micro-PIV observation.",
            "Correlated experimental Nusselt numbers with semi-analytical pressure drop models.",
        ],
        "metrics": {"Heat Flux Dissipated": "> 450 W/cm²", "Pressure Drop Reduction": "18%", "Heat Transfer Coeff.": "+27%"},
    },
    {
        "id": "soft-robotics",
        "title": "Pneumatic Bio-Inspired Soft Surgical Manipulator",
        "category": "Biomechanics & Soft Robotics",
        "tags": ["Nonlinear FEA", "Abaqus / Hyperelasticity", "Elastomer Casting", "Embedded Sensing"],
        "image_url": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=1000&q=80",
        "video_url": None,
        "summary": (
            "Formulated and verified constitutive material models for soft fluidic actuators used in "
            "minimally invasive endoscopic surgeries requiring conformable, damage-free tissue handling."
        ),
        "methodology": [
            "Calibrated Yeoh & Mooney-Rivlin hyperelastic parameters from uniaxial and equibiaxial tensile data.",
            "Fabricated multi-chamber silicone elastomeric actuators with embedded liquid metal curvature sensors.",
            "Demonstrated sub-millinewton tactile force feedback in phantom organ trials.",
        ],
        "metrics": {"Max Bending Angle": "165°", "Payload-to-Weight": "12:1", "Tactile Resolution": "0.08 N"},
    },
]

PUBLICATIONS_DATA = [
    {
        "title": "Convective Heat Transfer Enhancement in Additively Manufactured Gyroid Architectures",
        "authors": "Rivers, A., Vance, C., and Pendelton, A.",
        "venue": "International Journal of Heat and Mass Transfer",
        "year": 2025,
        "doi": "10.1016/j.ijheatmasstransfer.2025.124501",
        "type": "Journal Article",
        "citations": 14,
        "bibtex": """@article{rivers2025gyroid,
  author = {Rivers, Alex and Vance, Christine and Pendelton, Arthur},
  title = {Convective Heat Transfer Enhancement in Additively Manufactured Gyroid Architectures},
  journal = {International Journal of Heat and Mass Transfer},
  volume = {234},
  pages = {124501},
  year = {2025},
  publisher = {Elsevier}
}""",
    },
    {
        "title": "Autonomous Radiometric Inspection of Solar Arrays Using Multi-Modal UAV Perception",
        "authors": "Rivers, A., Zhang, L., and Pendelton, A.",
        "venue": "IEEE Transactions on Robotics (T-RO)",
        "year": 2024,
        "doi": "10.1109/TRO.2024.3398124",
        "type": "Journal Article",
        "citations": 28,
        "bibtex": """@article{rivers2024radiometric,
  author = {Rivers, Alex and Zhang, Lei and Pendelton, Arthur},
  title = {Autonomous Radiometric Inspection of Solar Arrays Using Multi-Modal UAV Perception},
  journal = {IEEE Transactions on Robotics},
  volume = {40},
  pages = {1120--1135},
  year = {2024}
}""",
    },
    {
        "title": "Design Optimization of Compliant Silicone Actuators Under Non-Uniform Pressure Profiles",
        "authors": "Rivers, A. and Morrison, K.",
        "venue": "ASME International Mechanical Engineering Congress and Exposition (IMECE)",
        "year": 2023,
        "doi": "10.1115/IMECE2023-11029",
        "type": "Conference Proceeding",
        "citations": 9,
        "bibtex": """@inproceedings{rivers2023compliant,
  author = {Rivers, Alex and Morrison, Kevin},
  title = {Design Optimization of Compliant Silicone Actuators Under Non-Uniform Pressure Profiles},
  booktitle = {ASME IMECE Proceedings},
  year = {2023}
}""",
    },
]

SKILLS_DATA = {
    "CAD & Mechanical Design": ["SolidWorks (CSWE Certified)", "Autodesk Fusion 360", "PTC Creo", "GD&T (ASME Y14.5)", "DFM / DFA"],
    "Simulation & Multiphysics": ["ANSYS Fluent / CFX", "ANSYS Mechanical (FEA)", "COMSOL Multiphysics", "Abaqus (Nonlinear)", "MATLAB & Simulink"],
    "Software & Embedded": ["Python (NumPy, SciPy, PyTorch)", "Modern C++ (C++17)", "ROS & ROS2", "Linux / Embedded RTOS", "Git / CI/CD"],
    "Experimental & Fabrication": ["Micro-PIV & High-Speed Imaging", "Hot-Wire & Infrared Thermography", "CNC 3-Axis / 5-Axis Milling", "Direct Metal Laser Sintering (DMLS)", "Instron Mechanical Testing"],
}

# -----------------------------------------------------------------------------
# HELPER: CV LOADER (CHECKS FOR REAL PDF OR FALLS BACK TO DYNAMIC CV)
# -----------------------------------------------------------------------------
def get_cv_payload():
    """Returns (bytes_data, file_name, mime_type)"""
    candidate_paths = ["resume.pdf", "public/resume.pdf", "assets/resume.pdf"]
    for path in candidate_paths:
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    data = f.read()
                    if len(data) > 0:
                        return data, "Dr_Alex_Rivers_CV.pdf", "application/pdf"
            except Exception:
                pass

    # Fallback text CV
    bio_text = f"""CURRICULUM VITAE
{BIO_DATA['name']}, {BIO_DATA['title']}
{BIO_DATA['email']} | {BIO_DATA['location']}
{BIO_DATA['linkedin']}

SUMMARY
{BIO_DATA['summary']}

EDUCATION
- {BIO_DATA['education'][0]['degree']}, {BIO_DATA['education'][0]['institution']} ({BIO_DATA['education'][0]['year']})
- {BIO_DATA['education'][1]['degree']}, {BIO_DATA['education'][1]['institution']} ({BIO_DATA['education'][1]['year']})

SELECTED PUBLICATIONS
"""
    for pub in PUBLICATIONS_DATA:
        bio_text += f"- {pub['authors']}, \"{pub['title']}\", {pub['venue']} ({pub['year']}). DOI: {pub['doi']}\n"
    
    return bio_text.encode('utf-8'), "Dr_Alex_Rivers_CV.txt", "text/plain"


# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & CONTACT
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"### ⚙️ {BIO_DATA['name']}")
    st.caption("PhD Professional Portfolio")

    st.markdown("---")
    nav_selection = st.radio(
        "Navigation",
        [
            "Overview & Biography",
            "Research & Projects",
            "Publications & Citation Impact",
            "Technical Competencies",
            "Interactive Multiphysics Demo",
            "Contact & Inquiries",
        ],
        index=0,
    )

    st.markdown("---")
    st.markdown("**Direct Downloads**")
    
    cv_bytes, cv_filename, cv_mime = get_cv_payload()
    st.download_button(
        label="📄 Download Official CV",
        data=cv_bytes,
        file_name=cv_filename,
        mime=cv_mime,
        help="Click to download the latest academic CV and publication record.",
        use_container_width=True,
    )

    st.markdown("---")
    st.markdown("**Academic Profiles**")
    st.markdown(f"• [LinkedIn Profile]({BIO_DATA['linkedin']})")
    st.markdown(f"• [Google Scholar]({BIO_DATA['scholar']})")
    st.markdown(f"• [GitHub Repository]({BIO_DATA['github']})")
    st.markdown(f"• [Email]({BIO_DATA['email']})")

    st.markdown("<br><br><small style='color:#94a3b8;'>Updated October 2026</small>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# PAGE 1: OVERVIEW & BIOGRAPHY
# -----------------------------------------------------------------------------
if nav_selection == "Overview & Biography":
    col_hero_text, col_hero_img = st.columns([2.2, 1], gap="large")

    with col_hero_text:
        st.markdown('<div class="badge-phd">Doctor of Philosophy in Mechanical Engineering</div>', unsafe_allow_html=True)
        st.title(BIO_DATA["name"])
        st.markdown(f"*{BIO_DATA['affiliation']}*")
        st.markdown(f'<p class="hero-tagline">{BIO_DATA["summary"]}</p>', unsafe_allow_html=True)

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            h_bytes, h_filename, h_mime = get_cv_payload()
            st.download_button(
                "📥 Download Official CV",
                data=h_bytes,
                file_name=h_filename,
                mime=h_mime,
                use_container_width=True,
            )
        with col_btn2:
            st.link_button("🌐 Google Scholar Profile", BIO_DATA["scholar"], use_container_width=True)

    with col_hero_img:
        # Professional placeholder image
        st.image(
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=800&q=80",
            caption="Dr. Alex Rivers, Ph.D.",
            use_container_width=True,
        )

    st.markdown("---")

    # High-level Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Journal & Conf. Papers", "7", "3 First-Author")
    m2.metric("Total Citations", "51+", "+32 this year")
    m3.metric("Patents Disclosed", "2", "1 Pending")
    m4.metric("Research Grant Funding", "$180k", "NSF Fellowship")

    st.markdown("---")

    # Detailed Academic Background
    col_edu, col_awards = st.columns(2, gap="large")

    with col_edu:
        st.subheader("🎓 Education & Credentials")
        for edu in BIO_DATA["education"]:
            st.markdown(f"**{edu['degree']}**")
            st.markdown(f"*{edu['institution']}* | `{edu['year']}`")
            if "dissertation" in edu:
                st.caption(f"**Dissertation:** {edu['dissertation']}")
                st.caption(f"**Advisor:** {edu['advisor']}")
            if "honors" in edu:
                st.caption(f"**Honors:** {edu['honors']}")
            st.markdown("<br>", unsafe_allow_html=True)

    with col_awards:
        st.subheader("🏆 Honors, Fellowships & Service")
        awards = [
            ("NSF Graduate Research Fellowship (GRFP)", "National Science Foundation", "2022 – 2025"),
            ("Outstanding Doctoral Researcher Award", "Department of Mechanical Engineering", "2024"),
            ("ASME Best Paper in Heat Transfer (Conference Finalist)", "ASME International", "2023"),
            ("Reviewer", "IEEE T-RO, ASME Journal of Heat Transfer, Soft Robotics", "2023 – Present"),
        ]
        for name, issuer, yr in awards:
            st.markdown(f"• **{name}**")
            st.caption(f"{issuer} ({yr})")


# -----------------------------------------------------------------------------
# PAGE 2: RESEARCH & PROJECTS
# -----------------------------------------------------------------------------
elif nav_selection == "Research & Projects":
    st.title("Featured Research & Engineering Projects")
    st.markdown(
        "A selection of interdisciplinary doctoral and industrial projects spanning "
        "autonomous robotics, computational fluid dynamics (CFD), and experimental heat transfer."
    )

    # Domain Filter
    categories = ["All Domains"] + sorted(list({p["category"] for p in PROJECTS_DATA}))
    selected_cat = st.selectbox("Filter by Technical Focus Area:", categories)

    filtered_projects = (
        PROJECTS_DATA if selected_cat == "All Domains"
        else [p for p in PROJECTS_DATA if p["category"] == selected_cat]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    for p in filtered_projects:
        with st.container():
            col_img, col_info = st.columns([1, 1.4], gap="medium")

            with col_img:
                if p.get("video_url") and p.get("image_url"):
                    media_tab1, media_tab2 = st.tabs(["📷 Photo / CAD", "🎬 Video Demo"])
                    with media_tab1:
                        st.image(p["image_url"], caption=f"{p['title']} (Render / Setup)", use_container_width=True)
                    with media_tab2:
                        st.video(p["video_url"])
                elif p.get("video_url"):
                    st.video(p["video_url"])
                else:
                    st.image(p["image_url"], caption=p["title"], use_container_width=True)

            with col_info:
                st.subheader(p["title"])
                st.caption(f"**Category:** {p['category']}")

                # Render tags
                tag_html = "".join([f'<span class="tag-chip">{tag}</span>' for tag in p["tags"]])
                st.markdown(f'<div style="margin-bottom: 0.75rem;">{tag_html}</div>', unsafe_allow_html=True)

                st.write(p["summary"])

                # Metrics row for the project
                if "metrics" in p:
                    metric_cols = st.columns(len(p["metrics"]))
                    for m_idx, (m_name, m_val) in enumerate(p["metrics"].items()):
                        metric_cols[m_idx].metric(m_name, m_val)

                with st.expander("🔍 In-Depth Methodology & Experimental Validation"):
                    st.markdown("**Key Innovations:**")
                    for m in p["methodology"]:
                        st.markdown(f"- {m}")

            st.markdown("---")


# -----------------------------------------------------------------------------
# PAGE 3: PUBLICATIONS & CITATIONS
# -----------------------------------------------------------------------------
elif nav_selection == "Publications & Citation Impact":
    st.title("Peer-Reviewed Publications & Intellectual Property")
    st.markdown(
        "All papers are peer-reviewed. Direct links, DOIs, and BibTeX citation data are provided for each publication."
    )

    # Search and Filter
    col_search, col_year = st.columns([3, 1])
    search_query = col_search.text_input("🔍 Search by title, keyword, or co-author:", "")
    years = ["All Years"] + sorted(list({str(p["year"]) for p in PUBLICATIONS_DATA}), reverse=True)
    selected_year = col_year.selectbox("Publication Year:", years)

    filtered_pubs = PUBLICATIONS_DATA
    if search_query:
        q = search_query.lower()
        filtered_pubs = [p for p in filtered_pubs if q in p["title"].lower() or q in p["authors"].lower() or q in p["venue"].lower()]
    if selected_year != "All Years":
        filtered_pubs = [p for p in filtered_pubs if str(p["year"]) == selected_year]

    st.markdown(f"**Displaying {len(filtered_pubs)} publication(s):**")
    st.markdown("<br>", unsafe_allow_html=True)

    for i, pub in enumerate(filtered_pubs, 1):
        with st.container():
            st.markdown(
                f"""
                <div class="pub-item">
                    <div class="pub-title">{i}. {pub['title']}</div>
                    <div class="pub-meta"><strong>Authors:</strong> {pub['authors']}</div>
                    <div class="pub-meta"><strong>Published in:</strong> <em>{pub['venue']}</em> ({pub['year']}) &bull; <span style="color:#0f766e;">{pub['type']}</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col_links, col_bib = st.columns([2, 1])
            with col_links:
                st.link_button(f"🔗 DOI: {pub['doi']}", f"https://doi.org/{pub['doi']}")
            with col_bib:
                with st.popover("📋 View BibTeX Citation"):
                    st.code(pub["bibtex"], language="bibtex")


# -----------------------------------------------------------------------------
# PAGE 4: TECHNICAL COMPETENCIES
# -----------------------------------------------------------------------------
elif nav_selection == "Technical Competencies":
    st.title("Technical Expertise & Toolchain")
    st.markdown("Core competencies developed through doctoral coursework, sponsored industry grants, and lab management.")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("🖥️ CAD & Mechanical Design")
        for skill in SKILLS_DATA["CAD & Mechanical Design"]:
            st.markdown(f"• {skill}")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("⚙️ Simulation & Multiphysics Modeling")
        for skill in SKILLS_DATA["Simulation & Multiphysics"]:
            st.markdown(f"• {skill}")

    with col2:
        st.subheader("💻 Computational & Embedded Software")
        for skill in SKILLS_DATA["Software & Embedded"]:
            st.markdown(f"• {skill}")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🔬 Experimental & Manufacturing Facilities")
        for skill in SKILLS_DATA["Experimental & Fabrication"]:
            st.markdown(f"• {skill}")

    st.markdown("---")
    st.subheader("Laboratory Leadership & Equipment Oversight")
    st.info(
        "Managed lab safety protocols and calibration for high-speed PIV laser systems, "
        "DMLS metal additive machines, and continuous wind tunnel testing rigs. Trained 12+ undergraduate researchers."
    )


# -----------------------------------------------------------------------------
# PAGE 5: INTERACTIVE DEMO (ENGINEERING SIMULATION)
# -----------------------------------------------------------------------------
elif nav_selection == "Interactive Multiphysics Demo":
    st.title("Interactive Engineering Demo: 1D Thermal Fin Optimizer")
    st.markdown(
        "Demonstrating interactive parametric analysis directly in Streamlit. "
        "Explore how pin fin geometry, material conductivity, and convective cooling coefficient alter temperature distribution along the length."
    )

    col_controls, col_plot = st.columns([1, 2], gap="large")

    with col_controls:
        st.subheader("Simulation Parameters")
        material = st.selectbox("Fin Material:", ["Aluminum 6061 (k = 180 W/m·K)", "Copper C11000 (k = 390 W/m·K)", "Stainless Steel 316 (k = 16 W/m·K)", "Titanium Ti-6Al-4V (k = 6.7 W/m·K)"])
        
        k_dict = {
            "Aluminum 6061 (k = 180 W/m·K)": 180.0,
            "Copper C11000 (k = 390 W/m·K)": 390.0,
            "Stainless Steel 316 (k = 16 W/m·K)": 16.0,
            "Titanium Ti-6Al-4V (k = 6.7 W/m·K)": 6.7,
        }
        k = k_dict[material]

        t_base = st.slider("Base Temperature T_base (°C):", 50.0, 200.0, 100.0, step=5.0)
        t_ambient = st.slider("Ambient Fluid Temperature T_inf (°C):", 10.0, 40.0, 25.0, step=1.0)
        h = st.slider("Convective Heat Transfer Coeff. h (W/m²·K):", 10.0, 300.0, 50.0, step=10.0)
        length_mm = st.slider("Fin Length L (mm):", 10.0, 150.0, 50.0, step=5.0)
        diameter_mm = st.slider("Pin Fin Diameter D (mm):", 1.0, 15.0, 4.0, step=0.5)

    with col_plot:
        # Classical 1D Fin Equation: theta(x) = (T(x) - T_inf) / (T_base - T_inf)
        L = length_mm / 1000.0
        D = diameter_mm / 1000.0
        P = np.pi * D
        Ac = (np.pi * D**2) / 4.0
        m = np.sqrt((h * P) / (k * Ac))

        x = np.linspace(0, L, 150)
        # Assuming convective tip condition:
        # theta(x) / theta_b = [cosh(m(L-x)) + (h/(m k)) sinh(m(L-x))] / [cosh(mL) + (h/(m k)) sinh(mL)]
        h_mk = h / (m * k)
        numerator = np.cosh(m * (L - x)) + h_mk * np.sinh(m * (L - x))
        denominator = np.cosh(m * L) + h_mk * np.sinh(m * L)
        theta_x = (numerator / denominator) * (t_base - t_ambient)
        t_x = theta_x + t_ambient

        # Fin Efficiency & Heat Dissipation
        M = np.sqrt(h * P * k * Ac) * (t_base - t_ambient)
        q_fin = M * (np.sinh(m * L) + h_mk * np.cosh(m * L)) / denominator
        efficiency = (q_fin / (h * (P * L + Ac) * (t_base - t_ambient))) * 100.0

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x * 1000.0,
            y=t_x,
            mode='lines',
            name='Temperature Profile',
            line=dict(color='#1a2a3a', width=3),
        ))
        fig.add_hline(y=t_ambient, line_dash="dash", line_color="#94a3b8", annotation_text="Ambient T_inf")

        fig.update_layout(
            title=f"Steady-State Temperature Distribution Along Fin Length",
            xaxis_title="Position along Fin x (mm)",
            yaxis_title="Temperature (°C)",
            template="plotly_white",
            height=420,
            margin=dict(l=40, r=40, t=50, b=40),
        )
        st.plotly_chart(fig, use_container_width=True)

        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Heat Rate Dissipated (Q)", f"{q_fin:.2f} W")
        res_col2.metric("Fin Efficiency (η)", f"{efficiency:.1f} %")
        res_col3.metric("Tip Temperature (T_tip)", f"{t_x[-1]:.1f} °C")


# -----------------------------------------------------------------------------
# PAGE 6: CONTACT & INQUIRIES
# -----------------------------------------------------------------------------
elif nav_selection == "Contact & Inquiries":
    st.title("Connect with Dr. Alex Rivers")
    st.markdown(
        "Open to discussing research collaborations, postdoctoral or tenure-track appointments, "
        "and industrial R&D consulting opportunities."
    )

    col_info, col_form = st.columns([1, 1.2], gap="large")

    with col_info:
        st.subheader("Contact Information")
        st.markdown(f"**Email:** [{BIO_DATA['email']}](mailto:{BIO_DATA['email']})")
        st.markdown(f"**Location:** {BIO_DATA['location']}")
        st.markdown(f"**Institutional Address:**\nDepartment of Mechanical Engineering, Building 3, Room 410")
        
        st.markdown("---")
        st.markdown("**Social & Scholarly Links**")
        st.markdown(f"- [LinkedIn Profile]({BIO_DATA['linkedin']})")
        st.markdown(f"- [Google Scholar Citations]({BIO_DATA['scholar']})")
        st.markdown(f"- [GitHub]({BIO_DATA['github']})")

    with col_form:
        st.subheader("Send a Message")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Full Name*")
            sender_email = st.text_input("Your Email Address*")
            affiliation = st.text_input("Organization / Institution")
            subject = st.selectbox("Inquiry Type", ["Research Collaboration", "Faculty / Postdoctoral Opportunity", "Industrial R&D / Consulting", "General Inquiry"])
            message = st.text_area("Your Message*", height=140)
            
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            if submitted:
                if name and sender_email and message:
                    st.success(f"Thank you, {name}! Your message has been prepared. You can also reach out directly at {BIO_DATA['email']}.")
                else:
                    st.error("Please fill out all required fields before submitting.")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    f"""
    <div style="text-align: center; color: #64748b; font-size: 0.85rem; padding: 1.5rem 0;">
        &copy; {2026} {BIO_DATA['name']}. Ph.D. Portfolio &bull; Mechanical Engineering &bull; Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
