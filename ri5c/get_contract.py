# -*- coding: utf-8 -*-

# Let's get some data
from google.cloud import bigquery
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


def get_contract(contract_address):
    # Test subject 0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82
    # This needs to be converted to Parametrized SQL
    test_query = """
        #standardSQL
        SELECT
          *
        FROM
          `bigquery-public-data.ethereum_blockchain.token_transfers`
        WHERE
          token_address='%s'
        LIMIT
          1000
    """ % contract_address
    # Connect
    bql = bigquery.Client()
    # Query
    query_job = bql.query(test_query)
    iterator = query_job.result(timeout=30)
    rows = list(iterator)

    # This returns a simple dataset that can be used and tested
    return rows
    # Collect
    # How do I create the network? – how do i assign elements?  
    # Save
    
    # pass


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


# This is example code of a graph
'''
import sys

import pandas as pd
import networkx as nx
# Important because no GUI in vagrant
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from ri5c.get_contract import get_contract

G = nx.Graph()

# Where r is the result of get_contract
bct="0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82"
r = get_contract(bct)
df = pd.DataFrame(data=[list(x.values()) for x in r], columns=list(r[0].keys()))

nodes = df['to_address'].unique()
G.add_nodes_from(nodes)

for index, row in df.iterrows():
    G.add_edge(row['to_address'], row['from_address'])

# Our graph is G
# Because there is no GUI, file needs to be saved
import pylab
nx.draw(G)
pls.show()
pylab.savefig('foo.png')

'''

