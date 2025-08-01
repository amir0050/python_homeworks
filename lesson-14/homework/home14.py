
import json
import requests
import random
import os

# ========== 1. JSON Parsing ==========
def read_students():
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for student in data:
                print(f"Name: {student.get('name')}, Age: {student.get('age')}, Grade: {student.get('grade')}")
    except FileNotFoundError:
        print(" File 'students.json' not found.")
    except json.JSONDecodeError:
        print(" Invalid JSON format.")

# ========== 2. Weather API ==========
def get_weather():
    city = input("Enter city name (default: Tashkent): ") or "Tashkent"
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # ← ВСТАВЬ СВОЙ КЛЮЧ
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"\n Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description'].capitalize()}\n")
    else:
        print(" Error fetching weather data.")

# ========== 3. JSON Modification ==========
def load_books():
    if not os.path.exists("books.json"):
        return []
    with open("books.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)

def manage_books():
    while True:
        print("\n Book Manager")
        print("1. Add book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Show all books")
        print("5. Back to main menu")
        choice = input("Choose an option: ")

        books = load_books()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            books.append({"title": title, "author": author})
            save_books(books)
            print(" Book added.")
        elif choice == "2":
            title = input("Enter book title to update: ")
            for book in books:
                if book["title"] == title:
                    book["author"] = input("Enter new author: ")
                    save_books(books)
                    print(" Book updated.")
                    break
            else:
                print("Book not found.")
        elif choice == "3":
            title = input("Enter book title to delete: ")
            books = [book for book in books if book["title"] != title]
            save_books(books)
            print(" Book deleted.")
        elif choice == "4":
            if books:
                for book in books:
                    print(f"- {book['title']} by {book['author']}")
            else:
                print("No books found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

# ========== 4. Movie Recommendation ==========
def recommend_movie_by_genre():
    genre = input("Enter movie genre (e.g. Action, Drama, Comedy): ").strip()
    api_key = "YOUR_OMDB_API_KEY"  # ← ВСТАВЬ СВОЙ КЛЮЧ
    movie_titles = ["Inception", "Titanic", "The Matrix", "Gladiator", "Avengers", "Avatar", "Interstellar"]

    random.shuffle(movie_titles)
    for title in movie_titles:
        url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            movie = response.json()
            if genre.lower() in movie.get("Genre", "").lower():
                print(f"\n🎬 Title: {movie['Title']}")
                print(f"Genre: {movie['Genre']}")
                print(f"Plot: {movie['Plot']}")
                print(f"IMDb Rating: {movie['imdbRating']}")
                return
    print(" No movie found with that genre.")

# ========== MAIN MENU ==========
def main_menu():
    while True:
        print("\n========= MAIN MENU =========")
        print("1.


JSON Parsing (students.json)")
        print("2. Weather API (Tashkent)")
        print("3. JSON Book Manager (books.json)")
        print("4. Movie Recommendation by Genre")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            read_students()
        elif choice == "2":
            get_weather()
        elif choice == "3":
            manage_books()
        elif choice == "4":
            recommend_movie_by_genre()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Запуск программы
if name == "__main__":
    main_menu()
