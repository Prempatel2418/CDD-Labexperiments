# Experiment 3 — Branching, Merging, Rebasing and Conflict Resolution

## Aim
Use branches for parallel work, integrate changes, and resolve a conflict.

## Create and merge a feature branch
```bash
git switch -c feature-login
# Edit or add a file
git add .
git commit -m "Add login feature"
git switch main
git merge feature-login
git branch
git log --oneline --graph --all
```

## Practice a conflict safely
Create a branch and edit the same line differently on both branches:
```bash
git switch -c conflict-side
# Change the target line in shared.txt
git add shared.txt
git commit -m "Change shared line on conflict branch"
git switch main
# Change that same line in shared.txt to different text
git add shared.txt
git commit -m "Change shared line on main"
git merge conflict-side
```
Git may report a conflict. Open the file and remove `<<<<<<<`, `=======`, and `>>>>>>>`, keeping the intended final content. Then run `git add shared.txt`, `git commit -m "Resolve merge conflict"`, and `git status`.

## Rebase
Use a separate feature branch when appropriate:
```bash
git switch feature-login
git fetch origin
git rebase origin/main
```
For a rebase conflict, edit the file, remove markers, then run `git add <conflicted-file>` and `git rebase --continue`. Run `git rebase --abort` to cancel.

**Important:** avoid rebasing commits other collaborators already depend on unless agreed; rebase rewrites commit identities.

## Evidence to capture
Branch list/history graph, conflict markers before resolution, and clean status after resolution.
