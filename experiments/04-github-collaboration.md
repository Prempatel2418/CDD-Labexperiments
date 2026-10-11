# Experiment 4 — Repositories, Issues, Forks, Pull Requests and Reviews

## Aim
Use GitHub collaboration features to track work and review contributions.

## Procedure
1. Create or open a GitHub repository. Add a README if appropriate.
2. Open **Issues → New issue** and provide a clear title, description, and label.
3. If you lack write access to another person's repository, click **Fork**.
4. Clone your fork and create a branch:
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPOSITORY.git
   cd REPOSITORY
   git switch -c feature-update
   ```
5. Make a meaningful change, then run `git add .`, `git commit -m "Implement requested update"`, and `git push -u origin feature-update`.
6. Open **Pull requests → New pull request**, choose the head and base branches, describe the change, and link the issue (e.g. `Closes #1`).
7. Review the diff, comment or request changes, and push follow-up commits to update the PR.

## Concepts
- **Issue:** tracks a task, bug, or enhancement.
- **Fork:** a separate copy under another account.
- **Pull request:** proposes changes for discussion and integration.
- **Review:** feedback before merging.

## Evidence to capture
Issue, fork, PR conversation/diff, and review screen. Use real screenshots from your GitHub account.
