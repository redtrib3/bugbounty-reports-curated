# Critical IDOR - Get venue data of any organization remotely

**Target**: Veris

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Unspecified

**Report URL**: https://hackerone.com/reports/120305

## Summary
Veris is a smart automation company that provides services designing smart office automation. In context, a 'venue' is a physical location of an office.
A reseacher found a vulnerability in sandbox.veris.in that let's any user get sensitive information about a venue i.e an office.
using the endpoint `/api/v1/gatekeepers/?venue_id=36`, by incrementing the venue_id, we get the information about other organizations.

## Bounty received ($)
Swag

## References
- https://hackerone.com/reports/120305
## Tags
- IDOR
