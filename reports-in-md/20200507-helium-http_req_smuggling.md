# HTTP request Smuggling (CL.TE) - Helium

**Target**: Helium

**Reported on**: hackerone

**Bug Type**: HTTP request smuggling

**Severity**: High

**Report URL**: https://hackerone.com/reports/867952

## Summary
The researcher found an HTTP request smuggling (CL.TE) vulnerability in an application where the frontend uses Content length header and the backend uses Transfer encoding.
The researcher successfully demonstrated the impact by showing that a victim can be potentially redirected to attacker website.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/867952
## Tags
- http-request-smuggling
- http1.1-must-die
- desync
