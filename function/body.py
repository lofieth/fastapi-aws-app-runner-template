from fastapi import HTTPException, status
from fastapi import Body as body


def Body(default=None):
    try:
        # Add embed=True to the HTTP body to interpret
        # a single body parameter as a JSON field by default
        return body(default, embed=True)

    except Exception as e:
        # Handle any exceptions that occur during execution
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
