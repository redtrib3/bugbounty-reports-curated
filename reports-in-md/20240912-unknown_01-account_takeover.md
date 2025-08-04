# Interesting Story of an Account Takeover Vulnerability

**Target**: private

**Reported on**: hackerone

**Bug Type**: Account Takeover

**Severity**: Critical

**Report URL**: https://medium.com/@deepanshudev369/interesting-story-of-an-account-takeover-vulnerability-140a45a058a3

## Summary
While hunting on a private program, the researcher came across a host header injection in a password reset functionality.
The host header was reflected in the reset link if it contained the application's domain in it.

To build the reset link, the application took the host header, removed the TLD, and added the application's domain.
`https://abc.burpcollaborator.login.redacted.com/auth/realms/login-actions/action-token?key=<key>`, here `abc.burpcollaborator`
is the manipulated host header appended as a subdomain by the backend when building the reset link.

The research found a workaround this problem by adding the application domain in the URL port place, and the malicious collaborator url in the domain's place.
`Host: burpcollaboratorurl.com:login.redacted.com`.  

The request got through and reflected in the reset password mail, successfully letting an attacker takeover an account.

## Bounty received ($)
2000

## References
- https://medium.com/@deepanshudev369/interesting-story-of-an-account-takeover-vulnerability-140a45a058a3
## Tags
- account-takeover
- host-header-injection
