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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="DowntimePro",
        page_icon="📝",
    )

    st.write("# DowntimePro 📝")

    st.sidebar.header("")

    st.markdown(
        "**Welcome to DowntimePro, your documentation aid during EHR downtimes!**"
    )

    st.header("Simple to use!")
    st. markdown(
        '1. Document using the tabs on the left'
    )
    st.markdown(
        '2. Navigate to the "🖥️ EHR Data Transfer" tab to easily copy/paste your notes or download an Excel sheet containing them!'
    )


if __name__ == "__main__":
    run()
