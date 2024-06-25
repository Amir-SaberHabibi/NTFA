# Network Traffic Flow Analysis Project

## Overview
This project, developed by **Amir Saberhabibi**, is based on a project for the Algorithms Design course, mentored by **Dr. Maziar Salahi** at the **University of Guilan, Faculty of Mathematical Sciences**. This project aims to provide tools for better network analysis and visualization using graph-based algorithms.


## How to Run

1. **Install Dependencies**
    - Ensure you have Python and Streamlit installed.
        ```
      pip install -r requirements.txt
        ```

2. **Run the Application**
    - Start the Streamlit application by running the following command:
        ```
      streamlit run main.py
        ```

## Functionality

### Home
- Provides an introduction to the application and its capabilities.
- Users are guided to select different functionalities from the navigation bar.

### Network Traffic Flow Analysis
- Loads and processes the Unicauca Network Flows Dataset.
- Visualizes the network graph.
- Allows users to select source and destination nodes to compute the shortest path using Dijkstra's Algorithm.
- Displays the shortest path and its total cost.

### Dijkstra Algorithm
- Demonstrates Dijkstra's Algorithm on a randomly generated graph.
- Users can adjust the number of nodes, edges, and other parameters.
- Visualizes the graph and highlights the shortest path.

### Performance Analysis
- Analyzes the performance of Dijkstra's Algorithm.
- Allows users to configure the number of nodes, edges, and other parameters.
- Measures and visualizes the average runtime of the algorithm for different configurations.


## License
This project is licensed under the MIT License.
