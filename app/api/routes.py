# app/api/routes.py
from app.models.messages import RealTimeMessageRequest, RealTimeMessageResponse
from app.services.batch_service import BatchService
from app.services.message_service import MessageService

class RealTimeMessagesResource:
    async def on_post(self, req, resp):
        data = await req.media
        payload = RealTimeMessageRequest(**data)

        result = await MessageService.process_realtime_message(payload.user_message)
        print(result)

        response = RealTimeMessageResponse(
            user_message=payload.user_message,
            document_uploaded=payload.document_uploaded,
            match_count=len(result['matches']),
            matches=result['matches'],
            rules=result['rules']
        )
        resp.media = response.model_dump()

class BatchMessagesResource:
    async def on_get(self, req, resp):
        print("Batch processing started")
        result = await BatchService.process_batch()
        resp.media = {
            "message": "Batch processing completed successfully",
            "processed_count": len(result)
        }

# Route registration
def register_routes(app):
    app.add_route('/chat/messages/realtime', RealTimeMessagesResource())
    app.add_route('/chat/messages/batch', BatchMessagesResource())
