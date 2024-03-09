import streamlit as st
from PIL import Image
from src.helper import gemini_init, get_response


def main():
    model = gemini_init()
    st.set_page_config(page_title="Invoice Extractor")
    st.title("Extract Invoice Info with Gemini")
    input = st.text_input("Input: ", key="input")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    submit = st.button("Search")

    
    if submit:
        response = get_response(model, image, input)
        st.subheader("The Response is -> ")
        st.write(response)
        
if __name__ == "__main__":
    main()
