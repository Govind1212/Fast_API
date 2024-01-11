# FastAPI Login process implementing OAuth

This fastapi application demonstrates user authentication using OAuth2 bearer with JWT token. These app contains 4 api
/users	            : Create new user account
/auth/token	        : Create JWT Token
/auth/refresh-token	: Refresh JWT Token
/users/me	          : Get Authenticated User Detail

## To Replicate this in your system
### Clone the repository:
```>git clone https://github.com/Govind1212/Fast_API.git```

### Create Virtual Environment
```>python -m venv venv```

### Activate Virtual Environment
```>cd venv/Scripts```

```>activate.bat```

### Install Requirements
```>cd ../..```

```>pip install -r requirements.txt```

### Database Connectivity
In MySQL Workbench, create a schema named fast_api. Create a table named users in the schema
use following queries after creating schema
```
use fast_api;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(255) UNIQUE,
  password VARCHAR(100)
);

```
### Run the server for app
```>uvicorn main:app --reload```

### Docker Contarization
```docker compose up --build```
