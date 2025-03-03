import streamlit as st
import networkx as nx
import random
from pyvis.network import Network
import heapq
import numpy as np
import pandas as pd
import time
import streamlit.components.v1 as components


def dijkstra_algorithm_preview():
    def dijkstra(graph, src, dest):
        pq = [(0, src)]
        distances = {node: float('inf') for node in graph.nodes}
        distances[src] = 0
        parents = {node: None for node in graph.nodes}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == dest:
                break

            for neighbor, attributes in graph[current_node].items():
                weight = attributes['weight']
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        path = []
        node = dest
        while node is not None:
            path.append(node)
            node = parents[node]
        path.reverse()

        return path, distances

    def generate_graph(num_nodes, num_edges, seed):
        graph = nx.gnm_random_graph(num_nodes, num_edges, seed=seed)

        for u, v, data in graph.edges(data=True):
            data['weight'] = random.randint(1, 5)

        return graph

    def draw_graph(graph, path, bg_color):
        net = Network(notebook=False, height='600px', width='100%', directed=False, bgcolor=bg_color, font_color='white')

        for node in graph.nodes:
            net.add_node(node, label=str(node))

        edges_in_path = set(zip(path, path[1:]))

        for u, v, data in graph.edges(data=True):
            weight = data['weight']
            if (u, v) in edges_in_path or (v, u) in edges_in_path:
                net.add_edge(u, v, value=weight, title=f"Weight: {weight}", color='red', width=4)
            else:
                net.add_edge(u, v, value=weight, title=f"Weight: {weight}")

        # Apply ForceAtlas2 layout algorithm
        net.force_atlas_2based(gravity=-70, central_gravity=0.01, spring_length=180, spring_strength=0.08)

        return net

    def create_adjacency_matrix(graph):
        adjacency_matrix = nx.adjacency_matrix(graph).todense()
        return pd.DataFrame(adjacency_matrix, columns=graph.nodes, index=graph.nodes)

    st.title("Dijkstra's Algorithm Demo")
    st.markdown("""
        **Dijkstra's Algorithm** is a popular algorithm used for finding the **shortest paths between nodes** in a weighted graph. 
        It was conceived by computer scientist **Edsger W. Dijkstra** in 1956 and published three years later. 

        ### Key Features:
        - The algorithm works on both `directed` and `undirected` graphs.
        - It handles graphs with `non-negative` weights.
        - It uses a `priority queue` to efficiently select the next node with the smallest tentative distance.

        ### How It Works:
        1. Initialize the distance to the source node to 0 and all other nodes to infinity.
        2. Use a priority queue to explore the node with the smallest known distance.
        3. Update the distances to each neighboring node.
        4. Repeat until the destination node is reached or all nodes are explored.

        ### Visualization:
        This application allows you to visualize Dijkstra's Algorithm on a randomly generated graph. 
        You can adjust the parameters of the graph, such as the number of nodes and edges, and observe 
        the shortest path calculation in real-time.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Using rows to widen the screen
    row1 = st.columns(2)
    row2 = st.columns(2)

    with row1[0]:
        with st.expander("Adjust Graph Parameters", expanded=True):
            st.header("Graph Parameters")
            num_nodes = st.slider("Number of Nodes", min_value=2, max_value=100, value=6)
            num_edges = st.slider("Number of Edges", min_value=1, max_value=200, value=8)
            seed_value = st.number_input("Random Seed", min_value=1, max_value=100)
            bg_color = '#0E1117'
            # generate_button = st.button("Generate Graph")
            # reset_button = st.button("Reset Graph")
            col1, col2 = st.columns([1, 1])
    
            with col1:
                generate_button = st.button("Generate Graph")
            with col2:
                reset_button = st.button("Reset Graph")

    with row1[1]:
        if generate_button:
            start_time = time.time()
            graph = generate_graph(num_nodes, num_edges, seed_value)
            st.session_state['graph'] = graph
            end_time = time.time()

        if reset_button:
            if 'graph' in st.session_state:
                del st.session_state['graph']

        if 'graph' in st.session_state:
            graph = st.session_state['graph']

            with st.expander("Adjust Dijkstra's Algorithm Parameters", expanded=True):
                st.header("Nodes Selection")
                src = st.number_input("Source Node", min_value=0, max_value=num_nodes-1, value=0)
                trg = st.number_input("Target Node", min_value=0, max_value=num_nodes-1, value=num_nodes-1)
                compute_button = st.button("Compute Shortest Path")
        else:
            st.write("Click `Generate Graph` to create a new graph.")

    if 'graph' in st.session_state and compute_button:
        graph = st.session_state['graph']
        
        with st.expander("Graph", expanded=True):
            start_time = time.time()
            path, distances = dijkstra(graph, src, trg)
            net = draw_graph(graph, path, bg_color)
            net.save_graph('graph.html')
            end_time = time.time()

            st.write(f"`Source: {src}, Target: {trg}  |  Path: {path}  |   runtime: {end_time - start_time:.4f}s`")
            # st.write(f"Graph plotted in {end_time - start_time:.4f} seconds")

            components.html(open('graph.html', 'r').read(), height=650)


            st.write("The shortest path, identified by dijkstra's algorithm is highlighted in red.")

        with row2[0]:
            with st.expander("Adjacency Matrix", expanded=True):
                adjacency_matrix = create_adjacency_matrix(graph)
                # st.write("Adjacency Matrix:")
                st.dataframe(adjacency_matrix)

        # Display the route
        with row2[1]:
            route = {"address": path, "config": {"source": src, "target": trg, "seed_value": seed_value}}
            st.expander("Export shortest path route", expanded=True).write(route)


# Uncomment the following line to run the app
# dijkstra_algorithm_preview()
