# Home Price Prediction API

## Overview
This project is a **demonstration of containerization, deployment, and CI/CD automation on Google Cloud Platform (GCP)**.  
The main focus is **not** on building a highly accurate machine learning model, but rather on showcasing the full workflow of:

- Building a Dockerized application
- Deploying it to **Google Cloud Run**
- Automating builds and deployments with **Google Cloud Build (CI/CD pipeline)**

---

## Machine Learning Model
- A **minimal toy dataset** was used for training the model.  
- The goal was to provide a **working model** for API predictions, **not** to optimize ML performance.  
- The trained model (`./model/model.joblib) is packaged inside the container and exposed via a REST API endpoint.

---

## Tech Stack
- **Python** (FastAPI for defining the REST API endpoints and handle HTTP request + ASGI server for running the FastAPI application)
- **Docker** (containerization)
- **Google Artifact Registry** (storing images)
- **Google Cloud Run** (serverless deployment)
- **Google Cloud Build** (CI/CD pipeline)

---

## CI/CD Pipeline
1. **Cloud Build** is configured to watch the repository for changes.  
2. On **push to the `main` branch**:
   - A new Docker image of the app is built.
   - The image is pushed to **Google Artifact Registry**.
   - The latest image is deployed automatically to **Cloud Run**.  
3. Branch strategy:
   - **master** → used for development purposes (no automatic deployment).  
   - **main** → used for production deployment, triggers the CI/CD pipeline.  

---

## Running Locally

### On Local System
1. Create and activate a virtual environment.  
2. Install dependencies:  

   ```
   pip install -r requirements.txt
   ```
3. Start the app:

   ```
   python -m src.main
   ```

### On Docker
1. Build the image

   ```
   docker build -t home-price-api:1.0 .
   ```

2. Run the container with

   ```
   docker run --name home-price-container -p 8000:8000 home-price-api:1.0
   ```

### Testing with Postman

1. Create a new POST request to: http://127.0.0.1:8000/predict
2. In the Body tab, choose raw → JSON and provide input:

   ```
   {
    "size": 200,
    "location": "A"
   }
   ```

3. Send the request. You should receive a predicted home price in the response.
