"""
Load the Agatha Christie knowledge graph and run SPARQL queries.
Run with:  python query_kg.py
(needs: pip install rdflib)
"""
import rdflib
from rdflib import Graph

g = Graph()
g.parse("agatha_kg.ttl", format="turtle")
print(f"Loaded {len(g)} triples\n")

queries = {
    "1) novels and murderers": """
        PREFIX ac: <http://example.org/agatha/>

        SELECT ?novelName ?murdererName WHERE {
            ?novel a ac:Novel ;
                   ac:novelName ?novelName ;
                   ac:hasMurderer ?m .

            ?m ac:personName ?murdererName .
        }
        ORDER BY ?novelName
    """
}

for title, q in queries.items():
    print("=" * 64)
    print(title)
    print("=" * 64)

    rows = list(g.query(q))

    if not rows:
        print("  (no results)")

    for row in rows:
        print("  " + "  |  ".join(str(x) for x in row))

    print()