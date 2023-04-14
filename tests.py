import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_same_title_doesnt_add(self, collector):
        collector.add_new_book('Гарри Поттер и Тайная Комната')
        collector.add_new_book('Гарри Поттер и Тайная Комната')
        assert len(collector.get_books_rating()) == 1

    @pytest.mark.parametrize('rating_set, rating', [[-1, 1], [0, 1], [2, 2], [9, 9], [10, 10], [11, 1]])
    def test_get_book_rating(self, collector, rating_set, rating):
        collector.add_new_book('Гарри Поттер и Философский Камень')
        collector.set_book_rating('Гарри Поттер и Философский Камень', rating_set)
        assert collector.get_book_rating('Гарри Поттер и Философский Камень') == rating

    def test_get_books_with_specific_rating_two_books_return_one(self, collector):
        collector.add_new_book('Гарри Поттер и Дары Смерти')
        collector.set_book_rating('Гарри Поттер и Дары Смерти', 8)
        collector.add_new_book('Гарри Поттер и Проклятое Дитя')
        collector.set_book_rating('Гарри Поттер и Проклятое Дитя', 2)
        assert collector.get_books_with_specific_rating(8) == ['Гарри Поттер и Дары Смерти']

    def test_get_books_with_specific_rating_no_books_with_wanted_rating(self, collector):
        collector.add_new_book('Гарри Поттер и Дары Смерти')
        collector.set_book_rating('Гарри Поттер и Дары Смерти', 8)
        collector.add_new_book('Гарри Поттер и Проклятое Дитя')
        collector.set_book_rating('Гарри Поттер и Проклятое Дитя', 2)
        assert collector.get_books_with_specific_rating(7) == []

    def test_get_books_rating_returns_all_the_books_with_rating(self, collector):
        collector.add_new_book('Гарри Поттер и Философский Камень')
        collector.set_book_rating('Гарри Поттер и Философский Камень', 9)
        collector.add_new_book('Гарри Поттер и Тайная Комната')
        collector.set_book_rating('Гарри Поттер и Тайная Комната', 8)
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_rating('Гарри Поттер и Узник Азкабана', 10)
        assert collector.get_books_rating() == {'Гарри Поттер и Философский Камень': 9,
                                                'Гарри Поттер и Тайная Комната': 8,
                                                'Гарри Поттер и Узник Азкабана': 10}

    def test_add_book_in_favorites_add_two_books(self, collector):
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_new_book('Гарри Поттер и Кубок Огня')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Кубок Огня')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_same_title_doesnt_add(self, collector):
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_in_books_collector(self, collector):
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_deleted(self, collector):
        collector.add_new_book('Гарри Поттер и Философский Камень')
        collector.add_book_in_favorites('Гарри Поттер и Философский Камень')
        collector.delete_book_from_favorites('Гарри Поттер и Философский Камень')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гарри Поттер и Философский Камень')
        collector.add_book_in_favorites('Гарри Поттер и Философский Камень')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и Философский Камень']