# Experiment 6 — Continuous Integration with GitHub Actions

## Aim
Create a workflow that runs automatically on pushes and pull requests.

## Workflow file
`.github/workflows/ci.yml` triggers on pushes to `main`, pull requests targeting `main`, or manual dispatch. It checks out the repository, sets up Python 3.12, installs `requirements.txt`, and runs pytest.

## Procedure
1. Ensure the workflow and project files are committed.
2. Push to GitHub: `git add .github/workflows/ci.yml requirements.txt src tests`, `git commit -m "Add GitHub Actions CI workflow"`, `git push origin main`.
3. Open the repository's **Actions** tab.
4. Select the newest **Python CI** run and inspect each step's logs.

## Interpretation
A green run means the configured steps completed successfully; it does not prove untested behavior is correct. If a run fails, inspect the first failing step and its log.

## Evidence to capture
Workflow YAML in the repository and the actual run page showing job status and test output.
