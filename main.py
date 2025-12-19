from scraper import scrape_price, save_price_history

print("=== PRICE SCRAPER ===")
url = input("Įveskite produkto URL: ")

try:
    product = scrape_price(url)

    print("\nProduktas:")
    print(f"Pavadinimas: {product['title']}")
    print(f"Kaina: {product['price']}")

    save_price_history(product)
    print("\nDuomenys išsaugoti į data.json")

except Exception as e:
    print(f"Klaida: {e}")
