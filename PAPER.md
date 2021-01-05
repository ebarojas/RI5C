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
Close to twelve years after the genesis of Bitcoin [@bitcoin_nak], the first decentralised digital asset enabled by cryptography ^[i.e., What is now generally referred to as "cryptocurrency"] a new category of financial assets has emerged. One of the key differentiators of this new category is the introduction of a new issuance method for these digital assets that takes place on decentralised networks like Bitcoin or Ethereum. Inside of these networks any individual with technical know-how can create a new digital asset and sell it to investors via a private or public offering, furthermore these investors can trade these assets in highly liquid 24hr secondary markets. Fully understanding the behaviour of these new digital assets whose data is persisted in a public ledger colloquially known as a "Blockchain" and accessible as plain-text via public APIs requires data analysis and visualisation tools.

<!-- ABSTRACT 

Poco más de 10 años después de la génesis de Bitcoin, el primer activo digital habilitado por criptografía,\footnote{ También llamado criptodivisa} hemos visto una nueva categoría de activos financieros emerger. Con ello, una gran cantidad de criptodivisas han generado un mercado secundario altamente líquido. El valor de este mercado de activos basados en criptodivisas ha crecido enormemente, en su máximo histórico hasta \$829 millones de millones de dólares \cite{coinmarketcap}, equivalente al producto interno bruto de México en el 2005 \cite{GDPMEX}. Durante el 2017 se vivió una burbuja financiera dentro de este ecosistema emergente, en la cual estos activos se valorizaron con tasas de crecimiento exponenciales y que hicieron eco a las valoraciones de acciones de empresas tecnológicas en la burbuja \emph{\hyperref[s:dotcom]{PuntoCom}}. Uno de los factores significativos que contribuyeron a esta burbuja, fue la introducción de un nuevo método de emisión de activos digitales, que en el 2017 no seguía ninguna regulación. La emisión de estos activos se lleva a cabo a través de redes descentralizadas, como Bitcoin o Ethereum, en donde cualquier individuo con capacidad técnica puede emitir un activo digital, mientras que los inversionistas participantes pueden liquidar estos activos en mercados secundarios. El objetivo de esta investigación es encontrar un modelo de evaluación para estos sistemas de criptodivisas y transmitir el panorama económico y social que las rodea. En esta investigación se propone una metodología para evaluar un sistema de criptodivisas basado en la cadena de bloques, en forma de una herramienta de software original distribuida con una licencia de código abierto, de tal forma que la propia metodología propuesta, llamada RI5C, es el resultado principal de esta investigación. -->

# Statement of need

`RI5C` is an interactive blockchain explorer packaged as a web-application that allows users to visualise a network model of a subset of transactions on the Ethereum Blockchain, which is filtered by smart-contract addresses that represent a cryptocurrency. It is written in Python which allows for data collection, analysis and treatment as well as an easy web serving application. The first layer of interaction was designed to be used via www.ri5c.com [@ri5c] but its components are modular enough that users can clone the code and customise queries, graphs and networks. `RI5C` relies heavily on Google's Big Query Ethereum daily clones.

`RI5C` was designed to be used by developers, students, authorities and investors to further understand the behaviour of cryptocurrencies. It was the result of a PhD Thesis [@ri5c_phd:2020]. The visualisation capacities, ease and speed of use to non-technical users has aided in the understanding of these complex systems by a great number of people. `RI5C` has already processed queries for thousands of users through its web-application [@ri5c].

<!-- 
# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }
 -->
# Acknowledgements

We acknowledge contributions from Dr. Pablo Suárez Serrato for his help in the understanding of network analysis and the University of Basque Country for its help and accomodation during the research that led to the creation of RI5C.

<!-- # References -->

