
## Installation

1. Clone dette repository:

```
   git clone https://github.com/NikoKiru/product_service
   cd product_service
   docker build -t product_service .
   docker run -it --rm -p 5000:5000 -v ${PWD}:/home/data product_service
```

## API Endpoints

### FIND ALLE PRODUCTER

- **URL:** `/products`
- **Method:** `GET`
- **Request Body:** JSON

- **Response:**

  - **200** Products was returned

### Search Product by Title

- **URL:** `/product/search/<string:title>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns product by title