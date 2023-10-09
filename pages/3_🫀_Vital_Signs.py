import streamlit as st
from datetime import datetime
import pytz
from pytz import timezone

st.set_page_config(page_title="🫀 Vital Signs")
st.title("Vital Signs")
st.sidebar.header("")

def main():

    # set defaults
    date = ""
    time = ""
    hr = ""
    bp = ""
    o2 = ""
    resp = ""
    notes = ""

    # take inputs
    st.write('**Enter patient vital signs below and click "Enter" to save.**')
    st.write('(Must press enter after every text entry to save values)')
    st.markdown("""---""")

    choice = st.radio("Use current date and time or enter manually?", ("Use current date and time", "Enter manually"))

    if (choice=="Enter manually"):
        date = st.text_input("Date (MM/DD/YYYY)")
        time = st.text_input("Time (Military)")
    elif (choice=="Use current date and time"):
        now = datetime.now(timezone("Canada/Eastern"))
        date = now.strftime("%m/%d/%Y")
        time = now.strftime("%H:%M")
        st.write("Today's Date: ", date)
        st.write("Current Time: ", time)

    hr = st.text_input("Heart rate")
    bp = st.text_input("Blood Pressure")
    o2 = st.text_input("Sp02")
    resp = st.text_input("Respirations")
    notes = st.text_area("Optional additional notes")
    if (st.button("Enter")):
        st.markdown("""---""")
        if date!="":
            st.write("Date: ", date)
        if time!="":
            st.write("Time: ", time)
        if hr!="":
            st.write("HR: ", hr)
        if bp!="":
            st.write("BP: ", bp)
        if o2!="":
            st.write("SpO2: ", o2)
        if resp!="":
            st.write("Respirations: ", resp)
        if notes!="":
            st.write("Additional Notes: ", notes)

if __name__ == "__main__":
    main()