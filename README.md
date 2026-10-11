# Git and GitHub Laboratory Experiments

This repository contains practical notes and runnable examples for the seven experiments in the supplied DevOps laboratory report:

1. Git installation, configuration, local repository, staging, commits, and history.
2. Clone, remote, fetch, pull, push, and synchronization.
3. Branching, merging, rebasing, and merge-conflict resolution.
4. GitHub repositories, issues, forks, pull requests, and code reviews.
5. Team collaboration and task-based branching workflow.
6. Continuous integration with GitHub Actions.
7. Automated build and testing workflows.

## Project example used for CI

A small Python calculator under `src/` with tests under `tests/` gives the two GitHub Actions workflows real build/test commands rather than placeholder `echo` statements.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Important evidence note

The written experiment guides explain what to run and where screenshots belong. Screenshots and claims about successful remote operations or GitHub Actions runs must be captured from actual execution; they are not fabricated in this repository. Replace personal/institution placeholders in your report and add your own evidence before submission.

See [`experiments/`](experiments/) for each experiment and [`experiments/COMMAND-CHEATSHEET.md`](experiments/COMMAND-CHEATSHEET.md) for a quick reference.
