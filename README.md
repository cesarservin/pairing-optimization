# pairing-optimization

# Quickstart guide
### ⚠️ Follow the next instructions inside your project folder ⚠️


### To install the package `po` in your local environment:

**You must have Python 3.10 or later**. Ideally, you use Python 3.11.
1. If Hatch is not already **installed**, install it: `pip install hatch`

2.  **Clone** `pairing-optimization`
3. Type **insde your project folder terminal**:
    > `hatch shell` (in your laptop)

    **That's it! You can now use your package in your local environment.**

4.  To **run** the project use `notebooks\*-main.ipynb`


## (Optional) Configure VS Code and Jupyter to recognize your Python package

After a successful installation with hatch, type:
> `conda deactivate` (if you are using conda)
>
>`hatch shell`
>
> `hatch run python -m ipykernel install --user --name po`


## (Optional) Configure PyCharm to recognize your Python package

Alternatively, you can use the following command to find the location of your hatch environment:

- `hatch shell`
- `hatch run python -c "import sys;print(sys.executable)"`

The first command activates the environment, the second command tells you the location of the environment.


# Code documentation

Your environment comes with `mkdocs` configured for you. To generate the documentation you can run the following command:

`hatch run docs:build`

This will create a `site` folder in the root directory of the project

Alternatively, you can run the following command to see the documentation in your browser:

`hatch run docs:serve`
or
`mkdocs serve`


## How is the documentation generated?

The code documentation is generated using Google style docstrings. You can find more information 
about it [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

You can even configure your IDE to follow Google style docstrings.

After writing your docstrings, you need to reference them using the `:::` directive. An example is already provided
to you in the `docs` folder.

It is also possible to add or remove sections from the documentation. You can do that by modifying 
the `mkdocs.yml` file.

## FAQ (Docs)
<details>
  <summary><i>How does the docs generation work?</i></summary>
When you run `hatch run docs:build`, it will run the following command:

- `mkdocs build`

</details>

<details>
    <summary>How can I add or remove a section in the left navigation bar?</summary>
These sections are defined in the `mkdocs.yml` file. You can add or remove sections by modifying this file.
</details>

<details>
    <summary>How can I customize the documentation?</summary>
We recommend that you use our guidelines. However, you can customize the documentation by taking a 
look at the `mkdocs` documentation [here](https://www.mkdocs.org/).
</details>

# Linting and formatting

Your project comes with a suggested configuration for `ruff` which is a linter and formatter that is replacing pylint,
flake8, and black.

To use it you can run the following command:

`hatch fmt`

This will detect linting issues and if possible fix them. If there are issues that cannot be fixed automatically, 
you will get a message with the line number and the issue. 

The formatter runs automatically after the linting process finishes. The configuration resembles `black`.

## FAQ (Linting and formatting)

<details>
  <summary><i>How does the `hatch fmt` work?</i></summary>
When you run `hatch fmt`, it will run the following command:

- `ruff check --fix`
- `ruff format`

</details>
<details>
  <summary><i>How can I configure the linter and formatter?</i></summary>
You can configure the linter and formatter by modifying the `pyproject.toml` file in the `[tool.ruff]` section.
Take a look at the [ruff documentation](https://docs.astral.sh/ruff/) for more information.
</details>
<details>
<summary>Can I use ruff directly?</summary>

**Yes!** You can use ruff directly by running `ruff check` or `ruff format` in your terminal. Make sure 
you are in the hatch shell.

</details>

# Pre-commit hooks

This project comes with pre-commit hooks preconfigured. If you want to enable them,
type:

`pre-commit install`

This will install the pre-commit hooks in your project and **at every commit the hooks will run**. 

You can also run the pre-commit hooks manually by typing:

`pre-commit run --all-files`

The pre-commit hooks will run the following checks:

- check-yaml
- end-of-file-fixer
- trailing-whitespace
- ruff
- pretty-format-yaml
- pretty-format-toml
- bandit

## FAQ (Pre-commit hooks)

<details>
  <summary><i>How can I skip the pre-commit hooks?</i></summary>
You can skip the pre-commit hooks by adding the `--no-verify` flag to your git commit command. For example:
`git commit -m "My commit message" --no-verify`
</details>

# FAQ

What if I want to add a new Python package?

> Install it as always via `pip` in your hatch environment (`hatch shell`). 
> Don't forget to add it to the `pyproject.toml` file in the `dependencies` section.
> Alternatively, you can exit your environment (`exit`) and add it to the `pyproject.toml`, the 
> next time you restart your hatch environment it will be installed.

# Contribute
To contribute create a PR a use conventional commits https://www.conventionalcommits.org/en/v1.0.0/#summary