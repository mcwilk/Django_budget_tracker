# Expense Tracker

### Table of Contents
* [Introduction](#introduction)
* [Features](#-features)
* [Quick Start](#-quick-start)
* [Tech Stack](#-tech-stack)
* [Testing & Quality](#-testing--quality)
* [CI/CD](#-cicd)
* [Screenshots](#-screenshots)
* [Status](#-status)
* [Sources](#-sources)
* [Contact](#-contact)

## 💡 Introduction
A Django-based web application for tracking and categorizing personal expenses, built with a PostgreSQL database and structured following MVT (Model-View-Template) architecture. The project includes a comprehensive test suite with integration and smoke tests. CI/CD pipelines implemented via GitHub Actions. 

## 🚀 Features
- Registration of private user accounts
- Authentication and access control for personalized dashboards
- Budget creation with custom categorization and limits
- Adding and tagging expenses across multiple budget categories
- Interactive expense analytics and monthly summaries
- Django admin panel for managing users, categories, and transactions

## ⚡ Quick Start
⚠️ Note: Before you begin, make sure you have Docker ≥ 27.5 installed on your machine.

#### 🚧 SECTION UNDER DEVELOPMENT 🚧

## 🧪 Tech Stack
- Backend: Python (3.11), Django (4.2), PostgreSQL
- Frontend: Django templates, HTML5, CSS3, Highcharts for dynamic data visualization
- Testing: pytest, pytest-django
- Infrastructure: Docker, Docker Compose, Kubernetes (in progress)
- DevOps (in progress or planned): GitHub Actions, Helm Charts, NGINX, GitOps via ArgoCD

## ✅ Testing & Quality
- Integration tests covering forms, views and models using pytest-django
- Smoke tests executed against Docker containers to verify core app functionality after deployment
- End-to-End (E2E) planned with Selenium or Playwright

## 🔄 CI/CD
CI/CD pipelines implemented with GitHub Actions. Automated steps include:
- Static code analysis with pylint
- Integration and regression tests with pytest
- Docker image build and push to DockerHub registry
- Improvement of environment separation for development, testing/staging and production (planned)
- Deployment to Kubernetes via ArgoCD using GitOps workflows (planned)

## 📷 Screenshots

![Screenshot2](other/screenshots/dashboard.png)

![Screenshot3](other/screenshots/analysis_v1.png)

## 📌 Status
Project is: _in_progress_

Currently being extended with GitOps-based deployment using Kubernetes and ArgoCD.

Planned enhancements:
- Helm charts for application packaging
- NGINX for routing
- Monitoring and alerting with Prometheus and Grafana
- Deployment to self-hosted VPS server environment

## 📂 Sources
Charts provided by: www.highcharts.com

## 📬 Contact
Email: mcwilk.dev@gmail.com
