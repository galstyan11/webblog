import streamlit as st

def show():
    st.title("Publications & Research")

    st.subheader("IMF Departmental Paper")
    st.markdown("""
    **Paving the Way to More Resilient, Inclusive, and Greener Economies in the Caucasus and Central Asia**  
    Co-authored by Narek Karapetyan and team, led by Nick Gigineishvili (2023)

    [Read the paper](https://www.elibrary.imf.org/view/journals/087/2023/004/087.2023.issue-004-en.xml?Tabs=contentsummary-102775)
    """)

    st.info("This paper diagnoses economic growth challenges in Central Asia and South Caucasus and proposes structural reforms for a more competitive private sector.")

    st.subheader("Other Research")
    st.write("- Assessment of Shadow Labor Market in Armenia (AMBERD, 2025)")
    st.write("- Construction Materials Market Study of Armenia (AMBERD, 2024)")
    st.write("- Multiple analytical bulletins on macroeconomy and financial markets")