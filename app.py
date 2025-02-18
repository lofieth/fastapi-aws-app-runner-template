from fastapi.middleware.cors import CORSMiddleware
from API.hello_world import hello_world
from function.body import Body
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Add webapp url here
        # TODO adjust origin list before production
        "http://localhost",
        "https://localhost",
        "http://localhost:8080",
        "https://localhost:8080",
        "http://localhost:3000",
        "https://localhost:3000",
        "http://localhost:8000",
        "https://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(path="/")
async def hello_world_endpoint(
    text: str = Body(),
):
    return await hello_world(text)


if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        api,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        debug=os.getenv("DEBUG", False),
        log_level=os.getenv('LOG_LEVEL', "info"),
        proxy_headers=True
    )
