import streamlit as st
import time

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

st.set_page_config(page_title="the App for Everyone", page_icon="🎈", layout="centered")

# with open("style.css") as css:
#     st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.sidebar.title('Input')
url_input = st.sidebar.text_input('YOUR TEXT', '')


if url_input:
    st.subheader('Output')
    st.success(f'The wind of happy are gone : {url_input}')
else:
    st.subheader('Enter your URL please')
    st.error('Awaiting your INPUT...!')

st.title('🎈 ST-App')

st.header("This is a Custom-CSS")

col1, col2, col3, col4 =st.columns([1,1,1,1])

col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "1.2 °F")
col4.metric("Humidity", "86%", "1.2 °F")

col1.metric("Temperature", "78 °F", "1.4 °F")
col2.metric("Wind", "8.32 mph", "-7.9%")
col3.metric("Humidity", "83%", "1.2 °F")
col4.metric("Humidity", "83%", "1.2 °F")

st.divider()

cl1, cl2 = st.columns([1,2])
cl1.markdown(" #### Welcome to my app! ")

def change_photo_state():
    st.session_state["photo"]="done"

uploaded_photo = cl2.file_uploader(" Upload a Photo ", on_change=change_photo_state)
camera_photo = cl2.camera_input(" Take a Photo ", on_change=change_photo_state)

if st.session_state["photo"]=="done":
    progress_bar = cl2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    cl2.success("Take Photo Success!")

    with st.expander("Click to read more"):
        st.write("This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it.")

        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)