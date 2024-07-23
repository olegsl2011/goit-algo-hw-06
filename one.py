import networkx as nx
import matplotlib.pyplot as plt


graph = {
    "Маршрут 22": {"Маршрут 11": {"weight": 5}},
    "Маршрут 11": {"Маршрут 33": {"weight": 4}, "Маршрут 44": {"weight": 3}, "Маршрут 2": {"weight": 3}},
    "Маршрут 33": {"Маршрут 44": {"weight": 3}, "Маршрут 2": {"weight": 3}},
    "Маршрут 44": {"Маршрут 6": {"weight": 2}, "Маршрут 87": {"weight": 1}},
    "Маршрут 2": {"Маршрут 37": {"weight": 3}},
    "Маршрут 6": {"Маршрут 87": {"weight": 1}},
    "Маршрут 87": {"Маршрут 37": {"weight": 3}},
}


G = nx.Graph(graph)


pos = nx.spring_layout(G)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [{node: deg} for node, deg in G.degree()]


if __name__ == "__main__":
    print(f"Кількість вершин: {num_nodes} дорівнює кількості родичів")
    print(f"Кількість ребер: {num_edges} дорівнює кількості зв'язків між родичами")
    print(f"Ступені вершин {degrees} дорівнює кількості зв'язків кожного з родичів")

    plt.show()
