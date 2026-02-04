def route_query(q):
    q = q.lower()
    if "count" in q or "how many" in q:
        return "sql"
    if "depends" in q or "relationship" in q:
        return "graph"
    return "vector"
