import requests
import json

def get_neutral_google_suggests(query, language='ja', region='jp'):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&hl={language}&gl={region}&q={query}"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return []
    
    suggestions = json.loads(response.text)[1]
    return suggestions
