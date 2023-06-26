class AuthorCRUD:
    def __init__(self, database):
        self.db = database

    def create_author(self, name, age, gender):
        query = "CREATE (:Author {name: $name,age: $age,gender: $gender})"
        parameters = {"name": name, "age": age, "gender": gender}
        self.db.execute_query(query, parameters)

    def get_author(self):
        query = "MATCH (au:Author) RETURN au.name AS name"
        results = self.db.execute_query(query)
        return print([result["name"] for result in results])

    def update_author(self, name, age, gender):
        query = "MATCH (a:Author {name: $name}) SET a.age = $age,a.gender = $gender"
        parameters = {"name": name, "age": age, "gender": gender}
        self.db.execute_query(query, parameters)

    def delete_author(self, name):
        query = "MATCH (a:Author {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def insert_author_book(self, author_name, book_name):
        query = "MATCH (a:Author{name: $author_name}) MATCH (b:Book {name: $book_name}) CREATE (a)-[:WROTE]->(b)"
        parameters = {"author_name": author_name, "book_name": book_name}
        self.db.execute_query(query, parameters)

    def get_wrote(self, name):
        query = "MATCH (a:Author{name: $name})-[:WROTE]->(b:Book) RETURN DISTINCT b.name AS bname"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["bname"] for result in results]
