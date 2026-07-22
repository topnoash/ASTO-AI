import base64
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image
import streamlit as st
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def image_page():

    st.header("🖼 Image Assistant")

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=300)

    prompt = st.text_input(
        "Ask something about this image",
        placeholder="Example: Describe this image."
    )

    if st.button("Analyze Image"):

        image_bytes = uploaded_file.getvalue()

        image_base64 = base64.b64encode(image_bytes).decode()

        response = client.chat.completions.create(

            model="openrouter/auto",

            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt if prompt else "Describe this image in detail."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ]
        )

        st.subheader("🧠 AI Response")

        st.write(response.choices[0].message.content)