# 🚀 DevOps Engineer Practical Challenge

## Production-Ready Application Deployment using AWS ECS, Docker, Terraform & GitHub Actions

---

# 📌 Project Overview

This project demonstrates a complete end-to-end DevOps implementation for deploying a production-ready containerized application using modern DevOps tools and cloud-native technologies.

The objective of this project was to:

* Containerize a Python Flask application using Docker
* Provision AWS infrastructure using Terraform
* Deploy the application to AWS ECS Fargate
* Implement CI/CD automation using GitHub Actions
* Configure monitoring and logging using AWS CloudWatch
* Maintain a modular, reusable, and production-style deployment workflow

The deployment process is fully automated and follows Infrastructure as Code (IaC) and DevOps best practices.

---

# 🎯 Project Objectives

The project was designed to achieve the following:

✅ Infrastructure automation using Terraform
✅ Application containerization using Docker
✅ Automated CI/CD pipeline using GitHub Actions
✅ AWS ECS Fargate deployment
✅ CloudWatch monitoring & logging
✅ Repeatable and scalable deployment workflow
✅ Production-style DevOps architecture

---

# 🏗️ Solution Architecture

## Architecture Workflow

```text id="r201"
Developer
   ↓
GitHub Repository
   ↓
GitHub Actions CI/CD Pipeline
   ↓
Docker Image Build
   ↓
Docker Hub Registry
   ↓
AWS ECS Fargate Deployment
   ↓
CloudWatch Monitoring & Logging
```

---

# 📊 Architecture Components

| Component       | Purpose                      |
| --------------- | ---------------------------- |
| GitHub          | Source code management       |
| GitHub Actions  | CI/CD automation             |
| Docker          | Application containerization |
| Docker Hub      | Docker image registry        |
| Terraform       | Infrastructure provisioning  |
| AWS ECS Fargate | Container orchestration      |
| AWS CloudWatch  | Monitoring and logging       |
| IAM Roles       | ECS execution permissions    |
| VPC/Subnets     | Network infrastructure       |

---

# ⚙️ Technologies Used

## ☁️ Cloud Platform

* AWS (Amazon Web Services)

## 🏗️ Infrastructure as Code

* Terraform

## 🐳 Containerization

* Docker

## 🚀 CI/CD Automation

* GitHub Actions

## 📦 Container Orchestration

* AWS ECS Fargate

## 📊 Monitoring & Logging

* AWS CloudWatch

## 🐍 Backend Framework

* Python Flask

## 🔐 Version Control

* Git & GitHub

---

# 📂 Project Structure

```bash id="r202"
devops-project/
│
├── apps/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── terraform/
│   ├── iam.tf
│   ├── alb.tf
│   ├── ecs.tf
│   ├── network.tf
│   ├── security.tf
│   ├── variables.tf
│   └── provider.tf
  
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── README.md
├── DevOps_Architecture2.png
└── .gitignore
```

---

# 🐍 Flask Application

The application was developed using Python Flask.

## Initial Application

```python id="r203"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Taiwo DevOps Challenge App Running Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

# 🎨 Professional UI Enhancement

The application interface was later upgraded with:

* Modern HTML/CSS UI
* Responsive layout
* Professional DevOps dashboard appearance
* Deployment status display

This improved the project presentation and production readiness.

---

# 🐳 Docker Implementation

Docker was used to containerize the Flask application.

## Dockerfile

```dockerfile id="r204"
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

# 🚀 Docker Commands Used

## Build Docker Image

```bash id="r205"
docker build -t devops-app ./apps
```

Builds the Docker image from the application directory.

---

## Run Docker Container

```bash id="r206"
docker run -p 5000:5000 devops-app
```

Runs the Docker container locally.

---

## Run on Different Port

```bash id="r207"
docker run -p 5001:5000 devops-app
```

Used when port 5000 was already occupied.

---

## List Running Containers

```bash id="r208"
docker ps
```

Displays active Docker containers.

---

## Stop Running Container

```bash id="r209"
docker stop <container_id>
```

Stops a running Docker container.

---

# ☁️ AWS Infrastructure Deployment

AWS infrastructure was provisioned using Terraform.

---

# 🏗️ Infrastructure Components Created

## Networking

* VPC
* Public Subnets
* Internet Gateway
* Route Tables

## Security

* Security Groups
* IAM Roles

## Compute

* ECS Cluster
* ECS Service
* ECS Task Definition

## Monitoring

* CloudWatch Log Groups

---

# 🏗️ Terraform Implementation

Terraform was used to provision AWS infrastructure in a modular and reusable way.

---

# 📌 Terraform Commands Used

## Initialize Terraform

```bash id="r210"
terraform init
```

Downloads required providers and initializes Terraform.

---

## Validate Configuration

```bash id="r211"
terraform validate
```

Checks Terraform syntax and configuration.

---

## Preview Infrastructure

```bash id="r212"
terraform plan
```

Displays infrastructure changes before deployment.

---

## Apply Infrastructure

```bash id="r213"
terraform apply
```

Deploys AWS infrastructure resources.

---

## Destroy Infrastructure

```bash id="r214"
terraform destroy
```

Deletes all provisioned infrastructure.

---

# 🔐 AWS CLI Configuration

AWS CLI was configured locally for Terraform and ECS deployment.

## Configure AWS Credentials

```bash id="r215"
aws configure
```

Prompts:

* AWS Access Key
* AWS Secret Key
* Region
* Output format

---

## Verify AWS Credentials

```bash id="r216"
aws sts get-caller-identity
```

Verifies AWS authentication.

---

# 🚀 ECS Deployment

Amazon ECS Fargate was selected because:

* Fully managed container service
* No EC2 management required
* Production-ready scalability
* Simplified deployment workflow

---

# 📦 ECS Components Used

* ECS Cluster
* ECS Task Definition
* ECS Service
* Fargate Launch Type

---

# 🔄 CI/CD Pipeline Implementation

GitHub Actions was used to automate the complete deployment pipeline.

---

# ⚡ CI/CD Workflow

The workflow automatically triggers whenever code is pushed to the `main` branch.

---

# 📌 CI/CD Steps

## 1. Checkout Source Code

```yaml id="r217"
uses: actions/checkout@v4
```

Fetches latest repository code.

---

## 2. Configure AWS Credentials

```yaml id="r218"
uses: aws-actions/configure-aws-credentials@v4
```

Authenticates GitHub Actions with AWS.

---

## 3. Docker Hub Authentication

```yaml id="r219"
docker login
```

Authenticates Docker Hub access.

---

## 4. Build Docker Image

```yaml id="r220"
docker build -t devops-app ./apps
```

Builds updated application image.

---

## 5. Push Docker Image

```yaml id="r221"
docker push username/devops-app:latest
```

Pushes image to Docker Hub.

---

## 6. Deploy to ECS

```yaml id="r222"
aws ecs update-service \
--cluster devops-cluster \
--service devops-service \
--force-new-deployment
```

Forces ECS to deploy latest image.

---

# 📄 Final GitHub Actions Workflow

```yaml id="r223"
name: DevOps CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_KEY }}
          aws-region: us-east-1

      - name: Docker Hub Login
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker Image
        run: docker build -t devops-app ./apps

      - name: Tag Docker Image
        run: docker tag devops-app ${{ secrets.DOCKER_USERNAME }}/devops-app:latest

      - name: Push Docker Image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/devops-app:latest

      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster devops-cluster \
            --service devops-service \
            --force-new-deployment
```

---

# 🔐 GitHub Secrets Configuration

Sensitive credentials were securely stored using GitHub Secrets.

---

# 📌 Secrets Configured

| Secret Name     | Purpose                 |
| --------------- | ----------------------- |
| AWS_ACCESS_KEY  | AWS authentication      |
| AWS_SECRET_KEY  | AWS authentication      |
| DOCKER_USERNAME | Docker Hub login        |
| DOCKER_PASSWORD | Docker Hub access token |

---

# 📊 Monitoring & Logging

AWS CloudWatch was implemented for:

* Container logs
* ECS monitoring
* Deployment troubleshooting
* Runtime visibility

---

# ☁️ CloudWatch Features

* ECS task logs
* Container stdout/stderr logs
* Centralized logging

---

# 🧪 Testing & Validation

The following validations were performed:

✅ Terraform validation
✅ Docker image build test
✅ ECS deployment verification
✅ CloudWatch log verification
✅ GitHub Actions CI/CD testing
✅ External IP accessibility testing

---

# 🔧 Challenges Encountered & Solutions

| Challenge                         | Solution                          |
| --------------------------------- | --------------------------------- |
| Duplicate Terraform provider      | Removed duplicate provider block  |
| Invalid AWS token                 | Reconfigured AWS CLI              |
| Docker Hub authentication failure | Used Docker access token          |
| GitHub push rejection             | Pulled remote changes with rebase |
| Docker build path error           | Corrected apps directory path     |
| Port already allocated            | Used alternative localhost port   |
| Folder casing conflict            | Fixed Git folder naming           |

---

# 📈 Design Decisions

## Why ECS Fargate?

* Serverless container management
* Simplified operations
* Production-ready service

## Why Terraform?

* Infrastructure as Code
* Repeatable deployments
* Reusable infrastructure

## Why Docker?

* Portable runtime environment
* Consistent deployments
* Simplified dependency management

## Why GitHub Actions?

* Native GitHub integration
* Easy CI/CD automation
* Fast deployment workflow

---

# 🔒 Security Considerations

The following security best practices were implemented:

* IAM Roles for ECS execution
* GitHub Secrets for credentials
* No hardcoded secrets
* Security Group restrictions
* Infrastructure managed through Terraform

---

# ⚠️ Limitations

Current implementation limitations:

* No Auto Scaling
* Single environment deployment
* Basic monitoring only

---

# 🚀 Future Improvements

Potential enhancements:

* Implement Auto Scaling
* Add HTTPS with ACM
* Use AWS ECR instead of Docker Hub
* Implement Blue/Green deployment
* Add Prometheus & Grafana monitoring
* Implement Kubernetes (EKS)

---

# 📌 Deployment Workflow Summary

```text id="r224"
Code Development
      ↓
Git Push to GitHub
      ↓
GitHub Actions Trigger
      ↓
Docker Build
      ↓
Docker Hub Push
      ↓
AWS ECS Deployment
      ↓
CloudWatch Monitoring
```

---

# 👨‍💻 Author

**Taiwo Peter Olatunji**
DevOps Engineer Practical Challenge Submission

---

# 📎 Repository Link

GitHub Repository:

[DevOps Project Repository](https://github.com/Taiwo-Peter2023/devops-project)

---

# ✅ Conclusion

This project successfully demonstrates a production-style DevOps deployment pipeline using:

* Docker containerization
* Terraform infrastructure provisioning
* AWS ECS Fargate deployment
* Load Balancer
* GitHub Actions CI/CD automation
* CloudWatch monitoring

The implementation provides:

* Automated infrastructure deployment
* Automated application deployment
* Scalable container orchestration
* Production-style DevOps workflow
* End-to-end CI/CD automation
