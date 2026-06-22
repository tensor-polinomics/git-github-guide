# Pinned-source verification log

All claims below were live-verified on the access date shown. Each
entry records: the claim as it will appear in the book, the
authoritative source, the exact supporting text, and the chapter that
relies on it. Re-verify before any future edition; web docs drift.

Verifier environment: sandbox, git 2.34.1, git-filter-repo 2.47.0.

---

## V1. git-filter-repo is the recommended history-rewrite tool

Access date: 2026-06-21
Source: GitHub Docs, "Removing sensitive data from a repository"
URL: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
Used in: Ch.6

Supporting text (quoted): "When altering your repository's history
using tools like `git-filter-repo`, it's crucial to understand the
implications." The purge procedure is titled "Purging a file from
your local repository's history using git-filter-repo" and step 1
says: "Install the latest release of the `git-filter-repo` tool. You
need a version with the `--sensitive-data-removal` flag, meaning at
least version 2.47."

Notes: The page no longer leads with `git filter-branch`; filter-repo
is the documented path. BFG is mentioned elsewhere on GitHub as an
alternative but the canonical procedure here uses filter-repo. Book
rule (never BFG/filter-branch as the primary recommendation) holds.
Installed filter-repo in sandbox is 2.47.0 (has the flag); confirmed
via `git filter-repo --version` and `git filter-repo --help`.

---

## V2. Rotate/revoke the secret FIRST, before rewriting history

Access date: 2026-06-21
Source: same GitHub page as V1, section "About removing sensitive
data from a repository"
Used in: Ch.6 (the central safety claim), Ch.16

Supporting text (quoted): "if the sensitive data you need to remove
is a secret (e.g. password/token/credential), as is often the case,
then as a first step you need to revoke and/or rotate that secret.
Once the secret is revoked or rotated, it can no longer be used for
access, and that may be sufficient to solve your problem. Going
through the extra steps to rewrite the history and remove the secret
may not be warranted."

Also (section "About sensitive data exposure"): a force-pushed
rewrite still leaves the secret reachable "In any clones or forks",
"Directly via their SHA-1 hashes in cached views on GitHub", and
"Through any pull requests that reference them". And: "GitHub Support
won't remove non-sensitive data, and will only assist in the removal
of sensitive data in cases where we determine that the risk can't be
mitigated by rotating affected credentials."

Notes: This is why the book frames rotation as step zero and history
rewriting as damage-limitation, not a fix. Verified verbatim.

---

## V3. Side effects of rewriting history

Access date: 2026-06-21
Source: same GitHub page, section "Side effects of rewriting history"
Used in: Ch.6 PITFALL

Supporting text (paraphrase of bulleted list, verified present):
high risk of recontamination (a colleague's `git pull` then
`git push` reintroduces the data); changed commit hashes for the bad
commit and every commit after it; branch-protection force-push
blocks must be lifted; broken PR diff views; lost commit/tag
signatures. Quote used in book: "Rewriting history will change the
hashes of the commits that introduced the sensitive data *and* all
commits that came after."

---

## V4. GitHub push protection blocks secrets at push time

Access date: 2026-06-21
Source: GitHub Docs, "About push protection"
URL: https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
Used in: Ch.6 (prevention), Ch.16

Supporting text (paraphrase, verified): push protection "blocks
pushes that contain secrets before they reach your repository"; when
a potential secret is detected it "will block the push and provide a
detailed message"; anyone with write access can bypass with a stated
reason. The "Removing sensitive data" page also recommends enabling
push protection under "Avoiding accidental commits in the future".

Notes: Framed in the book as a safety net, NOT a substitute for a
`.gitignore` and not committing secrets in the first place. Free for
public repos; private repos need GitHub Advanced Security / a paid
plan, so the book states it as "if available to you".

---

## V5. Claude Code / agent permission model

Access date: 2026-06-21
Source: Claude Code Docs, "Security"
URL: https://docs.claude.com/en/docs/claude-code/security
Used in: Ch.16 (terminal vs agent; what an agent must never do)

Supporting text (paraphrase, verified): a built-in set of read-only
commands such as `ls`, `cat`, and `git status` runs without a
prompt; actions that modify the system (editing files, running
commands) require explicit permission, approved once or allowlisted;
the agent "can only write to the folder where it was started and its
subfolders"; web-fetching commands like `curl`/`wget` are not
auto-approved; "Bypass Permissions" mode auto-approves everything and
is flagged "Use with extreme caution."

Notes: Book uses this to ground the rule that destructive Git
commands (force-push, reset --hard, history rewrites, branch
deletion) should require human approval, and that a clean working
tree + committed checkpoint is the real safety net, not the agent's
own promises. Stated as vendor-specific (Claude Code) with the
general principle abstracted.

---

## V6. git reflog default expiry windows

Access date: 2026-06-21
Source: Git Docs, git-reflog / git-config
URL: https://git-scm.com/docs/git-reflog
Used in: Ch.5 and Ch.16 RECOVERY callouts (reflog as safety net)

Supporting text (verified): reachable reflog entries expire after
90 days (`gc.reflogExpire`, default 90 days); unreachable entries
expire after 30 days (`gc.reflogExpireUnreachable`, default 30 days).

Notes: Book claim is the conservative one: "for at least 30 days,
usually 90, your previous state is recoverable from the reflog even
after a bad reset." Locally confirmable: `git config gc.reflogExpire`
returns empty (i.e. the built-in default applies).
