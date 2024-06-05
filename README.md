# DockerKube

## Overview

**DockerKube** is a web hosting application designed to simplify the deployment of Docker images to a Kubernetes cluster. This project leverages a Python-based frontend and backend for user interaction and utilizes Jenkins for continuous integration and continuous deployment (CI/CD) automation. DockerKube enables users to seamlessly manage their applications in a Kubernetes environment, ensuring efficient deployment and scalability.

## Features

- **User-Friendly Interface**: Built with Python, the web application provides an intuitive interface for users to manage their Docker images and Kubernetes deployments.
- **Docker Image Management**: Users can upload and manage Docker images directly from the application.
- **Kubernetes Deployment**: Simplified deployment process of Docker images to Kubernetes clusters.
- **CI/CD Automation**: Integrated Jenkins pipeline to automate the build, test, and deployment processes.

## Project Structure

The project directory is structured as follows:

```
├─ src/
│  ├─ controllers/
│  │  ├─ __init__.py
│  │  └─ jenkins_controller.py        # Handles Jenkins integration and API requests
│  ├─ helpers/
│  │  ├─ __init__.py
│  │  ├─ init.py                      # Initialization helper (if needed)
│  │  ├─ config_xml.py               # Generates and manages Jenkins configuration files
│  │  ├─ deploy_pipeline_generator.py  # Generates deployment pipelines for Jenkins
│  │  ├─ generate_port.py             # Utility for generating available ports
│  │  └─ scan_pipeline_generator.py    # Scans and generates pipeline configurations
│  ├─ routes/
│  │  ├─ __init__.py
│  │  └─ routes.py                    # Defines application routes and API endpoints
│  ├─ services/
│  │  ├─ __init__.py
│  │  └─ jenkins_service.py           # Contains service logic for Jenkins interactions
│  └─ app.py                          # Main application file
├─ utils/
│  ├─ __init__.py
│  ├─ escape_xml.py                   # Utility for escaping XML strings
│  ├─ exception.py                     # Custom exception handling
│  └─ logger.py                       # Logging utilities
├─ .gitignore                         # Specifies files and directories to ignore in version control
├─ app.py                             # Entry point for the application
├─ config.py                          # Configuration settings for the application
├─ LICENSE                            # License information for the project
├─ README.md                          # Project documentation
├─ requirements.txt                   # List of required Python packages
└─ setup.py                           # Setup script for package distribution
```

## Requirements

- Python (version 3.6 or later)
- Flask (for the web application)
- Docker
- Kubernetes
- Jenkins
- Required Python libraries:
  - `requests`
  - `flask`
  - `flask-restful`
  - `docker`
  - `kubernetes`

## Installation

### Clone the Repository

```bash
git clone https://github.com/Pirate-Emperor/DockerKube.git
cd DockerKube
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Jenkins

1. Install Jenkins and required plugins (Docker and Kubernetes).
2. Configure Jenkins with your Docker registry credentials.
3. Set up a Jenkins pipeline to build and deploy Docker images to the Kubernetes cluster.

### Set Up Kubernetes Cluster

1. Ensure you have a Kubernetes cluster running (e.g., Minikube, GKE, EKS).
2. Configure `kubectl` to interact with your Kubernetes cluster.

## Usage

1. **Run the Application**: Start the Flask application by executing:

   ```bash
   python app.py
   ```

2. **Access the Web Interface**: Open a web browser and navigate to `http://localhost:5000` to access the DockerKube application.

3. **Deploy Docker Images**:
   - Upload your Docker image using the provided interface.
   - Specify deployment configurations (e.g., replicas, namespace).
   - Click on "Deploy" to initiate the deployment process to the Kubernetes cluster.

4. **CI/CD Pipeline**: Jenkins will automatically trigger builds and deployments based on your configurations.

## Conclusion

The **DockerKube** project provides a comprehensive solution for deploying Docker images to Kubernetes, integrating CI/CD practices for automated deployments. This tool streamlines the deployment process, enabling developers to focus on building applications rather than managing infrastructure.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Pirate-Emperor**

[![Twitter](https://skillicons.dev/icons?i=twitter)](https://twitter.com/PirateKingRahul)
[![Discord](https://skillicons.dev/icons?i=discord)](https://discord.com/users/1200728704981143634)
[![LinkedIn](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/piratekingrahul)

[![Reddit](https://img.shields.io/badge/Reddit-FF5700?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/u/PirateKingRahul)
[![Medium](https://img.shields.io/badge/Medium-42404E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@piratekingrahul)

- GitHub: [Pirate-Emperor](https://github.com/Pirate-Emperor)
- Reddit: [PirateKingRahul](https://www.reddit.com/u/PirateKingRahul/)
- Twitter: [PirateKingRahul](https://twitter.com/PirateKingRahul)
- Discord: [PirateKingRahul](https://discord.com/users/1200728704981143634)
- LinkedIn: [PirateKingRahul](https://www.linkedin.com/in/piratekingrahul)
- Skype: [Join Skype](https://join.skype.com/invite/yfjOJG3wv9Ki)
- Medium: [PirateKingRahul](https://medium.com/@piratekingrahul)

---

