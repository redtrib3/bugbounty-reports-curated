# IDOR when moving contents at CrowdSignal

**Target**: automattic

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/915127

## Summary
An IDOR in the “Move to” functionality allowed attackers to take over any user’s content by modifying the `actionable[]` parameter in a POST request. 
With a free account, attackers could move victim content to their own account with limited control. With a team account, attackers could transfer victim content to 
another account within their team, gaining full access. Content IDs are sequential, enabling easy enumeration. _This summary is generated using AI_

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/915127
## Tags
- IDOR
- broken-access-control
