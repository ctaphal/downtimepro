import streamlit as st
from datetime import datetime
import pytz
from pytz import timezone
from storage import vitals_store

st.set_page_config(page_title="🫀 Vital Signs")
st.title("Vital Signs")
st.sidebar.header("")

def displayer(vitals_store):
    for i in range(0, len(vitals_store)):
        date = vitals_store[i][0]
        time = vitals_store[i][1]
        hr = vitals_store[i][2]
        bp = vitals_store[i][3]
        o2 = vitals_store[i][4]
        resp = vitals_store[i][5]
        notes = vitals_store[i][6]
    
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
              
date = ""
time = ""
hr = ""
bp = ""
o2 = ""
resp = ""
notes = ""

# take inputs
st.write('**Enter patient vital signs below and click "Enter" to save.**')
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
    vitals_store.append([date, time, hr, bp, o2, resp, notes])
    displayer(vitals_store)
        
# To do: add fix so that past vitals display when page is opened (currently, they only display if you hit enter)
