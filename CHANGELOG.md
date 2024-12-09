## 0.5.5 (2024-12-04)

### Fix

- **release.yml**: reorganize artifact download steps and append version to filenames
- **release.yml**: remove duplicate artifact download steps and improve workflow clarity

## 0.5.4 (2024-12-04)

### Fix

- **release.yml**: update output file naming and artifact handling in release workflow

## 0.5.3 (2024-12-04)

### Fix

- **release.yml**: update output file naming in info script and artifact upload
- **release.yml**: correct path parameter in upload-artifact action
- **release.yml**: add dependency for bump-version job on generate-sys-files
- **release.yml**: update upload-artifact action to version 4 in release workflow

## 0.5.2 (2024-12-04)

### Fix

- **release.yml**: redirect output of main.py to os_version.txt and include python_version.txt in release files

## 0.5.1 (2024-12-04)

### Fix

- **release.yml**: add step to capture Python version in workflow
- **release.yml**: update script execution to use main.py instead of info.py
- **main.py**: add shorthand flags for os and python version arguments

## 0.5.0 (2024-12-04)

### Feat

- **main.py**: add CLI to print OS and Python versions

### Fix

- **release.yml**: change trigger branch from main to staging for version bump
- **release.yml**: update GitHub token to use GITHUB_TOKEN and enable push for changelog generation
- **release.yml**: update GitHub token to use PERSONAL_ACCESS_TOKEN for changelog generation
- **release.yml**: update GitHub token to use DEPLOY_KEY for changelog generation
- **release.yml**: added os and python ver printout on script

## 0.4.0 (2024-12-01)

### Feat

- **release.yml**: added os release on seperate branch tot est pull req's

## 0.3.1 (2024-12-01)

### Refactor

- **release.yml**: add newlines for better readability in workflow steps

## 0.3.0 (2024-12-01)

### Feat

- **release.yml**: added release file w/ printout as archive

### Fix

- **release.yml**: fixing release syntax problem
- **release.yml**: update action-gh-release to v2 and correct file input syntax

## 0.2.0 (2024-12-01)

### Feat

- **release.yml**: adding release build

## 0.1.0 (2024-12-01)

### Feat

- **README.md**: updated docs
