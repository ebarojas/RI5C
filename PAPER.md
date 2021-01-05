---
title: 'RI5C: A Visual Blockchain Navigator'
tags:
  - Cryptocurrency
  - Network
  - Python
  - Ethereum

authors:
  - name: Everardo J. Barojas-Méndez
    orcid: 0000-0003-4182-1537
    affiliation: 1
  - name: Fernando Ramírez Alatriste
    orcid: 0000-0001-7991-7951
    affiliation: 3
  - name: María Saiz Santos
    affiliation: 2
  - name: Abdolreza Rashnavady Nodjoumi
    affiliation: 1
affiliations:
 - name: Universidad Nacional Autónoma de México
   index: 1
 - name: Universidad de País Vasco
   index: 2
 - name: Universidad Autónoma de la Ciudad de México
   index: 3
date: 28 December 2020
bibliography: paper.bib

---

# Summary

Close to twelve years after the genesis of Bitcoin [@bitcoin_nak], the first decentralised digital asset enabled by cryptography ^[i.e., What is now generally referred to as "cryptocurrency"] a new category of financial assets has emerged. One of the key differentiators of this new category is the introduction of a new issuance method for these digital assets that takes place on decentralised networks like Bitcoin or Ethereum. Inside of these networks any individual with technical know-how can create a new digital asset and sell it to investors via a private or public offering, furthermore these investors can trade these assets in highly liquid secondary markets. Fully understanding the behaviour of these new digital assets where data is persisted in a public ledger colloquially known as a "Blockchain" and accessible as plain-text via public APIs requires data analysis and visualisation tools.

# Statement of need

`RI5C` is an interactive blockchain explorer packaged as a web-application that allows users to visualise a network diagram of a subset of transactions on the Ethereum Blockchain. This subset is filtered by smart-contract addresses, where each address represents a cryptocurrency. It is written in Python and Javascript which together allow for data collection, analysis and treatment as well as an easy-to-use web serving application. The first layer of interaction was designed to be accessed via a public website accessible at `www.ri5c.com` [@ri5c] but its components are modular enough that users can clone the code and customise queries, graphs and networks.

`RI5C` was designed to be used by developers, students, authorities and investors to further understand the behaviour of cryptocurrencies. It was the result of a PhD Thesis [@ri5c_phd:2020]. The visualisation capacities, ease and speed of use to non-technical users has aided in the understanding of these complex systems by a great number of people. `RI5C` has already processed queries for thousands of users through its web-application [@ri5c] and has helped Master's students understand the structure of transactions in a decentralised network.

# Acknowledgements

We acknowledge contributions from Pablo Suárez-Serrato for his help in the understanding of network analysis, and much support from María Saiz Santos  and the University of Basque Country for its accommodation during the research that led to the creation of RI5C.

# References

