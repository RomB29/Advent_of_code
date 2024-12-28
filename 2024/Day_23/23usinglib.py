import networkx as nx

# Créer un graphe vide
G = nx.Graph()

# Lire le fichier et ajouter les arêtes au graphe
with open("23.in") as f:
    for ln in f:
        l, r = ln.strip().split("-")
        G.add_edge(l, r)

# Trouver toutes les cliques de taille 3
tt = [list(t) for t in nx.enumerate_all_cliques(G) if len(t) == 3]

# Filtrer les cliques contenant un nom qui commence par "t"
ft = [t for t in tt if any(n.startswith("t") for n in t)]
print("ONE:", len(ft))

# Trouver la clique la plus grande
cc = list(nx.find_cliques(G))
lc = max(cc, key=len)
print("TWO:", ",".join(sorted(lc)))
