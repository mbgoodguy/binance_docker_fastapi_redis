Project Structure:
├── README.md
├── docker-compose.yaml
├── docker/
│   ├── api/
│   │   ├── Dockerfile
│   ├── redis/
│   │   ├── Dockerfile
├── .env
├── .gitignore
├── tree.py
├── app/
│   ├── package/
│   │   ├── redis_tools/
│   │   │   ├── tools.py
│   │   │   ├── __init__.py
│   ├── configuration/
│   │   ├── server.py
│   │   ├── routes/
│   │   │   ├── routes.py
│   │   │   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   ├── internal/
│   │   ├── events/
│   │   │   ├── startup.py
│   │   ├── schemas/
│   │   │   ├── currency.py
│   │   ├── routes/
│   │   │   ├── user.py
│   │   │   ├── currency.py
│   ├── __init__.py

Commands to run app:
1. git clone git@github.com:mbgoodguy/binance_docker_fastapi_redis.git
2. 
