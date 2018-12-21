
# RI5C Risk Index Coefficient
## Python - NetworkX – Postgres implementation of an easy to use, interoperable framework to measure the risk coefficient of ERC20 contracts.  First implementation will use NetworkX: https://github.com/networkx/networkx

## Motivation
Due to the public nature of transaction data on blockchain based financial systems, it is possible to model these systems as a network and analyze its structure to provide and define whether the different variables that emerge in the transaction history of ERC20 tokens can be used to correlate the health of the system and therefore propose a risk coefficient that quantifies how active the token is, how distributed it is and inferr how likely it is to respond to contagion and how stable the price is.

## Quick start
As is standard everything you need is ```requirements.txt```. 
```
vagrant up
get server running and start creating stuff
vagrant ssh

$ cd /vagrant/
$ python # To run a console
```

Database created is called "mydb", to load psql console type:
```
psql -d mydb
```

### Configuring BigQuery
Note that this software uses Google's BigQuery Ethereum dataset, based on the fantastic work found of Evgeny Medvedev: https://github.com/blockchain-etl/ethereum-etl.

You should activate a BigQuery account following these instructions: https://cloud.google.com/blog/products/data-analytics/ethereum-bigquery-public-dataset-smart-contract-analytics

and you should have your access info in ```ri5c/config/big_query_cred.json```

PS: the location of that file is specified in an environment variable called ```GOOGLE_APPLICATION_CREDENTIALS```


## Load data and Evaluate
Find an interesting contract: ([OmiseGo](https://omisego.network)) ```omisego = "0xd26114cd6ee289accf82350c8d8487fedb8a0c07"```

And now, from Python console run:

```from ri5c.get_contract import network_this```

```network_this(omisego, limit=3000)```

Where *limit* is the transaction limit.

This will save an image called *network.png* in your source folder.

### Other interesting contracts

```
omisego = "0xd26114cd6ee289accf82350c8d8487fedb8a0c07"
cryptokitties = "0x06012c8cf97bead5deae237070f9587f8e7a266d"
bct = "0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82"
```
