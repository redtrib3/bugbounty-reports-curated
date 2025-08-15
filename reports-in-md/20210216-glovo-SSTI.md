# Server Side Template Injection on Name parameter during Sign Up process

**Target**: Glovo

**Reported on**: hackerone

**Bug Type**: SSTI

**Severity**: High

**Report URL**: https://hackerone.com/reports/1104349

## Summary
The researcher found a SSTI vulnerability in the username field during signup. On registering with the username `{{7*7}}`, the researcher noticed that the welcome email reflected the output `49`.
The researcher also points out that further testing could not be done as the initial exploitation seems to have broke the code in the backend, as a result no more welcome emails were being sent, affecting availability.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1104349
## Tags
- SSTI
- RCE
