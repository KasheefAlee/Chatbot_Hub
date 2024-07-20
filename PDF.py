from flask import Flask, request, jsonify, render_template
import fitz  # PyMuPDF
import openai

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Global variable to store extracted text
pdf_text = ""

@app.route('/')
def index():
    return render_template('PDF_chatbot.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global pdf_text
    file = request.files['file']
    pdf_text = extract_text_from_pdf(file)
    return jsonify({"message": "PDF uploaded and text extracted successfully!"})

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question')
    response = query_openai(pdf_text, question)
    return jsonify({"answer": response})

def query_openai(context, question):
    openai.api_key = 'sk-proj-CG1b6UBushn6OwJnTRg9T3BlbkFJhzneSBlpPd8A2Dcymjfv'
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"{context}\n\nQuestion: {question}\nAnswer:",
        max_tokens=150,
        temperature=0.5
    )
    answer = response.choices[0].text.strip()
    return answer

if __name__ == '__main__':
    app.run(debug=True, port=9090) 
