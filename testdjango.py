import requests
import concurrent.futures

# Function to send a test request
def send_test_request():
    try:
        response = requests.get('http://13.48.26.31:8000/')
        if response.status_code == 200:
            print("Request successful, status code 200")
        elif response.status_code == 500:
            print("Server error, status code 500")
        else:
            print(f"Request failed, status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Main script
if __name__ == "__main__":
    # Number of concurrent threads
    num_threads = 10000

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_test_request) for _ in range(num_threads)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")