import json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, status, Response
import time
from loggers.logconfig import formatter, handler
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(
            f"-------------Middleware code to claculate time received!------------------")
        start_time = time.time()
        response = await call_next(request)
        try:
            total_time = time.time() - start_time
            response.headers["X-time-taken"] = str(total_time)
            logger.info(
                f"Response took {str(total_time)}secs to respond. Added in the response header")
            logger.info(
                f"-------------Middleware code to claculate time Finished!------------------")
            return response
        except RuntimeError as exc:
            if str(exc) == 'No response returned.' and await request.is_disconnected():
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            raise
