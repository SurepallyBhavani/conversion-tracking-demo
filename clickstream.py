# ---------------------------------
# Version 2: Simulated logs + analytics (with log display)
# ---------------------------------
import requests, time, random, re, pandas as pd
from datetime import datetime

# Step 1: Simulate log data (like a web server)
pages = [
    "https://httpbin.org/get",
    "https://example.com/",
    "https://reqres.in/api/users",
    "https://jsonplaceholder.typicode.com/posts"
]

log_lines = []
print("Simulating web server log data...\n")
for i in range(5):   # simulate 10 visits
    url = random.choice(pages)
    start = time.strftime("[%d/%b/%Y:%H:%M:%S +0000]")
    r = requests.get(url)
    line = f"127.0.0.1 - - {start} \"GET {url} HTTP/1.1\" {r.status_code} {len(r.text)}"
    log_lines.append(line)
    print("Visited:", url)
    time.sleep(0.5)

print("\n✅ Simulated log data generated successfully!\n")

# Step 1.5: Display the simulated log entries
print("=== Web Server Log Data (Simulated) ===")
for line in log_lines:
    print(line)
print("=======================================\n")

# Step 2: Parse the simulated log data
pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<ts>[^\]]+)\] "(?:GET|POST) (?P<url>\S+) HTTP/1.\d" (?P<status>\d{3}) (?P<size>\d+)'
)

records = []
for line in log_lines:
    m = pattern.search(line)
    if m:
        d = m.groupdict()
        d["ts"] = datetime.strptime(d["ts"], "%d/%b/%Y:%H:%M:%S +0000")
        records.append(d)

df = pd.DataFrame(records)
df.sort_values(by=["ts"], inplace=True)

df["size"] = pd.to_numeric(df["size"], errors="coerce")
df["status"] = pd.to_numeric(df["status"], errors="coerce")

# Step 3: Simple Web Usage Analytics
print("--- Web Usage Analytics ---")
print("Total Requests:", len(df))
print("\nTop URLs:\n", df["url"].value_counts())

# Step 4: Simple Clickstream (Chronological order)
print("\n--- Clickstream Path (Chronological Order) ---")
for i, row in enumerate(df.itertuples(), 1):
    print(f"{i}. {row.url}")

print("\n✅ Web Analytics & Clickstream Analysis Completed.")

avg_size = df["size"].mean()
print("\nAverage Response Size (bytes):", round(avg_size, 2))
