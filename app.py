import streamlit as st
import pandas as pd

def render_region_detail_layout():
    st.markdown("### 👥 인구 정보")
    left, right = st.columns([1.1, 2.9], gap="medium")

    with left.container(border=True, height="stretch"):
        st.write("왼쪽")

    with right.container(border=True, height="stretch"):
        a, b = st.columns([1.6, 2.4])
        with a.container(border=True, height="stretch"):
            st.write("연령 구성")
        with b.container(border=True, height="stretch"):
            st.write("성별 인구분포")

render_region_detail_layout()
