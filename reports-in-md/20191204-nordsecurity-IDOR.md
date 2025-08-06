# IDOR allow access to payments data of any user - nordsecurity

**Target**: Nord VPN

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/751577

## Summary
A Researcher found a vulnerable API endpoint - /api/v1/orders in domain.nordvpn.com that is accessible without auth and will return the transaction details of the user.
The API endpoint had a json key called "user_id" that accepted a numerical id, changing the value to any higher or lower id will return the transaction
detail of another user.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/751577
## Tags
- IDOR
- PII-leak
- sensitive-data
- broken-access-control
