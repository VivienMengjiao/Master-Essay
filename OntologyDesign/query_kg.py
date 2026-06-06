import rdflib
from rdflib import Graph

g = Graph()
g.parse("agatha_kg.ttl", format="turtle")
print(f"Loaded {len(g)} triples\n")

queries = {
    "1) novels and murderers": """
        
        SELECT ?novelName ?murdererName WHERE {
            ?novel a ac:Novel ;
                   ac:novelName ?novelName ;
                   ac:hasMurderer ?m .

            ?m ac:personName ?murdererName .
        }
        ORDER BY ?novelName
    """,
   "2)murderers and motives": """
      
      SELECT ?murdererName ?Motive WHERE{
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:hadMotive  ?motive.
            
            ?motive rdfs:label ?Motive.
        }
        ORDER BY ?murdererName
    """,
    "3)murderers and killingMethod":"""
      
      SELECT ?murdererName   ?killingMethod WHERE{
             ?m a ac:Murderer;
                ac:personName ?murdererName;
                ac:usedMethod ?method.
            ?method rdfs:label ?killingMethod.
    }
        ORDER BY ?murdererName
      """,
    "3)suspect and relationToVictim":"""
       
       SELECT ?suspect ?relation WHERE{
              ?s a ac:Suspect;
                    ac:personName ?suspect;
                    ac:relationToVictim ?relation.
    }
         ORDER BY ?suspect
    """,
    "4)murderers and theirFate": """
       SELECT ?murdererName ?fate WHERE{
       ?m a ac:Murderer;
            ac:personName ?murdererName;
            ac:fate ?fate.
            }
            ORDER BY ?murdererName
    """,
    "5)murderers and quoted speeches": """
       SELECT ?murdererName ?quotedSpeeches WHERE{
       ?m a ac:Murderer;
            ac:personName ?murdererName;
            ac:quotedSpeeches ?quotedSpeeches.
            }
            ORDER BY ?murdererName
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
