# MerakiLabs
PDF Question Extractor

Overview

This project extracts multiple-choice and descriptive questions from a PDF document. It uses pdfplumber to extract text, re (Regular Expressions) to parse questions and answers, and json to store structured output.

Process

Core Technologies Used

Python → Core language for processing

pdfplumber → Extracts text from PDFs

Regular Expressions (Regex) → Identifies questions, answer choices, and answer keys

JSON → Stores extracted questions in a structured format

Approach to the Problem

1️⃣ Extract Text from PDF

Used pdfplumber to read text from the document.

Extracted text from all pages and combined it into a single string.

2️⃣ Extract Multiple-Choice Questions (MCQs)

Used regex to detect MCQ patterns with four options (A, B, C, D).

Stored each question with its answer choices.

3️⃣ Extract Descriptive Questions

Used regex to identify descriptive questions based on question format.

Stored each question separately without answer choices.

4️⃣ Identify Correct Answers

Extracted the answer key section using regex.

Matched answers to their corresponding MCQs.

5️⃣ Store Questions in JSON

Structured the extracted data and saved it in JSON format.

Installation & Usage

Dependencies

Ensure you have Python installed. Then, install the required packages:

pip install pdfplumber

Run the Script

python script.py

This will extract questions from the provided PDF and save them as questions.json.

Expected Output Format

The extracted questions will be stored in a JSON file as follows:

[
    {
        "question_id": 1,
        "question_type": "MCQ",
        "question_text": "What is the capital of France?",
        "answer_choices": {
            "A": "Berlin",
            "B": "Madrid",
            "C": "Paris",
            "D": "Rome"
        },
        "correct_answer": "C"
    },
    {
        "question_id": 2,
        "question_type": "Descriptive",
        "question_text": "Explain Newton's Laws of Motion.",
        "answer_choices": [],
        "correct_answer": null
    }
]

Future Improvements

Enhance regex patterns for better question detection.

Improve handling of images and equations in PDFs.

Add a GUI for easy PDF upload and extraction

Estimate of Correctly Extracted Questions : 31 (MCQ'S and Descriptive questions)

