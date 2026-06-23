# Ch.15 source-verification log (replication package batch)

Phase 4b-4. Live-verified on the access dates shown. Ch.15 (shipping a
replication package) is almost entirely DOCUMENTED, not executed: the
release + Zenodo steps are QUARANTINED per the CLAUDE.md Zenodo rule
(no real release/DOI cut without the user's explicit approval). The one
LIVE worked example is the book's own repo files (CITATION.cff, LICENSE,
LICENSE-CC-BY-4.0, README.md), which already exist at the repo root and
are shown verbatim. Re-verify before any future edition: AEA policy,
the template README version, Zenodo's GitHub-integration UI, and the
TIER protocol version all drift.

---

## R1. TIER Protocol 4.0 (folder hierarchy + master script)

Access date: 2026-06-23
Source: Project TIER, "TIER Protocol 4.0" (root + overview pages);
BITSS resource page.
URL: https://www.projecttier.org/tier-protocol/protocol-4-0/
      https://www.projecttier.org/tier-protocol/protocol-4-0/root/
      https://www.bitss.org/resources/tier-protocol-4-0/
Used in: Ch.15 (project-structure conventions).

Verified claims: the TIER Protocol specifies the contents and
organization of reproduction documentation for a project that does
computations on statistical data. Everything lives in one Project
folder. Version 4.0's default top-level hierarchy is Data/ (the data in
its various versions), Scripts/ (the command files that process and
analyze), and Output/ (figures, tables, results the scripts generate).
A single Master Script runs the whole pipeline end to end, so a third
party reproduces the project with essentially one command after setting
the working directory. The current version is 4.0 (3.0 is prior).
Presented as one named convention, alongside Gentzkow-Shapiro, not as
the book's own layout.

---

## R2. Gentzkow & Shapiro, Code and Data for the Social Sciences

Access date: 2026-06-23
Source: Gentzkow & Shapiro, "Code and Data for the Social Sciences: A
Practitioner's Guide" (Chicago Booth / NBER), last updated Jan 2014.
URL: https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf
      https://web.stanford.edu/~gentzkow/research/CodeAndData.xhtml
Used in: Ch.15 (project-structure principles).

Verified claims: the guide is a widely cited practitioner's manual whose
sections are Automation, Version Control, Directories, Keys,
Abstraction, Documentation, and Management (plus a Code Style appendix).
Its directory advice: separate inputs from outputs, give each step its
own directory, and automate the whole build so it runs top to bottom
without manual steps. Its "Automation" and "Version Control" chapters
are the same principles this book teaches (a seeded build + Git). Cited
as a principles source, not quoted; the book does not reproduce its
exact directory tree.

---

## R3. AEA Data and Code Availability Policy + openICPSR deposit

Access date: 2026-06-23
Source: AEA "Data and Code Availability Policy" + FAQ; openICPSR AEA
Data and Code Repository deposit instructions; Office of the AEA Data
Editor guidance.
URL: https://www.aeaweb.org/journals/data/data-code-policy
      https://www.aeaweb.org/journals/data/faq
      https://www.openicpsr.org/openicpsr/aea/deposit-instructions
      https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit
Used in: Ch.15 (journal data-editor requirements).

Verified claims: the AEA requires authors of empirical, simulation, or
experimental work to deposit data, code, documentation, and related
materials in a trusted repository before publication, and the package is
checked for compliance by the AEA Data Editor. The AEA Data and Code
Repository at openICPSR is the default/strongly-encouraged home; other
"trusted" repositories are accepted if they meet display + repro
criteria. A Data Availability Statement is required, and when raw or
analysis data cannot be shared (confidential/identifying data, data use
agreements that bar redistribution), the reason must be stated there.
Presented as the concrete instance of "a journal will check this," tied
back to Ch.8 (restricted data) and Ch.6 (never commit restricted data).

---

## R4. Social Science Data Editors template README (v1.1)

Access date: 2026-06-23
Source: Social Science Data Editors, "A template README for social
science replication packages"; AEA Data Editor template-README post;
AEADataEditor/replication-template.
URL: https://social-science-data-editors.github.io/template_README/
      https://social-science-data-editors.github.io/template_README/template-README.html
      https://github.com/social-science-data-editors/template_README
      https://aeadataeditor.github.io/posts/2020-12-08-template-readme
Used in: Ch.15 (the replication-package README).

Verified claims: the template README is the cross-journal best-practice
schema endorsed by data editors at several social-science journals
(current version v1.1; available as Markdown/txt, Word, LaTeX, PDF). Its
use is strongly encouraged, not strictly required: authors may supply
the same information elements in another format. Required information
elements include where the data come from, what data are provided,
software used WITH version numbers as run, additional packages with
versions, the hardware used (OS, CPU, memory, disk), the wall-clock run
time, and step-by-step instructions to reproduce (data prep separate
from analysis), plus a map of which output maps to which exhibit. The
book's point: this is the same code+data+environment recipe from Ch.8,
formalized into a document a stranger can follow.

---

## R5. CITATION.cff 1.2.0 + GitHub "Cite this repository" button

Access date: 2026-06-23
Source: GitHub Docs "About CITATION files"; Citation File Format.
URL: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
      https://citation-file-format.github.io/
Used in: Ch.15 (CITATION.cff; the book's own file is the worked example).

Verified claims: CITATION.cff is a plain-text YAML file (human- and
machine-readable) placed in the repo root. With `cff-version: 1.2.0` and
the minimal fields (message, title, authors), GitHub adds a "Cite this
repository" link in the right sidebar of the default branch and renders
the metadata as APA and BibTeX; reference managers (e.g. Zotero) can
import it. The book's own root CITATION.cff (type: book, CC-BY-4.0,
version 0.1.0, date-released 2026-06-21) is the live example and is
shown verbatim. Matches the file present in the repo at capture time.

---

## R6. Zenodo GitHub integration, concept vs version DOI, size limits

Access date: 2026-06-23
Source: Zenodo Help "GitHub and Software", "Archive a release from
GitHub", "Enable a repository", "FAQ versioning".
URL: https://help.zenodo.org/docs/github/
      https://help.zenodo.org/docs/github/archive-software/github-upload/
      https://help.zenodo.org/docs/github/enable-repository/
      https://zenodo.org/help/versioning
Used in: Ch.15 (minting a citable DOI for the archived release).
Cross-ref: Ch.8 source note (2026-06-21) already pinned Zenodo's 50 GB
per-record limit and the "archive a tagged release" capability; this
note adds the DOI-versioning + enable-repo mechanics.

Verified claims: you connect Zenodo to GitHub and flip a repository
"on"; thereafter each new GitHub RELEASE triggers Zenodo to download the
repo as a ZIP at that tag, create a record, and mint a DOI. Zenodo issues
two DOI kinds: a VERSION DOI for each specific release and a CONCEPT DOI
that always resolves to the latest version (cite the concept DOI for
"the software," the version DOI for the exact version used). Default
per-record limit is 100 files and 50 GB (raisable to 200 GB via the EU
Open Research Repository). QUARANTINE NOTE: cutting a real release + DOI
is permanent and citable; per the CLAUDE.md Zenodo rule the book hands
the user the `git tag` / `gh release create` commands and the Zenodo
enable steps but RUNS NOTHING. No DOI was minted for this repo.
