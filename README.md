🏷️ YouTube Hashtag Generator (GenAI, Streamlit + Hugging Face)
Generate relevant and trending YouTube hashtags for your videos using Generative AI!
Built with Streamlit and the Hugging Face Inference API (Mistral-7B-Instruct-v0.3).

🚀 Features
AI-powered hashtag generation
Enter your video script or summary and instantly get a list of engaging, SEO-friendly hashtags.

No local model downloads required
Uses Hugging Face’s cloud API for fast, reliable results.

User-friendly web interface
Built with Streamlit for easy interaction and instant output.

Download results
Save generated hashtags as a .txt file for quick upload to YouTube.

Robust error handling
Handles API errors and edge cases gracefully.

⚡ Quick Start
Clone this repo
Or download as ZIP and extract.

Install dependencies
Open your terminal or command prompt in the project folder and run:


text
pip install -r requirements.txt
Or, install manually:


text
pip install streamlit requests
Add your Hugging Face API token

Create a file at .streamlit/secrets.toml in your project root:


text
HF_TOKEN = "your_hugging_face_token_here"
Get your token from Hugging Face
(Enable “Inference API” and “Inference Providers” permissions.)

Run the app
In your terminal, run:


text
streamlit run app.py
📝 Usage
Paste your video script or summary.

Click Generate Hashtags.

Copy or download your AI-generated hashtags for use on YouTube!

🧑‍💻 Tech Stack
Frontend/UI: Streamlit

AI Model: Mistral-7B-Instruct-v0.3 via Hugging Face Inference API

Language: Python 3.8+

🧪 Testing
Tested with a variety of video topics and styles.

Handles both short and long scripts.

Robust to missing or ambiguous input.

Average response time: 3–8 seconds.

🌱 Future Work
Support for Instagram/TikTok hashtag generation

Trending hashtag suggestions based on latest data

Multi-language support

Accessibility features (voice input, screen reader support)

SCREENSHOTS:

INTERFACE:
![Screenshot 2025-06-30 212625](https://github.com/user-attachments/assets/b985f7e7-1cbb-4d63-9738-65a729ea97da)



![Screenshot 2025-06-30 212636](https://github.com/user-attachments/assets/86e17e95-2dda-4356-89c0-4799f30327bb)

GNERATED HASTAGS:
![Screenshot 2025-06-30 212706](https://github.com/user-attachments/assets/677c4bea-28b7-4153-8c42-405043873802)

DOWNLOADED HASHTAGS:-
![Screenshot 2025-06-30 212723](https://github.com/user-attachments/assets/728ed431-dd25-4659-b739-c9bce79b13e1)
