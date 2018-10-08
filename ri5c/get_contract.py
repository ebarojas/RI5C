# Let's get some data
from google.cloud import bigquery
bigquery_client = bigquery.Client()


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
    # Collect
    # Save
    pass


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