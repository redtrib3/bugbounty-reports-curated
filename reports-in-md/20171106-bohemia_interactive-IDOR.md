# IDOR to view User Order Information

**Target**: Bohemia interactive

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/287789

## Summary
The reseacher found a IDOR vulnerability in the endpoint - https://store.bistudio.com/order/1003793?confirmed=true where `1003793` is the placeholder for the ID.
The id is numerical and guessable, on increasing or decreasing it, we get the Order data of other users which is PII including public IP addresses.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/287789
## Tags
- IDOR
- Information-Disclosure
- PII-LEAK
- sensitive-data
