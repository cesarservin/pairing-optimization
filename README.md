# pairing-optimization

## Description
What `problem` does it `solve`?

This project is a `solution` to the business problem of reducing `excess` products or creating new products from `pairing up existing ones`. It uses a sample data source that resembles a dataset in the business. 


![Pairs](docs/img/suggestion.jpg)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

[![View Project](https://img.shields.io/badge/Material-View_Project-purple?logo=MaterialforMKDOCS)](https://cesarservin.com/pairing-optimization/index.html)
[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-blue?logo=Jupyter)](https://github.com/cesarservin/pairing-optimization/blob/main/notebooks/main.ipynb)
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/cesarservin/pairing-optimization)



## Table of contents

- [pairing-optimization](#pairing-optimization)
  - [Description](#description)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data](#data)
  - [Model](#model)
  - [Results](#results)
  - [Examples](#examples)
  - [Documentation](#documentation)
  - [Contributing](#contributing)
  - [License](#license)
  - [Roadmap](#roadmap)
  - [Enhancements](#enhancements)
  - [Acknowledgments](#acknowledgments)
  - [Changelog](#changelog)


## Installation

⚠️ Follow the next instructions inside your project folder

1. **Prerequisites**:
   - To install the project `pairing-optimization` in your local environment
**you must have Python 3.10 or later**. Ideally, you use Python 3.11.
1. **Setup**:
   - If Hatch is not already **installed**, install it: `pip install hatch`
   - To activate your environment with `pairing-optimization` type **inside your project folder**:
`hatch shell` 

**That's it! You can now use your package in your local environment.**

## Usage
- **Basic Usage**: Use `main.ipynb`
- **Configuration**: Modify pyproject.toml to add or remove packages.

## Data
- **Sources**: The dataset is synthetic generated.
- **Structure**: Table of key parameters.

| constraints | component | resource |
|-------------|-----------|----------|
| Brand 1     | PANT      | 3        |

    constraints: product or item features
    component: components that makes up the pair
    resource: numeric / quantities of the products

## Model

- **Algorithms**: Methods used.
    - Linear Algebra and reshaping of datasets.

## Results

 - **Findings:**
   - This interactable tool in D3 returns total number of combinations of products and maximum number of continous combinations. This will not return estimation but actual combinations based on parameters.

- **Visualizations**:
  - Example visualization

![Pairs](/docs/img/pairing_optimization_tool.jpg)

## Examples

```python
from po.data.readingdata import file_path_finder
from po.features.pairing_optimization import po
from po.features.pairing_optimization import max_streak
```


## Documentation

[Documentation](https://cesarservin.com/pairing-optimization/index.html)


## Contributing

To contribute create a PR a use conventional [commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)

```
fix: <description>
feat: <description>
docs: <description>
refactor: <description>
```
## License
[License](./LICENSE) information.

## Roadmap

- Generate pairs using clustering algorithms.

## Enhancements
OuOther potential future work that can be done to extend the project is create interactive Power BI dashboard.

## Acknowledgments

Inspired by experience.

## Changelog
- v1.0: Initial release
- v1.1: Added visualization/tool and improved model performance.
