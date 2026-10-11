# Experiment 5 — Team Collaboration and Branching Strategies

## Aim
Coordinate a shared project through task-specific branches and pull requests.

## Suggested workflow
1. Clone the team repository: `git clone https://github.com/OWNER/TEAM-REPOSITORY.git` then `cd TEAM-REPOSITORY`.
2. Update main: `git switch main` and `git pull origin main`.
3. Create a task branch: `git switch -c feature/<task-name>`.
4. Edit files, commit, and publish: `git add .`, `git commit -m "Describe the change"`, `git push -u origin feature/<task-name>`.
5. Open a PR into the team's target branch and request a teammate review.
6. Synchronize with new work: `git fetch origin`, `git merge origin/main`.
7. Resolve conflicts, test, and push updates if needed.

## Branching recommendations
- Keep one branch focused on one task.
- Use descriptive names, e.g. `feature/login-form` or `fix/navbar-overflow`.
- Make small commits with clear messages.
- Review diffs and run tests before merging.
- Follow the team's agreed rules for approvals and protected branches.

## Evidence to capture
Feature branch, PR with review feedback, and updated history. A real second collaborator is required to demonstrate a teammate review.
