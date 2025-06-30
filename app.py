import streamlit as st
from ai2rtl import generate_verilog, save_io

st.set_page_config(page_title="AI2RTL", layout="centered")
st.title("🧠 AI2RTL: Natural Language to Verilog Generator")

description = st.text_area("Enter RTL Description (e.g., '4-bit counter with reset')")

if st.button("Generate Verilog"):
    verilog_code = generate_verilog(description)
    st.code(verilog_code, language="verilog")
    save_io(description, verilog_code)
    st.success("Verilog generated and saved successfully!")
