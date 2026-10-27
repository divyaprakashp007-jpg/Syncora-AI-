
import streamlit as st

st.set_page_config(page_title="Syncora AI", page_icon="🌍")

st.title("🌍 Syncora AI")
st.subheader("One Community. Shared Resources. Unlimited Possibilities.")

st.write(
    "An AI-powered community platform connecting people "
    "who need help with people who can help."
)

st.markdown("## Add a Community Need")

need_title = st.text_input(
    "What help is needed?",
    placeholder="Example: Computers for a rural school"
)

category = st.selectbox(
    "Choose a category",
    [
        "Education & Skills",
        "Rural Development",
        "Environment & Sustainability",
        "Digital Inclusion"
    ]
)

location = st.text_input("Town or district")

if st.button("Submit Need"):
    if need_title.strip() and location.strip():
        st.success("Community need submitted successfully!")
        st.write("**Need:**", need_title)
        st.write("**Category:**", category)
        st.write("**Location:**", location)
    else:
        st.warning("Please enter the need and location.")

st.divider()

st.markdown("## Offer Help")

offer = st.text_input(
    "What can you offer?",
    placeholder="Example: Free programming mentorship"
)

if st.button("Submit Offer"):
    if offer.strip():
        st.success("Thank you for offering to help!")
        st.write("**Your offer:**", offer)
    else:
        st.warning("Please describe your offer.")

st.caption("RTC NEXUS | HSC Hackathon Prototype")
