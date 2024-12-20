books = [
    {"title": "1984", "author": "Джордж Оруэлл", "year": 1949},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
    {"title": "Убить пересмешника", "author": "Харпер Ли", "year": 1960},
    {"title": "Гордость и предубеждение", "author": "Джейн Остин", "year": 1813},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866}
]

for i, book in enumerate(books, start=1):
    print(f"---------------------- Книга {i} -----------------------")
    print(f"Название: {book['title']}, Автор: {book['author']},")
    print(f"-------------------------{book['year']}-------------------------\n")
