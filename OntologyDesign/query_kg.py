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
    """,
   "2)murderers and motives": """
      PREFIX ac: <http://example.org/agatha/>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      SELECT ?murdererName ?Motive WHERE{
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:hadMotive  ?motive.
            
            ?motive rdfs:label ?Motive.
        }
        ORDER BY ?murdererName
    """,
    "3)murderers and killingMethod":"""
      PREFIX ac: <http://example.org/agatha/>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      SELECT ?murdererName   ?killingMethod WHERE{
             ?m a ac:Murderer;
                ac:personName ?murdererName;
                ac:usedMethod ?method.
            ?method rdfs:label ?killingMethod.
    }
        ORDER BY ?murdererName
      """,
    "4)suspect and relationToVictim":"""
       PREFIX ac: <http://example.org/agatha/>
       SELECT ?suspect ?relation WHERE{
              ?s a ac:Suspect;
                    ac:personName ?suspect;
                    ac:relationToVictim ?relation.
    }
         ORDER BY ?suspect
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
