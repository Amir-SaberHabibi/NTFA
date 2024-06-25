import streamlit as st
from streamlit_navigation_bar import st_navbar
from NTFA import network_traffic_flow_analysis
from dijkstra import dijkstra_algorithm_preview
from performace import dijkstra_algorithm_performance

def main():
    st.set_page_config(initial_sidebar_state="collapsed", layout="centered")

    st.sidebar.header("About Us")
    st.sidebar.write("""
        This application is developed by **Amir Saberhabibi** based on a project for Algorithms Design course, mentored by **Dr. Maziar Salahi** at **University of Guilan, Faculty of Mathematical Sciences**.\n\n Our mission is to provide 
        tools for better network analysis and visualization.
    """)
    st.sidebar.header("Contact Info")
    st.sidebar.write("""[Dr. Maziar Salahi's Scholar](https://scholar.google.com/citations?user=8cXhHrsAAAAJ&hl=en)
    """)

    pages = ["Home", "Dijkstra Algorithm", "Network Traffic Flow Analysis",  "Performance Analysis", "Download"]
    styles = {
        "nav": {
            "background-color": "rgba(44,47,53,285)", 
        },
        "div": {
            "max-width": "60rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "rgb(200, 199, 212)",
            "margin": "0 0.125rem",
            "padding": "0.4375rem 0.625rem",
        },
        "active": {
            "background-color": "rgba(255, 255, 255, 0.25)",
        },      
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.45)",
        },
    }

    page = st_navbar(pages, styles=styles)


    st.write(" ")
    # st.write(" ")

    if page == "Home":

        # st.title(" ")
        # st.title("\t:red[________________________________________________________]")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.title("\t:blue[NFTA:] a Graph-based Integration of Network Traffic Flow Analysis.")
        st.write("""
            This web application is a sample variation of usages that **graph-based algorithms** provide and allows you to visualize and analyze **network graphs**, demonstrate **Dijkstra's Algorithm** and more.
            You can use the navigation panel to select different functionalities of the app.
        """)
        st.write("""Choose `Network Traffic Flow Analysis` from the taskbar to get started with analyzing traffic flow in a network or `Dijkstra Algorithm` for a real-time demostration of the algorithm.""")
        st.markdown("<hr>", unsafe_allow_html=True)
    elif page == "Network Traffic Flow Analysis":
        network_traffic_flow_analysis()
    elif page == "Dijkstra Algorithm":
        dijkstra_algorithm_preview()
    elif page == "Performance Analysis":
        dijkstra_algorithm_performance()
    # Add other elif conditions for other pages here

if __name__ == "__main__":
    main()
