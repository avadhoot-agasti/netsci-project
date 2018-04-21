## `pydgraph` - Python Dependencies Graph
A directed graph for all python dependencies present in local system

### Motivation

Its very interesting problem to solve and find out how various python packages are dependent on each other and does it make sense to bundle some of the very common packages used along with base python distribution. It is interesting to understand the dependency strucutre but also to understand the community structure of these modules and what kind of network they form. Any other phenomenon exist when we analyze this graph. This analysis can be used to optimize the imports, remove cyclic dependencies between modules. Similar approach can be extended to other programming languages like `java`, `ruby`, `perl` etc.

### Pre-requisites
You can install pre-requisite python modules to run this application by installing modules listed in `requirements.txt`

```bash
# activate your virtualenv, if you have one.
pip install -r requirement.txt
```

### Running the project
```bash
./run.sh
```
#### Raw output graph
![Alt text](./pydgraph/raw.png?raw=true "Generated graph")

### List of files

```
├── LICENSE
├── README.md
├── requirements.txt               <---- pre-requisites
├── pydgraph
│   ├── README.md
│   ├── __init__.py
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   ├── crawler                    <---- crawler module
│   │   ├── __init__.py
│   │   ├── crawler.py
│   │   ├── graph.py
│   │   └── parser.py              <---- recursively parses the dependency tree to generate the graph(gml) 
│   ├── package_installer          <---- installs anaconda packages, not needed to run this project 
│   │   ├── anaconda_package_list_macos.csv
│   │   └── install_packages.py
│   ├── resources                   <----- generated dependecy tree
│   │   ├── data.txt
│   │   ├── pydgraph.gml            <----- generated graph from dependency tree
│   │   └── requirements.txt
│   └── run.sh                      <---- main executable
├── pydgraph_analysis
│   ├── G-Betweenness-Modularity.png
│   ├── GNew-InDegree.png
│   ├── GNew-OutDegree.png
│   └── graph_analysis.ipynb
└── report
    ├── ACM-Reference-Format.bst
    ├── Makefile
    ├── README.md
    ├── compile.py
    ├── introduction.tex
    ├── main.bib
    ├── main.pdf
    ├── main.tex
    ├── references.bib
    ├── relatedwork.tex
    ├── requirements.tex
    └── technicalsolution.tex
```

#### Crawler
Pydgraph uses `pipdeptree` to generate dependency tree from current virtual environment.
The generated dependency graph is stored in `pydgraph/resources` folder. If you delete
 this folder or contents of this folder, crawler module will regenerate the dependency tree from the python modules installed in current virtual environment. Along with the dependency tree the `parser` generates the `pydgraph.gml` which contains the actual directed graph built from the dependency tree built from previous step. Further, this `pydgraph.gml` can be used to analyze the various graph models and community structure, friendship paradox etc. Current crawler has a limitation of not able to crawl all packages available on [pypi](https://pypi.org/). Further, version can be enhanced to crawl all packages available on [pypi](https://pypi.org/) without manually installing them locally.

### Project location
https://github.com/avadhoot-agasti/netsci-project 

## Authors

* **Abhishek Gupta**  - abhigupt@iu.edu 
* **Avadhoot Agasti** - aagasti@iu.edu 
