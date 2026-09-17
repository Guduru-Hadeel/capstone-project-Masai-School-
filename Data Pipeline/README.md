# 🕸️ Data Pipeline Module

This module automates the process of extracting online book data, transforming/cleaning it with Pandas, and loading it into a structured SQLite database.

## 🚀 Features
* **Web Scraping:** Programmatically extracts the first 3 pages of data from *Books to Scrape*.
* **Data Transformation:** Parses HTML elements, extracts titles, scales numeric review ratings (1–5), cleans raw text, and computes local currency values (`price_inr`).
* **Relational Database Design:** Normalizes the data into structured, relational SQLite tables (`books` and `categories`) with constraints and foreign keys.
* **Analysis Verification:** Runs built-in SQL validation checks and evaluates successful Pandas DataFrame integration via SQL joins.

---

## 🛠️ Installation & Setup

1. **Install Dependencies:**  
   Ensure you have the required external libraries installed before executing the script:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

2. **Run the Pipeline:**  
   Execute your script or Jupyter Notebook:
   ```bash
   python scrape_books.py
   ```

---

## 🗄️ Database Architecture (`books.db`)

The script automatically initializes a relational SQLite database structure:

### 1. `categories` Table
Stores unique category names to avoid data redundancy.
* `id`: INTEGER, Primary Key
* `category_name`: TEXT, Unique

### 2. `books` Table
Stores granular book metadata linked back to the parent category.
* `book_id`: INTEGER, Primary Key
* `title`: TEXT
* `price_gbp`: REAL (Original British Pounds)
* `price_inr`: REAL (Converted Indian Rupees at an exchange index of 105.50)
* `rating`: INTEGER (Mapped values from 1 to 5)
* `availability`: TEXT
* `category_id`: INTEGER, Foreign Key references `categories(id)`

---

## 📊 Verification Queries Included
Once executed, the script automatically triggers verification queries to print data insights directly to your terminal:
* The absolute total count of books successfully scraped and logged.
* Distinct numerical review scores parsed.
* The top 5 most expensive books sorted descending by Indian Rupee (`price_inr`) valuations.
* A target join confirmation demonstrating clear validation between local DataFrames and backend SQL storage data.
