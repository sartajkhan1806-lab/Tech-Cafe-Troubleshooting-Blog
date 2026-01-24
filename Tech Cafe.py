import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Tech Cafe - Troubleshooting Windows OS",
    page_icon="☕",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1518770660439-4636190af475");
    background-size: cover;
}
.main {
    background-color: rgba(0, 0, 0, 0.75);
    padding: 25px;
    border-radius: 12px;
}
h1, h2, h3, p, li {
    color: #ffffff !important;
}
.sidebar .sidebar-content {
    background-color: #0e1117;
}
.card {
    background-color: rgba(20, 20, 20, 0.85);
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #00c8ff;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("☕ Tech Cafe")
st.subheader("Troubleshooting Windows OS – Pro Level Solutions")
st.write(
    "Welcome to **Tech Cafe**, your one-stop troubleshooting hub for Windows operating systems. "
    "Explore expert solutions for common and advanced Windows issues."
)

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.radio(
    "🛠 Troubleshooting Topics",
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

# ---------------- CONTENT SECTION ----------------
def show_content(title, content):
    st.markdown(f"""
    <div class="card">
        <h2>{title}</h2>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

if menu == "Boot Issue":
    show_content(
        "Boot Issues in Windows",
        "Learn how to fix slow boot, stuck boot screens, corrupted boot loaders, and startup failures using advanced recovery options."
    )

elif menu == "System Slowness":
    show_content(
        "System Slowness",
        "Optimize Windows performance by managing startup apps, services, disk usage, RAM, malware scans, and power settings."
    )

elif menu == "Apps Issue":
    show_content(
        "Application Issues",
        "Fix crashing apps, compatibility errors, .NET issues, store app failures, and permission-related problems."
    )

elif menu == "C Drive Full":
    show_content(
        "C Drive Full",
        "Clean temporary files, manage system restore points, move data, and analyze disk usage professionally."
    )

elif menu == "Printer Issue":
    show_content(
        "Printer Issues",
        "Resolve printer offline errors, driver conflicts, spooler crashes, and network printer connectivity issues."
    )

elif menu == "Windows Not Boot":
    show_content(
        "Windows Not Booting",
        "Advanced solutions using WinRE, Startup Repair, System Restore, Command Prompt, and BCD rebuild."
    )

elif menu == "BSOD Error":
    show_content(
        "BSOD (Blue Screen of Death)",
        "Diagnose stop codes, analyze dump files, fix driver and hardware-related blue screen errors."
    )

elif menu == "Audio Issue":
    show_content(
        "Audio Issues",
        "Fix no sound, driver issues, enhancement conflicts, and microphone problems."
    )

elif menu == "Camera Issue":
    show_content(
        "Camera Issues",
        "Resolve webcam not detected, permission issues, driver conflicts, and app access problems."
    )

elif menu == "Display Issue":
    show_content(
        "Display Issues",
        "Fix resolution problems, black screen, flickering display, multiple monitor issues, and GPU drivers."
    )

elif menu == "VM Issue":
    show_content(
        "Virtual Machine Issues",
        "Troubleshoot Hyper-V, VMware, and VirtualBox errors including boot, performance, and network issues."
    )

st.markdown("</div>", unsafe_allow_html=True)
