from flask import Flask, render_template, request
from rdflib import Graph, Literal, RDF, URIRef, Namespace

app = Flask(__name__)

# Step 1: Create RDF graph
g = Graph()
ex = Namespace("http://example.org/")

# Step 2: Add sample data (Book triples)
books = [
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy", 4.8),
    ("1984", "George Orwell", "Dystopian", 4.6),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 4.9),
    ("The Alchemist", "Paulo Coelho", "Fiction", 4.5),
    ("Pride and Prejudice", "Jane Austen", "Romance", 4.7),
    ("The Midnight Library", "Matt Haig", "Fiction", 4.4),
    ("Project Hail Mary", "Andy Weir", "Sci-Fi", 4.7),
    ("The Silent Patient", "Alex Michaelides", "Thriller", 4.3),
    ("Where the Crawdads Sing", "Delia Owens", "Mystery", 4.6),
    ("The Song of Achilles", "Madeline Miller", "Historical Fiction", 4.8),
    ("Atomic Habits", "James Clear", "Self-help", 4.9),
    ("The Psychology of Money", "Morgan Housel", "Finance", 4.8),
    ("Dune", "Frank Herbert", "Sci-Fi", 4.5),
    ("A Court of Thorns and Roses", "Sarah J. Maas", "Fantasy", 4.7),
    ("It Ends with Us", "Colleen Hoover", "Romance", 4.6),
    ("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "Fiction", 4.8),
    ("Fourth Wing", "Rebecca Yarros", "Fantasy", 4.7),
    ("The House in the Cerulean Sea", "T.J. Klune", "Fantasy", 4.9),
    ("The Martian", "Andy Weir", "Sci-Fi", 4.8),
    ("The Girl on the Train", "Paula Hawkins", "Thriller", 4.3),
]


for i, (title, author, genre, rating) in enumerate(books, start=1):
    book_uri = ex[f"Book{i}"]
    g.add((book_uri, RDF.type, ex.Book))
    g.add((book_uri, ex.hasTitle, Literal(title)))
    g.add((book_uri, ex.hasAuthor, Literal(author)))
    g.add((book_uri, ex.hasGenre, Literal(genre)))
    g.add((book_uri, ex.hasRating, Literal(rating)))


# Step 3: Flask Routes
@app.route("/")
def index():
    # Extract unique genres for dropdown
    genres = sorted(set(str(o) for s, p, o in g.triples((None, ex.hasGenre, None))))
    return render_template("index.html", genres=genres, books=None)


@app.route("/recommend", methods=["POST"])
def recommend():
    selected_genre = request.form.get("genre")
    results = []

    for s, p, o in g.triples((None, ex.hasGenre, Literal(selected_genre))):
        title = g.value(s, ex.hasTitle)
        author = g.value(s, ex.hasAuthor)
        rating = g.value(s, ex.hasRating)
        results.append((title, author, rating))

    # Sort by rating (descending)
    results.sort(key=lambda x: float(x[2]), reverse=True)

    genres = sorted(set(str(o) for s, p, o in g.triples((None, ex.hasGenre, None))))
    return render_template(
        "index.html", genres=genres, books=results, selected_genre=selected_genre
    )


if __name__ == "__main__":
    app.run(debug=True)
