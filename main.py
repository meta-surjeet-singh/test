import uvicorn
# from config.constant import HOST, PORT
from fastapi import FastAPI
# from routes.index import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI

app = FastAPI()
@app.post("/test-API")
async def test():
    return {"msg":"tesing API"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start_server():
    uvicorn.run(
        'main:app',
        port=8000,
        host='localhost',
        log_level="debug",
        timeout_keep_alive=600, # Set the timeout keep-alive to 600 seconds (10 minutes)
        reload=True,
    )

if __name__ == "__main__":
    start_server()


@app.get("/") 
async def read_root():
    return {"Hello": "World"}
