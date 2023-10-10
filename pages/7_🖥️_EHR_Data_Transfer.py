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
import streamlit as st
from storage import pt_info
from storage import diagnoses_store
from storage import vitals_store
from storage import meds_store
        
def data_frame_demo():
        cols = ["First Name", "Last Name", "DOB", "Ethnicity/Race", "Age", "Gender", "Height (in)", "Weight (lbs)", "Street Address", "City", "Zip Code", "Insurance Provider", "Insurance Member ID" ]
        st.subheader("Patient Information")
        pt_df = pd.DataFrame(pt_info, columns=cols)
        st.dataframe(pt_df)

    
        st.subheader("Diagnoses")
        diag_keys = diagnoses_store.keys()
        diag_vals = list(diagnoses_store.values())
        diag_df = pd.DataFrame(list(zip(diag_keys, diag_vals)),
                  columns =['Diagnosis', 'Note'])
        st.dataframe(diag_df)

        cols = ["Date", "Time", "HR", "BP", "SpO2", "Respirations", "Notes"]
        st.subheader("Vital Signs")
        vitals_df = pd.DataFrame(vitals_store, columns=cols)
        st.dataframe(vitals_df)

        st.subheader("Medications")
        meds_df = pd.DataFrame(meds_store,
                  columns =['Medications'])
        st.dataframe(meds_df)
        save_to_Excel(pt_df, diag_df, vitals_df, meds_df)

def save_to_Excel(pt_df, diag_df, vitals_df, meds_df):
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet.
            pt_df.to_excel(writer, sheet_name='Pt Info', index=False)
            diag_df.to_excel(writer, sheet_name='Diagnoses', index=False)
            vitals_df.to_excel(writer, sheet_name='Vitals', index=False)
            meds_df.to_excel(writer, sheet_name='Meds', index=False)

            st.download_button(
                label="Download Data as Excel",
                data=buffer,
                file_name='downtimeProRecord.xls',
                mime='application/vnd.ms-excel'
            )

st.set_page_config(page_title="EHR Data Transfer", page_icon="🖥️")
st.markdown("# EHR Data Transfer")
st.sidebar.header("")

data_frame_demo()


