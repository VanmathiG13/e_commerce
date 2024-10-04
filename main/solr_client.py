# from pysolr import Solr

# # Assuming you have a Solr instance running and accessible
# SOLR_URL = 'http://localhost:8983/solr/newproducts'
# solr = Solr(SOLR_URL)

# def solr_search(query, filters=None):
#     # Construct the Solr query
#     solr_query = query

#     # Add filters if provided
#     if filters:
#         filter_query = ' AND '.join(filters)
#         solr_query += f' AND {filter_query}'  # Combine query and filters

#     # Print the query for debugging
#     print(f'Solr Query: {solr_query}')

#     # Perform the search
#     results = solr.search(solr_query)
    
#     # Convert results to a list of dictionaries (or any format you need)
#     return [result for result in results]
from pysolr import Solr

# Assuming you have a Solr instance running and accessible
SOLR_URL = 'http://localhost:8983/solr/newproducts'
solr = Solr(SOLR_URL)

def solr_search(query, min_price=None, max_price=None):
    # Tokenize the query into individual words (tokens)
    keywords = query.split()

    # Build Solr query for matching product name or description
    solr_query = ' OR '.join([f'product_name:*{keyword}* OR description:*{keyword}*' for keyword in keywords])

    # Add price filters if provided
    filters = []
    if min_price is not None:
        filters.append(f'discounted_price:[{min_price} TO *]')
    if max_price is not None:
        filters.append(f'discounted_price:[* TO {max_price}]')

    # Combine query and filters
    filter_query = ' AND '.join(filters)
    if filter_query:
        solr_query += f' AND {filter_query}'

    # Print the final Solr query for debugging
    print(f'Solr Query: {solr_query}')

    # Perform the search
    results = solr.search(solr_query)
    
    # Convert results to a list of dictionaries (or any format you need)
    return [result for result in results]
