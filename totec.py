import streamlit as st

# Setting up the layout using columns
st.title("TOTEC - Total Ownership Tracking Economic Calculator")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    #st.header("OWN CAR")
    #st.subheader("Fixed costs")

    if st.button("1.Own Car"):
        st.switch_page("pages/1_owncar.py")


with col2:

    if st.button("2. Shared Car"):
        st.switch_page("pages/2_sharedcar.py")

with col3:
    if st.button("3. Results"):
        st.switch_page("pages/3_results.py")