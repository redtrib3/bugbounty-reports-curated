# Race condition in joining CTF group

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: Race condition

**Severity**: Low

**Report URL**: https://hackerone.com/reports/1540969

## Summary
The researcher found a race condition in https://ctf.hacker101.com/group/join that allows a user to join the same CTF group multiple times. 
The user will also show up in the group member list multiple times, and affect the group statistics.

## Bounty received ($)
500

## References
- https://hackerone.com/reports/1540969
## Tags
- race-condition
