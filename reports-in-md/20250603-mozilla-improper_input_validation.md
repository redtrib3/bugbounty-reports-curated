# Bypass "No Links" Restriction in Biography via Protocol-Relative URL (//)

**Target**: Mozilla

**Reported on**: hackerone

**Bug Type**: Improper Input Validation

**Severity**: Low

**Report URL**: https://hackerone.com/reports/3175695

## Summary
In addons.allizom.org (a website for android addons), the user has a profile where he can add a bio.
It only allows adding certain html tags:
Some HTML supported: `<abbr title> <acronym title> <b> <blockquote> <code> <em> <i> <li> <ol> <strong> <ul>. Links are forbidden.`

But an <a> tag can be added with a functional hyperlink (starts with "//")
payload: `<a href="//evil.com">click</a>`
This will successfully display the click hyperlink in bio.

## Bounty received ($)
Unspecified

## References
- https://hackerone.com/reports/3175695
## Tags
- input-validation
- html-injection
- bypass
- url-scheme
- frontend
- content-restriction
