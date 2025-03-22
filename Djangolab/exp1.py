from collections import defaultdict,deque,Counter,namedtuple,OrderedDict
Book=namedtuple('Book',('book_id','title','author'))
class Library:
    def __init__(self):
        self.books={}
        self.stock=Counter()
        self.borrowing_history=defaultdict(deque)
        self.recent_books=OrderedDict()
        self.priority_requests=deque()
    def add_book(self, book_id, title, author, quantity):
        book=Book(book_id, title, author)
        self.books[book_id]=book
        self.stock[book_id]+=quantity
        self.recent_books[book_id]=book
        print(f"'{title}' by {author} added to the library with {quantity} copies.")
    def borrow_book(self, user_id, book_id):
        if self.stock[book_id] > 0:
            self.stock[book_id] -= 1
            borrowed_book = self.books[book_id]
            self.borrowing_history[user_id].appendleft(borrowed_book)
            if len(self.borrowing_history[user_id]) > 3:
                self.borrowing_history[user_id].pop()
            print(f"User {user_id}' borrowed '{borrowed_book.title}'.")
        else:
            print(f"Sorry '{self.books[book_id].title}' is not available right now.")

   
    def return_book(self, user_id, book_id):
        self.stock[book_id] += 1
        print(f"User {user_id} returned '{self.books[book_id].title}'.")
    def add_priority_request(self, user_id, book_id):
        self.priority_requests.appendleft((user_id, book_id))
        print(f"VIP user {user_id} requested '{self.books[book_id].title}'.")
    def process_priority_request(self):
        while self.priority_requests:
            user_id, book_id =self.priority_requests.popleft()
            self.borrow_book(user_id, book_id)
    def get_popular_books(self):
        borrow_counter = Counter()
        for user_borrows in self.borrowing_history.values():
            for book in user_borrows:
                borrow_counter[book.title]+=1
        return borrow_counter.most_common(2)
    def get_user_borrow_history(self, user_id):
        if user_id in self.borrowing_history:
            return list(self.borrowing_history[user_id])
        else:
            return []
    def show_recent_books(self):
        print("Recently Added Books:")
        for book_id, book in self.recent_books.items():
            print(f" '{book.title}' by {book.author}")

library=Library()

library.add_book(1, 'Pride and Prejudice', 'Jane Austen', 5)
library.add_book(2, '1984', 'George Orwell', 3)
library.add_book(3, 'Frankenstein', 'Mary Shelley', 2)
library.borrow_book(101, 1)
library.borrow_book(102, 2)
library.borrow_book(101, 2)
library.add_priority_request(201, 3)
library.add_priority_request(202, 1)
library.process_priority_request()
library.return_book(101, 1)
popular_books = library.get_popular_books()
print("\n Most Popular Books:")
for title, count in popular_books:
    print(f"'{title}' -Borrowed {count} times")
history=library.get_user_borrow_history(101)
print("\n User 101's Borrowing History:")
for book in history:
    print(f"'{book.title}' by {book.author}")
library.show_recent_books()
