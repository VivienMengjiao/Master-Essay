"""
Load the Agatha Christie knowledge graph and run SPARQL queries.
Export results to CSV files.
Run with: python query_kg.py (needs: pip install rdflib pandas)
"""

import rdflib
from rdflib import Graph
import pandas as pd
import os

g = Graph()
g.parse("agatha_kg.ttl", format="turtle")
print(f"Loaded {len(g)} triples\n")

# Create output folder
os.makedirs("query_results", exist_ok=True)

queries = {
    "1_novels_and_murderers": """
        SELECT ?novelName ?murdererName WHERE {
            ?novel a ac:Novel ;
                   ac:novelName ?novelName ;
                   ac:hasMurderer ?m .
            ?m ac:personName ?murdererName .
        }
        ORDER BY ?novelName
    """,

    "2_murderers_and_motives": """
        SELECT ?murdererName ?Motive WHERE {
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:hadMotive ?motive.
            ?motive rdfs:label ?Motive.
        }
        ORDER BY ?murdererName
    """,

    "3_murderers_and_killingMethod": """
        SELECT ?murdererName ?killingMethod WHERE {
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:usedMethod ?method.
            ?method rdfs:label ?killingMethod.
        }
        ORDER BY ?murdererName
    """,

    "3_suspect_and_relationToVictim": """
        SELECT ?suspect ?relation WHERE {
            ?s a ac:Suspect;
               ac:personName ?suspect;
               ac:relationToVictim ?relation.
        }
        ORDER BY ?suspect
    """,

    "4_murderers_and_theirFate": """
        SELECT ?murdererName ?fate WHERE {
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:fate ?fate.
        }
        ORDER BY ?murdererName
    """,

    "5_murderers_and_quoted_speeches": """
        SELECT ?murdererName ?quotedSpeeches WHERE {
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:quotedSpeeches ?quotedSpeeches.
        }
        ORDER BY ?murdererName
    """,

    "6_murderers_and_their_mentions": """
        SELECT ?murdererName ?mention ?suspect ?suspectMention WHERE {
            ?b a ac:Novel;
               ac:hasMurderer ?m;
               ac:hasSuspect ?s.
            ?m a ac:Murderer;
               ac:personName ?murdererName;
               ac:beenMentioned ?mention.
            ?s a ac:Suspect;
               ac:personName ?suspect;
               ac:beenMentioned ?suspectMention
        }
        ORDER BY ?murdererName
    """,
    "7)_murderers_and_their_occupations":"""
        SELECT ?murdererName ?occupation WHERE{
        ?m a ac:Murderer;
        ac:personName ?murdererName;
        ac:hasOccupation ?occupation
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
        print("  (no results)\n")
        continue

   
    columns = [str(var) for var in rows[0]]

   
    data = [[str(x) for x in row] for row in rows]

    
    df = pd.DataFrame(data, columns=columns)

   
    csv_file = f"query_results/{title}.csv"
    df.to_csv(csv_file, index=False, encoding='utf-8')

  
    for row in rows:
        print("  " + "  |  ".join(str(x) for x in row))

    print(f"\n✓ Saved to: {csv_file}\n")

print("=" * 64)
print("All queries exported to query_results/ folder!")
print("=" * 64)
