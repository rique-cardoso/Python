def are_orthogonal(v1, v2):
    """Check if two vectors are orthogonal.

    Args:
        v1 (list of float): First vector.
        v2 (list of float): Second vector."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length.")
    
    dot_product = sum(a * b for a, b in zip(v1, v2))
    return dot_product == 0