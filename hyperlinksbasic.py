# ----------------------------------------
# Web Analytics – Hyperlink Data
# ----------------------------------------
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the hyperlink structure (edges represent hyperlinks)
# Each tuple (A, B) means "Page A contains a hyperlink to Page B"
hyperlinks = [
    ('Home', 'About'),
    ('Home', 'Products'),
    ('Products', 'Product1'),
    ('Products', 'Product2'),
    ('Product1', 'Cart'),
    ('Product2', 'Cart'),
    ('Cart', 'Checkout'),
    ('Checkout', 'Home'),   # returning link
    ('About', 'Home')
]

# Step 2: Create a directed graph
G = nx.DiGraph()
G.add_edges_from(hyperlinks)

# Step 3: Compute basic hyperlink metrics
print("=== Web Structure (Hyperlink) Analysis ===")
print("Total Pages (Nodes):", G.number_of_nodes())
print("Total Hyperlinks (Edges):", G.number_of_edges())

# In-degree: how many links point *to* a page (popularity)
# Out-degree: how many links a page *has* (connectivity)
in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())

print("\nPage In-Degree (incoming links):")
for page, deg in in_degrees.items():
    print(f"{page}: {deg}")

print("\nPage Out-Degree (outgoing links):")
for page, deg in out_degrees.items():
    print(f"{page}: {deg}")

# Step 4: Visualize the hyperlink structure
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos,
        with_labels=True,
        node_color='lightgreen',
        node_size=2500,
        arrows=True,
        arrowsize=20,
        font_size=10)
plt.title("Web Analytics – Hyperlink Structure Graph")
plt.show()

# Step 5: Optional – Identify important pages (PageRank)
pagerank = nx.pagerank(G)
print("\nPage Importance (PageRank Values):")
for page, score in pagerank.items():
    print(f"{page}: {round(score, 3)}")
