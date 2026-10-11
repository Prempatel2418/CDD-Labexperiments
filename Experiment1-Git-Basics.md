# Experiment 1 — Installation and Configuration of Git

## Aim
Install/configure Git, create a local repository, and perform basic version-control operations.

## Procedure
1. Verify installation: `git --version`
2. Configure your identity using your own details:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   git config --list
   ```
3. Create a practice repository:
   ```bash
   mkdir git-lab
   cd git-lab
   git init
   ```
4. Create and inspect a file: `echo "Git laboratory exercise" > student.txt`, then `git status`.
5. Stage and commit: `git add student.txt` then `git commit -m "Initial commit"`.
6. Inspect history and status: `git log --oneline` and `git status`.

## Expected observation
The file first appears as untracked, then staged, and after committing the working tree should be clean. The commit appears in `git log --oneline`.

## Evidence to capture
Screenshots of Git version, repository initialization, status, successful commit, and commit history. Capture actual outputs on your machine.
