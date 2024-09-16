import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL', 'https://elastic:NF7Ne7F691OSKwJNcGDNLQjw@04ae44a42e8e437abd819f24a3cd1015.eastus2.azure.elastic-cloud.com:443')
    POSTGRES_URL = os.getenv('POSTGRES_URL', 'postgresql://postgres.ecaazettexwdvahwhaen:zG9Dtbm0xuL5xmm4@aws-0-ca-central-1.pooler.supabase.com:6543/postgres')