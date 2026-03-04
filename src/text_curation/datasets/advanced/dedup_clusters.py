from collections import defaultdict, Counter
from datasets import Dataset


def analyze_duplicate_clusters(
    dataset: Dataset,
    *,
    column: str = "text",
):
    """
    Analyze duplicate clusters within a dataset.

    This tool identifies groups of identical documents
    and produces statistics describing duplicate density
    and cluster size distribution.

    This function does NOT modify the dataset.
    """

    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")

    texts = dataset[column]

    if not all(isinstance(t, str) for t in texts):
        raise TypeError("Dataset column must contain strings")

    groups = defaultdict(list)

    for idx, text in enumerate(texts):
        groups[text].append(idx)

    cluster_sizes = []
    duplicate_clusters = 0

    for indices in groups.values():

        size = len(indices)

        if size > 1:
            duplicate_clusters += 1

        cluster_sizes.append(size)

    cluster_size_distribution = Counter(cluster_sizes)

    total_documents = len(texts)
    duplicated_documents = sum(
        size for size in cluster_sizes if size > 1
    )

    duplicate_density = (
        duplicated_documents / total_documents
        if total_documents
        else 0.0
    )

    return {
        "documents": total_documents,
        "duplicate_clusters": duplicate_clusters,
        "duplicate_density": round(duplicate_density, 6),
        "cluster_size_distribution": dict(cluster_size_distribution),
    }
