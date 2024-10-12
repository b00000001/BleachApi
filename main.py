from scraper import scrape_bleach_character

# Example usage with a specific character URL
url = "https://bleach.fandom.com/wiki/Ichigo_Kurosaki"
character_data = scrape_bleach_character(url)

# Print the scraped information
for key, value in character_data.items():
    print(f"{key}: {value}")