# test-commitizen-action
This is a test on how to use commitizen on github actions.

# General Notes
- ONLY change the version on a change in main.
- if building assets, probs have a separate release.yml build file that works only when main is pushed?

```yml
name: Bump version

on:
  push:
    branches:
      - stagin
```

- due to auth issues, i've decided to create an undeletable staging branch. this preserves pull request requirements for main whilest still generating a releases file using commitizen github actions. 
  - staging can be run at any random time - pull's can be made whenever even by pulling from main. 
  - releases watch for changes in staging.
  - release artifacts are also generated as per usual