# Insecure Direct Object Reference (IDOR) - Delete Campaigns

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/1969141

## Summary
A researcher found a vulnearbility in a graphql api endpoint that lets a user delete a campaign by manipulating the campaign_id parameter.
The campaign_id takes a base64 of the string - `gid://hackerone/Campaign/244`. On changing the number 244 to another valid campaign (which is guessable),
the respective campaign is deleted.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1969141
- https://www.first.org/cvss/v3-0/user-guide#3-2-Confidentiality-and-Integrity-versus-Availability-Impacts
## Tags
- IDOR
- sensitive-data
