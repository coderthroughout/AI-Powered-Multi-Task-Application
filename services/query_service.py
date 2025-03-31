import requests
import pandas as pd
import openai
from .supabase_service import SupabaseService


class QueryService:
    def __init__(self):
        self.supabase_service = SupabaseService()

    def research(self, query):
        # Check Supabase for existing research
        existing_research = self.supabase_service.fetch_research(query)

        if existing_research:
            return self.analyze_research(existing_research, query)

        # Perform new research using Perplexity API
        perplexity_response = self.perplexity_research(query)

        # Convert response to CSV
        csv_data = self.convert_to_csv(perplexity_response)

        # Analyze research using Claude
        result = self.analyze_research(csv_data, query)

        # Store research in Supabase
        self.supabase_service.store_research(query, csv_data, result)

        return result

    def perplexity_research(self, query):
        # Implement Perplexity API call here
        pass

    def convert_to_csv(self, data):
        # Convert data to CSV format
        pass

    def analyze_research(self, csv_data, query):
        response = openai.ChatCompletion.create(
            model="claude-3-sonnet-20240229",
            messages=[
                {"role": "system",
                 "content": "Analyze the following research data and provide a comprehensive answer to the query."},
                {"role": "user", "content": f"Research data:\n{csv_data}\n\nQuery: {query}"}
            ]
        )
        return response.choices[0].message.content