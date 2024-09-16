import falcon
import logging
from datetime import datetime
from app.models.messages import RealTimeMessageRequest, BatchMessageResponse, RealTimeMessageResponse
from app.services.batch_service import BatchService
from app.services.message_service import MessageService
from app.utils.file_utils import save_to_csv

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class RealTimeMessagesResource:
    """
    Represents a resource for handling real-time messages.

    Methods:
    - on_post: Handles the POST request for real-time messages.

    Handles the POST request for real-time messages.

    Parameters:
    - req: The request object.
    - resp: The response object.
    """
    async def on_post(self, req, resp):
        """
        Handle POST requests.

        Parameters:
        - req: The request object.
        - resp: The response object.

        Returns:
        None
        """
        data = await req.media
        payload = RealTimeMessageRequest(**data)
        result = await MessageService.process_realtime_message(payload.user_message)
        try:
            response = RealTimeMessageResponse(
                emp_id=payload.emp_id,
                user_message=payload.user_message,
                document_uploaded=payload.document_uploaded,
                violation_timestamp= datetime.now(tz=None).isoformat(timespec='seconds'),
                match_count=len(result['matches']),
                **result
            ).to_custom_dict()
            resp.media = response
        except Exception as e:
            logger.error(f"Error processing response: {e}")
            resp.status = falcon.HTTP_500
            resp.media = {
                "title": "500 Internal Server Error",
                "description": str(e)
            }

class BatchMessagesResource:
    """
    Represents a resource for batch messages.

    Methods:
    - on_get: Handles the GET request for batch messages.

    Handles the GET request for batch messages.

    Parameters:
    - req: The request object.
    - resp: The response object.
    """
    async def on_get(self, req, resp):
        """
        Handle GET requests.

        Parameters:
        - req: The request object.
        - resp: The response object.

        Returns:
        None

        Description:
        This method is responsible for handling GET requests. It starts batch processing, retrieves the results,
        converts them to a custom dictionary format, and saves them to a CSV file.
        """
        print("Batch processing started")
        results = await BatchService.process_batch_messages()

        for i, result in enumerate(results):
            results[i] = BatchMessageResponse(**result).to_custom_dict()

        resp.media = await save_to_csv(results)

def register_routes(app):
    app.add_route('/chat/messages/realtime', RealTimeMessagesResource())
    app.add_route('/chat/messages/batch', BatchMessagesResource())
