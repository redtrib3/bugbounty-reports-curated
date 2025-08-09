# IDOR - Unauthorized access to `Videos` of Channel whose privacy is set to `Private`.

**Target**: Vimeo

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: Unspecified

**Report URL**: https://hackerone.com/reports/45960

## Summary
The researcher found an IDOR vulnerablity which lets an attacker see the list of private videos of a channel (not access them).
The vulnerability was present in the `badge_channel` parameter of ` /tools/widget/montage?widget=1&preview=1&user_id=36807051&badge_stream=channel&badge_channel=870575&badge_album=3231945&badge_layout=horizontal&badge_quantity=6&show_titles=no&badge_size=80`,
allowing any user to enumerate the value with valid id and viewing their thumbnails thus allowing to see LIST of private videos.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/45960
## Tags
- IDOR
