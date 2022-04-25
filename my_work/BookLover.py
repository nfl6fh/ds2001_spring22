"""
author: Nathan Lindley (nfl6fh)

BookLover Programming Assignment
"""

import unittest


class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list=None):
        if book_list is None:
            book_list = []
        self.name: str = name
        self.email: str = email
        self.fav_genre: str = fav_genre
        self.num_books: int = num_books
        self.book_list = book_list

    def addBook(self, bookName: str, rating: int) -> None:
        if not self.hasRead(bookName):
            self.book_list.append((bookName, rating))
            self.num_books += 1

    def hasRead(self, bookName: str) -> bool:
        for book in self.book_list:
            if bookName == book[0]:
                return True
        return False

    def numBooksRead(self) -> int:
        return self.num_books

    def favBooks(self) -> []:
        favs = []
        for book in self.book_list:
            if book[1] > 3:
                favs.append(book)
        return favs


class BookLoverTest(unittest.TestCase):
    reader = BookLover('Nate', 'nfl6fh', 'mystery')

    def test1and2_addBook(self):
        self.reader.addBook('HP', 5)
        self.assertEqual(self.reader.book_list, [('HP', 5)])
        self.assertEqual(self.reader.num_books, 1)
        self.reader.addBook('HP', 5)
        self.assertEqual(self.reader.book_list, [('HP', 5)])
        self.assertEqual(self.reader.num_books, 1)

    def test3and4_hasRead(self):
        self.assertTrue(self.reader.hasRead('HP'))
        self.assertFalse(self.reader.hasRead('gf'))

    def test5_numBooksRead(self):
        self.assertEqual(self.reader.numBooksRead(), 1)

    def test6_favBooks(self):
        self.reader.addBook('gh', 4)
        self.reader.addBook('inl', 2)
        self.reader.addBook('fg', 5)
        self.assertEqual(self.reader.favBooks(), [('HP', 5), ('gh', 4), ('fg', 5)])


if __name__ == '__main__':
    unittest.main()
