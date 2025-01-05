# Tree Structure Creator

A Python script to create folder and file structures from a tree-like input file.

## Features
- Automatically generates directories and files based on a `tree.txt` input.
- Handles inconsistencies and invalid lines gracefully.
- Command-line friendly with clear error messages.

## Requirements
- Python 3.7 or higher.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/tanmoythebot/tree-structure-creator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tree-structure-creator
   ```
3. Run the script:
   ```bash
   python src\tree.py -t <Path to the tree file> -o <output_directory>
   ```

## Example
Input `tree.txt`:
```
my-python-project
├── .github
│   ├── workflows
│   │   └── ci.yml
├── my_python_project
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models
│   │   └── my_model.py
│   ├── services
│   │   └── my_service.py
│   ├── utils
│   │   ├── helper.py
│   │   └── logger.py
│   ├── data
│   │   ├── data_processor.py
│   │   └── datasets
│   │       ├── dataset1.csv
│   │       └── dataset2.csv
│   ├── api
│   │   ├── api_controller.py
│   │   └── api_routes.py
│   └── tests
│       ├── __init__.py
│       ├── test_main.py
│       ├── test_models.py
│       ├── test_services.py
│       └── test_utils.py
├── docs
│   ├── index.rst
│   ├── installation.rst
│   ├── usage.rst
│   └── api_reference.rst
├── scripts
│   ├── data_analysis.py
│   └── run_server.py
├── requirements.txt
├── setup.py
├── LICENSE
├── README.md
├── .gitignore
├── .env
└── pyproject.toml

```