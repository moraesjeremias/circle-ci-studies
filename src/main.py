import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/circle_ci')
def hello_circle_ci():
    return JSONResponse({'message': 'hello_circle_ci'})


if __name__ == '__main__':
    uvicorn.run("src.main:app",
                port=os.getenv('PORT', 8080),
                debug=True
                )
