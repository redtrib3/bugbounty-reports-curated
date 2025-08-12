# Information Disclosure in /skills call

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: Information Disclosure

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/188719

## Summary
The researcher found out that there was a flaw in the new skillset feature in hackerone that responded with sensitive user data.
The skill set feature is used to send tailored invitations for private programs. Hackers have to submit reports as proof for their skills. 
Due to an incorrectly written query, the proof, which includes report titles, was exposed to all other hackers that applied for the same skill set.

## Bounty received ($)
10000

## References
- https://hackerone.com/reports/188719
## Tags
- misconfiguration
- information-disclosure
