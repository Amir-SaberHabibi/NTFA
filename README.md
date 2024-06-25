# Network Traffic Flow Analysis Project

## Overview
This project, developed by **Amir Saberhabibi**, is based on a project for the Algorithms Design course, mentored by **Dr. Maziar Salahi** at the **University of Guilan, Faculty of Mathematical Sciences**. The goal of this project is to provide tools for better network analysis and visualization using graph-based algorithms.

## Project Structure

### Main Components

1. **main.py**
    - The main entry point for the Streamlit application.
    - Provides a navigation bar for different functionalities.
    - Contains an "About Us" section with contact information and project details.

2. **NTFA.py**
    - Implements the Network Traffic Flow Analysis module.
    - Uses the Unicauca Network Flows Dataset for analysis.
    - Visualizes the network graph and computes the shortest path using Dijkstra's Algorithm.

3. **dijkstra.py**
    - Demonstrates Dijkstra's Algorithm on a randomly generated graph.
    - Allows users to visualize the shortest path and adjust graph parameters.

4. **performance.py**
    - Analyzes the performance of Dijkstra's Algorithm.
    - Measures the average runtime of the algorithm for different graph sizes and configurations.

## How to Run

1. **Install Dependencies**
    - Ensure you have Python and Streamlit installed.
    - Install required packages using the following command:
        ```sh
        pip install streamlit networkx pandas numpy plotly
        ```

2. **Run the Application**
    - Start the Streamlit application by running the following command:
        ```sh
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

### Download
- Placeholder for future functionality related to downloading data or results.

## Contact Information
For more information, please refer to:

- **Amir Saberhabibi**
- **Mentor: Dr. Maziar Salahi**
- [Dr. Maziar Salahi's Scholar](https://scholar.google.com/citations?user=8cXhHrsAAAAJ&hl=en)

## License
This project is licensed under the MIT License.

---

This README file provides a general overview and a solid representation of the overall functionality of the project without delving into too much detail.
