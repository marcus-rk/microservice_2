# Microservices Project

This project demonstrates a microservices-based architecture using Flask and Docker. It consists of three microservices: 
- **Inventory Service**: Manages product inventory.
- **Product Service**: Provides product details and communicates with the currency service.
- **Currency Service**: Converts prices between different currencies using real-time exchange rates.

The services are containerized using Docker and communicate with each other over a custom Docker network.

## Prerequisites

To run this project, you need to have the following installed:
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

## Getting Started

Follow these steps to clone, build, and run the microservices:

### 1. Clone the Repository
Use your prefered terminal and clone the repo using git
```bash
git clone https://github.com/marcus-rk/microservice_2.git
cd microservice_2
```

### 2. Build the Docker Images
Use your prefered terminal and run these commands
```bash
# Build currency_service
cd microservice/currency_service
docker build -t currency_service .

# Build product_service
cd ../product_service
docker build -t product_service .

# Build inventory_service
cd ../inventory_service
docker build -t inventory_service .

# Build api_gateway
cd ../api_gateway
docker build -t api_gateway .
```

### 3. Create a Docker Network
The services will communicate over a custom Docker network called microservice-network. Use this command in terminal:
```bash
docker network create microservice-network
```
You can check your networks using this command in the terminal:
```bash
docker network ls
```

### 4. Run the Docker Containers
Run each service in a Docker container and connect them to the microservice-network.
```bash
# Run currency_service
docker run -d \
  --name currency_service \
  --network microservice-network \
  -p 5003:5003 \
  currency_service

# Run product_service
docker run -d \
  -p 5002:5002 \
  -e CURRENCY_SERVICE_URL=http://currency_service:5003 \
  --name product_service \
  --network microservice-network \
  product_service

# Run inventory_service
docker run -d \
  -p 5001:5001 \
  -e PRODUCT_SERVICE_URL=http://product_service:5002 \
  --name inventory_service \
  --network microservice-network \
  inventory_service

# Run api_gateway
docker run -d \
  --name api_gateway \
  --network microservice-network \
  -p 5004:5004 \
  api_gateway
```

### 5. Verify Running Containers
You can verify that all services are running with the following command:
```bash
docker ps
```
or check in Docker Desktop under the containers section

---

## API Endpoints

### Currency Service
| Method | Endpoint                           | Description                                             |
|--------|-------------------------------------|---------------------------------------------------------|
| GET    | `/currency/<currency>/<price>`      | Converts a price from USD to the given currency.         |

#### Example:
```bash
GET http://localhost:5003/currency/EUR/100
```

#### Response:
```json
{
  "currency": 92.35
}
```

### Product Service
| Method | Endpoint                           | Description                                             |
|--------|-------------------------------------|---------------------------------------------------------|
| GET    | `/product/<id>`      | Fetches product details and its price in a specified currency.         |

### Inventory Service
| Method | Endpoint                           | Description                                             |
|--------|-------------------------------------|---------------------------------------------------------|
| GET    | `/inventory/<product_id>`      | Retrieves inventory details for a given product.         |

---
## Testing the Microservices with Postman
Once the services are running, you can use **Postman** or **curl** to interact with the APIs.
### Example Test Flow
1. Currency Conversion: Test the currency_service by converting USD to another currency (e.g., EUR).
```bash
GET http://localhost:5003/currency/EUR/100
```
Expected response:
```json
{
  "currency": 92.35
}
```
2. Product Service: The product_service interacts with the currency_service to return product details with price conversions.
```bash
GET http://localhost:5002/product/121
```
3. Inventory Service: The inventory_service interacts with the product_service to retrieve product details, including stock availability.
```bash
GET http://localhost:5001/inventory/121
```
