import requests
from typing import Optional, Dict

API_URL = "https://dummyjson.com/quotes/random"
TRANSLATE_URL = "https://api.mymemory.translated.net/get"


def translate_to_pt(text: str, timeout_seconds: int = 5) -> str:
    """
    Traduz o texto de inglês para português utilizando a API do MyMemory.
    Caso a tradução falhe por timeout ou rede, retorna o texto original sem quebrar o fluxo.
    """
    try:
        params = {"q": text, "langpair": "en|pt-br"}
        response = requests.get(TRANSLATE_URL, params=params, timeout=timeout_seconds)
        
        if response.status_code == 200:
            data = response.json()
            translated_text = data.get("responseData", {}).get("translatedText")
            if translated_text:
                return translated_text
    except requests.RequestException:
        pass
    
    return text


def fetch_quote_from_api(timeout_seconds: int = 8) -> Optional[Dict[str, str]]:
    """
    Consome uma citação da DummyJSON e traduz dinamicamente para português.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(API_URL, headers=headers, timeout=timeout_seconds)
        response.raise_for_status()
        data = response.json()
        
        raw_quote = data.get("quote")
        author = data.get("author")
        
        if raw_quote and author:
            quote_pt = translate_to_pt(raw_quote)
            return {
                "quote": quote_pt,
                "author": author
            }
        return None
        
    except requests.RequestException:
        return None