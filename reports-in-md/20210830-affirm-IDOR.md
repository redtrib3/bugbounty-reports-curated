# UniFi v3.2.10 Cross-Site Request Forgeries / Referer-Check Bypass

**Target**: Affirm

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/1323406

## Summary
The researcher found an IDOR vulnerability in a payment inteface api, one of the parameter to the API is `checkout_ari`, when replaced with the value of other user, it dumped the order information of the user the checkout_ari belonged to.

## Bounty received ($)
500

## References
- https://hackerone.com/reports/1323406
## Tags
- IDOR
- broken-access-control
