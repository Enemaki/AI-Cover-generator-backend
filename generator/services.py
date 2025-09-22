import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# --- IMPORTANT: API Key Setup ---
# It's a best practice to load your API key from an environment variable
# rather than hardcoding it directly in your script.
# Before running your Django server, you need to set this environment variable
# in your terminal:
#
# export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
#
# You can get an API key from Google AI Studio: https://aistudio.google.com/
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
except AttributeError:
    # This error can happen if the key is not set. We'll raise an exception
    # to make it clear that the API key is missing.
    raise RuntimeError("GOOGLE_API_KEY environment variable not set.")


def generate_cover_letter_from_ai(job_description: str, resume_text: str) -> str:
    """
    Generates a cover letter using the Google Generative AI (Gemini) model.

    This function constructs a detailed prompt and makes a live API call
    to the Gemini model.

    Args:
        job_description: The text of the job description.
        resume_text: The user's skills, experience, or full resume text.

    Returns:
        A string containing the generated cover letter.
    
    Raises:
        ValueError: If the API call fails or returns no content.
    """
    
    # --- 1. Prompt Engineering ---
    # This prompt is designed to give the AI a clear role, context, and instructions.
    prompt = f"""
    Act as an expert career coach and professional cover letter writer. Your task is to write a compelling, 
    concise, and professional cover letter. The tone should be enthusiastic and confident.

    CONTEXT:
    The user is applying for the job described below. You must use the user's provided skills and experience 
    to tailor the letter specifically to the job's requirements.

    JOB DESCRIPTION:
    ---
    {job_description}
    ---

    USER'S RESUME/SKILLS:
    ---
    {resume_text}
    ---

    INSTRUCTIONS:
    - Write a three-paragraph cover letter.
    - The first paragraph should express excitement for the role and briefly introduce the user.
    - The second paragraph must connect the user's skills/experience directly to 2-3 key requirements from the job description.
    - The final paragraph should reiterate interest and include a strong call to action.
    - Do not invent any skills or experience not mentioned in the user's resume.
    - The final output should only be the cover letter text, with no extra commentary or pleasantries like "Here is the cover letter:".
    """

    # --- 2. Live AI API Call ---
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Send the prompt to the model
        response = model.generate_content(prompt)

        # Extract and return the generated text
        if response.text:
            return response.text.strip()
        else:
            # Handle cases where the API returns a response with no text
            raise ValueError("The AI model returned an empty response.")
            
    except Exception as e:
        # Catch potential API errors (e.g., network issues, invalid API key)
        # In a real app, you would log this error for debugging.
        print(f"An error occurred during the Google AI API call: {e}")
        # Re-raise the exception to be handled by the view
        raise ValueError(f"Failed to generate cover letter due to an API error: {e}") from e

