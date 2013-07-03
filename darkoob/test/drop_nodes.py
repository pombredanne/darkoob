from py2neo import neo4j, cypher

graph_db = neo4j.GraphDatabaseService()
query = "start node=relationship(*) delete node;"
query2 = "start node=node(*) delete node;"
data, metadata = cypher.execute(graph_db, query)
data, metadata = cypher.execute(graph_db, query2)
