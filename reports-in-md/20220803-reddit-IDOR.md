# Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability

**Target**: reddit

**Reported on**: hackerone

**Bug Type**: IDOR

**Severity**: High

**Report URL**: https://hackerone.com/reports/1658418

## Summary
There was a vulnerability in reddit's GraphQL endpoint that enables any user to see moderator logs of any subreddit. The vulnerability could be reproduced by logging in as any user,
and sending a request to `gql.reddit.com` with the data - `{"id":"6243efcbc61d","variables":{"subredditName":"any-subreddit"}}`, This dumped the moderator logs of any subreddit the user mentions.
If the moderator logs had multiple pages, the response had a `hasNextPage` boolean key value pair indicating that. to see the next page take teh endCursor code value from the first response and simply add the variable `"after": "code-from-endCursor"`.

## Bounty received ($)
5000

## References
- https://hackerone.com/reports/1658418
## Tags
- IDOR
- Information-Disclosure
- sensitive-data
- broken-access-control
