from flask import Flask , render_template , request , jsonify
import os 
from dotenv import load_dotenv
from groq import Groq


app = Flask(__name__)
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html") 

@app.route("/ask", methods = ["POST"])
def ask():
    question = request.form.get("Query")  # matches the HTML input's name="Query"
    if not question:
        return jsonify({"error": "No query provided"}), 400
    try:
        response = client.chat.completions.create(
            model= "openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "Act like a helpful assistant"},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        answer = response.choices[0].message.content.strip()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"response" : answer}) , 200

@app.route("/summarize" , methods=["POST"])
def summarize():
    email_text = request.form.get("Email")
    if not email_text:
        return jsonify({"error": "No query provided"}), 400
    prompt = f"summarize the following email in brief with consedring important points in the email in  4-5  sentences,   :{email_text}"
    try:
        response = client.chat.completions.create(
            model= "openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "Act like an AI assistant"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1024
        )
        
        summary =response.choices[0].message.content.strip()



    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"summary": summary}), 200  


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(denug=True)