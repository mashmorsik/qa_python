# qa_python

### Список реализованных тестов:

1. _test_add_new_book_add_two_books_ - проверка добавления новых книг в
словарь _books_rating_.
2. _test_add_new_book_same_title_doesnt_add_ - проверяем, что книга, 
которая уже есть в словаре _books_rating_ не добавляется повторно.
3. _test_set_book_rating_less_than_11_changes_to_new_ - проверка изменения 
рейтинга книге на число меньше 11.
4. _test_set_book_rating_more_than_10_stays_the_same_ - проверка изменения
рейтинга книги на число больше 10, рейтинг он остается прежним.
5. _test_set_book_rating_0_stays_the_same_ - при попытке изменить рейтинг на
0, он остается прежним.
6. _test_get_book_rating_ - проверка получения рейтинга книги.
7. _test_get_books_with_specific_rating_two_books_return_one_ - проверка 
возвращения книги с определенным рейтингом.
8. _test_get_books_with_specific_rating_no_books_with_wanted_rating_ - проверка
возвращения книги с определенным рейтингом, нет книги с нужным рейтингом.
9. _test_get_books_rating_ - проверка возвращения словаря книг с рейтингом.
10. _test_add_book_in_favorites_add_two_books_ - проверка добавления книг
в список избранных.
11. _test_add_book_in_favorites_same_title_doesnt_add_ - проверка на то, что
нельзя добавить книгу дважды.
12. _test_add_book_in_favorites_not_in_books_collector_ - проверка на то, что
нельзя добавить книгу в список избранных, если ее нет в словаре _books_rating_.
13. _test_delete_book_from_favorites_book_deleted_ - проверка удаления книги
из списка избранных.
14. _test_get_list_of_favorites_books_ - проверка получения списка избранных.