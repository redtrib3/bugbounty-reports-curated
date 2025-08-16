# Race condition in performing retest allows duplicated payments

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: Race condition

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/429026

## Summary
The researcher found a race condition vulnerability in the retest feature of bounty reporting in hackerone, when you submit a report and gets triaged, the Triage team can ask you for retest, and a retest is paid a specific amount.
The researcher found out that by concurrently sending the retest request multiple times, multiple payments are made from hackerone.

## Bounty received ($)
2500

## References
- https://hackerone.com/reports/429026
## Tags
- race-condition
