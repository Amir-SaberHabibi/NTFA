import streamlit as st
import networkx as nx
import random
import time
import heapq
import plotly.graph_objects as go
import numpy as np

def dijkstra(graph, src):
    pq = [(0, src)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[src] = 0
    parents = {node: None for node in graph.nodes}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, parents

def generate_graph(num_nodes, num_edges):
    G = nx.gnm_random_graph(num_nodes, num_edges)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)
    return G

def moving_average(data, window_size):
    cumsum = np.cumsum(np.insert(data, 0, 0))
    return (cumsum[window_size:] - cumsum[:-window_size]) / float(window_size)

def run_performance_analysis(start_nodes, end_nodes, step_nodes, num_edges_factor, num_runs, plot_placeholder, window_size):
    run_times = []
    x_data = []
    y_data = []

    for num_nodes in range(start_nodes, end_nodes + 1, step_nodes):
        num_edges = num_nodes * num_edges_factor
        current_run_times = []

        for _ in range(num_runs):
            G = generate_graph(num_nodes, num_edges)
            start_node = random.randint(0, num_nodes - 1)
            start_time = time.time()
            dijkstra(G, start_node)
            end_time = time.time()
            run_time = end_time - start_time
            current_run_times.append(run_time)
        
        avg_time = sum(current_run_times) / num_runs
        x_data.append(num_nodes)
        y_data.append(avg_time)

        if len(y_data) >= window_size:
            smooth_y_data = moving_average(y_data, window_size)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_data[window_size-1:], y=smooth_y_data, mode='lines+markers', name='Avg runtime'))

            fig.update_layout(
                title="Performance of Dijkstra's Algorithm",
                xaxis_title="Number of Nodes",
                yaxis_title="Average Runtime (seconds)",
                legend_title="Legend"
            )

            plot_placeholder.plotly_chart(fig)
        time.sleep(0.1)  # Simulate real-time update

def dijkstra_algorithm_performance():
    # st.markdown("## **Dijkstra's Algorithm Performance Analysis**")
    st.markdown("## Choose Configuration:")

    col1, col2 = st.columns([1, 3])

    with col1:
        start_nodes = st.number_input("Start number of nodes", min_value=5, max_value=200, value=10, key="start_nodes")
        end_nodes = st.number_input("End number of nodes", min_value=5, max_value=2000, value=100, key="end_nodes")
        step_nodes = st.number_input("Step size for number of nodes", min_value=1, max_value=50, value=10, key="step_nodes")
        num_edges_factor = st.number_input("Number of edges factor (edges = nodes * factor)", min_value=1, max_value=20, value=2, key="num_edges_factor")
        num_runs = st.number_input("Number of runs per configuration", min_value=1, max_value=100, value=5, key="num_runs")
        window_size = st.number_input("Smoothing window size", min_value=1, max_value=20, value=5, key="window_size")

        if st.button("Run Performance Analysis"):
            plot_placeholder = col2.empty()
            run_performance_analysis(start_nodes, end_nodes, step_nodes, num_edges_factor, num_runs, plot_placeholder, window_size)

    with col2:
        st.write("The performance diagram will appear here.")

if __name__ == "__main__":
    dijkstra_algorithm_performance()
