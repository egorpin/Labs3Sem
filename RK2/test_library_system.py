import unittest
from library_system import Library, Book, LibraryBook, LibrarySystem, create_sample_data

class TestLibrarySystem(unittest.TestCase):
    """Тесты для системы управления библиотекой"""

    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.system = create_sample_data()

    def test_get_books_ending_with_a(self):
        """Тест 1: Поиск книг, названия которых заканчиваются на 'А'"""
        # Arrange
        expected_titles = ["Анна Каренина", "Евгения Онегина", "Мастер и Маргарита"]

        # Act
        books = self.system.get_books_ending_with_a()

        # Assert
        self.assertEqual(len(books), 3, f"Должно быть найдено 3 книги")

        actual_titles = [book.title for book in books]
        for expected_title in expected_titles:
            self.assertIn(expected_title, actual_titles,
                         f"Книга '{expected_title}' должна быть в результате")

        # Проверяем, что все найденные книги действительно заканчиваются на 'а'
        for book in books:
            self.assertTrue(book.title.endswith('а'),
                          f"Название книги '{book.title}' должно заканчиваться на 'а'")

    def test_get_library_avg_pages(self):
        """Тест 2: Расчет среднего количества страниц по библиотекам"""
        # Arrange & Act
        library_avg_pages = self.system.get_library_avg_pages()

        # Assert
        self.assertEqual(len(library_avg_pages), 4, "Должно быть 4 библиотеки")

        # Проверяем правильность расчета для конкретной библиотеки
        library_names = [lib[0] for lib in library_avg_pages]

        # Находим "Академическую библиотеку" и проверяем расчет
        for lib_name, avg_pages, book_count in library_avg_pages:
            if lib_name == "Академическая библиотека":
                # В Академической библиотеке должны быть книги с ID 1, 3, 5
                # Книга 1: 1225 стр., книга 3: 320 стр., книга 5: 672 стр.
                expected_avg = (1225 + 320 + 672) / 3
                self.assertAlmostEqual(avg_pages, expected_avg, places=1,
                                      msg=f"Неправильное среднее для {lib_name}")
                self.assertEqual(book_count, 3, f"Неправильное количество книг для {lib_name}")
                break

        # Проверяем сортировку по возрастанию среднего количества страниц
        for i in range(len(library_avg_pages) - 1):
            self.assertLessEqual(library_avg_pages[i][1], library_avg_pages[i + 1][1],
                               "Библиотеки должны быть отсортированы по возрастанию среднего количества страниц")

    def test_get_libraries_starting_with_a_with_books(self):
        """Тест 3: Поиск библиотек с названием на 'А' и их книг"""
        # Arrange & Act
        libraries_with_books = self.system.get_libraries_starting_with_a_with_books()

        # Assert
        # Должно быть 3 библиотеки, начинающиеся на 'А'
        self.assertEqual(len(libraries_with_books), 3, "Должно быть 3 библиотеки на 'А'")

        expected_library_names = ["Академическая библиотека",
                                 "Абонемент художественной литературы",
                                 "Абонемент научной литературы"]

        actual_library_names = [lib[0].name for lib in libraries_with_books]

        for expected_name in expected_library_names:
            self.assertIn(expected_name, actual_library_names,
                         f"Библиотека '{expected_name}' должна быть в результате")

        # Проверяем, что у библиотек есть правильные книги
        for library, books_list in libraries_with_books:
            # Проверяем, что название библиотеки начинается с 'А'
            self.assertTrue(library.name.startswith('А'),
                          f"Название библиотеки '{library.name}' должно начинаться с 'А'")

            # Для Академической библиотеки проверяем количество книг
            if library.name == "Академическая библиотека":
                self.assertEqual(len(books_list), 3,
                               f"В Академической библиотеке должно быть 3 книги")

                # Проверяем наличие конкретных книг
                book_titles = [book.title for book in books_list]
                expected_books = ["Война и мир", "Евгения Онегина", "Преступление и наказание"]
                for expected_book in expected_books:
                    self.assertIn(expected_book, book_titles,
                                 f"Книга '{expected_book}' должна быть в Академической библиотеке")

    def test_get_library_by_id(self):
        """Дополнительный тест: Получение библиотеки по ID"""
        # Arrange
        library_id = 1

        # Act
        library = self.system.get_library_by_id(library_id)

        # Assert
        self.assertIsNotNone(library, "Библиотека должна быть найдена")
        self.assertEqual(library.id, library_id, "ID библиотеки должен совпадать")
        self.assertEqual(library.name, "Академическая библиотека",
                        "Название библиотеки должно быть 'Академическая библиотека'")

    def test_get_book_by_id(self):
        """Дополнительный тест: Получение книги по ID"""
        # Arrange
        book_id = 1

        # Act
        book = self.system.get_book_by_id(book_id)

        # Assert
        self.assertIsNotNone(book, "Книга должна быть найдена")
        self.assertEqual(book.id, book_id, "ID книги должен совпадать")
        self.assertEqual(book.title, "Война и мир",
                        "Название книги должно быть 'Война и мир'")

if __name__ == "__main__":
    unittest.main(verbosity=2)
