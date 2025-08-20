# Remove Every User, Admin, And Owner Out Of Their Teams on developers.mtn.com via IDOR + Information Disclosure

**Target**: MTN Group

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/1448550

## Summary
The vulnerability lies in the team management functionality on developers.mtn.com. When a user removes another member from their team, the server relies on client-supplied `user_id` and `team_id` values without validating ownership or permissions. By intercepting and modifying this request, an attacker can target arbitrary `user_id` and `team_id` values belonging to accounts and teams they do not control. 
Exploitation allows a low-privileged attacker to remove any user, including admins and owners, from any team. This not only disrupts team structures but also results in sensitive information disclosure since the server response leaks usernames and team names. With brute force against the 4-digit `user_id` and `team_id`, an attacker could systematically remove every user from every team within hours, leading to mass account disruption across the platform.
This is an Insecure Direct Object Reference (IDOR) with severe business impact: arbitrary account manipulation, privilege abuse, mass denial of service to teams, and sensitive information disclosure.

_This summary was generated using AI_

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/1448550
## Tags
- IDOR
- business-logic-error
