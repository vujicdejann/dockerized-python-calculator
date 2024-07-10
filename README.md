# Dockerized Python Calculator

## Overview
This project contains a Dockerized version of a Python-based calculator that supports basic arithmetic operations like addition, subtraction, multiplication, and division. It is designed to run in a Docker container to ensure a consistent environment across different systems.

## Features
- Perform basic arithmetic operations.
- Docker containerization ensures compatibility and ease of deployment.

## Prerequisites
- Docker must be installed on your system. You can download it from [Docker's official site](https://www.docker.com/products/docker-desktop).

## Installation and Setup
1. **Clone the repository:**
   ```
   git clone https://github.com/vujicdejann/dockerized-python-calculator.git
   ```
2. **Navigate to the project directory:**
   ```
   cd dockerized-python-calculator
   ```

## Building the Docker Image
To build the Docker image for the calculator, run the following command in the project's root directory:
```
docker build -t calculator .
```

## Running the Calculator
To run the calculator, use the following command:
```
docker run calculator <operation> <number1> <number2> ...
```
Replace `<operation>` with `add`, `subtract`, `multiply`, or `divide` and follow with the numbers you wish to operate on.

### Examples
- To add numbers:
  ```
  docker run calculator add 1 2 3 4
  ```
- To multiply numbers:
  ```
  docker run calculator multiply 1 2 3 4
  ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

## Authors
- Dejan Vujić - Initial work

## Acknowledgments
- Thanks to all contributors who have helped in refining this project.

