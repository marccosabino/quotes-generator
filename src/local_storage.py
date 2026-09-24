import json
import random
from pathlib import Path
from typing import Optional, Dict

FALLBACK_PATH = Path(__file__).resolve().parent.parent / "data" / "quotes.json"

def get_fallback_quote() -> Optional[Dict[str, str]]:
    """Recupera uma citação aleatória do arquivo JSON local."""
    if not FALLBACK_PATH.exists():
        return None
    
    try:
        with open(FALLBACK_PATH, "r", encoding="utf-8") as f:
            quotes = json.load(f)
            return random.choice(quotes) if quotes else None
    except (json.JSONDecodeError, OSError):
        return None