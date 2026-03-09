## Python
Install packages
- `pip install <package>` — Installs package from PyPI
- `python <script.py>` — Runs a Python script using the current Python environment

## Conda
Packages 
- `conda install <package>` — Installs a package into the active environment
- `conda remove <package>` — Removes a package from the active environment
- `conda update <package>` — Updates a package in the active environment

Environments
- `conda env list` — Lists all available Conda environments
- `conda activate <env-name>` — Activates a Conda environment
- `conda deactivate` — Deactivates the current environment
- `conda create -n <env-name>` — Creates a new Conda environment
- `conda env remove -n <env-name>` — Deletes an environment
- `conda create --name <new-env> --clone <existing-env>` — Clones an existing environment

YAML Environments
- `conda env create -f environment.yml` — Creates an environment from an environment file
- `conda env update -f environment.yml --prune` — Updates an environment using an environment file and removes unused packages

YAML file template
```yaml
name: my-environment
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pip:
      - beautifulsoup4
```