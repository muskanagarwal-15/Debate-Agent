import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

class AIModel:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Configure API key
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("API key not found. Create a .env file with GEMINI_API_KEY=your_key")
        
        # Configure the model
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def generate_response(self, prompt):
        """Generate a response from the model with error handling and rate limiting"""
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            error_msg = f"Error: {str(e)[:100]}..."
            if "quota" in str(e).lower():
                print(error_msg)
                print("API limit reached. Waiting 60 seconds...")
                time.sleep(60)
                # Retry once after waiting
                try:
                    response = self.model.generate_content(prompt)
                    return response.text.strip()
                except:
                    return f"Failed to generate response after waiting: {error_msg}"
            return f"Failed to generate response: {error_msg}"