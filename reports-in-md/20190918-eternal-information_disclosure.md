# Information Disclosure through Sentry Instance.

**Target**: Eternal

**Reported on**: hackerone

**Bug Type**: Information Disclosure

**Severity**: High

**Report URL**: https://hackerone.com/reports/697512

## Summary
The researcher identified an exposed API endpoint related to the Sentry error monitoring tool. 
This endpoint returned sensitive information from logged error events directly in the HTTP response, 
including internal hostnames, environment details, and potentially credentials. 
The data could be accessed without authentication by sending crafted requests to the `/api/<project_id>/store` endpoint, 
then rendering the returned event data in the UI. This exposure could allow attackers to gather intelligence 
about the internal infrastructure and use leaked secrets to compromise the system.

## Bounty received ($)
750

## References
- https://hackerone.com/reports/697512
## Tags
- misconfiguration
- information-disclosure
- sentry
