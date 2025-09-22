from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import generate_cover_letter_from_ai

class CoverLetterGeneratorView(APIView):
    """
    An API View to handle the generation of a cover letter.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests containing a job description and user's resume text.
        """
        # 1. Extract data from the incoming request
        job_description = request.data.get('job_description')
        resume_text = request.data.get('resume_text')

        # 2. Basic validation to ensure data is present
        if not job_description or not resume_text:
            return Response(
                {'error': 'Both job_description and resume_text are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 3. Call the service function to handle the business logic (AI call)
            # This keeps the view clean and focused on handling HTTP requests.
            generated_letter = generate_cover_letter_from_ai(job_description, resume_text)

            # 4. Return the successful response
            return Response(
                {'cover_letter': generated_letter},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            # 5. Handle any unexpected errors gracefully
            # In a real app, you would log this error.
            return Response(
                {'error': f'An unexpected error occurred: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

