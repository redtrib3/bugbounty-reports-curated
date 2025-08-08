# IDOR in https://3d.cs.money/

**Target**: CS Money

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/990878

## Summary
A researcher found a medium level IDOR vulnerability in a online gaming skin marketplace, where an attacker can clear the build list of a victim, by changing the `steamID` cookie in request to `/sync` from the attacker's profile to that of the Victim.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/990878
## Tags
- IDOR
