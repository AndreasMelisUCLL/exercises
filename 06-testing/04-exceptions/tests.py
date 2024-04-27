import pytest
from book import Book

@pytest.mark.parametrize('title, isbn', [
    ('Watchmen', '978-1779501127'),
    ('A.I.', '978 9463939591'),
    ('Een kleine geschiedenis van intelligentie', '978-94-027-1349 7'),
    
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert (book.title, book.isbn) == (title, isbn)
    
    
@pytest.mark.parametrize('title, isbn', [
    ('', '978-1779501127'),
    (' ', '978 9463939591'),
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
    
    
@pytest.mark.parametrize('title, isbn', [
    ('Watchmen', '978-1779501128'),
    ('A.I.', '978 9463939592'),
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)