from fastapi import HTTPException, status


def example(example: dict):
    try:
        # Create a response example dictionary
        response_example = {
            200: {  # HTTP status code for success
                "content": {
                    "application/json": {  # Content type for JSON response
                        "example": example,  # The example data passed as argument
                    }
                }
            }
        }
        # Return the response example dictionary
        return response_example

    except Exception as e:
        # Handle any exceptions that occur during execution
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
