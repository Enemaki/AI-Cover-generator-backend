AI Career Copilot - Backend
This is the Django backend for the AI Career Copilot, an application that generates cover letters based on a job description and user's skills.

Project Overview
This backend provides a single, stateless API endpoint to handle the cover letter generation logic. It is built with Django and Django REST Framework.

Features
A simple, clean API endpoint: POST /api/generator/cover-letter/

Receives a job description and user's resume text.

(Currently simulated) Interacts with a Large Language Model (LLM) to generate a tailored cover letter.

Returns the generated text in a JSON format.

Setup and Installation
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.8+

pip (Python package installer)

A virtual environment tool (venv is recommended)

Installation Steps
Clone the repository:

git clone <your-repo-url>
cd <your-repo-folder>

Create and activate a virtual environment:

# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Apply the initial database migrations:
(Even though we don't use models in the generator app, Django needs its own tables.)

python manage.py migrate

Run the development server:

python manage.py runserver

The backend will now be running at http://127.0.0.1:8000/.

API Endpoint Testing
You can test the endpoint using a tool like curl or Postman.

Using curl
Open a new terminal and run the following command:

curl -X POST [http://127.0.0.1:8000/api/generator/cover-letter/](http://127.0.0.1:8000/api/generator/cover-letter/) \
-H "Content-Type: application/json" \
-d '{
    "job_description": "We are looking for a proactive software engineer with experience in Python and cloud services.",
    "resume_text": "Experienced Python developer with 3 years of work on AWS (S3, Lambda). Skilled in building scalable REST APIs."
}'

Expected Response
You should receive a JSON response with the generated cover letter:

{
    "cover_letter": "Dear Hiring Manager,\\n\\nI am writing to express my enthusiastic interest in the Software Engineer position... [rest of the generated letter]"
}
