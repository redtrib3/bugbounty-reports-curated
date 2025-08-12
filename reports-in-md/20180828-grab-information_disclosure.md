# [Grab Android/iOS] Insecure deeplink leads to sensitive information disclosure

**Target**: Grab

**Reported on**: hackerone

**Bug Type**: Information Disclosure

**Severity**: High

**Report URL**: https://hackerone.com/reports/401793

## Summary
The Grab Passenger app exposes a deep link that loads arbitrary web pages inside an internal WebView
(ZendeskSupportActivity). This WebView exposes a JavaScript interface named 'Android' with methods like `getGrabUser()`
that return sensitive user data. Because the deep link allows an attacker to specify any URL, they can host a malicious
page that calls these exposed methods to steal sensitive information without user consent. The issue arises due to
lack of restrictions on loaded URLs and unrestricted access to sensitive native methods via the JavaScript interface.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/401793
## Tags
- misconfiguration
- information-disclosure
- mobile-pentesting
