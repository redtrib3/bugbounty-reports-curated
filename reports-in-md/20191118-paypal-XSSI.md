# The Bug That Exposed Your PayPal Password

**Target**: Paypal

**Reported on**: hackerone

**Bug Type**: XSSI

**Severity**: High

**Report URL**: https://medium.com/@alex.birsan/the-bug-that-exposed-your-paypal-password-539fc2896da9

## Summary
The researcher discovered that after multiple failed login attempts on PayPal, users were shown a CAPTCHA challenge. Once the CAPTCHA was solved, the server responded with a self-submitting HTML form that included the user’s email address and password in plaintext.
This form could be triggered in the victim’s browser and captured by an attacker using a specially crafted webpage, as PayPal also leaked CSRF and session tokens via a JavaScript file. By chaining these two issues, the attacker could remotely extract login credentials without direct interaction from the victim.
In some checkout flows, a similar behavior led to the exposure of full credit card details in plaintext, which made the impact even more severe.
This vulnerability existed due to improper handling of authentication flow, poor token isolation, and echoing sensitive user data back to the client-side.

_This summary was partially generated using AI_

## Bounty received ($)
15300

## References
- https://medium.com/@alex.birsan/the-bug-that-exposed-your-paypal-password-539fc2896da9
## Tags
- XSSI
- CSRF
- brute-force
- security-challenge
- captcha-bypass
