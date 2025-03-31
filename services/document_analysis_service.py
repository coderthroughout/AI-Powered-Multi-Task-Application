import openai
from .supabase_service import SupabaseService


class DocumentAnalysisService:
    def __init__(self):
        self.supabase_service = SupabaseService()

    def analyze_document(self, document_content, query):
        # Check Supabase for existing analysis
        existing_analysis = self.supabase_service.fetch_document_analysis(document_content, query)

        if existing_analysis:
            return existing_analysis

        # Perform new analysis using Claude
        response = openai.ChatCompletion.create(
            model="claude-3-sonnet-20240229",
            messages=[
                {"role": "system", "content": "Analyze the following document and answer the query."},
                {"role": "user", "content": f"Document content:\n{document_content}\n\nQuery: {query}"}
            ]
        )

        analysis = response.choices[0].message.content

        # Store analysis in Supabase
        self.supabase_service.store_document_analysis(document_content, query, analysis)

        return analysis