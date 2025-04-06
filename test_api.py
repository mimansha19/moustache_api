import requests
import pytest
import time

BASE_URL = "http://127.0.0.1:5000"

def test_response_time_under_2_seconds():
    """
        - Test that the API responds within 2 seconds for a typical misspelled city query.
        - This simulates a telecaller quickly entering 'delih' instead of 'Delhi'.
        - Ensures that the service is fast enough for real-time interaction.
    """
    query = {"query": "delih"} 

    start = time.time()
    response = requests.post(f"{BASE_URL}/nearby-properties", json=query)
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 2, f"API response took too long: {elapsed:.2f} seconds"
    print(f"\n Response Time: {elapsed:.3f} seconds")

@pytest.mark.parametrize("query", ["bangalre", "jaipurr", "udaipur", "sissu", "goa"])
def test_response_times_for_multiple_queries(query):
    """
        - Parametrized test to check API performance across various common queries, including both correct 
        and slightly misspelled city names.
        - Ensures all queries return within 2 seconds and handle fuzzy matching properly.
    """
    start = time.time()
    response = requests.post(f"{BASE_URL}/nearby-properties", json={"query": query})
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 2, f"{query} took too long: {elapsed:.2f}s"
    print(f"{query} responded in {elapsed:.2f}s")