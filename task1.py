import networkx as nx


def build_graph():
    G = nx.DiGraph()

    # Додавання ребер з пропускними здатностями
    edges = [
        ("Термінал 1", "Склад 1", 25),
        ("Термінал 1", "Склад 2", 20),
        ("Термінал 1", "Склад 3", 15),
        ("Термінал 2", "Склад 3", 15),
        ("Термінал 2", "Склад 4", 30),
        ("Термінал 2", "Склад 2", 10),
        ("Склад 1", "Магазин 1", 15),
        ("Склад 1", "Магазин 2", 10),
        ("Склад 1", "Магазин 3", 20),
        ("Склад 2", "Магазин 4", 15),
        ("Склад 2", "Магазин 5", 10),
        ("Склад 2", "Магазин 6", 25),
        ("Склад 3", "Магазин 7", 20),
        ("Склад 3", "Магазин 8", 15),
        ("Склад 3", "Магазин 9", 10),
        ("Склад 4", "Магазин 10", 20),
        ("Склад 4", "Магазин 11", 10),
        ("Склад 4", "Магазин 12", 15),
        ("Склад 4", "Магазин 13", 5),
        ("Склад 4", "Магазин 14", 10),
    ]

    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)

    return G


def compute_max_flow(G, source, target):
    # Використання алгоритму Едмондса-Карпа
    flow_value, flow_dict = nx.maximum_flow(G, source, target)
    return flow_value, flow_dict


def main():
    G = build_graph()

    # Додаємо джерело та стоки
    G.add_node("Джерело")
    G.add_node("Сток")

    # З'єднуємо джерело з терміналами
    G.add_edge(
        "Джерело", "Термінал 1", capacity=50
    )  # Залежить від загальної доступності
    G.add_edge("Джерело", "Термінал 2", capacity=50)

    # З'єднуємо магазини зі стоком
    for i in range(1, 15):
        G.add_edge(f"Магазин {i}", "Сток", capacity=float("inf"))

    # Розрахунок максимального потоку
    flow_value, flow_dict = compute_max_flow(G, "Джерело", "Сток")

    print(f"Максимальний потік: {flow_value}")
    print("Розподіл потоків:")
    for node, flows in flow_dict.items():
        for target, flow in flows.items():
            if flow > 0:
                print(f"{node} -> {target}: {flow}")


if __name__ == "__main__":
    main()
