# Sensitive user information disclosure at bonjour.uber.com/marketplace/_rpc via the 'userUuid' parameter.

**Target**: Uber

**Reported on**: hackerone

**Bug Type**: Information Disclosure

**Severity**: High

**Report URL**: https://hackerone.com/reports/542340

## Summary
The researcher found out that it was possible to pass in another user's UUID to `userUuid` post parameter to `https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails` 
and retrieved data, which included mobile API token which could be potentially used to takeover the driver/rider account.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/542340
## Tags
- misconfiguration
- information-disclosure
- API-vulnerability
