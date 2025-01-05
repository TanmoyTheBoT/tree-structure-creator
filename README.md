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
structure/
├── _layouts/
│   ├── default.html
│   ├── home.html
│   ├── post.html
├── _includes/
│   ├── header.html
│   ├── footer.html
│   ├── nav.html
├── _sass/
│   ├── _variables.scss
│   ├── _mixins.scss
├── assets/
│   ├── css/
│   │   ├── style.scss
│   ├── js/
│   │   ├── theme.js
├── _posts/
│   ├── 2024-01-01-example.md
├── _config.yml
├── index.html
├── LICENSE.txt
├── README.md


```