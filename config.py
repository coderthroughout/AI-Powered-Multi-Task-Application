import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
IMAGE_GEN_API_KEY = os.getenv("IMAGE_GEN_API_KEY")
# VIDEO_GEN_API_KEY = os.getenv("VIDEO_GEN_API_KEY")


# def SECRET_KEY():
#     return None
def SECRET_KEY():
    return None