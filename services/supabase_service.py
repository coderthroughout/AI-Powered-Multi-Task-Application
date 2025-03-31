from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY


class SupabaseService:
    def __init__(self):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def store_data(self, table, data):
        try:
            response = self.supabase.table(table).insert(data).execute()
            return response.data
        except Exception as e:
            print(f"Error storing data in Supabase: {str(e)}")
            return None

    def fetch_data(self, table, query):
        try:
            response = self.supabase.table(table).select("*").eq("query", query).execute()
            return response.data
        except Exception as e:
            print(f"Error fetching data from Supabase: {str(e)}")
            return None

    def update_data(self, table, id, data):
        try:
            response = self.supabase.table(table).update(data).eq("id", id).execute()
            return response.data
        except Exception as e:
            print(f"Error updating data in Supabase: {str(e)}")
            return None

    def delete_data(self, table, id):
        try:
            response = self.supabase.table(table).delete().eq("id", id).execute()
            return response.data
        except Exception as e:
            print(f"Error deleting data from Supabase: {str(e)}")
            return None

    def fetch_similar_chat(self, message):
        pass

    def store_chat(self, message, ai_response, emotion):
        pass
