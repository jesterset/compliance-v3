from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Literal, Optional, Union
import os
# import uuid

# class Redis(BaseModel):
#     HOST: str = Field(default_factory=lambda: os.getenv('REDIS_HOST'))
#     PORT: str = Field(default_factory=lambda: os.getenv('REDIS_PORT'))
#     USERNAME: str = Field(default_factory=lambda: os.getenv('REDIS_USERNAME'))
#     PASSWORD: str = Field(default_factory=lambda: os.getenv('REDIS_PASSWORD'))
#     MAX_RETRIES_PER_REQUEST: str = Field(default_factory=lambda: os.getenv('REDIS_MAX_RETRIES_PER_REQUEST'))

# class Elastic(BaseModel):
#     HOST: str = Field(default_factory=lambda: os.getenv('ELASTIC_HOST'))
#     PORT: str = Field(default_factory=lambda: os.getenv('ELASTIC_PORT'))
#     AUTH: str = Field(default_factory=lambda: os.getenv('ELASTIC_AUTH'))
#     USERNAME: str = Field(default_factory=lambda: os.getenv('ELASTIC_USERNAME'))
#     PASSWORD: str = Field(default_factory=lambda: os.getenv('ELASTIC_PASSWORD'))
#     INDEX: str = Field(default_factory=lambda: os.getenv('ELASTIC_INDEX'))

# class Postgres(BaseModel):
#     HOST: str = Field(default_factory=lambda: os.getenv('POSTGRES_HOST'))
#     PORT: str = Field(default_factory=lambda: os.getenv('POSTGRES_PORT'))
#     USERNAME: str = Field(default_factory=lambda: os.getenv('POSTGRES_USERNAME'))
#     PASSWORD: str = Field(default_factory=lambda: os.getenv('POSTGRES_PASSWORD'))
#     DATABASE: str = Field(default_factory=lambda: os.getenv('POSTGRES_DATABASE'))
#     TABLE: str = Field(default_factory=lambda: os.getenv('POSTGRES_TABLE'))

# class S3(BaseModel):
#     BUCKET_NAME: str = Field(default_factory=lambda: os.getenv('S3_BUCKET_NAME'))
#     PREFIX: str = Field(default_factory=lambda: os.getenv('S3_PREFIX'))
#     ENDPOINT: str = Field(default_factory=lambda: os.getenv('S3_ENDPOINT'))
#     PATH: str = Field(default_factory=lambda: f"{os.getenv('S3_ENDPOINT')}/{os.getenv('S3_BUCKET_NAME')}/{os.getenv('S3_PREFIX')}")
#     ACCESS_KEY_ID: str = Field(default_factory=lambda: os.getenv('S3_ACCESS_KEY_ID'))
#     SECRET_ACCESS_KEY: str = Field(default_factory=lambda: os.getenv('S3_SECRET_ACCESS_KEY'))
#     REGION: str = Field(default_factory=lambda: os.getenv('S3_REGION'))

class App(BaseModel):
    CODE: str = Field(default_factory=lambda: os.getenv('APP_CODE'))
    NAME: str = Field(default_factory=lambda: os.getenv('APP_NAME'))
    OPERATION_MODE: dict = Field(default_factory=lambda: {
        "DEBUG": os.getenv('DEBUG') == 'true',
        "PROFILING": os.getenv('PROFILE') == 'true',
        "SAFETY": os.getenv('SAFETY') == 'true',
    })
    ENV: dict = Field(default_factory=lambda: {
        "NODE_ENV": os.getenv('NODE_ENV')
    })

# class Kafka(BaseModel):
#     PROCESS_ID: str = Field(default_factory=lambda: str(uuid.uuid4()))
#     BOOTSTRAP_SERVERS: str = Field(default_factory=lambda: os.getenv('KAFKA_BOOTSTRAP_SERVERS'))
#     BOOTSTRAP_SERVERS_PORT: str = Field(default_factory=lambda: os.getenv('KAFKA_BOOTSTRAP_SERVERS_PORT'))
#     GROUP_ID: str = Field(default_factory=lambda: f"{os.getenv('KAFKA_GROUP_ID')}_{os.getenv('APP_CODE')}_{str(uuid.uuid4())}")
#     AUTO_OFFSET_RESET: str = Field(default_factory=lambda: os.getenv('KAFKA_AUTO_OFFSET_RESET'))
#     ALLOW_AUTO_CREATE_TOPICS: str = Field(default_factory=lambda: os.getenv('KAFKA_ALLOW_AUTO_CREATE_TOPICS'))
#     SECURITY_PROTOCOL: Literal['sasl_ssl'] = Field(default_factory=lambda: os.getenv('KAFKA_SECURITY_PROTOCOL'))
#     SASL_MECHANISM: str = Field(default_factory=lambda: os.getenv('KAFKA_SASL_MECHANISM'))
#     SASL_USERNAME: str = Field(default_factory=lambda: os.getenv('KAFKA_SASL_USERNAME'))
#     SASL_PASSWORD: str = Field(default_factory=lambda: os.getenv('KAFKA_SASL_PASSWORD'))
#     SESSION_TIMEOUT: str = Field(default_factory=lambda: os.getenv('KAFKA_SESSION_TIMEOUT'))
#     DR_MSG_CB: bool = Field(default_factory=lambda: os.getenv('KAFKA_DR_MSG_CB') == 'true')
#     TOPIC: str = Field(default_factory=lambda: os.getenv('KAFKA_TOPIC', 'test'))

# class AiDAParser(BaseModel):
#     DEV: str = Field(default_factory=lambda: os.getenv('AIDA_PARSER_DEV'))
#     UAT: str = Field(default_factory=lambda: os.getenv('AIDA_PARSER_UAT'))
#     PROD: str = Field(default_factory=lambda: os.getenv('AIDA_PARSER_PROD'))

class Payload(BaseModel):
    MULTIPART: bool = True
    KEEP_EXTENSIONS: bool = False
    MAX_FILE_SIZE: int = 2000 * 1024 * 1024

class Default(BaseModel):
    FILE: dict = Field(default_factory=lambda: {
        "STATE_FILE": {
            "FOLDER_PATH": ".",
            "FILE_NAME": ".cache",
        },
        "CONTROLLER": {
            "FOLDER_PATH": "../api/controllers",
            "FILE_NAME": "controller.ts",
        }
    })
    QUEUE: dict = Field(default_factory=lambda: {
        "JOB": {
            "NAME": "nate-jobs",
        },
        "TAG": {
            "NAME": "nate",
        },
    })
    TOPIC: dict = Field(default_factory=lambda: {
        "NATE": {
            "NAME": "nate",
        },
    })

class HeaderOptions(BaseModel):
    CONTENT_TYPE: str = "content-type"
    ORIGIN: str = "origin"
    X_REGISTERED_WITH: str = "x-registered-with"
    ACCEPT: str = "accept"

class HashDigest(BaseModel):
    HEX: Literal['hex'] = 'hex'
    BASE64: Literal['base64'] = 'base64'
    BASE64URL: Literal['base64url'] = 'base64url'
    BINARY: Literal['binary'] = 'binary'

class OriginOptions(BaseModel):
    ALL: str = "*"

class HttpVerb(BaseModel):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    PATCH: str = "PATCH"
    DELETE: str = "DELETE"
    OPTIONS: str = "OPTIONS"
    HEAD: str = "HEAD"

class StorageOption(BaseModel):
    S3: str = "s3"
    POSTGRES: str = "postgres"
    ELASTIC: str = "elastic"
    REDIS: str = "redis"

class EventOption(BaseModel):
    KAFKA: str = "kafka"

class MessengerOption(BaseModel):
    BULLMQ: str = "bullmq"

# TODO: use httpx package in the future
class HttpResponseStatus(BaseModel):
    INFORMATIONAL: dict = Field(default_factory=lambda: {
        "CONTINUE": {"CODE": 100, "TAG": "Continue"},
        "SWITCHING_PROTOCOL": {"CODE": 101, "TAG": "Switching Protocols"},
        "PROCESSING": {"CODE": 102, "TAG": "Processing"},
        "EARLY_HINTS": {"CODE": 103, "TAG": "Early Hints"},
    })
    SUCCESS: dict = Field(default_factory=lambda: {
        "OK": {"CODE": 200, "TAG": "OK"},
        "CREATED": {"CODE": 201, "TAG": "Created"},
        "ACCEPTED": {"CODE": 202, "TAG": "Accepted"},
        "NON_AUTHORITATIVE_INFORMATION": {"CODE": 203, "TAG": "Non-Authoritative Information"},
        "NO_CONTENT": {"CODE": 204, "TAG": "No Content"},
        "RESET_CONTENT": {"CODE": 205, "TAG": "Reset Content"},
        "PARTIAL_CONTENT": {"CODE": 206, "TAG": "Partial Content"},
        "MULTI_STATUS": {"CODE": 207, "TAG": "Multi-Status"},
        "ALREADY_REPORTED": {"CODE": 208, "TAG": "Already Reported"},
        "IM_USED": {"CODE": 226, "TAG": "IM Used"},
    })
    REDIRECTION: dict = Field(default_factory=lambda: {
        "MULTIPLE_CHOICES": {"CODE": 300, "TAG": "Multiple Choices"},
        "MOVED_PERMANENTLY": {"CODE": 301, "TAG": "Moved Permanently"},
        "FOUND": {"CODE": 302, "TAG": "Found"},
        "SEE_OTHER": {"CODE": 303, "TAG": "See Other"},
        "NOT_MODIFIED": {"CODE": 304, "TAG": "Not Modified"},
        "TEMPORARY_REDIRECT": {"CODE": 307, "TAG": "Temporary Redirect"},
        "PERMANENT_REDIRECT": {"CODE": 308, "TAG": "Permanent Redirect"},
    })
    CLIENT_ERROR: dict = Field(default_factory=lambda: {
        "BAD_REQUEST": {"CODE": 400, "TAG": "Bad Request"},
        "UNAUTHORIZED": {"CODE": 401, "TAG": "Unauthorized"},
        "PAYMENT_REQUIRED": {"CODE": 402, "TAG": "Payment Required"},
        "FORBIDDEN": {"CODE": 403, "TAG": "Forbidden"},
        "NOT_FOUND": {"CODE": 404, "TAG": "Not Found"},
        "METHOD_NOT_ALLOWED": {"CODE": 405, "TAG": "Method Not Allowed"},
        "NOT_ACCEPTABLE": {"CODE": 406, "TAG": "Not Acceptable"},
        "PROXY_AUTHENTICATION_REQUIRED": {"CODE": 407, "TAG": "Proxy Authentication Required"},
        "REQUEST_TIMEOUT": {"CODE": 408, "TAG": "Request Timeout"},
        "CONFLICT": {"CODE": 409, "TAG": "Conflict"},
        "GONE": {"CODE": 410, "TAG": "Gone"},
        "LENGTH_REQUIRED": {"CODE": 411, "TAG": "Length Required"},
        "PRE_CONDITION_FAILED": {"CODE": 412, "TAG": "Precondition Failed"},
        "CONTENT_TOO_LARGE": {"CODE": 413, "TAG": "Content Too Large"},
        "URI_TOO_LONG": {"CODE": 414, "TAG": "URI Too Long"},
        "UNSUPPORTED_MEDIA_TYPE": {"CODE": 415, "TAG": "Unsupported Media Type"},
        "RANGE_NOT_SATISFIABLE": {"CODE": 416, "TAG": "Range Not Satisfiable"},
        "EXPECTATION_FAILED": {"CODE": 417, "TAG": "Expectation Failed"},
        "MISDIRECTED_REQUEST": {"CODE": 421, "TAG": "Misdirected Request"},
        "UNPROCESSABLE_CONTENT": {"CODE": 422, "TAG": "Unprocessable Content"},
        "LOCKED": {"CODE": 423, "TAG": "Locked"},
        "FAILED_DEPENDENCY": {"CODE": 424, "TAG": "Failed Dependency"},
        "TOO_EARLY": {"CODE": 425, "TAG": "Too Early"},
        "UPGRADE_REQUIRED": {"CODE": 426, "TAG": "Upgrade Required"},
        "PRECONDITION_REQUIRED": {"CODE": 428, "TAG": "Precondition Required"},
        "TOO_MANY_REQUESTS": {"CODE": 429, "TAG": "Too Many Requests"},
        "REQUEST_HEADER_FIELDS_TOO_LARGE": {"CODE": 431, "TAG": "Request Header Fields Too Large"},
        "UNAVAILABLE_FOR_LEGAL_REASONS": {"CODE": 451, "TAG": "Unavailable for Legal Reasons"},
    })
    SERVER_ERROR: dict = Field(default_factory=lambda: {
        "INTERNAL_SERVER_ERROR": {"CODE": 500, "TAG": "Internal Server Error"},
        "NOT_IMPLEMENTED": {"CODE": 501, "TAG": "Not Implemented"},
        "BAD_GATEWAY": {"CODE": 502, "TAG": "Bad Gateway"},
        "SERVICE_UNAVAILABLE": {"CODE": 503, "TAG": "Service Unavailable"},
        "GATEWAY_TIMEOUT": {"CODE": 504, "TAG": "Gateway Timeout"},
        "HTTP_VERSION_NOT_SUPPORTED": {"CODE": 505, "TAG": "HTTP Version Not Supported"},
        "VARIANT_ALSO_NEGOTIATES": {"CODE": 506, "TAG": "Variant Also Negotiates"},
        "INSUFFICIENT_STORAGE": {"CODE": 507, "TAG": "Insufficient Storage"},
        "LOOP_DETECTED": {"CODE": 508, "TAG": "Loop Detected"},
        "NETWORK_AUTHENTICATION_REQUIRED": {"CODE": 511, "TAG": "Network Authentication Required"},
    })

class labeler(BaseModel):
    INFERENCE: dict = Field(default_factory=lambda: {
        "RESULT_KEY": {
            "RESULT": "crawler_results",
            "NOT_FOUND": "not_found",
            "NOT_FOUND_COUNT": "not_found_count",
            "FOUND": "found",
            "FOUND_COUNT": "found_count",
            "EXECUTION_TIME": "execution_time",
        }
    })


# Define constants using Enum and Literal
class FileType(str, Enum):
    HTML = '.html'
    HTM = '.htm'
    XML = '.xml'

class FileEncoding(str, Enum):
    UTF8 = 'utf8'

class HTMLTag(str, Enum):
    ANCHOR = 'a'

class HashAlgorithmType(str, Enum):
    SHA256 = 'sha256'

class MIMEType(str, Enum):
    TEXT_HTML = 'text/html'
    APPLICATION_XML = 'application/xml'
    APPLICATION_JSON = 'application/json'

# Define Pydantic models
class URLMetadata(BaseModel):
    url: str
    lastModified: str
    lastCrawled: str
    hash: str

class PageMetadata(BaseModel):
    content: str

CrawlerResult = Union[URLMetadata, PageMetadata]

class CrawlerState(BaseModel):
    lastCrawledURL: Optional[str] = None

class CrawlerAPIResult(BaseModel):
    result: Dict[str, Union[CrawlerResult, List[Dict[str, Any]]]]

class FetchResult(BaseModel):
    result: Dict[str, Union[str, Dict[str, Any]]]

class CrawlerOptions(BaseModel):
    storagePaths: Optional[List[str]] = None
    politenessDelay: Optional[int] = None

class SitemapURL(BaseModel):
    loc: str
    lastmod: Optional[str] = None
    changefreq: Optional[str] = None
    priority: Optional[str] = None

class CrawlerRequest(BaseModel):
    urls: List[str]

class JobStateResult(BaseModel):
    jobObj: Optional[str] = None # Job
    jobId: Optional[str] = None
    state: Optional[str] = None
    progress: Union[int, Dict[str, Any]]

# Instantiate the urations
# redis = Redis()
# elastic = Elastic()
# postgres = Postgres()
# s3 = S3()
# app = App()
# kafka = Kafka()
# aida_parser = AiDAParser()
# payload = Payload()
# default = Default()
# header_options = HeaderOptions()
# hash_digest = HashDigest()
# origin_options = OriginOptions()
# http_verb = HttpVerb()
# storage_option = StorageOption()
# event_option = EventOption()
# messenger_option = MessengerOption()
# http_response_status = HttpResponseStatus()
# crawler = Crawler()