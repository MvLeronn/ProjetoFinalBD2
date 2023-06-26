class BookCRUD:
    def __init__(self, database):
        self.db = database

    def create_book(self, name, pages, genre):
        pages = int(pages)
        query = "CREATE (:Book {name: $name,pages: $pages,genre: $genre})"
        parameters = {"name": name, "pages": pages, "genre": genre}
        self.db.execute_query(query, parameters)

    def get_book(self):
        query = "MATCH (b:Book) RETURN b.name AS name"
        results = self.db.execute_query(query)
        return print([result["name"] for result in results])

    def update_book(self, name, pages, genre):
        pages = int(pages)
        query = "MATCH (b:Book {name: $name}) SET b.pages = $pages,b.genre = $genre"
        parameters = {"name": name, "pages": pages, "genre": genre}
        self.db.execute_query(query, parameters)

    def delete_book(self, name):
        query = "MATCH (b:Book {name: $name}) DETACH DELETE b"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_book_avg_pages(self):
        query = "MATCH (b:Book) RETURN AVG(b.pages) AS pages"
        results = self.db.execute_query(query)
        return print([result["pages"] for result in results])


