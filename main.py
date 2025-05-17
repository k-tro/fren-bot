from scraper.wa_scraper import WhatsAppScraper
from database.db_handler import MessageDB

def main():
    scraper = WhatsAppScraper()
    db = MessageDB()

    scraper.login()
    messages = scraper.get_messages()
    for sender, text in messages:
        print(f"{sender}: {text}")
        db.insert_message(sender, text)

if __name__ == "__main__":
    main()
