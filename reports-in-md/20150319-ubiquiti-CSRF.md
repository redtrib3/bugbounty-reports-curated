# UniFi v3.2.10 Cross-Site Request Forgeries / Referer-Check Bypass

**Target**: Ubiquiti Inc.

**Reported on**: hackerone

**Bug Type**: CSRF

**Severity**: Unspecified

**Report URL**: https://hackerone.com/reports/52635

## Summary
The researcher found a CSRF bypass vulnerability in UniFi v3.2.10 - Router, the only CSRF protection present in the interface was checking wheather Referer header is present and
if it matches the host where the system is running - `default: 127.0.0.1`. On removing the referer header, it successfully bypasses any CSRF protection on the entire interface.

## Bounty received ($)
500

## References
- https://hackerone.com/reports/52635
## Tags
- CSRF
