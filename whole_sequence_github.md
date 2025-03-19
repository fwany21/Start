# Workflow Diagram Using Mermaid.js

```mermaid
sequenceDiagram
    participant Upstream as Original GitHub Repo (upstream)
    participant Origin as Forked GitHub Repo (origin)
    participant Local as Local Machine
    participant CI as CI/CD System

    Upstream ->> Origin: Fork repository
    Origin ->> Local: Clone forked repository
    Local ->> Local: Add upstream remote (`git remote add upstream [url]`)
    Upstream ->> Local: Pull updates from upstream (`git pull upstream main`)
    Local ->> Local: Make changes and commit
    Local ->> CI: Run pre-commit checks (Linting, Tests)
    CI ->> Local: Validation Results
    Local ->> Origin: Push changes to forked repo (`git push origin feature-branch`)
    Local ->> Origin: Create pull request
    Origin ->> CI: Run automated tests and build pipeline
    CI ->> Origin: Test Results
    Origin ->> Upstream: Submit pull request for merge
    Upstream ->> Upstream: Conduct code review
    Upstream ->> Local: Request changes or approve PR
    Local ->> Origin: Push updated changes (if needed)
    Origin ->> Upstream: Resubmit PR
    Upstream ->> Upstream: Merge pull request
    Upstream ->> Upstream: Tag release version (`git tag -a v1.0 -m "Release"`)
    Upstream ->> Local: Update local repository with changes (`git pull upstream main`)
