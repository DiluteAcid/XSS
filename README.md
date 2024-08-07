# XSS Vulnerability Testing Project

## Overview

This project demonstrates the process of identifying and exploiting Cross-Site Scripting (XSS) vulnerabilities in web applications. It uses the Damn Vulnerable Web Application (DVWA) as a testing environment to explore different types of XSS attacks, including reflected, stored, and DOM-based XSS.

## Prerequisites

- Kali Linux (or any Linux distribution with necessary tools)
- DVWA installed and configured
- Basic understanding of HTML, JavaScript, and web application security

## Setup

1. Install and configure DVWA:

   ```
   sudo apt install dvwa
   ```

2. Start necessary services:

   ```
   sudo service apache2 start
   sudo service mysql start
   ```

3. Configure DVWA database and settings (refer to DVWA documentation for detailed steps)

4. Set DVWA security level to low for testing purposes

## XSS Testing Procedures

### 1. Reflected XSS Testing

- Navigate to the Reflected XSS page in DVWA
- Test basic payload: `<script>alert('Reflected XSS')</script>`
- Analyze response and page source

### 2. Stored XSS Testing

- Navigate to the Stored XSS page
- Input payload: `<script>alert('Stored XSS')</script>`
- Verify persistence of the attack

### 3. DOM-based XSS Testing

- Navigate to the DOM XSS page
- Modify URL parameter: `default=<script>alert('DOM XSS')</script>`
- Analyze page source and JavaScript code

## Vulnerability Analysis

Identified vulnerable code in DOM-based XSS:

```html
<script>
    if (document.location.href.indexOf("default=") >= 0) {
        var lang = document.location.href.substring(document.location.href.indexOf("default=")+8);
        document.write("<option value='" + lang + "'>" + decodeURI(lang) + "</option>");
        // ... (rest of the code)
    }
</script>
```

This code is vulnerable due to unsanitized user input being directly inserted into the DOM.

## Mitigation Strategies

- Implement proper input validation and sanitization
- Use Content Security Policy (CSP) headers
- Apply output encoding
- Utilize secure JavaScript functions for DOM manipulation

## Ethical Considerations

This project is for educational purposes only. Always obtain proper authorization before testing for vulnerabilities on any system you do not own.

## License

This project is open source and available under the [MIT License](LICENSE).


