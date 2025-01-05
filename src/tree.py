import os

def create_structure_from_tree(tree_file, output_path):
    """
    Creates a directory and file structure based on a tree-like structure described in a file.

    Args:
        tree_file (str): Path to the input file containing the tree structure.
        output_path (str): Directory where the structure will be created.

    Raises:
        FileNotFoundError: If the input tree file does not exist.
        ValueError: If the input tree file is empty or improperly formatted.
    """
    if not os.path.exists(tree_file):
        raise FileNotFoundError(f"Input tree file '{tree_file}' not found.")

    with open(tree_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        raise ValueError(f"Input tree file '{tree_file}' is empty.")

    root = None
    stack = []

    for line_no, line in enumerate(lines, start=1):
        stripped_line = line.lstrip('│├└─ ')  # Remove tree characters and spaces
        depth = (len(line) - len(stripped_line)) // 4  # Each indent is 4 spaces
        name = stripped_line.strip()

        if not name:
            print(f"Skipping empty or invalid line at {line_no}")
            continue

        if root is None:
            root = os.path.join(output_path, name)
            os.makedirs(root, exist_ok=True)
            stack = [root]
        else:
            while len(stack) <= depth:
                stack.append(stack[-1])

            current_path = os.path.join(stack[depth], name)

            if "." in name:
                os.makedirs(os.path.dirname(current_path), exist_ok=True)
                with open(current_path, "w", encoding="utf-8") as f:
                    pass
            else:
                os.makedirs(current_path, exist_ok=True)

            stack = stack[:depth + 1]
            stack.append(current_path)

    print(f"Structure successfully created at: {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Create a folder and file structure from a tree-like input file."
    )
    parser.add_argument("-t", "--tree", required=True, help="Path to the tree file.")
    parser.add_argument(
        "-o",
        "--output",
        default="output_structure",
        help="Directory where the structure will be created (default: 'output_structure').",
    )

    args = parser.parse_args()

    try:
        create_structure_from_tree(args.tree, args.output)
    except Exception as e:
        print(f"Error: {e}")
