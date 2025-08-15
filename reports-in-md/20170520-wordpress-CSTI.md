# uber.com may RCE by Flask Jinja2 Template Injection

**Target**: uber

**Reported on**: hackerone

**Bug Type**: CSTI

**Severity**: Low

**Report URL**: https://hackerone.com/reports/230232

## Summary
The researcher found a Client side template injection in the address saving feature of wordpress that lets a user put in template code and get it executed in addresses section.
This was classified as a stored self xss as there is no way for another client to access the endpoint where the XSS is stored.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/230232
## Tags
- CSTI
- stored-XSS
