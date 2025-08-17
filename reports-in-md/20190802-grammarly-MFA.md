# “email” MFA mode allows bypassing MFA from victim’s device when the device trust is not expired

**Target**: grammarly

**Reported on**: hackerone

**Bug Type**: MFA

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/665722

## Summary
The researcher found a vulnerability in grammarly that lets an attacker login by skipping the 2FA step. This exploitation could only be done based on certain conditions.
When a user performs a signin/signup, the device from which the action was performed becomes trusted. These devices identify themselves by `tdi` cookies. The vulnerability allowed bypassing MFA when the following conditions are met:
1. Login request was made from the device with the same tdi cookie and UserAgent header.
2. Login request was made when the device's trust wasn't expired.

Due to the complexity of the exploitation, the report was triaged as a Medium.

## Bounty received ($)
2500

## References
- https://hackerone.com/reports/665722
## Tags
- 2FA
- MFA-bypass
