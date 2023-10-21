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
│   │   ├── server.py
│   │   ├── routes/
│   │   │   ├── routes.py  # 
│   │   │   ├── __init__.py
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
1. git clone git@github.com:mbgoodguy/binance_docker_fastapi_redis.git
2. 
