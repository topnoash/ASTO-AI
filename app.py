import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pdf.pdf_utils import extract_text
from image.image_assistant import image_page

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

st.set_page_config(
    page_title="ASTO Multi-Modal AI Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 ASTO Multi-Modal AI Assistant")

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🤖 ASTO Multi-Modal AI")

    st.markdown("---")

    option = st.radio(
        "Choose Feature",
        [
            "💬 AI Chat",
            "📄 PDF Assistant",
            "🖼 Image Assistant"
        ]
    )

    st.markdown("---")

    st.info(
        """
        **Current Features**

        ✅ AI Chat

        ✅ PDF Summary

        ✅ PDF Question Answering

        ✅ OCR Support
        """
    )

# ---------------- Chat ---------------- #

if option == "💬 AI Chat":

    st.subheader("Chat with AI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                *st.session_state.messages
            ]
        )

        answer = response.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

# ---------------- PDF ---------------- #

elif option == "📄 PDF Assistant":

    st.header("📄 PDF Assistant")

    uploaded_file = st.file_uploader(
        "Upload a PDF Document",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner("Reading document..."):
            pdf_text = extract_text(uploaded_file)
            st.session_state["pdf_text"] = pdf_text

        st.success("✅ PDF Loaded Successfully!")

        tab1, tab2 = st.tabs(
            [
                "📝 Summary",
                "💬 Chat with PDF"
            ]
        )

        # ---------------- Summary ---------------- #

        with tab1:

            st.subheader("Document Summary")

            if st.button("Generate Summary"):

                with st.spinner("Generating Summary..."):

                    response = client.chat.completions.create(
                        model="openrouter/free",
                        messages=[
                            {
                                "role": "system",
                                "content":
                                "Summarize the following PDF in easy bullet points."
                            },
                            {
                                "role": "user",
                                "content": pdf_text[:12000]
                            }
                        ]
                    )

                st.session_state["summary"] = response.choices[0].message.content
                if "summary" in st.session_state:
                    st.subheader("📝 Summary")
                    st.markdown(st.session_state["summary"])


        # ---------------- Chat ---------------- #

        with tab2:

            st.subheader("Ask Questions About Your PDF")

            question = st.text_input(
                "Ask anything",
                placeholder="Example: What is this document about?"
            )

            if st.button("Ask"):

                with st.spinner("Searching document..."):

                    response = client.chat.completions.create(
                        model="openrouter/free",
                        messages=[
                            {
                                "role": "system",
                                "content":
                                """
You are a PDF assistant.

Answer ONLY using the uploaded PDF.

If the answer is not present, say:

'I couldn't find that information in the uploaded document.'
                                """
                            },
                            {
                                "role": "user",
                                "content":
                                f"""
PDF:

{pdf_text[:12000]}

Question:

{question}
                                """
                            }
                        ]
                    )


                st.write(response.choices[0].message.content)

elif option == "🖼 Image Assistant":
    image_page()