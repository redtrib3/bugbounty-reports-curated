# Urgent: Server side template injection via Smarty template allows for RCE

**Target**: unikrn

**Reported on**: hackerone

**Bug Type**: SSTI

**Severity**: Unspecified

**Report URL**: https://hackerone.com/reports/164224

## Summary
The researcher found SSTI vulnerability in a webapp using smarty. The researcher initially passed in the payload `{7*7}` for usrename 
and was met with an error in rendered email when sending a join request to a friend. The error specified a smarty syntax error. The researcher was further able to escalate
the bug by using the `{php}` tag in smarty to achieve code execution and demostrated that the attacker can read files using `file_get_contents`.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/164224
## Tags
- SSTI
- RCE
