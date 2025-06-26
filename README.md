# docker-sl-project

This Repo is used to demostrate the Docker project described below. 
I have created a Todo App which will use Fastapi in the backend and Postgresql to store all the Todo entries.

A user is tasked to deploy a multi-tier application on a cloud-based virtual
machine using Docker Compose. After installing Docker, Docker Compose,
and Git, they clone the application repository and update configuration files
with the machine's public IP to ensure proper communication between the
frontend, API, and backend components.
Post these updates, the user runs docker compose to bring up the
application, adjust the security group settings to allow traffic on specific ports
(8080, 5000), and verify the deployment by accessing the application via the
public IP. This confirms that all components are accessible and functional.
