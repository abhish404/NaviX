# NaviX - AI-Powered Route Optimization

NaviX is an AI-powered route optimization and visualization tool designed to optimize sales vehicle routes efficiently. It focuses on maximizing potential sales while minimizing costs using machine learning and heuristic algorithms.

## 🚀 Features

- **Optimization Mode**: Assigns delivery points to distribution centers while minimizing travel costs.
- **Recommendation Mode**: Suggests optimal locations for distribution points and vehicle allocations.
- **Visualization**: Interactive mapping using Streamlit and Mapbox to display delivery routes.

## 🛠️ Tech Stack

- **Machine Learning**: Modified K-NN for clustering destinations.
- **Routing Optimization**: K-Means clustering and Traveling Salesman Problem (TSP) optimization.
- **Visualization**: Streamlit and Mapbox for real-time route visualization.
- **Cloud Services**: Azure Maps (routing API), Azure ML, and Azure App Service.

## 📌 Project Workflow

1. **Cluster delivery points** using a modified K-Means algorithm.
2. **Assign optimized vehicle routes** while minimizing fuel costs.
3. **Optimize final routes** using TSP algorithms.
4. **Visualize the results** on an interactive dashboard.

## 🎯 Why This Project?

This project showcases my skills in:

- **AI-driven optimization**
- **Cloud-based development**
- **Interactive data visualization**

It was developed as part of a hackathon challenge, demonstrating my ability to solve real-world logistics problems efficiently.

## 📍 Deployment

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NaviX.git
   cd NaviX
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the project using Streamlit:
   ```bash
   streamlit run app.py
   ```

### Cloud Deployment

NaviX is hosted on Azure using App Service and Maps API. To deploy:

1. Set up an Azure App Service.
2. Deploy the application using Azure Functions.
3. Integrate Azure Maps API for routing.

---

🚀 **Optimizing routes, minimizing costs!**

