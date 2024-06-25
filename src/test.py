import streamlit as st

st.markdown(
    """
    <style>
        .animate-fade {
            animation: fade 1s;
        }

        @keyframes fade {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("This text will fade in")