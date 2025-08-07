# IDOR allows an attacker to modify the links of any user

**Target**: reddit

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/1661113

## Summary
The researcher found a way to edit the social links in the profiles of other users due to an IDOR vulnerability in Reddit’s GraphQL API. By querying a user's profile, an attacker could retrieve
internal IDs of social links and then use those IDs in an unauthorized update mutation to modify the link titles or URLs. No ownership or authorization checks were enforced on these operations.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1661113
## Tags
- IDOR
- Information-Disclosure
- sensitive-data
- broken-access-control
