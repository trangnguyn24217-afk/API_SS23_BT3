import logging
import time
import uuid

logger = logging.getLogger("secure_learning_api")


def register_request_middleware(app):
    @app.middleware("http")
    async def request_middleware(request, call_next):
        request_id = str(uuid.uuid4())
        started = time.perf_counter()

        response = await call_next(request)

        process_time = time.perf_counter() - started
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = f"{process_time:.6f}"

        logger.info(
            "%s %s %s %.6f %s",
            request_id,
            request.method,
            request.url.path,
            response.status_code,
            process_time,
        )

        return response
