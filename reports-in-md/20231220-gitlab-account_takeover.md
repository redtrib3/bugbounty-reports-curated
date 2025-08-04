# Account Takeover via Password Reset without user interactions

**Target**: gitlab

**Reported on**: hackerone

**Bug Type**: Account Takeover

**Severity**: Critical

**Report URL**: https://hackerone.com/reports/2293343

## Summary
"The researcher found a way to successfully takeover an account by exploiting a logical flaw in the reset password functionality.
**Proof of concept:** <br>
- Go to "Forgot Your Password?" link<br>
- Enter the victim's email and intercept the submit request via Burp Suite.<br>
- Then right-click on the HTTP Editor inside Burp Suite and select Extensions -> Content-Type Converter -> Convert to JSON (make sure to have the Content-Type Converter plugin installed from the BApp Store)<br>
- Now replace this converted JSON line  "user[email]":"victim@gmail.com", to
 ```
 "user" {
   "email" [
            "victim@gmail.com",
            "attacker@gmail.com"
     ]
 },```
<br>
 - forward the request and the reset link is sent to the attacker email as well."

## Bounty received ($)
35000

## References
- https://hackerone.com/reports/2293343
## Tags
- account-takeover
- gitlab
- burpsuite
