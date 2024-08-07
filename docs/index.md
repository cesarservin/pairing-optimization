Documentation
==============

## Overview

This project is a `solution` to the business problem of reducing `excess` products or creating new products from `pairing up existing ones`. It uses a sample data source that resembles a dataset in the business.

![Pairs](img/suggestion.jpg)


## Algorithms

1.  Pairing optimization (PO) maximizes the number of products that can be generated whithout leaving any oprhan pairs.
2.  Sequential analysis of pairs that can be generated. This answers the concern of generating pairs in different sizes of the spectrum.

## Usage

To use the project, you will need to have a sample data file in the same directory as the project code. The sample data file should be xlsx file with the following columns:

!!! example
    Input data format

| constraints | component | resource |
|-------------|-----------|----------|
| Brand 1     | PANT      | 3        |

    constraints: product or item features
    component: components that makes up the pair
    resource: numeric / quantities of the products


## Result ✅
This will generate a report that shows the number of assortments/kits/bundles/sets that can be generated, as well as the maximum amounts of continous combinations.

Directory Structure
==============

    .
    ├── docs <- markdown files for mkdocs
    │   └── img <- assets
    ├── notebooks <- jupyter notebooks for exploratory analysis and explanation
    └── src - scripts for processing data eg. transformations, dataset merges etc.
    │   ├── data <- loading, saving and modelling your data
    │   └── features <- algorithms and feature engineering
    ├── LICENSE <- License
    ├── mkdocs.yml <- config for mkdocs
    ├── pyproject.yml <- config project
    └── README.md <- README file of the package

**Contributing**

To contribute create a PR a use conventional [commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)

```
fix: <description>
feat: <description>
docs: <description>
refactor: <description>
```

**License**

The project is licensed under the MIT License.

I hope this is helpful! 😄
