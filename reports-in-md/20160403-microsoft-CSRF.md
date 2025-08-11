# Obtaining Login Tokens for an Outlook, Office or Azure Account

**Target**: Microsoft

**Reported on**: Microsoft Security Response Center (MSRC)

**Bug Type**: CSRF

**Severity**: Critical

**Report URL**: https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/

## Summary
"Since microsoft has multiple services spread across different domains, to handle authentication, requests are made to login.live.com, login.microsoftonline.com, and 
login.windows.net to get a session for the user.

The flow for outlook.office.com is as follows:"

  - User browses to https://outlook.office.com
  - User is redirected to https://login.microsoftonline.com/login.srf?wa=wsignin1.0&rpsnv=4&wreply=https%3a%2f%2foutlook.office.com%2fowa%2f&id=260563
  - Provided that the user is logged in, a POST request is made back to the value of `wreply`, with the form field `t` containing a login token for the user
  
capturing this token somehow, allows anyone to login to microsoft services.

placing any other external non-microsoft domain link in the `wreply` parameter returns an error as expected.
The researcher found a bypass to this microsoft domain check by using the authentication format in urls.

`https://outlook.office.com%2f@poc-ssl.fin1te.net/microsoft/` - In this the outlook domain is placed in the username part of the url.

This trick caused the authentication token to be sent to an attacker-controlled server, enabling token theft without the user’s knowledge. With stolen tokens, attackers could fully impersonate victims on Microsoft cloud services, accessing emails, files, and other resources.
Microsoft fixed the issue by tightening validation rules on acceptable wreply URLs to prevent such bypasses."

## Bounty received ($)
Unspecified

## References
- https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/
## Tags
- csrf
- authentication
- token-theft
- url-parsing
- domain-validation-bypass
