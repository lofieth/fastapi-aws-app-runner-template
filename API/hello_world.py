from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from database.database import database
import os


async def hello_world(text):
    try:
        # Accessing an environment variable in Python
        hello = os.getenv("hello")
        # Concatenate "hello_world " with the provided text and store it in the database
        world = database("world")

        # Return a JSON response with the result
        return JSONResponse({"message": hello + " " + world + " " + text})

    except Exception as e:
        # Handle any exceptions that occur during execution
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
