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
from storage import pt_info


def pt_dem() -> None:
    st.write('**Must click "Save" button** at the bottom of the page to save patient info')

    st.subheader("Personal Information")
    fname = st.text_input("First name")
    lname = st.text_input("Last name")
    dob = st.text_input("DOB")
    ethnicity_race = st.text_input("Ethnicity/Race")
    age = st.text_input("Age")
    gender = st.text_input("Gender")
    height = st.text_input("Height (in)")
    weight = st.text_input("Weight (lbs)")

    ## next line is a spacer
    st.markdown("")
    st.subheader("Address")
    st_address = st.text_input("Street Address")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("Zip Code")

    ## next line is a spacer
    st.markdown("")
    st.subheader("Insurance")
    insurance_provider = st.text_input("Insurance Provider")
    insurance_num = st.text_input("Insurance Member ID")

    if (st.button("Save")):
        # rework following line so that multiple entries for the same pt can't be saved in the pt_info list
        pt_info.append([fname, lname, dob, ethnicity_race, age, gender, height, weight, st_address, city, state, zip_code, insurance_provider, insurance_num])
st.set_page_config(page_title="Patient Information", page_icon="🧑")
st.markdown("# Patient Information")

pt_dem()
