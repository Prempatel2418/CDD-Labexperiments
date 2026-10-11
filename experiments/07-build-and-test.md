# Experiment 7 — Automated Build and Testing Workflows

## Aim
Automate a build/check stage and make the test stage wait for that stage to succeed.

## Workflow file
`.github/workflows/build-test.yml` contains:
- a `build` job that installs dependencies and compiles Python source/tests;
- a `test` job with `needs: build`, so it starts only after `build` succeeds;
- push, pull-request, and manual triggers.

## Procedure
1. Review `.github/workflows/build-test.yml`.
2. Commit and push it: `git add .github/workflows/build-test.yml`, `git commit -m "Automate build and test workflow"`, `git push origin main`.
3. Open **Actions**, select **Build and Test**, and inspect both jobs.
4. Confirm `build` passes before `test` starts. If either fails, inspect logs and fix the cause.

## Why compileall is used
The supplied report does not specify a project build system. This repository uses a small Python project, so `python -m compileall -q src tests` is a real syntax/build check and pytest runs meaningful tests.

## Evidence to capture
An actual workflow run showing the build and test jobs and their logs. Do not report a hosted run as successful until you verify it on GitHub.
