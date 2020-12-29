---
title: 'RI5C: Methodolgy for the Evaluation of Cryptocurrency Systems'
tags:
  - Cryptocurrency
  - Network
  - Python
  - Ethereum

authors:
  - name: Everardo J. Barojas-Méndez
    orcid: 0000-0003-4182-1537
    affiliation: 2
  - name: Fernando Ramírez Alatriste
    orcid: 0000-0001-7991-7951
    affiliation: 4
  - name: María Saiz Santos
    affiliation: 3
  - name: Abdolreza Rashnavady Nodjoumi
    affiliation: 2
affiliations:
 - name: Universidad Nacional Autónoma de México
   index: 2
 - name: Universidad de País Vasco
   index: 3
 - name: Universidad Autónoma de la Ciudad de México
   index: 4
date: 28 December 2020
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary
Close to twelve years after the genesis of Bitcoin, the first decentralised digital asset enabled by cryptography ^[i.e., Cryptocurrency] a whole new category of financial assets has emerged. One of the key differentiators of this newfound ecosystem is the introduction of a new issuance method for digital assets that takes place on decentralised networks like Bitcoin or Ethereum, where any individual with technical knowhow can create a new digital asset and sell it to investors, that can buy or liquidate these assets in secondary markets. Understanding these new digital assets, whose data is usually publically accessible as plain-text, requires data analysis and visualisation tools.

<!-- ABSTRACT 

Poco más de 10 años después de la génesis de Bitcoin, el primer activo digital habilitado por criptografía,\footnote{ También llamado criptodivisa} hemos visto una nueva categoría de activos financieros emerger. Con ello, una gran cantidad de criptodivisas han generado un mercado secundario altamente líquido. El valor de este mercado de activos basados en criptodivisas ha crecido enormemente, en su máximo histórico hasta \$829 millones de millones de dólares \cite{coinmarketcap}, equivalente al producto interno bruto de México en el 2005 \cite{GDPMEX}. Durante el 2017 se vivió una burbuja financiera dentro de este ecosistema emergente, en la cual estos activos se valorizaron con tasas de crecimiento exponenciales y que hicieron eco a las valoraciones de acciones de empresas tecnológicas en la burbuja \emph{\hyperref[s:dotcom]{PuntoCom}}. Uno de los factores significativos que contribuyeron a esta burbuja, fue la introducción de un nuevo método de emisión de activos digitales, que en el 2017 no seguía ninguna regulación. La emisión de estos activos se lleva a cabo a través de redes descentralizadas, como Bitcoin o Ethereum, en donde cualquier individuo con capacidad técnica puede emitir un activo digital, mientras que los inversionistas participantes pueden liquidar estos activos en mercados secundarios. El objetivo de esta investigación es encontrar un modelo de evaluación para estos sistemas de criptodivisas y transmitir el panorama económico y social que las rodea. En esta investigación se propone una metodología para evaluar un sistema de criptodivisas basado en la cadena de bloques, en forma de una herramienta de software original distribuida con una licencia de código abierto, de tal forma que la propia metodología propuesta, llamada RI5C, es el resultado principal de esta investigación. -->

# Statement of need

`RI5C` is an interactive blockchain explorer web app that allows users to input a smart contract and visualise the network of internal transactions. It is written in Python which allows for web-serving application, data-analysis and treatment. It was designed to be used via a www.ri5c.com but it's components are modular enough that users can download the code and customise queries, graphs and networks. `RI5C` relies heavily on Google's Big Query Ethereum daily clones.

`RI5C` was designed to be used by developers, students, authorities and investors to further understand the behaviour of cryptocurrencies. It was the result of a PhD Thesis [cite PhD]. The visualisation capacities, ease and speed of use to non-technical users has aided in the understanding of these complex systems by a great number of people. `RI5C` has already processed thousands of network models through its web app www.ri5c.com.

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

