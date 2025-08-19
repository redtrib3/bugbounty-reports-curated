# Full read SSRF in www.evernote.com that can leak aws metadata and local file inclusion

**Target**: evernote

**Reported on**: hackerone

**Bug Type**: SSRF

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/1189367

## Summary
The researcher found a vulnerable url in evernote - `https://www.evernote.com/ro/aHR0cDovLzE2OS4yNTQuMTY5LjI1NC8jdGVzdC5qcw==/-1430533899.js` that allowed SSRF. the base64 encoded value can be replaced with a external url or a internal file (using file:// wrapper.), allowing SSRF and Path traversal.
The only whitelisting done on the url was the need for the url to end with *.js or *.css, which can be achieved by using a '#' character followed by the any *.js filename.

## Bounty received ($)
5000

## References
- https://hackerone.com/reports/1189367
## Tags
- SSRF
- path-traversal
