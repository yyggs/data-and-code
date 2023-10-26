from rdflib import Graph
import pprint

# Change the following line to your SPARQL end point.
SPARQL_ENDPOINT = 'http://localhost:3030/s2484724-epcc/sparql'

g = Graph()
g.parse(SPARQL_ENDPOINT, format="application/rdf+xml")

# Query and print all the triples in the dataset (i.e., triple store).
sparql_query = "SELECT ?s ?p ?o where {?s ?p ?o}"
print(f'SPARQL query -> {sparql_query}')
result = g.query(sparql_query)
for row in result:
    print(row)

print()
print('*********************')
print()

# Query only the people in the RDF data store (i.e., just the names)
prefixes = '''
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX : <http://www.epcc.ed.ac.uk/education-training/general-training/about-us/staff#>
    PREFIX dbpedia: <http://dbpedia.org/resource/#>
    PREFIX usgov: <http://whitehouse.gov/administration/#>
'''
# Write your SELECT query here
# Place your query after the prefixes.

# Query people who live near Edinburgh
sparql_query = prefixes + '''
    SELECT ?name WHERE {
        ?person foaf:based_near dbpedia:Edinburgh .
        ?person foaf:name ?name .
    }
'''
print('People who live near Edinburgh:')
result = g.query(sparql_query)
for row in result:
    print(row[0])
