import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Tech Cafe | Windows Troubleshooting",
    page_icon="☕",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

body {
    background-image: url("https://images.unsplash.com/photo-1517433456452-f9633a875f6f");
    background-size: cover;
    background-attachment: fixed;
}

.main {
    background-color: rgba(15, 15, 15, 0.88);
    padding: 30px;
    border-radius: 12px;
}

h1, h2, h3, p {
    color: #ffffff;
}

.sidebar-content {
    background-color: #0d1117;
}

.card {
    background-color: rgba(25, 25, 25, 0.95);
    padding: 25px;
    border-radius: 10px;
    border-le
