# Quick Command Reference

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git init
git status
git add .
git commit -m "Describe the change"
git log --oneline --graph --all
git branch
git switch -c feature/name
git switch main
git merge feature/name
git rebase main
git remote -v
git fetch origin
git pull origin main
git push -u origin feature/name
```

For a merge conflict, edit conflicted files, remove markers, run `git add <file>`, then `git commit`. For a rebase conflict, edit files, run `git add <file>`, then `git rebase --continue`; use `git rebase --abort` to cancel.
