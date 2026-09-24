from src.api_client import fetch_quote_from_api
from src.local_storage import get_fallback_quote

def display_quote(quote: str, author: str, source: str) -> None:
    print("-" * 60)
    print(f'"{quote}"')
    print(f"  — {author}")
    print(f"  [Origem: {source}]")
    print("-" * 60)

def main():
    print("Obtendo citação inspiradora...\n")
    
    # 1. Tentativa via API externa
    quote_data = fetch_quote_from_api()
    source = "API Externa"

    # 2. Fallback caso a API esteja fora ou sem rede
    if not quote_data:
        quote_data = get_fallback_quote()
        source = "Backup Local (Offline)"

    # 3. Exibição ou falha crítica total
    if quote_data and quote_data.get("quote"):
        display_quote(
            quote=quote_data["quote"],
            author=quote_data.get("author", "Autor Desconhecido"),
            source=source
        )
    else:
        print("Erro: Não foi possível obter nenhuma citação (API inacessível e backup indisponível).")

if __name__ == "__main__":
    main()