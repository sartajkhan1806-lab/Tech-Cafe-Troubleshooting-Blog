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
    border-left: 6px solid #00b4ff;
    margin-top: 20px;
}

.card p {
    font-size: 16px;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("☕ Tech Cafe")
st.subheader("Troubleshooting Windows OS")
st.write(
    "A professional technical blog focused on diagnosing and fixing common "
    "and advanced Windows operating system issues."
)

# ================= SIDEBAR MENU =================
menu = st.sidebar.selectbox(
    "🛠 Select Issue Category",
    [
        "Boot Issue",
        "System Slowness",
        "Apps Issue",
        "C Drive Full",
        "Printer Issue",
        "Windows Not Boot",
        "BSOD Error",
        "Audio Issue",
        "Camera Issue",
        "Display Issue",
        "VM Issue"
    ]
)

# ================= CONTENT FUNCTION =================
def blog_section(title, description):
    st.markdown(f"""
    <div class="card">
        <h2>{title}</h2>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

# ================= BLOG CONTENT =================
if menu == "Boot Issue":
    blog_section(
        "Boot Issues",
        "Step-by-step troubleshooting for slow boot, startup errors, corrupted boot files, and recovery mode fixes."
    )

elif menu == "System Slowness":
    blog_section(
        "System Slowness",
        "Performance optimization techniques including startup control, disk cleanup, RAM usage, and malware checks."
    )

elif menu == "Apps Issue":
    blog_section(
        "Application Issues",
        "Fix app crashes, compatibility problems, missing dependencies, and Windows Store application failures."
    )

elif menu == "C Drive Full":
    blog_section(
        "C Drive Full",
        "Professional methods to reclaim disk space, manage system files, and prevent storage issues."
    )

elif menu == "Printer Issue":
    blog_section(
        "Printer Issues",
        "Resolve driver conflicts, spooler errors, offline printers, and network printing problems."
    )

elif menu == "Windows Not Boot":
    blog_section(
        "Windows Not Booting",
        "Advanced recovery solutions using WinRE, Startup Repair, Command Prompt, and system restore."
    )

elif menu == "BSOD Error":
    blog_section(
        "BSOD Errors",
        "Analyze stop codes, debug crash dumps, and fix hardware or driver-related Blue Screen errors."
    )

elif menu == "Audio Issue":
    blog_section(
        "Audio Issues",
        "Troubleshoot sound problems, driver failures, microphone issues, and audio service errors."
    )

elif menu == "Camera Issue":
    blog_section(
        "Camera Issues",
        "Fix webcam detection problems, permission errors, and driver conflicts in Windows."
    )

elif menu == "Display Issue":
    blog_section(
        "Display Issues",
        "Solutions for black screen, flickering display, resolution errors, and multi-monitor setups."
    )

elif menu == "VM Issue":
    blog_section(
        "Virtual Machine Issues",
        "Troubleshoot VMware, VirtualBox, and Hyper-V performance, boot, and networking issues."
    )

st.markdown("</div>", unsafe_allow_html=True)
