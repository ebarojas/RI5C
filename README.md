
# RI5C Risk Index Coefficient
## Python - NetworkX – Postgres implementation of an easy to use, interoperable framework to measure the risk coefficient of ERC20 contracts.  First implementation will use NetworkX: https://github.com/networkx/networkx

## Motivation
Due to the public nature of transaction data on blockchain based financial systems, it is possible to model these systems as a network and analyze its structure to provide and define whether the different variables that emerge in the transaction history of ERC20 tokens can be used to correlate the health of the system and therefore propose a risk coefficient that quantifies how active the token is, how distributed it is and inferr how likely it is to respond to contagion and how stable the price is.

## Quick start
```
vagrant up
get server running and start creating stuff
vagrant ssh

$ cd /vagrant/
$ python # To run a console
```
## Load data
Here a contract address should be specified ```0x...```

Database created is called "mydb", to load psql console type:
```
psql -d mydb
```

### BigQuery
Note that this software uses Google's BigQuery Ethereum dataset, based on the fantastic work found in this repo https://github.com/blockchain-etl/ethereum-etl.

You should activate a BigQuery account following these instructions: https://cloud.google.com/blog/products/data-analytics/ethereum-bigquery-public-dataset-smart-contract-analytics

and you should have your access info in ```ri5c/config/big_query_cred.json```

PS: the location of that file is specified in an environment variable called ```GOOGLE_APPLICATION_CREDENTIALS```

## Evaluate
Where the magic will happen – we extract transactions, model the network and provide an analysis.
