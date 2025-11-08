# ----------------------------------------
# Web Analytics – Web Usage Data & Clickstream Analysis
# ----------------------------------------
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Sample clickstream-like data
data = {
    'user_id': [1, 1, 2, 3, 3],
    'page': ['home', 'product', 'home', 'home', 'checkout'],
    'duration': [10, 30, 20, 15, 25]
}
df = pd.DataFrame(data)

# Step 2: Basic Web Usage Analysis
print("=== Web Usage Analysis ===")
print("Total Users:", df['user_id'].nunique())
print("Total Page Views:", len(df))
print("\nAverage Time Spent on Each Page:")
usage = df.groupby('page')['duration'].mean()
print(usage)

# Step 3: Clickstream Path Analysis (User Navigation Flow)
df = df.sort_values(['user_id']).copy()
df['next_page'] = df.groupby('user_id')['page'].shift(-1)
click_pairs = df.dropna(subset=['next_page'])

# Count transitions between pages
transitions = click_pairs.groupby(['page', 'next_page']).size().reset_index(name='count')
print("\n=== Clickstream Transitions ===")
print(transitions)

# Step 4: Simple Visualization – Average Time on Page
usage.plot(kind='bar', color='skyblue', title='Average Time on Page (sec)')
plt.xlabel('Page')
plt.ylabel('Average Duration (sec)')
plt.tight_layout()
plt.show()

# Step 5: Optional – Clickstream Graph Visualization
G = nx.DiGraph()
for _, r in transitions.iterrows():
    G.add_edge(r['page'], r['next_page'], weight=r['count'])

plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1800, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title("Clickstream Flow (User Navigation)")
plt.show()
