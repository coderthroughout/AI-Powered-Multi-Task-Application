import os
import requests


class VideoGenerationService:
    def __init__(self):
        self.api_key = os.getenv("HEYGEN_API_KEY")
        self.base_url = "https://api.heygen.com/v1"

    def generate_video(self, template_id, modifications):
        try:
            headers = {
                "X-Api-Key": self.api_key,
                "Content-Type": "application/json"
            }
            data = {
                "template_id": template_id,
                "modifications": modifications
            }
            response = requests.post(f"{self.base_url}/videos", headers=headers, json=data)
            response.raise_for_status()
            return response.json()["video_url"]
        except Exception as e:
            print(f"Error generating video: {str(e)}")
            return None
