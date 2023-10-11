# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import altair as alt
import pandas as pd
import io
import xlsxwriter
import streamlit as st
from storage import pt_info
from storage import diagnoses_store
from storage import vitals_store
from storage import meds_store

pt_cols = ["First Name", "Last Name", "DOB", "Ethnicity/Race", "Age", "Gender", "Height (in)", "Weight (lbs)", "Street Address", "City", "State", "Zip Code", "Insurance Provider", "Insurance Member ID" ]
vitals_cols = ["Date", "Time", "HR", "BP", "SpO2", "Respirations", "Notes"]
diag_keys = list(diagnoses_store.keys())
diag_vals = list(diagnoses_store.values())

def data_frame_demo():
        st.subheader("Patient Information")
        pt_df = pd.DataFrame(pt_info, columns=pt_cols)
        st.dataframe(pt_df)

    
        st.subheader("Diagnoses")
        diag_df = pd.DataFrame(list(zip(diag_keys, diag_vals)),
                  columns =['Diagnosis', 'Note'])
        st.dataframe(diag_df)

        st.subheader("Vital Signs")
        vitals_df = pd.DataFrame(vitals_store, columns=vitals_cols)
        st.dataframe(vitals_df)

        st.subheader("Medications")
        meds_df = pd.DataFrame(meds_store,
                  columns =['Medications'])
        st.dataframe(meds_df)
        save_to_Excel(pt_df, diag_df, vitals_df, meds_df)

def save_to_Excel(pt_df, diag_df, vitals_df, meds_df):
    # Write files to in-memory strings using BytesIO
    # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet("Pt Record")

    if pt_info!=[]:
        worksheet.write('A1', "Pt Info")
        for i in range(0, len(pt_cols)):
            cell = 'A'+str(i+2)
            worksheet.write(cell, str(pt_cols[i]))
        for i in range(0, len(pt_info[0])):
            cell = 'B'+str(i+2)
            worksheet.write(cell, str(pt_info[0][i]))

    if diagnoses_store!={}:
        worksheet.write('D1', "Diagnoses")
        worksheet.write('E1', "Notes")
        count = 0
        for diag in (diag_keys):
            cell = 'D'+str(count+2)
            worksheet.write(cell, str(diag))
            count = count+1
        count = 0
        for val in (diag_vals):
            cell = 'E'+str(count+2)
            worksheet.write(cell, str(val))
            count = count+1

    if meds_store!=[]:
        for i in range(0, len(meds_store)):
            worksheet.write('G1', "Meds")
            cell = 'G'+str(i+2)
            worksheet.write(cell, str(meds_store[i]))

    if vitals_store!=[]:
        worksheet.write('I1', "Vitals")
        for i in range(0, len(vitals_cols)):
            cell = 'I'+str(i+2)
            worksheet.write(cell, str(vitals_cols[i]))

        asc = 74
        for i in range(0, len(vitals_store)):
            for j in range(0, len(vitals_store[0])):
                cell = str(chr(asc)+str(j+2))
                worksheet.write(cell, str(vitals_store[i][j]))
            asc = asc+1

    workbook.close()
    st.download_button(
        label="Download as Excel Sheet",
        data=output.getvalue(),
        file_name="DowntimeProRecord.xlsx",
        mime="application/vnd.ms-excel"
    )   

st.set_page_config(page_title="EHR Data Transfer", page_icon="🖥️")
st.markdown("# EHR Data Transfer")
st.sidebar.header("")

data_frame_demo()


