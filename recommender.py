# recommender.py
# Semantic Book Recommender - minimal console app using rdflib

from rdflib import Graph, Literal, RDF, URIRef, Namespace

# --- Setup graph and namespace ---
g = Graph()
ex = Namespace("http://example.org/schema/")

# Bind prefix (makes output nicer if serialized)
g.bind("ex", ex)


# --- Helper to add a book with properties ---
def add_book(id_, title, author, genre, year, rating):
    book_uri = ex[id_]
    g.add((book_uri, RDF.type, ex.Book))
    g.add((book_uri, ex.hasTitle, Literal(title)))
    g.add((book_uri, ex.hasAuthor, Literal(author)))
    g.add((book_uri, ex.hasGenre, Literal(genre)))
    g.add((book_uri, ex.hasYear, Literal(year)))
    g.add((book_uri, ex.hasRating, Literal(rating)))
    return book_uri


# --- Sample data (you can expand this) ---
add_book("book1", "The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, 4.8)
add_book("book2", "1984", "George Orwell", "Dystopian", 1949, 4.6)
add_book("book3", "HarryPotter1", "J.K. Rowling", "Fantasy", 1997, 4.9)
add_book("book4", "ToKillAMockingbird", "Harper Lee", "Fiction", 1960, 4.7)
add_book("book5", "Dune", "Frank Herbert", "Sci-Fi", 1965, 4.5)
add_book("book6", "BraveNewWorld", "Aldous Huxley", "Dystopian", 1932, 4.2)
add_book("book7", "Mistborn", "Brandon Sanderson", "Fantasy", 2006, 4.4)

# --- Newer books (2010–2024) ---
add_book("book8", "The Midnight Library", "Matt Haig", "Fiction", 2020, 4.3)
add_book("book9", "Project Hail Mary", "Andy Weir", "Sci-Fi", 2021, 4.7)
add_book("book10", "A Court of Thorns and Roses", "Sarah J. Maas", "Fantasy", 2015, 4.5)
add_book("book11", "The Silent Patient", "Alex Michaelides", "Thriller", 2019, 4.1)
add_book("book12", "The Song of Achilles", "Madeline Miller", "Romance", 2011, 4.6)
add_book("book13", "Circe", "Madeline Miller", "Fantasy", 2018, 4.4)
add_book("book14", "The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "Fiction", 2017, 4.7)
add_book("book15", "Atomic Habits", "James Clear", "Self-Help", 2018, 4.8)
add_book("book16", "The Subtle Art of Not Giving a F*ck", "Mark Manson", "Self-Help", 2016, 4.3)
add_book("book17", "The House in the Cerulean Sea", "TJ Klune", "Fantasy", 2020, 4.8)
add_book("book18", "Iron Flame", "Rebecca Yarros", "Fantasy", 2023, 4.6)
add_book("book19", "Fourth Wing", "Rebecca Yarros", "Fantasy", 2023, 4.7)
add_book("book20", "Tomorrow, and Tomorrow, and Tomorrow", "Gabrielle Zevin", "Fiction", 2022, 4.5)
add_book("book21", "Lessons in Chemistry", "Bonnie Garmus", "Fiction", 2022, 4.6)
add_book("book22", "The Ballad of Songbirds and Snakes", "Suzanne Collins", "Dystopian", 2020, 4.2)
add_book("book23", "The Measure", "Nikki Erlick", "Fiction", 2022, 4.3)
add_book("book24", "Light Bringer", "Pierce Brown", "Sci-Fi", 2023, 4.6)
add_book("book25", "The Atlas Paradox", "Olivie Blake", "Fantasy", 2022, 4.1)
# --- Additional books (2010–2025) ---
add_book("book26", "Vicious", "V.E. Schwab", "Fantasy", 2013, 4.4)
add_book("book27", "Vengeful", "V.E. Schwab", "Fantasy", 2018, 4.5)
add_book("book28", "The Priory of the Orange Tree", "Samantha Shannon", "Fantasy", 2019, 4.6)
add_book("book29", "Red, White & Royal Blue", "Casey McQuiston", "Romance", 2019, 4.7)
add_book("book30", "One of Us Is Lying", "Karen M. McManus", "Thriller", 2017, 4.3)
add_book("book31", "One of Us Is Next", "Karen M. McManus", "Thriller", 2020, 4.2)
add_book("book32", "Crying in H Mart", "Michelle Zauner", "Memoir", 2021, 4.5)
add_book("book33", "The Lincoln Highway", "Amor Towles", "Fiction", 2021, 4.4)
add_book("book34", "Sea of Tranquility", "Emily St. John Mandel", "Fiction", 2022, 4.3)
add_book("book35", "Tomorrow, and Tomorrow, and Tomorrow", "Gabrielle Zevin", "Fiction", 2022, 4.5)
add_book("book36", "The Candy House", "Jennifer Egan", "Fiction", 2022, 4.2)
add_book("book37", "Lessons in Chemistry", "Bonnie Garmus", "Fiction", 2022, 4.6)
add_book("book38", "A Desolation Called Peace", "Arkady Martine", "Sci-Fi", 2021, 4.4)
add_book("book39", "Axiom’s End", "Lindsay Ellis", "Sci-Fi", 2020, 4.2)
add_book("book40", "Sea of Tranquility", "Emily St. John Mandel", "Fiction", 2022, 4.3)
add_book("book41", "The Fault in Our Stars", "John Green", "Young Adult", 2012, 4.7)
add_book("book42", "Looking for Alaska", "John Green", "Young Adult", 2005, 4.5)
add_book("book43", "Paper Towns", "John Green", "Young Adult", 2008, 4.4)
add_book("book44", "An Abundance of Katherines", "John Green", "Young Adult", 2006, 4.2)
add_book("book45", "The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, 4.1)
add_book("book46", "To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 4.8)
add_book("book47", "Pride and Prejudice", "Jane Austen", "Romance", 1813, 4.7)
add_book("book48", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 4.3)
add_book("book49", "Moby-Dick", "Herman Melville", "Adventure", 1851, 4.0)
add_book("book50", "War and Peace", "Leo Tolstoy", "Historical Fiction", 1869, 4.4)


# --- Functions to query the graph ---
def recommend_by_genre(genre):
    print(f"\n📚 Recommended books in genre: {genre}")
    found = False
    for book in g.subjects(predicate=ex.hasGenre, object=Literal(genre)):
        title = g.value(book, ex.hasTitle)
        author = g.value(book, ex.hasAuthor)
        rating = g.value(book, ex.hasRating)
        print(f"- {title} by {author} (Rating: {rating})")
        found = True
    if not found:
        print("No books found for that genre.")


def recommend_by_author(author):
    print(f"\n📚 Books by author: {author}")
    found = False
    for book in g.subjects(predicate=ex.hasAuthor, object=Literal(author)):
        title = g.value(book, ex.hasTitle)
        genre = g.value(book, ex.hasGenre)
        rating = g.value(book, ex.hasRating)
        print(f"- {title} (Genre: {genre}, Rating: {rating})")
        found = True
    if not found:
        print("No books found for that author.")


def recommend_top_rated(min_rating=4.5):
    print(f"\n📚 Books with rating >= {min_rating}:")
    found = False
    for book in g.subjects(predicate=ex.hasRating, object=None):
        rating = g.value(book, ex.hasRating)
        try:
            if float(rating) >= float(min_rating):
                title = g.value(book, ex.hasTitle)
                author = g.value(book, ex.hasAuthor)
                print(f"- {title} by {author} (Rating: {rating})")
                found = True
        except Exception:
            continue
    if not found:
        print("No books found with that rating or higher.")


# --- Optional: SPARQL example using graph.query ---
def sparql_example_find_by_year(year):
    q = f"""
    PREFIX ex: <http://example.org/schema/>
    SELECT ?title ?author ?genre ?rating
    WHERE {{
      ?book a ex:Book ;
            ex:hasYear {year} ;
            ex:hasTitle ?title ;
            ex:hasAuthor ?author ;
            ex:hasGenre ?genre ;
            ex:hasRating ?rating .
    }}
    """
    qres = g.query(q)
    print(f"\n📚 Books published in {year}:")
    found = False
    for row in qres:
        print(
            f"- {row.title} by {row.author} (Genre: {row.genre}, Rating: {row.rating})"
        )
        found = True
    if not found:
        print("No books found for that year.")


# --- Main interactive loop ---
def main():
    print("=== Semantic Book Recommender (rdflib) ===")
    while True:
        print("\nChoose an option:")
        print("1) Recommend by genre")
        print("2) Recommend by author")
        print("3) Recommend top-rated books")
        print("4) SPARQL: Find by year")
        print("5) Show all RDF triples")
        print("6) Export graph to 'books.ttl'")
        print("0) Exit")
        choice = input("Enter option: ").strip()

        if choice == "1":
            gname = input("Enter genre (e.g., Fantasy, Dystopian, Sci-Fi): ").strip()
            recommend_by_genre(gname)
        elif choice == "2":
            a = input("Enter author (exact name): ").strip()
            recommend_by_author(a)
        elif choice == "3":
            mr = input("Minimum rating (default 4.5): ").strip() or "4.5"
            recommend_top_rated(mr)
        elif choice == "4":
            y = input("Enter publication year (e.g., 1997): ").strip()
            if y.isdigit():
                sparql_example_find_by_year(y)
            else:
                print("Invalid year.")
        elif choice == "5":
            print("\n--- RDF Triples ---")
            for s, p, o in g:
                print(s, p, o)
        elif choice == "6":
            g.serialize(destination="books.ttl", format="turtle")
            print("Exported 'books.ttl' to project folder.")
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
