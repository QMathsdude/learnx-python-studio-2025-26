## Setup
- `git config --global user.name "Your Name"` — Sets your name for all commits
- `git config --global user.email "you@email.com"` — Sets your email for all commits

## Creating & Cloning
- `git init` — Initialises a new Git repo in the current directory
- `git clone <url>` — Clones a remote repo into a new local directory

## Staging & Committing
- `git status` — Shows working tree status (modified, staged, untracked files)
- `git add <file>` — Stages a specific file
- `git add .` — Stages all changes in the current directory
- `git commit -m "message"` — Commits staged changes with a message
- `git commit -m "message" -m "description"` — Commits staged changes with a message and description
- `git commit --amend` — Edits the most recent commit (message or content)

## Viewing History
- `git log` — Shows full commit history
- `git log --graph` — Shows commit history as a graph

## Branching
- `git branch` — Lists all local branches
- `git branch <name>` — Creates a new branch
- `git checkout <name>` — Switches to a different branch
- `git merge <name>` — Merges a branch into the current branch
- `git branch -d <name>` — Deletes a branch (safe — only if merged)

## Remote
- `git remote -v` — Lists remote connections
- `git push origin <branch>` — Pushes branch to remote
- `git pull` — Fetches and merges changes from remote
- `git fetch` — Fetches changes from remote without merging

## Undoing
- `git restore <file>` — Discards unstaged changes in a file
- `git restore --staged <file>` — Unstages a file (keeps changes)
- `git reset --mixed HEAD` — Resets working tree to last commit (soft, mixed, hard)