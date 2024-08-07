Algorithm
==============
::: po.features.pairing_optimization.po


### Example of pairing optimization (po)

!!! note
    Group observations based on the determined constraints and compenents that can be created with the resources

| Brand   | ColorName | Gender | Size | Type | On Hand |
|---------|-----------|--------|------|------|---------|
| Brand 9 | color 95  | WOMEN  | XL   | TOP  | 0       |
| Brand 9 | color 95  | WOMEN  | XS   | PANT | 10      |


!!! note
    Shape dataframe to find pairing of components for the given constraints

| Brand   | ColorName | Gender | Size | PANT | TOP |
|---------|-----------|--------|------|------|-----|
| Brand 9 | color 95  | WOMEN  | M    | 14   | 0   |
| Brand 9 | color 95  | WOMEN  | S    | 0    | 0   |


!!! note
    determine if pair is possible

| Brand   | ColorName | Gender | Size | PANT | TOP | pairfilter |
|---------|-----------|--------|------|------|-----|------------|
| Brand 9 | color 95  | WOMEN  | M    | 14   | 0   | 0          |
| Brand 9 | color 95  | WOMEN  | S    | 0    | 0   | 0          |


!!! note
    Find successful pairs

| Brand   | ColorName  | Gender | Size | PANT | TOP |
|---------|------------|--------|------|------|-----|
| Brand 9 | color 5953 | WOMEN  | M    | 263  | 160 |
| Brand 9 | color 5953 | WOMEN  | S    | 218  | 106 |


!!! note
    Reshape dataframe back to initial shape where features are each column to find max number of pairs

| Brand   | ColorName  | Gender | Size | Type | On Hand |
|---------|------------|--------|------|------|---------|
| Brand 1 | color 1    | WOMEN  | L    | PANT | 2       |
| Brand 1 | color 1    | WOMEN  | L    | TOP  | 103     |


!!! success
    Maximum amount of possible pairs

| Brand   | ColorName  | Gender | Size | On Hand |
|---------|------------|--------|------|---------|
| Brand 1 | color 1    | WOMEN  | L    | 2       |
| Brand 1 | color 1    | WOMEN  | XL   | 1       |


::: po.features.pairing_optimization.max_streak
