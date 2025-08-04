# Server Side Request Forgery (SSRF) via Analytics Reports

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: SSRF

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/2262382

## Summary
A security researcher found a SSRF vulnerability present in the analytics creation feature in hackerone - https://hackerone.com/organizations/ORG/analytics/reports
PoC - 1. create a new report, choose some filters, click apply and intercept the request. in any template field, inject any html payload - such as an Ifram reading from a internal file.
This leads to read of internal files as the analytics dashboard is loaded, allowing SSRF.

## Bounty received ($)
25000

## References
- https://hackerone.com/reports/2262382
## Tags
- SSRF
