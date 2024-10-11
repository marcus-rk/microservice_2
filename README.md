```bash
git clone https://github.com/marcus-rk/microservice_2.git
cd microservices_project
```
```bash
cd inventory_service
docker build -t inventory_service .
```
```bash
cd ../product_service
docker build -t product_service .
```
```bash
docker build -t currency-service https://github.com/Emythiel/ita23-3semester.git#main:micro-services/currency-service
```
```bash
docker network create microservice-network
```
```bash
docker run -d \                           
  --name currency-service \
  --network microservice-network \
  -p 5003:5000 \
  currency-service
```
```bash
docker run -d \                           
  -p 5002:5002 \           
  -e CURRENCY_SERVICE_URL=http://currency-service:5000 \
  --name product_service \
  --network microservice-network \
  product_service
```
```bash
docker run -d \                           
  -p 5001:5001 \           
  -e PRODUCT_SERVICE_URL=http://product_service:5002 \  
  --name inventory_service \
  --network microservice-network \
  inventory_service
```
