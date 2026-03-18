"""
filename: graph_recommend.py
build the person/book graph and get recommendations for spencer.
Contributions: Sahana Dhar
"""
from graph_api import add_node, add_edge, get_recommendations


def build_graph():
    # people
    add_node("Emily", "Person", {"name": "Emily"})
    add_node("Spencer", "Person", {"name": "Spencer"})
    add_node("Brendan", "Person", {"name": "Brendan"})
    add_node("Trevor", "Person", {"name": "Trevor"})
    add_node("Paxton", "Person", {"name": "Paxton"})

    # books
    add_node("Cosmos", "Book", {"title": "Cosmos", "price": 17.00})
    add_node("Database Design", "Book", {"title": "Database Design", "price": 195.00})
    add_node("The Life of Cronkite", "Book", {"title": "The Life of Cronkite", "price": 29.95})
    add_node("DNA and you", "Book", {"title": "DNA and you", "price": 11.50})

    # bought edges
    add_edge("Emily", "Database Design", "bought")
    add_edge("Spencer", "Cosmos", "bought")
    add_edge("Spencer", "Database Design", "bought")
    add_edge("Brendan", "Database Design", "bought")
    add_edge("Brendan", "DNA and you", "bought")
    add_edge("Trevor", "Cosmos", "bought")
    add_edge("Trevor", "Database Design", "bought")
    add_edge("Paxton", "Database Design", "bought")
    add_edge("Paxton", "The Life of Cronkite", "bought")

    # knows edges
    add_edge("Emily", "Spencer", "knows")
    add_edge("Spencer", "Emily", "knows")
    add_edge("Spencer", "Brendan", "knows")


def main():
    build_graph()
    recs = get_recommendations("Spencer")
    print("book recommendations for spencer:")
    for book in recs:
        print(book)


if __name__ == "__main__":
    main()

