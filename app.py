import streamlit as st
import requests

# --- App Config ---
st.set_page_config(
    page_title="YouTube Hashtag Generator (AI)",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Secrets ---
HF_TOKEN = st.secrets.get("HF_TOKEN", "")
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

# --- Sidebar ---
with st.sidebar:
    st.title("🎬 YouTube Hashtag Generator")
    st.markdown("### How to use:")
    st.write("1. Enter your video title")
    st.write("2. Add SEO keywords")
    st.write("3. Select tone")
    st.write("4. Click generate and copy the hashtags")
    st.divider()
    st.caption("Paste these hashtags in your YouTube video description for best results!")
    st.caption("Powered by Hugging Face 🤗")

# --- Main Content ---
st.title("🎬 YouTube Hashtag Generator (AI-Powered)")
st.markdown("Boost your video's discoverability with AI-generated hashtags")

col1, col2 = st.columns([2, 1])
with col1:
    video_title = st.text_input("Video Title:", "DR.DOOM", help="Enter your video title here")
    keywords = st.text_input("SEO Keywords (comma-separated):", "MARVEL, comics, VILLIAN, DR.DOOM, DOOMS DAY", help="List keywords for your video")
    tone = st.selectbox("Select tone:", ("Casual", "Professional", "Funny", "Inspirational"), help="Choose the tone for your hashtags")

# --- AI Hashtag Generation ---
def generate_ai_hashtags(title, keywords, tone):
    prompt = f"""
You are a YouTube SEO expert. Generate a list of trending, relevant hashtags for a YouTube video.

Video title: {title}
Keywords: {keywords}
Tone: {tone}

Format output as:
HASHTAGS: [list of hashtags, separated by spaces]
"""
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7,
            "do_sample": True,
            "return_full_text": False
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        st.error(f"API Error {response.status_code}: {response.text}")
        return ""
    result = response.json()
    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]
    else:
        return str(result)

if st.button("✨ Generate Hashtags (AI)", type="primary"):
    if not HF_TOKEN:
        st.error("Hugging Face API token is missing. Add it to secrets.toml as HF_TOKEN")
        st.stop()
    with st.spinner("Generating hashtags with AI..."):
        result = generate_ai_hashtags(video_title, keywords, tone)
        if "HASHTAGS:" in result:
            hashtags = result.split("HASHTAGS:")[1].strip()
            st.success("✅ AI-Generated Hashtags:")
            st.code(hashtags, language="markdown")
            st.download_button(
                "📥 Download Hashtags",
                hashtags,
                file_name="youtube_hashtags_ai.txt"
            )
        else:
            st.error("Failed to parse response. Showing raw output:")
            st.code(result, language="markdown")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ by you | Powered by Streamlit & Hugging Face")
