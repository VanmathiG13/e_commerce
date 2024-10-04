# solr_test.py
from solr_client import solr_search

def test_solr_search():
    # Call the solr_search function with a test query
    query = "laptop"  # Replace with your test query
    results = solr_search(query)

    # Check if the results are what you expect
    print(f"Test Results: {results}")

if __name__ == "__main__":
    test_solr_search()

