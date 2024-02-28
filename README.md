Little app for getting currencies pairs from binance.com

Project Structure:
```
├── README.md
├── docker-compose.yaml
├── docker/
│   ├── api/
│   │   ├── Dockerfile
│   ├── redis/
│   │   ├── Dockerfile
├── .env  # environment variables
├── .gitignore
├── app/
│   ├── package/  # interaction with other services, not fastapi
│   │   ├── redis_tools/
│   │   │   ├── tools.py  # set interaction with redis
│   │   │   ├── __init__.py
│   ├── configuration/
│   │   ├── server.py  # creating and configuring a FastAPI application
│   │   ├── routes/
│   │   │   ├── routes.py  # manage the registration of routers (Routes class)
│   │   │   ├── __init__.py  # initialize __routes__ for access to router
│   ├── routes/
│   │   ├── __init__.py
│   ├── internal/  # interaction with fastapi
│   │   ├── events/
│   │   │   ├── startup.py  # async defs for receiving data from the exchange
│   │   ├── schemas/
│   │   │   ├── currency.py  # currency parse classes
│   │   ├── routes/
│   │   │   ├── currency.py  # currency pair getting logic
│   ├── __init__.py  # FastAPI app creating
```
Commands to run app:
1. ```git clone git@github.com:mbgoodguy/binance_docker_fastapi_redis.git```
2. ```cd binance_docker_fastapi_redis```
3. ```docker-compose build```
4. ```docker-compose up -d```

Now u can run postman and send GET response to http://127.0.0.1:8000/api/v1/currency/<VALUE_OF_SUMBOL_KEY_FROM_LIST_OF_CURRENCIES>

https://api.binance.com/api/v3/ticker/price - full list of currencies. U can get value of 'symbol' key from it and insert it in postman after /currency/

Examples of URLS for postman:
http://127.0.0.1:8000/api/v1/currency/LTCBTC
http://127.0.0.1:8000/api/v1/currency/ETHBTC
