# CSRF to change password

**Target**: Nord VPN

**Reported on**: hackerone

**Bug Type**: CSRF

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/204703 This report describes a Cross-Site Request Forgery (CSRF) vulnerability in NordVPN's profile management page. An attacker could craft a malicious webpage that, when visited by an authenticated user, automatically submits a form to change the victim’s account password without their consent. The vulnerability affects the password change functionality, potentially allowing account takeover if exploited. A proof-of-concept HTML form demonstrating the attack was provided by the reporter.

## Summary


## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/204703
## Tags
- CSRF
