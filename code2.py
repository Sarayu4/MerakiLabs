import pdfplumber
import json
import re

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF using pdfplumber."""
    extracted_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text.append(text)
    return "\n".join(extracted_text)

def extract_answer_key(text):
    """Extracts answer keys if present in the document."""
    answer_key = {}
    answer_pattern = re.findall(r"Q\.(\d+)\s+Answer:\s+([A-D0-9,]+)", text)
    for match in answer_pattern:
        question_id = int(match[0])
        correct_answer = match[1].strip()
        answer_key[question_id] = correct_answer
    return answer_key

def parse_questions(text):
    """Parses extracted text into structured questions using regex."""
    questions = []
    question_pattern = re.compile(r"Q\.(\d+)\s+(.*?)\n\(A\) (.*?)\s+\(B\) (.*?)\s+\(C\) (.*?)\s+\(D\) (.*?)\n", re.DOTALL)
    
    matches = question_pattern.findall(text)
    for idx, match in enumerate(matches):
        question_id = int(match[0])
        question_text = match[1].strip()
        answer_choices = {
            "A": match[2].strip(),
            "B": match[3].strip(),
            "C": match[4].strip(),
            "D": match[5].strip()
        }
        
        question_data = {
            "question_id": question_id,
            "question_type": "MCQ",
            "question_text": question_text,
            "answer_choices": answer_choices,
            "correct_answer": None  # Updated later if answer key is found
        }
        questions.append(question_data)
    
    # Extract descriptive questions
    descriptive_pattern = re.findall(r'Q\.(\d+)\s+(.*?)(?:\?|\.)', text, re.DOTALL)
    for match in descriptive_pattern:
        question_id = int(match[0])
        if not any(q["question_id"] == question_id for q in questions):
            questions.append({
                "question_id": question_id,
                "question_type": "Descriptive",
                "question_text": match[1].strip(),
                "answer_choices": [],
                "correct_answer": None
            })
    
    return questions

def save_to_json(data, output_file="questions.json"):
    """Saves extracted questions to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def process_pdf(pdf_path):
    """Main function to process PDF and extract questions."""
    print("Extracting text from PDF...")
    text_data = extract_text_from_pdf(pdf_path)
    
    print("Parsing questions...")
    extracted_questions = parse_questions(text_data)
    
    print("Extracting answer key...")
    answer_key = extract_answer_key(text_data)
    
    for q in extracted_questions:
        q_id = q["question_id"]
        if q_id in answer_key:
            q["correct_answer"] = answer_key[q_id]
    
    save_to_json(extracted_questions)
    print("✅ Extraction complete. Questions saved in 'questions.json'.")

# Example usage
pdf_file = "2024_1_English.pdf"
process_pdf(pdf_file)
