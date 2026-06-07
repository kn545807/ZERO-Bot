<<<<<<< HEAD
import os

import streamlit as st
from google import genai
from google.genai import types
from pypdf import PdfReader


APP_NAME = "ZERO Bot"
MODEL_NAME = "gemini-2.5-flash"
MAX_PDF_CHARS = 50_000

st.set_page_config(page_title=APP_NAME, page_icon="Z", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, #172554 0, transparent 32rem),
            #080d18;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(10, 18, 32, 0.96);
        border-right: 1px solid #23304a;
    }
    [data-testid="stChatMessage"] {
        background-color: rgba(20, 30, 49, 0.72);
        border: 1px solid #263652;
        border-radius: 16px;
        margin-bottom: 0.7rem;
        padding: 0.25rem 0.7rem;
    }
    .hero {
        padding: 1rem 0 1.4rem;
    }
    .hero h1 {
        margin-bottom: 0.15rem;
    }
    .hero p {
        color: #a9b8d0;
        font-size: 1.05rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return os.getenv("GEMINI_API_KEY")


@st.cache_data(show_spinner=False)
def extract_pdf_text(pdf_bytes: bytes) -> str:
    """Extract readable text from a PDF upload."""
    from io import BytesIO

    reader = PdfReader(BytesIO(pdf_bytes))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n\n".join(page.strip() for page in pages if page.strip())
    if not text:
        raise ValueError("No readable text was found in this PDF.")
    return text


def generate_reply(prompt: str, pdf_text: str) -> str:
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "Gemini API key is missing. Add GEMINI_API_KEY to "
            ".streamlit/secrets.toml."
        )

    client = genai.Client(api_key=api_key)

    # The current prompt is already the last user message in session state.
    recent_messages = st.session_state.messages[:-1][-8:]
    conversation = "\n".join(
        f"{message['role'].title()}: {message['content']}"
        for message in recent_messages
    )

    context = ""
    if pdf_text:
        context = (
            "\n\nUse these uploaded notes when relevant:\n"
            f"{pdf_text[:MAX_PDF_CHARS]}"
        )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"Recent conversation:\n{conversation}{context}\n\nUser: {prompt}",
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are ZERO Bot, a clear and encouraging study assistant. "
                    "Explain concepts accurately, use examples when useful, and "
                    "say when the provided material does not contain the answer."
                )
            ),
        )
        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")
        return response.text
    finally:
        client.close()


if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""


with st.sidebar:
    st.write("API Found:", bool(get_api_key()))
    st.title(APP_NAME)
    st.caption("Your AI study companion")

    if st.button("New chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.subheader("Study material")
    uploaded_pdf = st.file_uploader(
        "Upload a PDF",
        type=["pdf"],
        help="Text-based PDFs work best. Scanned pages require OCR.",
    )

    if uploaded_pdf and uploaded_pdf.name != st.session_state.pdf_name:
        try:
            with st.spinner("Reading the PDF..."):
                st.session_state.pdf_text = extract_pdf_text(uploaded_pdf.getvalue())
                st.session_state.pdf_name = uploaded_pdf.name
            st.success(f"Loaded {uploaded_pdf.name}")
        except Exception as error:
            st.session_state.pdf_text = ""
            st.session_state.pdf_name = ""
            st.error(f"Could not read the PDF: {error}")
    elif st.session_state.pdf_name:
        st.success(f"Using {st.session_state.pdf_name}")

    if st.session_state.pdf_text and st.button(
        "Remove PDF", use_container_width=True
    ):
        st.session_state.pdf_text = ""
        st.session_state.pdf_name = ""
        st.rerun()

    st.divider()
    key_status = "Connected" if get_api_key() else "API key required"
    st.caption(f"Gemini: {key_status}")
    st.caption(f"Messages: {len(st.session_state.messages)}")


st.markdown(
    """
    <div class="hero">
        <h1>ZERO Bot</h1>
        <p>Ask a question, explore an idea, or upload notes to study from.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if not st.session_state.messages:
    st.info(
        "Try: 'Explain photosynthesis simply' or upload a PDF and ask for a summary."
    )

=======
import streamlit as st
from ollama import chat

# Page Config
st.set_page_config(
    page_title="ZERO Bot",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🤖 ZERO Bot")
    st.markdown("Local AI Assistant powered by Ollama")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main Title
st.title("🤖 ZERO Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I am ZERO Bot. How can I help you today?"
        }
    ]

# Display messages
>>>>>>> cf5c435b2d94d9849800a542281455730422b4bf
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

<<<<<<< HEAD
if prompt := st.chat_input("Ask ZERO Bot anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                reply = generate_reply(prompt, st.session_state.pdf_text)
            st.markdown(reply)
        except Exception as error:
            reply = f"I could not generate a response: {error}"
            st.error(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
=======
# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = chat(
                    model="qwen2.5:1.5b",
                    messages=st.session_state.messages
                )

                reply = response["message"]["content"]

            except Exception as e:
                reply = f"⚠️ Error: {str(e)}"

            st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
>>>>>>> cf5c435b2d94d9849800a542281455730422b4bf
