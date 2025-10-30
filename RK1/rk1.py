from dataclasses import dataclass
from typing import List

@dataclass
class Library:
    id: int
    name: str

@dataclass
class Book:
    id: int
    title: str
    author: str
    pages: int
    library_id: int

@dataclass
class LibraryBook:
    library_id: int
    book_id: int

libraries = [
    Library(1, "Академическая библиотека"),
    Library(2, "Абонемент художественной литературы"),
    Library(3, "Городская центральная библиотека"),
    Library(4, "Абонемент научной литературы")
]

books = [
    Book(1, "Война и мир", "Л. Толстой", 1225, 1),
    Book(2, "Анна Каренина", "Л. Толстой", 864, 2),
    Book(3, "Евгения Онегина", "А. Пушкин", 320, 1),
    Book(4, "Мастер и Маргарита", "М. Булгаков", 480, 3),
    Book(5, "Преступление и наказание", "Ф. Достоевский", 672, 2),
    Book(6, "Физика для начинающих", "А. Эйнштейн", 350, 4),
    Book(7, "Химия органических соединений", "Д. Менделеев", 540, 4)
]

library_books = [
    LibraryBook(1, 1),
    LibraryBook(1, 3),
    LibraryBook(2, 2),
    LibraryBook(2, 5),
    LibraryBook(3, 4),
    LibraryBook(4, 6),
    LibraryBook(4, 7),
    LibraryBook(1, 5),
    LibraryBook(2, 1),
]

print("Библиотеки:")
for lib in libraries:
    print(f"  {lib.id}. {lib.name}")

print("Книги:")
for book in books:
    print(f"  {book.id}. '{book.title}' - {book.author} ({book.pages} стр.)")

print("Связи книг с библиотеками:")
for lb in library_books:
    lib_name = next((lib.name for lib in libraries if lib.id == lb.library_id), "Неизвестно")
    book_title = next((book.title for book in books if book.id == lb.book_id), "Неизвестно")
    print(f"  Библиотека '{lib_name}' -> Книга '{book_title}'")

print("ЗАПРОС 1: Книги, названия которых заканчиваются на 'А'")

books_ending_with_a = [book for book in books if book.title.endswith('а')]
for book in books_ending_with_a:
    library_name = next((lib.name for lib in libraries if lib.id == book.library_id), "Неизвестная библиотека")
    print(f"  '{book.title}' - {book.author} ({book.pages} стр.)")
    print(f"    Находится в: {library_name}")

print("ЗАПРОС 2: Библиотеки со средним количеством страниц в книгах")

library_avg_pages = []
for library in libraries:
    library_books_list = [book for book in books if book.library_id == library.id]
    if library_books_list:
        total_pages = sum(book.pages for book in library_books_list)
        avg_pages = total_pages / len(library_books_list)
        library_avg_pages.append((library.name, avg_pages, len(library_books_list)))

library_avg_pages_sorted = sorted(library_avg_pages, key=lambda x: x[1])

for lib_name, avg_pages, book_count in library_avg_pages_sorted:
    print(f"  {lib_name}:")
    print(f"    Среднее количество страниц: {avg_pages:.1f}")
    print(f"    Количество книг: {book_count}")

print("ЗАПРОС 3: Библиотеки с названием на 'А' и их книги")

libraries_starting_with_a = [lib for lib in libraries if lib.name.startswith('А')]

for library in libraries_starting_with_a:
    print(f"\n  Библиотека: {library.name}")

    library_book_ids = [lb.book_id for lb in library_books if lb.library_id == library.id]
    library_books_list = [book for book in books if book.id in library_book_ids]

    if library_books_list:
        for book in library_books_list:
            print(f"    - '{book.title}' - {book.author} ({book.pages} стр.)")
    else:
        print("    В этой библиотеке пока нет книг")
