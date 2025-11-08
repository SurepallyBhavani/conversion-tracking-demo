# ----------------------------------------
# Web Analytics – Hyperlink Data (Auto Extracted)
# ----------------------------------------
import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urljoin, urlparse

# Step 1: Choose a demo website to crawl (small and safe site)
base_url = "https://reqres.in/"   # you can replace with any safe website

print(f"Fetching hyperlinks from: {base_url}")

# Step 2: Fetch the webpage and parse all hyperlinks
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all href links on the page
links = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    full_url = urljoin(base_url, href)  # convert relative → absolute URL
    if full_url.startswith(base_url):   # keep only internal links
        links.append(full_url)

print(f"\nFound {len(links)} hyperlinks on the page:")
for link in links:
    print(" -", link)

# Step 3: Build the hyperlink graph
G = nx.DiGraph()
source_page = base_url.rstrip('/')
for target in links:
    G.add_edge(source_page, target)

# Step 4: Compute hyperlink metrics
print("\n=== Hyperlink Data Analysis ===")
print("Total Pages (Nodes):", G.number_of_nodes())
print("Total Hyperlinks (Edges):", G.number_of_edges())

in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())

print("\nIn-Degree (incoming links):", in_degrees)
print("Out-Degree (outgoing links):", out_degrees)

# Step 5: PageRank (importance)
pagerank = nx.pagerank(G)
print("\nPage Importance (PageRank):")
for page, score in pagerank.items():
    print(f"{page} : {round(score, 3)}")

# Step 6: Visualize hyperlink structure
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2300, arrows=True, arrowsize=20)
plt.title("Web Analytics – Hyperlink Structure (Auto Extracted)")
plt.show()
