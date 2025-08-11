# No CSRF token present in Customer service message form.

**Target**: Paypal

**Reported on**: Bugcrowd

**Bug Type**: CSRF

**Severity**: Medium

**Report URL**: https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/

## Summary
A CSRF vulnerability exists in PayPal’s “Customer Service Message” form, which allows sellers to configure a personalized message
shown to customers when they open a dispute. The form lacks anti-CSRF token, allowing an attacker to craft a malicious page that 
silently updates the message on behalf of an authenticated user.

## Bounty received ($)
750

## References
- https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/
## Tags
- csrf
- missing-csrf-token
- impersonation
