import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading

class BookScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Book Scraper - books.toscrape.com")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter number of pages to scrape:", font=("Arial", 12)).pack(pady=10)
        self.page_entry = tk.Entry(self.root, font=("Arial", 12), justify='center')
        self.page_entry.insert(0, "3")  # default
        self.page_entry.pack()

        self.scrape_button = tk.Button(self.root, text="Start Scraping", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.start_scraping_thread)
        self.scrape_button.pack(pady=15)

        self.status = tk.Label(self.root, text="", font=("Arial", 11), fg="blue")
        self.status.pack(pady=5)

    def start_scraping_thread(self):
        thread = threading.Thread(target=self.scrape)
        thread.start()

    def scrape(self):
        pages = self.page_entry.get().strip()
        if not pages.isdigit() or int(pages) < 1:
            messagebox.showerror("Invalid Input", "Please enter a valid number of pages (1 or more).")
            return

        num_pages = int(pages)
        self.status.config(text="🔍 Scraping in progress...")

        BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
        products = []

        try:
            for page in range(1, num_pages + 1):
                self.status.config(text=f"Scraping page {page}...")
                self.root.update_idletasks()

                url = BASE_URL.format(page)
                res = requests.get(url)
                soup = BeautifulSoup(res.text, 'html.parser')

                books = soup.find_all('article', class_='product_pod')

                for book in books:
                    name = book.h3.a['title']
                    price = book.find('p', class_='price_color').text
                    rating = book.p['class'][1]

                    products.append({
                        'Name': name,
                        'Price': price,
                        'Rating': rating
                    })

            df = pd.DataFrame(products)
            df.to_csv("products.csv", index=False)
            self.status.config(text="✅ Scraping completed. Data saved to products.csv")
            messagebox.showinfo("Done", "Books scraped successfully!")

        except Exception as e:
            self.status.config(text="❌ Failed during scraping.")
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = BookScraperApp(root)
    root.mainloop()
