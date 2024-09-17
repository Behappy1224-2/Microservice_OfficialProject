Official Microservice Project Created By JeffYu

## Overview
This project is a microservice designed to interact with a Line bot, providing functionalities like processing user commands, controlling devices, and checking device statuses.

The service is built using Flask, containerized with Docker, and deployed on Render with a fully automated CI/CD pipeline.

## Summary of Major Steps in This Project
1.Microservice Development:
Design Microservice Structure: We structured the microservice with key components like app.py, message_handler.py, api_client.py, and command_processor.py,etc.
2.Containerization with Docker:
Build Dockerfile and Local Testing: Successfully built and tested the Docker image locally, validating that the microservice functions are correct and interacts well with webhooks and other components.

3.Deployment to Cloud platform:
Deploy to Cloud: Deployed the Dockerized microservice to Render, providing a publicly accessible URL for the service.
Live Testing: Verified the deployment by interacting with the Line bot, ensuring the endpoints responded correctly in a production environment.
CI/CD Pipeline with GitHub Actions:

4.CI/CD Setup: Implemented a CI/CD pipeline using GitHub Actions to automate the process of building, testing, and deploying the microservice upon changes.
Automated Workflow: Configured the workflow to trigger on pushes and pull requests to the main branch, specifically targeting changes in the im_microservice directory and automated deploy to render server.

5.Integration of OpenAPI Specification:
OpenAPI Specification: Created an openapi.yaml file to document API endpoints, providing a clear, standardized guide for how each endpoint functions, including request and response formats.
Validation with OpenAPI Specification : Use tools like Swagger editor/ Postman / Spectral to validate OpenAPI file
