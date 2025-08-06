# IDOR - Delete all Licenses and certifications from users account using CreateOrUpdateHackerCertification GraphQL query

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/2122671

## Summary
A Researcher found a vulnerability in a graphql endpoint that allows a attacker to delete Licenses and Certifications stored in the profile with guessable ID.
A range of data - licenses and certifications can also be deleted by specifying a range value with the guessable ID.

## Bounty received ($)
12500

## References
- https://hackerone.com/reports/2122671
## Tags
- IDOR
- sensitive-data
