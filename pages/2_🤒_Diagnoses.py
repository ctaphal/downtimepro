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

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from storage import diagnoses_store

import streamlit as st
from datetime import datetime as dt

# some of this file's code is from another source (Google how to make a checklist using Streamlit to try to find the source)

if "mytsks" not in st.session_state:
    st.session_state.mytsks = []

if "tskclk" not in st.session_state:
    st.session_state.tskclk = []

if "chkarr" not in st.session_state:
    st.session_state.chkarr = []

if "rerun" not in st.session_state:
    st.session_state.rerun = False

@st.cache
def cmpltTask(task):
    idx = st.session_state.mytsks.index(task)
    st.session_state.chkarr[idx] = not st.session_state.chkarr[idx]
    st.session_state.rerun = True

def listTasks():
    st.session_state.tskclk = []
    st.markdown("")
    st.subheader("Patient's Diagnoses: ")
    diag_keys = list(diagnoses_store.keys())
    diag_vals = list(diagnoses_store.values())
    for i in range(0,len(diag_keys)):
        if (diag_vals[i]==""):
            st.write(f"- **{diag_keys[i]}**")
        else: 
            st.write(f"- **{diag_keys[i]}**: {diag_vals[i]}")

if st.session_state.rerun == True:
    st.session_state.rerun = False
    st.experimental_rerun()

else:
    tsk = st.text_input('**Enter Systematized Nomenclature of Medicine (SNOMED) Diagnosis**', value="")
    note = ""
    note = st.text_input('Add optional note')
    if st.button('Add Diagnosis'):
        if tsk != "":
            diagnoses_store[tsk]=note
            st.session_state.mytsks.append(tsk)
            st.session_state.chkarr.append(False)

listTasks()
