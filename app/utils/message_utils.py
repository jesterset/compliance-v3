from app.core.elastic import ElasticClient

async def get_matched_terms(index, user_message):
        elastic_results = await ElasticClient.search_terms(index, user_message)
        matched_terms = [{**hit['_source'],'score': hit['_score']} for hit in elastic_results['hits']['hits']]
        return matched_terms