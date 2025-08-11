# Google Docs link in JS files allows editing & reading survey information

**Target**: hackerone

**Reported on**: hackerone

**Bug Type**: Information disclosure

**Severity**: Medium

**Report URL**: https://hackerone.com/reports/2180521

## Summary
The researcher who was monitoring Javascript files of hackerone found a new update that introduced a variable with a google docs link.
The google docs link was leaked via the file `https://hackerone.com/assets/static/js/5930.078b8e86.chunk.js`, The document was editable and had global read permission.

## Bounty received ($)
2500

## References
- https://hackerone.com/reports/2180521
## Tags
- information-disclosure
- data-leak
- lack-of-permissions
