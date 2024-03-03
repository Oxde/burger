import time
from hotdog_oxde import check_website_status

def main():
    # Replace 'website_url' with the URL of the website you want to check
    website_url = 'https://www.example.com'

    # Check website status
    start_time = time.time()
    status_code = check_website_status(website_url)
    end_time = time.time()

    if status_code is not None:
        print(f"Status code of {website_url}: {status_code}")
    else:
        print("Failed to retrieve website status.")

    # Calculate ping time
    ping_time = end_time - start_time
    print(f"Ping time for {website_url}: {ping_time:.2f} seconds")


if __name__ == "__main__":
    main()
