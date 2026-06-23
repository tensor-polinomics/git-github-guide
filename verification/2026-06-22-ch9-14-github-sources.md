# Ch.9-14 source-verification log (GitHub + toolchain batch)

Live-verified on the access dates shown. This batch (Phase 4b-3:
Ch.9 Git->GitHub, Ch.10 GitHub beginners, Ch.11 GitHub advanced + gh,
Ch.12 collaboration, Ch.14 research toolchain) mixes EXECUTED captures,
PENDING path-A captures, and DOCUMENTED-NOT-EXECUTED facts:

- EXECUTED in-sandbox (Linux, Git 2.34.1): all remote mechanics
  (push/fetch/pull/clone) against a local bare repo standing in for
  GitHub's server side; the two-clone collaboration conflict loop;
  nbdime 4.0.4 and jupytext 1.19.4 notebook-diff demos, including
  `nbdime config-git --enable` and `jupytext --set-formats`. Transcripts
  under `transcripts/09_*`, `12_*`, `14_*`.
- EXECUTED on the user's Mac (path A, 2026-06-22): read-only
  `git remote -v` / `git ls-remote` / `git push --dry-run` against the
  real public repo; `gh --version`, `gh auth status`, `gh repo view`,
  `gh pr list`, `gh run list`, and `gh issue list` with gh 2.95.0
  authenticated as tensor-polinomics. Transcripts:
  `transcripts/09_real_remote.txt`, `transcripts/11_gh_readonly.txt`.
- PENDING on the user's Mac (path A; NOT yet captured): live renv
  init/snapshot/restore console + `renv.lock`. Until this lands, the
  Ch.14 renv block remains documented/instructional, not captured
  output, and the command list lives in RESUME.md's handover section.
- DOCUMENTED-NOT-EXECUTED and pinned below: GitHub web-UI flows
  (repo creation, license/.gitignore pickers, issues, PR review,
  protected branches/rulesets, the server-side "Create a pull request"
  hint), GitHub Actions, Overleaf-GitHub sync, RStudio/VS Code Git
  integration, Quarto+Git freeze guidance.

Re-verify before any future edition; GitHub UI, gh subcommands, Action
versions, and Overleaf plan boundaries drift.

---

## G1. gh CLI 2.95.0; read-only vs state-mutating subcommands

Access date: 2026-06-22
Source: GitHub CLI manual + cli/cli releases.
URL: https://cli.github.com/manual/
      https://github.com/cli/cli/releases
Used in: Ch.11 (gh CLI), Ch.9/Ch.10 (read-only inspection commands).

Verified claims: gh is GitHub's official CLI; v2.95.0 is current
(packaged 2026-06-18), matching the user's installed Homebrew build and
the live `gh --version` capture in `transcripts/11_gh_readonly.txt`.
READ-ONLY/inspection subcommands used in the book: `gh auth status`,
`gh repo view`, `gh pr list`, `gh pr view`, `gh pr diff`, `gh run list`,
`gh run view`, `gh issue list`. Live path-A capture confirms
authentication as tensor-polinomics over SSH with repo scope; `gh pr
list`, `gh run list`, and `gh issue list` returned no rows on the public
repo at capture time. STATE-MUTATING subcommands QUARANTINED for the
user to run deliberately (never in a copy-paste block): `gh pr create`,
`gh pr merge`, `gh repo create`, `gh repo edit`, `gh release create`,
`gh workflow run`, `gh issue create`. This is the CLAUDE.md gh rule
(Ch.16 "human decides hard-to-undo actions") applied to our workflow.

---

## G2. GitHub Actions workflow syntax (checkout@v4, runner, token)

Access date: 2026-06-22
Source: GitHub Docs "Workflow syntax for GitHub Actions" and
"Controlling permissions for GITHUB_TOKEN"; actions/checkout;
astral-sh/setup-uv.
URL: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
      https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token
      https://github.com/actions/checkout
      https://github.com/astral-sh/setup-uv
Used in: Ch.11 (Actions section + the validate-book workflow YAML).

Verified claims: a workflow is a YAML file under `.github/workflows/`
with `.yml`/`.yaml` extension. Keys: `name`, `on` (triggers, e.g.
`push`/`pull_request`), `jobs`. Each job sets `runs-on` (e.g.
`ubuntu-latest`, a GitHub-hosted runner) and a list of `steps` that
either `uses` an action or `run`s a shell command. `actions/checkout@v4`
checks the repo out into `$GITHUB_WORKSPACE` (single commit by default;
`fetch-depth: 0` for full history). `astral-sh/setup-uv` installs uv on
the runner. GITHUB_TOKEN permissions are set with the `permissions:`
key; `contents: read` is sufficient for a clone-and-lint job and is the
recommended least-privilege default. The book's example workflow runs
`uv run python tools/validate_book.py book` on push/PR to `main`, mirroring
the local gate. YAML NOTE: PyYAML parses the `on:` key as boolean `True`
(a YAML 1.1 quirk); GitHub's own parser reads `on:` correctly as the
trigger key, so the workflow is valid. Syntax-checked in-sandbox
(transcripts/11_actions_yaml_check.txt). The workflow is provided as a
quarantined add-this-file step, not run from the sandbox (no Actions
runner here).

---

## G3. Branch protection rules vs rulesets

Access date: 2026-06-22
Source: GitHub Docs "About protected branches", "About rulesets",
"Available rules for rulesets".
URL: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
      https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
Used in: Ch.11 (protected branches).

Verified claims: GitHub offers two mechanisms to protect a branch.
Classic "branch protection rules" are per-branch; only one applies to a
given branch at a time. Newer "rulesets" can layer (multiple apply at
once, aggregated, most-restrictive-wins), can be scoped across a repo or
org, and can enforce at branch-creation time (protection rules apply only
once a branch exists). Both can require a pull request before merging and
require status checks to pass. The book presents the protect-main intent
(no direct pushes, require a PR + passing checks + review) and notes
rulesets as the current, more flexible mechanism without depending on a
specific screen layout.

---

## G4. New-repository options: README, .gitignore template, license

Access date: 2026-06-22
Source: GitHub Docs "Creating a new repository", "Adding a license to a
repository"; github/gitignore; gh repo create manual; choosealicense.
URL: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
      https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
      https://github.com/github/gitignore
      https://cli.github.com/manual/gh_repo_create
      https://choosealicense.com
Used in: Ch.10 (create a repo; README/LICENSE/.gitignore).

Verified claims: when creating a repo on GitHub.com you can initialize
with a README, pick a `.gitignore` template (populated from
github/gitignore), and choose a license from the picker. IMPORTANT: the
license picker is offered only at new-project creation; to add a license
later you add a `LICENSE` file (the repo can still detect it). With the
CLI, `gh repo create` accepts `--add-readme`, `--gitignore <template>`,
and `--license <keyword>` (license keywords via `gh repo license list`
or choosealicense.com). The book's own repo (github.com/tensor-polinomics/
git-github-guide) is the live worked example: MIT for code, CC BY 4.0 for
prose/figures, a README and CITATION.cff at the root.

---

## G5. Pull request + fork basics; the push-time PR hint

Access date: 2026-06-22
Source: GitHub Docs "About pull requests", "Creating a pull request",
"About forks", "Creating a pull request from a fork".
URL: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
      https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
      https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
Used in: Ch.11 (PRs, review, forks), Ch.12 (PR-based collaboration).

Verified claims: a pull request proposes merging one branch (the head,
often a feature branch or a fork) into another (the base, often `main`),
with a diff, a discussion thread, line comments, and review states
(Comment / Approve / Request changes). After you push a new branch,
GitHub's web/CLI response surfaces a "Create a pull request" link for
that branch; this hint is generated by GitHub's server and does NOT
appear when pushing to a plain local/bare remote (confirmed in-sandbox:
the feature-branch push in transcripts/11_push_branch.txt shows only the
"[new branch]" line, no PR hint). A fork is a server-side copy of a repo
under your account; the outside-contributor workflow is fork -> branch ->
push to your fork -> open a PR to the upstream repo. Merging a PR is a
state-mutating action (QUARANTINED; `gh pr merge` or the green button).

---

## G6. Overleaf <-> GitHub synchronization

Access date: 2026-06-22
Source: Overleaf docs "GitHub synchronization", "Premium features".
URL: https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization
      https://docs.overleaf.com/getting-started/free-and-premium-plans/premium-features
Used in: Ch.14 (Overleaf-GitHub sync).

Verified claims: Overleaf's GitHub synchronization is a PREMIUM feature.
You link your Overleaf account to GitHub in Account Settings, then create
an Overleaf project via New Project -> Import from GitHub. Sync is
manual/explicit (a menu action that pushes/pulls between the Overleaf
project and the linked GitHub repo), not continuous. Documented limits:
you cannot link an EXISTING Overleaf project to an EXISTING repo (import
creates the project), and once linked a project cannot be unlinked to
create a new repo; Overleaf recommends under ~100 files per commit and
under ~100 MB total. Free-tier users use the git-bridge / manual push
instead. Documented from Overleaf docs, not exercised (no Overleaf
account driven here); flagged as such in the chapter.

---

## G7. renv (R) project environment workflow

Access date: 2026-06-22
Source: renv docs "Introduction to renv", snapshot/restore references;
Posit IDE renv guide.
URL: https://rstudio.github.io/renv/articles/renv.html
      https://rstudio.github.io/renv/reference/snapshot.html
      https://rstudio.github.io/renv/reference/restore.html
      https://docs.posit.co/ide/user/ide/guide/environments/r/renv.html
Used in: Ch.14 (R environment, analogue of uv.lock from Ch.8).

Verified claims: `renv::init()` creates a project-local library and an
initial `renv.lock`; `renv::snapshot()` records the current package
versions into `renv.lock`; `renv::restore()` reinstalls exactly those
versions from the lockfile. You commit `renv.lock`, `.Rprofile`,
`renv/settings.json`, and `renv/activate.R` to Git (renv writes a
project `.gitignore` that excludes the private library itself). This is
the direct R analogue of committing `uv.lock` (Ch.8). renv is NOT
installed in the sandbox (no R), so the chapter's renv section is
DOCUMENTED from the sources above, not captured. A live path-A
transcript and `renv.lock` from the user's Mac (to be saved as
`transcripts/14_renv_*`) will replace it in a later revision; until
then the renv block is presented as documented, not executed.

---

## G8. Quarto + Git: what to ignore, what to commit

Access date: 2026-06-22
Source: Quarto docs "Project Basics", "GitHub Pages".
URL: https://quarto.org/docs/projects/quarto-projects.html
      https://quarto.org/docs/publishing/github-pages.html
Used in: Ch.14 (Quarto + Git).

Verified claims: add the render OUTPUT directory to `.gitignore`
(`/_book/` for books, `/_site/` for websites), and Quarto adds `/.quarto/`
to `.gitignore` on render. When a project has executable code, Quarto
writes a top-level `_freeze/` directory caching computation results;
`_freeze/` SHOULD be committed so collaborators and CI reproduce outputs
without re-running everything, and it re-runs only the changed documents
on the next render. This is exactly how this book's own repo is
configured (it is a Quarto book under Git). Quarto itself is not in the
sandbox; the render-fidelity build is the user's Mac.

---

## G9. Notebook diffing: nbdime and jupytext (EXECUTED in-sandbox)

Access date: 2026-06-22
Source: nbdime docs; jupytext docs (versions captured live).
URL: https://nbdime.readthedocs.io/
      https://jupytext.readthedocs.io/
Used in: Ch.14 (Jupyter notebook diffing).

Verified claims: a Jupyter `.ipynb` is JSON, so a plain `git diff`
interleaves source, `execution_count`, and cell outputs, and on real
notebooks the base64-encoded image outputs make the diff unreadable.
nbdime (`nbdiff`, plus `nbdiff-web`) diffs notebooks cell-by-cell and can
ignore outputs/metadata; wiring it into Git is OPT-IN via
`nbdime config-git --enable` (which registers the diff/merge drivers in
the Git config, verified live). `jupytext --to py:percent` is a one-off
conversion; PAIRING (keeping the two files in sync) is set up separately
with `jupytext --set-formats ipynb,py:percent`, which writes the pairing
into the notebook metadata (verified live). Output STRIPPING is a third
tool, `nbstripout` (0.9.1 installed), whose `nbstripout --install`
registers a Git filter; nbdime does not strip outputs. EXECUTED
in-sandbox (nbdime 4.0.4, jupytext 1.19.4 via `uv tool install`):
transcripts 14_git_diff_ipynb.txt (noisy JSON diff), 14_nbdiff.txt
(clean cell-level diff, timestamp normalized), 14_jupytext_pair.txt
(`--to` conversion), 14_nbdime_configgit.txt (driver registration), and
14_jupytext_pair2.txt (`--set-formats` pairing).

---

## G10. IDE Git integration (RStudio, VS Code)

Access date: 2026-06-22
Source: Posit RStudio "Version Control with Git and SVN"; VS Code docs
"Using Git source control in VS Code".
URL: https://docs.posit.co/ide/user/ide/guide/tools/version-control.html
      https://code.visualstudio.com/docs/sourcecontrol/overview
Used in: Ch.14 (RStudio / VS Code Git).

Verified claims: RStudio has a built-in Git pane (stage, commit, diff,
push/pull, history) enabled per-project when the project is a Git repo;
it wraps the same Git commands the book teaches. VS Code has a built-in
Source Control view (stage, commit, branch, sync) and surfaces diffs in
the editor; the GitHub Pull Requests extension adds in-editor PR review.
The book's point is that these GUIs are convenience layers over the
exact commands from Ch.5/7/9, not a different Git. Documented from
official docs (neither IDE is driven in the sandbox); the underlying Git
operations are the ones already captured in earlier chapters.

---

## Captured transcripts backing this batch (provenance)

- 09_remote_none.txt    git remote -v on a fresh local repo (sandbox)
- 09_remote_add.txt     git remote add origin + remote -v (sandbox)
- 09_push.txt           git push -u origin main, first push (sandbox)
- 09_clone.txt          git clone + log + remote -v (sandbox)
- 09_fetch.txt          git fetch shows "behind" (sandbox)
- 09_pull.txt           git pull fast-forward (sandbox)
- 09_remote_show.txt    git remote show origin tracking (sandbox)
- 09_push_again.txt     plain git push of a later commit (sandbox)
- 09_real_remote.txt    real GitHub remote proof, read-only (path A)
- 11_push_branch.txt    git push -u of a feature branch (sandbox)
- 11_actions_yaml_check.txt  validate-book workflow YAML parse (sandbox)
- 11_gh_readonly.txt    gh auth/repo/PR/run/issue inspection (path A)
- 12_push_reject.txt    non-fast-forward push rejection (sandbox)
- 12_pull_conflict.txt  pull -> merge conflict on shared file (sandbox)
- 12_resolve_push.txt   resolve + commit + push (sandbox, path norm.)
- 12_coauthor.txt       Co-authored-by trailer in git log (sandbox)
- 14_git_diff_ipynb.txt noisy JSON diff of a notebook (sandbox)
- 14_nbdiff.txt         clean cell-level nbdiff (sandbox, ts norm.)
- 14_jupytext_pair.txt  jupytext --to .ipynb -> .py:percent (sandbox)
- 14_nbdime_configgit.txt  nbdime config-git --enable drivers (sandbox)
- 14_jupytext_pair2.txt  jupytext --set-formats pairing (sandbox)
- (path A, PENDING; not captured yet) renv init/snapshot/restore console
  + renv.lock.
