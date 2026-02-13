from fastapi import HTTPException, status


def database(filter):
    try:
        # Check if the filter matches "hello_world"
        if filter == "world":
            # Return "hello_world" if the filter matches
            return "world"
        # Return None if the filter does not match
        return None

    except Exception as e:
        # Handle any exceptions that occur during execution
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}",
        )
