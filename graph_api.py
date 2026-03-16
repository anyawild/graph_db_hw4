"""
filename: graph_api.py

graph api for storing graphs in redis (part ii).
"""
import redis

# connect to local redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def add_node(name, type, properties=None):
    """
    add a node of a given name and type and assign any properties.
    """
    key = "node:" + name
    data = {"type": type}
    if properties is not None:
        for k, v in properties.items():
            data[k] = v
    r.hset(key, mapping=data)


def add_edge(name1, name2, type):
    """
    add an edge between nodes named name1 and name2.
    """
    key = "edges:" + name1
    value = type + "|" + name2
    r.sadd(key, value)


def get_adjacent(name, node_type=None, edge_type=None):
    """
    get the names of all adjacent nodes. can filter by node_type and/or edge_type.
    """
    key = "edges:" + name
    neighbors = []

    for entry in r.smembers(key):
        parts = entry.split("|", 1)
        if len(parts) != 2:
            continue
        e_type, neighbor = parts[0], parts[1]

        if edge_type is not None and e_type != edge_type:
            continue

        if node_type is not None:
            n_key = "node:" + neighbor
            n_type = r.hget(n_key, "type")
            if n_type != node_type:
                continue

        neighbors.append(neighbor)

    return neighbors


def get_recommendations(name):
    """
    get all books purchased by people that a given person knows
    but exclude books already purchased by that person.
    """
    # people that name knows
    friends = get_adjacent(name, node_type="Person", edge_type="knows")

    # books bought by friends
    rec_books = set()
    for f in friends:
        books = get_adjacent(f, node_type="Book", edge_type="bought")
        for b in books:
            rec_books.add(b)

    # books already owned by name
    owned = set(get_adjacent(name, node_type="Book", edge_type="bought"))

    # remove already owned
    final = rec_books - owned

    return list(final)

