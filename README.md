# Azure Function - IBM db2 connection

This repository contains a Python-based Azure Function (V2) that connects to an IBM Db2 database and returns the results of a basic query. The project builds upon Microsoft's Azure Function documentation, with a single but a key addition being the connection to an IBM Db2 database and a few supporting Bash scripts for deployment.

---
## Getting Started

To get this project running, follow the steps below:

### Prerequisites
 - [Azure Functions Core Tools - Python]((https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python))
 - Docker  (if using the containerized approach)
 - IBM Db2 connection string

### Step 1: Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/gubiithefish/azure_function_db2_connection.git
cd azure_function_db2_connection
```

### Step 2: Configure IBM Db2 Connection String
Add your IBM Db2 connection string to the `local.settings.json` file.
- Use the provided `local.settings.json.example` as a template.

---

## Running the Function App

There are two approaches for running the Azure Function: locally using the Azure Functions Core Tools or using Docker.

### Option A: Using Azure Functions Core Tools
1. Ensure the Azure Functions Core Tools are installed and available in your environment.
2. Run the following command to start the Azure Function App:
```bash
func start
```
The app will be available at http://localhost:7071.

### Option B: Using Docker
Build and run the Docker image by 

a) executing the following commands:
```bash
docker build -t <image-name> .
docker run -p 8080:80 <image-name>
```
or b) executing the provided `docker_local_build_run.sh` script.

The app will be available at http://localhost:8080.



---

### Resources
1. [Create a function app in a local Linux container - Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-container-registry?tabs=acr%2Cbash&pivots=programming-language-python#build-the-container-image-and-verify-locally)
2. [Azure Functions developer guide - Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
3. [Develop Azure Functions locally using Core Tools - Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python)

---
Feel free to contribute, report issues, or ask questions by opening an issue on this repository.