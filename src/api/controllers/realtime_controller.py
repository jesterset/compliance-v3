# from pydantic import BaseModel, Field, ValidationError
# from typing import List, Dict, Any
# import falcon
# from falcon.asgi import App
# from handlers.storage_handler import StorageService
# from storage.s3_storage import StorageS3Service
# from web_crawler import WebCrawler
# from common.constants import HEADER_OPTIONS, MIMEType, HTTP_RESPONSE_STATUS, STORAGE_OPTION, S3, CRAWLER, POLITENESS_DELAY

# Pydantic models
class LabelRequest(BaseModel):
    urls: List[str]

class CrawlerAPIResult(BaseModel):
    found: List[str]
    not_found: List[str]

# # Falcon resource
# class InferenceController:
#     def __init__(self):
#         self.storage_service = StorageService()
#         self.storage_service.register_storage_service(STORAGE_OPTION["S3"], StorageS3Service)

#     async def on_post(self, req: falcon.Request, resp: falcon.Response):
#         if req.get_header(HEADER_OPTIONS["CONTENT_TYPE"]) != MIMEType["APPLICATION_JSON"]:
#             resp.status = falcon.HTTP_415
#             resp.media = {"error": HTTP_RESPONSE_STATUS["CLIENT_ERROR"]["UNSUPPORTED_MEDIA_TYPE"]["TAG"]}
#             return

#         try:
#             body = await req.media
#             crawler_request = CrawlerRequest(**body)
#         except (ValidationError, KeyError):
#             resp.status = falcon.HTTP_400
#             resp.media = {"error": HTTP_RESPONSE_STATUS["CLIENT_ERROR"]["BAD_REQUEST"]["TAG"]}
#             return

#         try:
#             crawler_options = {"politenessDelay": POLITENESS_DELAY}
#             web_crawler = WebCrawler(crawler_options)
#             results = await web_crawler.start_crawling_html_urls(crawler_request.urls)

#             await self.storage_service.write(STORAGE_OPTION["S3"], S3["PREFIX"], results)

#             resp.status = falcon.HTTP_200
#             resp.media = {
#                 "note": "Crawling and Uploading to S3 complete.",
#                 "s3": S3["PATH"],
#                 "crawled": {
#                     "count": len(results[CRAWLER["INFERENCE"]["RESULT_KEY"]["FOUND"]]),
#                     "urls": results[CRAWLER["INFERENCE"]["RESULT_KEY"]["FOUND"]],
#                 },
#                 "notCrawled": {
#                     "count": len(results[CRAWLER["INFERENCE"]["RESULT_KEY"]["NOT_FOUND"]]),
#                     "urls": results[CRAWLER["INFERENCE"]["RESULT_KEY"]["NOT_FOUND"]],
#                 },
#             }
#         except Exception as e:
#             resp.status = falcon.HTTP_500
#             resp.media = {"error": "An error occurred while starting the crawl"}
#             print(e)

from pydantic import BaseModel, Field, ValidationError
from typing import List, Dict, Any
import falcon
from falcon.asgi import App
from app.core.config import get_config
from handlers.storage_handler import StorageHandler
from storage.s3_storage import S3StorageService
from storage.postgres_storage import PostgresStorageService
from storage.elastic_storage import ElasticStorageService

from api.base import BaseController
from common.constants import header_options, mime_type, http_response_status, storage_option, s3, labeler, politeness_delay
from models.request import RealTimeMessageRequest
from models.response import RealTimeMessageResponse





# Falcon resource
class RealnameController(BaseController):
    def __init__(self):
        self._config = get_config()
        self.storage_service = StorageHandler()
        self.storage_service.register_storage_service(storage_option.S3, S3StorageService)
        self.storage_service.register_storage_service(storage_option.POSTGRES, PostgresStorageService)
        self.storage_service.register_storage_service(storage_option.ELASTIC, ElasticStorageService)


    def set_router(self, app: App):
        app.add_route('/inference', self)

    async def on_post(self, req: falcon.Request, resp: falcon.Response):
        if req.get_header(header_options.CONTENT_TYPE) != mime_type.APPLICATION_JSON:
            resp.status = falcon.HTTP_415
            resp.media = {"error": http_response_status.CLIENT_ERROR["UNSUPPORTED_MEDIA_TYPE"]["TAG"]}
            return

        try:
            body = await req.media
            label_request = LabelRequest(**body)
        except (ValidationError, KeyError):
            resp.status = falcon.HTTP_400
            resp.media = {"error": http_response_status.CLIENT_ERROR["BAD_REQUEST"]["TAG"]}
            return

        try:
            results = await self.parser_handler.parse(body, "realtime")

            await self.storage_service.write(storage_option.S3, s3, results)

            resp.status = falcon.HTTP_200
            resp.media = {
                "note": "Crawling and Uploading to S3 complete.",
                "s3": self._config.s3.path,
                "crawled": {
                    "count": len(results[labeler["INFERENCE"]["RESULT_KEY"]["FOUND"]]),
                    "urls": results[labeler["INFERENCE"]["RESULT_KEY"]["FOUND"]],
                },
                "notCrawled": {
                    "count": len(results[labeler["INFERENCE"]["RESULT_KEY"]["NOT_FOUND"]]),
                    "urls": results[labeler["INFERENCE"]["RESULT_KEY"]["NOT_FOUND"]],
                },
            }
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "An error occurred while starting the crawl"}
            print(e)