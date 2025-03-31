import os
from openai import OpenAI


class ImageGenerationService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("IMAGE_GEN_API_KEY"))

    def generate_image(self, prompt):
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            return response.data[0].url
        except Exception as e:
            print(f"Error generating image: {str(e)}")
            return None
