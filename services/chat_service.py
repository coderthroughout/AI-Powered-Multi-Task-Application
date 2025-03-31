import openai
from .emotion_analysis_service import EmotionAnalysisService
from .supabase_service import SupabaseService


class ChatService:
    def __init__(self):
        self.emotion_service = EmotionAnalysisService()
        self.supabase_service = SupabaseService()

    def chat(self, message):
        emotion = self.emotion_service.analyze(message)

        # Check Supabase for similar previous interactions
        previous_data = self.supabase_service.fetch_similar_chat(message)

        if previous_data:
            # Use previous data to inform the response
            context = f"Previous similar interaction: {previous_data}"
        else:
            context = ""

        response = openai.ChatCompletion.create(
            model="claude-3-sonnet-20240229",
            messages=[
                {"role": "system", "content": f"You are an AI assistant. The user's emotion is {emotion}. {context}"},
                {"role": "user", "content": message}
            ]
        )

        ai_response = response.choices[0].message.content

        # Store the interaction in Supabase
        self.supabase_service.store_chat(message, ai_response, emotion)

        return ai_response