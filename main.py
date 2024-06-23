from flask import Flask, render_template, request
from openai import OpenAI
from config import API_KEY
from docx import Document
from docx.shared import Inches, Pt
from docx2pdf import convert


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    text = request.form.get("text")
    print(text)
    
  # client = OpenAI(api_key=API_KEY)

  # context = [{"role": "user", "content": f"""We are making a book about Calculus. Create an outline for our book, which will have 5 chapters, and each chapter will have 3 subchapters

  # Outline For Output prompt:

  # 'python dict with a key: chapter title, value: a single list containing each subchapter title'"""}]

  # stream = client.chat.completions.create(
  #   model="gpt-3.5-turbo",
  #   messages=context
  # )
  
  outline = {
  "Chapter 1: Introduction to Calculus": ["1.1 What is Calculus?", "1.2 History of Calculus", "1.3 Importance of Calculus"],
  "Chapter 2: Differentiation": ["2.1 Understanding Derivatives", "2.2 Rules of Differentiation", "2.3 Applications of Differentiation"],
  "Chapter 3: Integration": ["3.1 Understanding Integrals", "3.2 Techniques of Integration", "3.3 Applications of Integration"],
  "Chapter 4: Limits and Continuity": ["4.1 Limit Definition", "4.2 Properties of Limits", "4.3 Continuity of Functions"],
  "Chapter 5: Advanced Topics in Calculus": ["5.1 Sequences and Series", "5.2 Multivariable Calculus", "5.3 Differential Equations"]
} # stream.choices[0].message.content
  
  chapters = outline.keys()
  
  document = Document()

  document.add_picture('image-filename.png')
  
  for chapter in chapters:
    print(chapter)
    subchapters = outline[chapter]
    document.add_heading(chapter, 1)
    for subchapter in subchapters:
      print(subchapter)
      
      document.add_heading(subchapter, 2)

      p4 = document.add_paragraph('This is a paragraph with exactly 20 pt line spacing.')

  document.save("test.docx")

  convert("test.docx", "book.pdf")
    

  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)