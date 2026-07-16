from openai import OpenAI
from dotenv import load_dotenv
import os

class ScratchModel:
    """A class representing a scratch model that interacts with the OpenAI API to generate responses based on user prompts."""
    def __init__(self, model_name, user_prompt: str):
        self.model_name = model_name
        self.user_prompt = user_prompt

        load_dotenv()

    def generate_response(self, prompt: str) -> str:
        """Generates a response from the model based on the provided prompt."""
        client = OpenAI(
            api_key=os.environ.get("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        )

        response = client.responses.create(
            input=self.user_prompt,
            model=self.model_name,
        )
        print(response.output_text)

        # Placeholder for the actual model inference logic
        return f"Response from {self.model_name} for prompt: {prompt}"
    

agent = ScratchModel(model_name="llama-3.3-70b-versatile", user_prompt="Who is likely to win FIFA World Cup 2026?")
agent.generate_response(agent.user_prompt)