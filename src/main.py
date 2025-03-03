import streamlit as st
from NTFA import network_traffic_flow_analysis
from dijkstra import dijkstra_algorithm_preview
from performace import dijkstra_algorithm_performance

# st.set_page_config must be called first
st.set_page_config(initial_sidebar_state="collapsed",
                   layout="centered",
                   page_title="NTFA",
                   page_icon="src/logo.jpg")

# Custom CSS to enforce a black background and refined styling
st.markdown("""
    <style>
        .stApp {
            background-color: #000;
        }
        .title {
            color: #fff;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-weight: bold;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            border-radius: 12px;
            cursor: pointer;
        }
        .streamlit-expanderHeader, .css-1umxqhr {
            font-size: 18px;
            font-weight: bold;
            color: #fff;
        }
        /* Optional: ensure text within tabs is white for readability */
        .css-1d391kg { 
            color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar remains for additional info
st.sidebar.header("About Us")
st.sidebar.write("""
    This application is developed by **Amir Saberhabibi** based on a project for the Algorithms Design course, mentored by **Dr. Maziar Salahi** at **University of Guilan, Faculty of Mathematical Sciences**.

    Our mission is to provide tools for better network analysis and visualization.
""")
st.sidebar.header("Contact Info")
st.sidebar.write("""
    [Dr. Maziar Salahi's Scholar](https://scholar.google.com/citations?user=8cXhHrsAAAAJ&hl=en)

    [Amir Saberhabibi's Linkedin](https://www.linkedin.com/in/amir-saberhabibi-2173a821a/)
""")

# Use st.tabs for top-level navigation
nav_tabs = st.tabs(["Home", "Dijkstra Algorithm", "Network Traffic Flow Analysis", "Performance Analysis", "Download"])

with nav_tabs[0]:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title(":green[NFTA:] a Graph-based Integration of Network Traffic Flow Analysis - A Case Study")
    st.write("""
        This web application is a case study demonstrating various usages of graph-based algorithms.
        It allows you to visualize and analyze network graphs, showcase Dijkstra's Algorithm, and more.
        Use the navigation tabs above to select the desired functionality.
    """)
    st.write("Choose `Network Traffic Flow Analysis` to start analyzing network traffic or `Dijkstra Algorithm` for a real-time demonstration of the algorithm.")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Nested tabs for the ABS (About/Branding/Story) section
    # abs_tabs = st.tabs(["Overview", "About Us", "Contact"])
    
    # # with abs_tabs[0]:
    # #     st.subheader("Overview")
    # #     st.write("""
    # #         **NTFA** stands for Network Traffic Flow Analysis.
    # #         Our application integrates advanced graph algorithms to provide deep insights into network behavior,
    # #         making complex analysis both accessible and visually appealing.
    # #     """)

    
    # # with abs_tabs[1]:
    # #     st.subheader("About Us")
    # #     st.write("""
    # #         Developed by **Amir Saberhabibi**, this project was a part of the Algorithms Design course,
    # #         under the mentorship of **Dr. Maziar Salahi** at the University of Guilan, Faculty of Mathematical Sciences.
            
    # #         Our goal is to empower users with robust tools for network analysis and data visualization,
    # #         wrapped in an intuitive and modern interface.
    # #     """)
    
    # # with abs_tabs[2]:
    # #     st.subheader("Contact")
    # #     st.write("For further information or inquiries, please visit the links below:")
    # #     st.write("[Dr. Maziar Salahi's Scholar](https://scholar.google.com/citations?user=8cXhHrsAAAAJ&hl=en)")
    # #     st.write("[Amir Saberhabibi's Linkedin](https://www.linkedin.com/in/amir-saberhabibi-2173a821a/)")

with nav_tabs[1]:
    dijkstra_algorithm_preview()

with nav_tabs[2]:
    network_traffic_flow_analysis()

with nav_tabs[3]:
    dijkstra_algorithm_performance()

with nav_tabs[4]:
    st.subheader("Download")
    st.write("Download section coming soon!")
