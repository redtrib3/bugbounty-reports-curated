# IDOR on removing Share

**Target**: Enter.health

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Unspecified

**Report URL**: https://hackerone.com/reports/85720

## Summary
The researcher found a authorization flaw in a shared crypto wallet where the user that the wallet was shared with can remove access to another user.
Only the owner of the wallet should be able to have the permissions to remove access to other user, but any shared user can user an endpoint to delete any other user's access.
The vulnerability can be reproduced by sending a POST request to  `/dashboard/account/<accountID>/sharing/delete` with the data containing the parameter bankUserId=<victim's ID> and the csrf token.

## Bounty received ($)
250

## References
- https://hackerone.com/reports/85720
## Tags
- IDOR
