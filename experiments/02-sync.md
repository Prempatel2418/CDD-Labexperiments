# Experiment 2 — Clone, Push, Pull, Fetch and Synchronization

## Aim
Copy a remote repository and synchronize local and remote changes.

## Procedure
1. `git clone https://github.com/OWNER/REPOSITORY.git` then `cd REPOSITORY`.
2. Inspect remotes and branch: `git remote -v`, `git branch`.
3. Fetch remote references without merging: `git fetch origin`, `git status`.
4. Integrate updates: `git pull origin main`.
5. Edit a file, then stage, commit, and push: `git add .`, `git commit -m "Update project files"`, `git push origin main`.

## Key distinction
- `fetch` downloads remote commits and updates remote-tracking references but does not merge into the current branch.
- `pull` fetches and integrates changes into the current branch.
- `push` publishes local commits to a remote branch.

Use the real repository URL and branch. If you lack write access, push to a fork and open a pull request.

## Evidence to capture
Clone output, `git remote -v`, fetch/pull output, and the GitHub commit page after a successful push.
