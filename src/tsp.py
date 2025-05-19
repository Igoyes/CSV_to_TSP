import argparse
import sys
from typing import List, Tuple, Dict
import numpy as np


class TSPGraph:
    def __init__(self):
        self.nodes: List[int] = []
        self.edges: List[Tuple[int, int, int]] = []
        self.node_index: Dict[int, int] = {}

    def load_from_csv(self, file_path: str) -> None:
        with open(file_path, "r") as f:
            next(f)  # Skip header
            for line in f:
                parts = line.strip().split(",")
                if len(parts) < 3:
                    continue
                u, v, w = int(parts[0]), int(parts[1]), int(parts[2])
                self.edges.append((u, v, w))
                if u not in self.nodes:
                    self.nodes.append(u)
                if v not in self.nodes:
                    self.nodes.append(v)
        self.nodes.sort()
        self.node_index = {node: idx for idx, node in enumerate(self.nodes)}

    def to_full_matrix(self, fill_value: int = None) -> np.ndarray:
        n = len(self.nodes)
        if fill_value is None:
            fill_value = max(w for _, _, w in self.edges) * 7000 if self.edges else 1
        mat = np.full((n, n), fill_value, dtype=int)
        for u, v, w in self.edges:
            i, j = self.node_index[u], self.node_index[v]
            mat[i, j] = w
            mat[j, i] = w
        np.fill_diagonal(mat, 0)
        return mat

    def to_edge_list(self) -> List[Tuple[int, int, int]]:
        return self.edges

    def __len__(self):
        return len(self.nodes)


class TSPWriter:
    def __init__(self, graph: TSPGraph, comment: str, experimental: bool):
        self.graph = graph
        self.comment = comment
        self.experimental = experimental

    def write(self, file_path: str) -> None:
        with open(file_path, "w") as f:
            print(f"NAME: {file_path}", file=f)
            print(f"COMMENT: //{self.comment}", file=f)
            print("TYPE: TSP", file=f)
            print(f"DIMENSION: {len(self.graph)}", file=f)
            print("EDGE_WEIGHT_TYPE: EXPLICIT", file=f)
            if self.experimental:
                print("EDGE_DATA_FORMAT: EDGE_LIST", file=f)
                for u, v, w in self.graph.to_edge_list():
                    print(f"{u} {v} {w}", file=f)
            else:
                print("EDGE_WEIGHT_FORMAT: FULL_MATRIX", file=f)
                print("EDGE_WEIGHT_SECTION:", file=f)
                mat = self.graph.to_full_matrix()
                for row in mat:
                    print(" ".join(map(str, row)), file=f)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert CSV to TSP format."
    )
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("output_file", help="Output TSP file")
    parser.add_argument("comment", help="Comment for the TSP file")
    parser.add_argument("experimental", choices=["Y", "N"], help="Experimental flag (Y/N)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input_file.endswith(".csv"):
        print("Input file must be a .csv file", file=sys.stderr)
        return 3

    graph = TSPGraph()
    try:
        graph.load_from_csv(args.input_file)
    except FileNotFoundError:
        print("File not found", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        return 1

    writer = TSPWriter(graph, args.comment, args.experimental == "Y")
    try:
        writer.write(args.output_file)
    except Exception as e:
        print(f"Can't create output file: {e}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())