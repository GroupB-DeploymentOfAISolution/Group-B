# Inventory Optimization  

## Group Members
| **Student Name**                  | **Student ID**  |
|------------------------------------|-----------------|
| Dhanush Chandar Sivakumar          | 500228646       |
| Rithwik Prem                       | 500220919       |
| Sweatha Palani                     | 500221321       |
| Oluwakanyinsola Adebanjo           | 500228268       |
| Rajesh Jayaraman                   | 500228177       |

---

## Project Overview
This repository contains an AI-driven inventory optimization system that leverages:
- **Time-Series Forecasting**: ARIMA for demand prediction.
- **Optimization Algorithms**: Linear programming to minimize costs and balance stock levels.
- **Automation Tools**: Jenkins and Ansible for CI/CD and deployment.

**GitHub Repository Link**: [Group B Inventory Optimization Project](https://github.com/GroupB-DeploymentOfAISolution/Group-B/tree/main)

---

## Abstract
This project focuses on the design and deployment of an AI-based inventory optimization system. By leveraging demand forecasting (ARIMA) and optimization algorithms, the system minimizes overstocking and stockouts, improving cost efficiency and customer satisfaction. The project also incorporates automation tools like Jenkins and Ansible to streamline development and deployment.

---

## Step 1: Initial Planning & Design

### Problem Definition
Retailers struggle with:
- **Overstocking:** High storage costs and wastage.
- **Understocking:** Missed sales and customer dissatisfaction.

**Solution:**  
A predictive system that analyzes historical sales data to determine optimal stock levels.

### Data Requirements
- **Sales Data:** Historical transactions.
- **Product Information:** Categories and pricing.
- **Seasonal Data:** Demand spikes.
- **Inventory Levels:** Stock notifications.

### System Architecture
- **Data Input:** Sales and inventory ingestion.
- **Forecasting Model:** ARIMA for predictions.
- **Optimization Algorithm:** Linear programming for restocking suggestions.
- **Database:** MySQL for centralized storage.

### Database Schema
- **Products Table:** Stores product details.
- **Sales Table:** Tracks transactions.
- **Inventory Table:** Maintains stock levels and history.

### GitHub Setup
- **Repository Structure**:
  - `/data`: Sample datasets.
  - `/models`: Scripts for forecasting and optimization.
  - `/docs`: Documentation.
- **Version Control**: Branching strategy for individual contributions.

---

## Step 2: Development Phase

### Data Preprocessing
- **Cleaning**: Removed duplicates and handled missing values using `dropna()`.
- **Outlier Detection**: Applied the IQR method for filtering extreme values.
- **Feature Engineering**:
  - Created features like `Total Price` = `Quantity * Price`.
  - Aggregated monthly sales trends for demand analysis.

---

### Forecasting Model Development (ARIMA)
- **Model Selection**: ARIMA was selected for time-series forecasting.
- **Metrics**:
  - **MSE**: 6981501284.1
  - **MAE**: 383153.88
- **Validation**: Split data into training and testing sets.

---

### Continuous Integration with Jenkins
- **Pipeline**:
  - Environment setup.
  - Dependency installation via `requirements.txt`.
  - Automated testing with `pytest`.

---

## Step 3: Advanced Development with Ansible

### Optimization Algorithms
- **Linear Programming**:
  - Used `scipy.optimize.linprog` to calculate optimal restocking.
  - Constraints: Storage capacity, supplier limits.

### Deployment Automation with Ansible
- **Playbooks**:
  - `setup_testing_environment.yml`: Installs Python, pip, and dependencies.
  - `deploy_application.yml`: Deploys the application.
- **Inventory**: Testing and production servers defined in `inventory.ini`.

---

### Testing and Validation
- **Unit Testing**: Verified individual modules (e.g., ARIMA, optimization).
- **Integration Testing**: Validated interactions between system components.
- **Performance Testing**: Benchmarked execution times using `pytest-benchmark`.

---

## Step 4: Production Deployment

### Deployment Pipeline Design
- **Tools**:
  - **Jenkins**: CI/CD pipeline for integration and testing.
  - **Ansible**: Automates environment setup and deployment.

### Monitoring and System Performance 
- **Monitoring Tools**:
  - Prometheus for system metrics.
  - Grafana for visualization.

---

## Conclusion
The project successfully implemented an AI-driven inventory optimization system with automation and robust testing. This solution addresses overstocking and understocking challenges effectively.

---

## Installation and Setup

Follow these steps to set up the project environment and deploy the solution:

### Clone the Repository
Clone the GitHub repository to your local system:
```bash
git clone https://github.com/GroupB-DeploymentOfAISolution/Group-B.git
cd Group-B
```
###  Set Up Python Environment
Create a virtual environment and install the necessary dependencies:

#### For Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
#### For Windows
```bash
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### Run Ansible Playbooks
Navigate to the Ansible directory:
```bash
cd ansible
```
### Deploy the Application
Run the deployment playbook:
```bash
ansible-playbook -i inventory.ini deploy_application.yml
```
___

## Notes
- Ensure Python 3.8 or higher is installed.
- SSH access must be configured for Ansible to connect to the target servers.
- Use the requirements.txt file to ensure all dependencies are correctly installed.
