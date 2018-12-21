# -*- coding: utf-8 -*-

from google.cloud import bigquery
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('Agg') # Important because no GUI in vagrant or server
import matplotlib.pyplot as plt
import community # Detecting communities
import pylab # Exporting figures

# Instantiate Big Query
bigquery_client = bigquery.Client()

# Nodos = addresses
# Aristas = proporcional a tamaño de transacción
# Colour?
# Distribución de grado – desviación estándar de distribución de grado
# Cuál es el tipo de red
# Teoría de redes
# Centralidad de nodos [la más importante es el grado]
# *Static or dynamic?*
# Maybe use pandas

# Do this https://cloud.google.com/bigquery/docs/parameterized-queries#bigquery-query-params-cli


def get_contract(contract_address, limit=1000):
    # Test subject 0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82
    # This needs to be converted to Parametrized SQL
    print "Getting query..."
    test_query = """
        #standardSQL
        SELECT
          *
        FROM
          `bigquery-public-data.ethereum_blockchain.token_transfers`
        WHERE
          token_address='%s'
        LIMIT
          %s
    """ % (contract_address, limit)

    # Connect
    bql = bigquery.Client()
    # Query
    query_job = bql.query(test_query)
    iterator = query_job.result(timeout=30)
    rows = list(iterator)

    print "Finished getting data"
    # This returns a simple dataset that can be used and tested
    return rows

def create_graph(contract):
    # Create graph
    print "Creating a simple graph..."
    G = nx.Graph()
    # Pandas dataframe
    df = pd.DataFrame(data=[list(x.values()) for x in contract], columns=list(contract[0].keys()))
    # Create Nodes
    nodes = df['to_address'].unique()
    G.add_nodes_from(nodes)
    # Create edges
    for index, row in df.iterrows():
        G.add_edge(row['to_address'], row['from_address'])

    print "Graph created."
    print(nx.info(G))
    return G

def draw_graph(graph, filename='network.png'):
    print "Starting to draw..."
    G = graph
    #first compute the best partition
    partition = community.best_partition(G)
    plt.figure(figsize=(100,100))
    #drawing
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    count = 0.
    for com in set(partition.values()) :
        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys()
                                    if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                    node_color = str(count / size))

    # Draw
    nx.draw_networkx_edges(G, pos, alpha=0.5)

    print "And now, let's save it in "+filename
    pylab.savefig('network.png')


def network_this(contract, limit=1000):
    contract = get_contract(contract, limit)
    graph = create_graph(contract)
    draw_graph(graph)
    print "Success"
    pass

'''
# TRY
from ri5c.get_contract import network_this
omisego = "0xd26114cd6ee289accf82350c8d8487fedb8a0c07"
cryptokitties = "0x06012c8cf97bead5deae237070f9587f8e7a266d"
bct = "0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82"
network_this("0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82", 3000)
'''

# query_params = [
#     bigquery.ScalarQueryParameter('gender', 'STRING', 'M'),
#     bigquery.ArrayQueryParameter(
#         'states', 'STRING', ['WA', 'WI', 'WV', 'WY'])
# ]
# job_config = bigquery.QueryJobConfig()
# job_config.query_parameters = query_params
# query_job = client.query(
#     query,
#     # Location must match that of the dataset(s) referenced in the query.
#     location='US',
#     job_config=job_config)  # API request - starts the query

# # Print the results
# for row in query_job:
#     print('{}: \t{}'.format(row.name, row.count))

# assert query_job.state == 'DONE'

# Good reference for BigQuery
# https://cloud.google.com/bigquery/docs/parameterized-queries#bigquery-query-params-python



# This is example code of a graph for python console should RM LATER
'''
import pandas as pd
import networkx as nx
# Important because no GUI in vagrant
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import community # Detecting communities
import pylab # Exporting figures
# My code
from ri5c.get_contract import get_contract

G = nx.Graph()

# Where r is the result of get_contract
bct="0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82"
limit = 4500
r = get_contract(bct, limit)
df = pd.DataFrame(data=[list(x.values()) for x in r], columns=list(r[0].keys()))

nodes = df['to_address'].unique()
G.add_nodes_from(nodes)

for index, row in df.iterrows():
    G.add_edge(row['to_address'], row['from_address'])

# Our graph is G
# Because there is no GUI, file needs to be saved


# DRAWING
#first compute the best partition
partition = community.best_partition(G)
plt.figure(figsize=(100,100))
#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G, pos, alpha=0.5)

# pls.show() # Show or just save
pylab.savefig('network.png')

'''

