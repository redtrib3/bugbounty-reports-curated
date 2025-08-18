# Request smuggling on admin-official.line.me could lead to account takeover

**Target**: LY corporation

**Reported on**: hackerone

**Bug Type**: HTTP request smuggling

**Severity**: High

**Report URL**: https://hackerone.com/reports/740037

## Summary
The researcher found an HTTP request smuggling (TE.CL) vulnerability in an application where the frontend uses Transfer encoding header and the backend uses Content Length.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/740037
## Tags
- http-request-smuggling
- http1.1-must-die
- desync
