# Greengraph - Python Package

This package analyses how much green space there is between two locations. It outputs a distribution of green pixels found on the Google maps of the discretized distance.

### Dependencies

Greengraph uses some open source Python libraries to perform properly:
* matplotlib
* geopy
* numpy
* argparse

### Installation

The package can be installed using pip directly from GitHub:

```sh
$ pip install git+https://github.com/xmariuca/MPHYG001-coursework1.git
```

Alternately, the package can be first cloned and installed using:

```sh
$ python setup.py install
```

### Usage

The package can be used:

* as a library by calling the function `plotGreenDistribution(startPos, endPos, steps, outFile)` from  `greengraph.getGraph`

```python
# example usage of the function
plotGreenDistribution('London', 'Cambridge', 10, 'outGraph.png')
```
* from the command line 

```sh
$ getGreenGraph --from London --to Cambridge --steps 10 --out outGraph.png
```

### Output

The package outputs a graph with the distribution of green pixels between the two locations.

Example image:

![Example Greengraph output]
(https://github.com/xmariuca/MPHYG001-coursework1.git)
(https://octodex.github.com/images/yaktocat.png)

### Documentation

The documentation was created using Sphinx. For more information about the code, please see the generated html files.

### Version
0.1

### License
MIT

## MPHYG001-coursework1

This package was created as part of the first coursework of the module MPHYG001 - Research Software Engineering with Python.

Author: Maria Ruxandra Robu,
MRes Medical Imaging, University College London 2015-2016

