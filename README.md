# AI-Assistant-Email-Summarizer


Readme · MD
AI Personal Assistant
A lightweight web app combining a conversational AI assistant and an email summarizer, built with Flask and powered by Groq's LLM API (openai/gpt-oss-120b).

Features
Ask Anything — a simple Q&A interface backed by an LLM, for quick answers to any question.
Email Summarizer — paste in a long email and get a concise, 4–5 sentence summary highlighting the key points.
Clean, minimal frontend with async requests (no page reloads) and loading indicators.
Tech Stack
Backend: Python, Flask
LLM Provider: Groq API (openai/gpt-oss-120b)
Frontend: HTML, CSS, vanilla JavaScript (fetch API)
Environment management: python-dotenv
Project Structure
.
├── app.py                 # Flask app and API routes
├── templates/
│   └── index.html         # Main page (Ask + Summarizer UI)
├── static/
│   ├── style.css           # Styling
│   └── script.js            # Frontend logic (fetch calls, form handling)
├── .env                    # API key (not committed)
└── README.md
Setup
1. Clone the repository
bash
git clone https://github.com/anuragyadav24/<repo-name>.git
cd <repo-name>
2. Create a virtual environment
bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install dependencies
bash
pip install flask python-dotenv groq
4. Add your Groq API key
Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here
Get a free API key from console.groq.com.

5. Run the app
bash
python app.py
Visit http://127.0.0.1:5000 in your browser.

API Endpoints
Endpoint	Method	Body (form-data)	Returns
/ask	POST	Query	{ "response": "<answer>" }
/summarize	POST	Email	{ "summary": "<summary>" }
Notes
Model used: openai/gpt-oss-120b via Groq's chat completions API.
Temperature is set lower (0.3) for summarization to keep outputs consistent and factual, and higher (0.7) for the Q&A assistant to allow more natural, varied responses.
License
This project is open source and available under the MIT License.


