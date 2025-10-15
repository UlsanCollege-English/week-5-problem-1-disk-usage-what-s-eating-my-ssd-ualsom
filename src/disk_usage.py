def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    if node is None:
        return 0
    node_type = node.get("type")
    if node_type == "file":
        return node.get("size", 0)
    elif node_type == "dir":
        return sum(total_size(child) for child in node.get("children", []))
    else:
        return 0
