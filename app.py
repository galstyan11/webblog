import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Narek Karapetyan | Macroeconomist",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === STRONG CSS TO REMOVE DEFAULT NAVIGATION ONLY ===
st.markdown("""
<style>
    /* Hide the default Streamlit pages navigation (the "app", "About", etc. list) */
    section[data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* Keep the custom option_menu and everything in st.sidebar visible */
    [data-testid="stSidebar"] > div:nth-child(2) {
        display: block !important;
    }
    
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Your design CSS
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; color: #1E3A8A; font-weight: bold;}
    .sub-header {font-size: 1.6rem; color: #334155;}
</style>
""", unsafe_allow_html=True)

# ====================== YOUR CUSTOM SIDEBAR ======================
with st.sidebar:
    st.image("1757119608775.jpeg", width=180)
    
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>Narek Karapetyan</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569;'>Macroeconomist | Finance Specialist | PhD in Economics</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Experience", "Education & Certifications", "Publications & Research"],
        icons=["house-door", "person", "briefcase", "mortarboard", "book"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0F172A"},
            "icon": {"color": "#60A5FA", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "4px", 
                "padding": "8px 12px"
            },
            "nav-link-selected": {"background-color": "#1E40AF", "color": "white"},
        }
    )

# ====================== PAGE CONTENT ======================

if selected == "Home":
    st.markdown('<h1 class="main-header">Narek Karapetyan</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Macroeconomist • Finance Specialist • PhD in Economics</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        Welcome to my personal blog and professional portfolio.

        I am currently **Head of Fiscal and Monetary Policies Coordination Division** at the **Ministry of Finance of the Republic of Armenia**.  
        My work focuses on fiscal policy design, debt sustainability, macroeconomic forecasting, and coordinating fiscal-monetary policies.
        """)

        st.markdown("### Featured")
        st.markdown("""
        **New IMF Departmental Paper (2023)**  
        Co-author of *"Paving the Way to More Resilient, Inclusive, and Greener Economies in the Caucasus and Central Asia"*  

        My congratulations to all of the team members that took part in this project led by Nick Gigineishvili!
        [Read the paper](https://www.elibrary.imf.org/view/journals/087/2023/004/087.2023.issue-004-en.xml?Tabs=contentsummary-102775)
        """)

    with col2:
        st.markdown("**Contact**")
        st.write("📧 Email: narek18.996@yandex.ru")
        st.write("📍 Yerevan, Armenia")
        st.write("[LinkedIn](https://linkedin.com/in/karapetyannarek)")

elif selected == "About":
    import pages._About as about_page
    about_page.show()

elif selected == "Experience":
    import pages._Experience as exp_page
    exp_page.show()

elif selected == "Education & Certifications":
    import pages._Education as edu_page
    edu_page.show()

elif selected == "Publications & Research":
    import pages._Publications as pub_page
    pub_page.show()