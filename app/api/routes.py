import falcon
import logging
from app.models.messages import RealTimeMessageRequest, BatchMessageResponse, RealTimeMessageResponse
from app.services.batch_service import BatchService
from app.services.message_service import MessageService
from app.utils.file_utils import save_to_csv

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class RealTimeMessagesResource:
    async def on_post(self, req, resp):
        data = await req.media
        payload = RealTimeMessageRequest(**data)
        result = await MessageService.process_realtime_message(payload.user_message)
        try:
            response = RealTimeMessageResponse(
                user_message=payload.user_message,
                document_uploaded=payload.document_uploaded,
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
    async def on_get(self, req, resp):
        print("Batch processing started")
        results = await BatchService.process_batch_messages()

        for i, result in enumerate(results):
            results[i] = BatchMessageResponse(**result).to_custom_dict()

        resp.media = await save_to_csv(results)

def register_routes(app):
    app.add_route('/chat/messages/realtime', RealTimeMessagesResource())
    app.add_route('/chat/messages/batch', BatchMessagesResource())
