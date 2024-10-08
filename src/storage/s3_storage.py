from pydantic import BaseModel
from typing import Dict, Any
import logging
from app.models.messages import RealTimeMessageResponse
import boto3
from botocore.exceptions import ClientError
from api.service.storage_service import StorageService
from common.constants import CRAWLER, S3, MIMEType

from common.config import get_config
from common.constants import URLMetadata

class S3StorageService(StorageService):
    _config = None

    def __init__(self):
        self._config = get_config()
        self.s3_client = boto3.client(
            's3',
            region_name=self._config.s3.region,
            endpoint_url=self._config.s3.endpoint,
            aws_access_key_id=self._config.s3.access_key_id,
            aws_secret_access_key=self._config.s3.secret_access_key
        )

    async def write(self, index: str, objs: RealTimeMessageResponse) -> None:
        for obj in objs.result.values():
            s3_key = f"{index}/{obj.url.replace('/', '_')}"
            s3_put_obj = {
                'Body': obj.json(),
                'Bucket': self._config.s3.bucket_name,
                'Key': s3_key,
                'ContentType': MIMEType.TEXT_HTML,
            }

            try:
                self.s3_client.put_object(**s3_put_obj)
                logging.info(f"Uploaded {obj.url} to S3 at {S3['BUCKET_NAME']}/{s3_key}")
            except ClientError as error:
                logging.error(f"Error uploading to S3 at {S3['BUCKET_NAME']}/{s3_key}: {error}")