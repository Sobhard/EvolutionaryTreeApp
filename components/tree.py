"""
Contains methods that handle formatting data and plotting the evolutionary tree
"""

import numpy as np
import streamlit as st
from models.traits import Region


def get_graph(animal_node_size: int, node_size: int):
    """Main method for this file. It returns the edges of the evolutionary graph formatted
    for apache echarts"""

    distances = create_distance_matrix()
    names = [a.name for a in st.session_state.animals]
    links = neighbor_joining(distances, names)

    node_names = set()
    for edge in links:
        node_names.add(edge["source"])
        node_names.add(edge["target"])

    data = []

    for name in node_names:
        if name[:5] == "Node_":
            data.append(
                {"name": name, "label": {"show": False}, "symbolSize": node_size}
            )

        else:
            data.append({"name": name, "symbolSize": animal_node_size})

    return {"data": data, "links": links}


def calculate_distance(first: dict, second: dict) -> int:
    """Calculates the hamming distance between two animals"""

    dist = 0
    for key in first:

        if key == "region":
            if (
                Region(first["region"]).ancient_continent
                != Region(second["region"]).ancient_continent
            ):
                dist += 1

        elif key in ("wings", "legs", "tentacles", "arms"):
            dist += abs(first[key] - second[key])
            pass

        elif first[key] != second[key]:
            dist += 1

    return dist


def create_distance_matrix() -> np.ndarray:
    """Returns a customized distance matrix that represents the distance between each animal"""

    animal_traits: list[dict] = [a.to_dict() for a in st.session_state.animals]

    for traits in animal_traits:
        traits.pop("name")
        traits.pop("user_generated")

    dist_matrix: np.ndarray = np.zeros(shape=(len(animal_traits), len(animal_traits)))

    for i, first_animal in enumerate(animal_traits):
        for j, second_animal in enumerate(animal_traits):
            dist_matrix[i][j] = calculate_distance(first_animal, second_animal)

    return dist_matrix


import numpy as np


def neighbor_joining(dist_matrix: np.ndarray, names: list[str]) -> list[dict]:
    """
    Implements the neighbor joining algorithm using vectorized NumPy operations.
    Returns a list of dictionaries formatted for Apache ECharts graph edges.
    """
    matrix = dist_matrix.copy().astype(float)
    active_nodes = names.copy()
    echarts_edges = []

    internal_node_id = 1

    while len(active_nodes) > 2:
        n = len(active_nodes)

        # 1. Vectorized Q-matrix calculation (Much faster than nested loops)
        r_sums = np.sum(matrix, axis=1)
        q_matrix = (n - 2) * matrix - r_sums.reshape(-1, 1) - r_sums.reshape(1, -1)
        np.fill_diagonal(q_matrix, np.inf)

        # 2. Identify indices of the absolute closest neighbors
        i, j = np.unravel_index(np.argmin(q_matrix), q_matrix.shape)

        node_i = active_nodes[i]
        node_j = active_nodes[j]
        new_ancestor_name = f"Node_{internal_node_id}"
        internal_node_id += 1

        # 3. Calculate separate branch lengths
        dist_i_to_ancestor = (matrix[i, j] / 2.0) + (
            (r_sums[i] - r_sums[j]) / (2.0 * (n - 2))
        )
        dist_j_to_ancestor = matrix[i, j] - dist_i_to_ancestor

        dist_i_to_ancestor = max(0.0, dist_i_to_ancestor)
        dist_j_to_ancestor = max(0.0, dist_j_to_ancestor)

        # 4. Append straight to ECharts links list
        echarts_edges.append(
            {
                "source": new_ancestor_name,
                "target": node_i,
                "value": round(dist_i_to_ancestor, 4),
            }
        )
        echarts_edges.append(
            {
                "source": new_ancestor_name,
                "target": node_j,
                "value": round(dist_j_to_ancestor, 4),
            }
        )

        # 5. Vectorized distance calculation from the new node to all remaining nodes
        new_node_distances = (matrix[i, :] + matrix[j, :] - matrix[i, j]) / 2.0

        # Remove i and j from our new 1D array so dimensions match after shrinking the main matrix
        new_node_distances = np.delete(new_node_distances, sorted([i, j], reverse=True))

        # 6. Shrink distance matrix
        for target_idx in sorted([i, j], reverse=True):
            matrix = np.delete(matrix, target_idx, axis=0)
            matrix = np.delete(matrix, target_idx, axis=1)
            active_nodes.pop(target_idx)

        # 7. Append the updated ancestral node array parameters
        new_col = new_node_distances.reshape(-1, 1)
        matrix = np.hstack((matrix, new_col))

        new_row = np.append(new_node_distances, 0.0).reshape(1, -1)
        matrix = np.vstack((matrix, new_row))

        active_nodes.append(new_ancestor_name)

    # --- FIX APPLIED HERE ---
    # Extract the scalar distance from the final 2x2 matrix
    final_weight = matrix[0][1]

    echarts_edges.append(
        {
            "source": active_nodes[0],  # Extract the actual string names
            "target": active_nodes[1],
            "value": round(max(0.0, float(final_weight)), 4),
        }
    )

    return echarts_edges


# def plot(graphing_schema: list[dict]):
