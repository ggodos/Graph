
import networkx as nx


def drawDefault(adj, isDir, weighted):
    if (isDir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    for i in adj:
        G.add_node(i)

    if (weighted):
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j, weight=adj[i][j])
    else:
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j)

    pos = nx.kamada_kawai_layout(G)

    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=1, edge_color='#750000')


def drawMinPath(adj, isDir, weighted, path):
    if (isDir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    for i in adj:
        G.add_node(i)
    
    for i in adj:
        for j in adj[i]:
            if (weighted):
                G.add_edge(i, j, weight=adj[i][j], color='#750000')
            else:
                G.add_edge(i, j, color='#750000')
            for k in range(len(path) - 1):
                if ((path[k] == i) and (path[k + 1] == j)) or ((path[k] == j) and (path[k+1] == i)):
                    if (weighted):
                        G.add_edge(i, j, weight=adj[i][j], color='blue')
                    else:
                        G.add_edge(i, j, color='blue')
                    break

    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=1, edge_color=nx.get_edge_attributes(G,'color').values())


def drawColoring(adj, isDir, weighted, colors):
    if (isDir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    def converter(colors):
        col_converted = []
        for i in colors:
            col_converted.append((colors[i][0] / 255, colors[i][1] / 255, colors[i][2] / 255))
        return col_converted
    
    for i in adj:
        G.add_node(i)
    
    if (weighted):
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j, weight=adj[i][j])
    else:
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j)
    
    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos=pos, with_labels=True, node_color=converter(colors), font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=1, edge_color='#750000')

