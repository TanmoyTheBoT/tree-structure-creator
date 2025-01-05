import os

def create_structure_from_tree(tree_file, output_path):
    """
    Creates a directory and file structure based on a tree.txt file.

    Args:
        tree_file (str): Path to the tree.txt file.
        output_path (str): Root directory where the structure will be created.
    """
    with open(tree_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    root = None
    stack = []

    for line_no, line in enumerate(lines, start=1):
        # Determine the depth of the current line based on leading characters
        stripped_line = line.lstrip('│├└─ ')  # Strip tree characters and spaces
        depth = (len(line) - len(stripped_line)) // 4  # Each indent is 4 spaces
        name = stripped_line.strip()

        if not name:
            print(f"Skipping empty line at {line_no}")
            continue  # Skip empty lines

        # Debug: Print line details
        print(f"[Line {line_no}] Depth: {depth}, Name: {name}")

        # If root is not set, this is the root folder
        if root is None:
            root = os.path.join(output_path, name)
            os.makedirs(root, exist_ok=True)
            stack = [root]  # Initialize stack with root path
        else:
            # Ensure stack has enough entries to handle current depth
            while len(stack) <= depth:
                stack.append(stack[-1])  # Duplicate the last valid directory

            # Handle subfolders and files
            current_path = os.path.join(stack[depth], name)

            if "." in name:  # Files have extensions
                os.makedirs(os.path.dirname(current_path), exist_ok=True)  # Ensure parent folder exists
                with open(current_path, "w", encoding="utf-8") as f:
                    pass  # Create an empty file
            else:
                # It's a folder
                os.makedirs(current_path, exist_ok=True)

            # Update the stack for the current depth
            stack = stack[:depth + 1]
            stack.append(current_path)

    print(f"Structure successfully created at: {output_path}")


# Example usage
tree_file_path = "tree.txt"  # Path to your tree.txt file
output_base_path = "output_structure"  # Base directory for the tree

create_structure_from_tree(tree_file_path, output_base_path)
