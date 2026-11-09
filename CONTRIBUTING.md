# How we work together

Our rules for Git and for working as a team. Read it once, then come back whenever you're unsure.

## Golden rules

1. Never push straight to `main`. Every change goes through a pull request (PR).
2. One card, one branch, one pull request.
3. Numbers come from code, never from the AI.
4. No API keys or passwords in the repo or the frontend. Ever.
5. Stuck for 30 minutes? Ask a teammate. Still stuck? Ask Khair.

---

## Part 1: Git

### First time only

```bash
git clone https://github.com/hizWindy/ph-advisory-weather-app.git
cd ph-advisory-weather-app
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email as your GitHub account so your commits show your name.

### For every card

**1. Get the latest `main`.**

```bash
git switch main
git pull
```

**2. Make a branch for your card.** Name it with the card number and a short description.

```bash
git switch -c 12-city-picker
```

Shortcut: on the issue page, in the right sidebar under **Development**, click **Create a branch**. GitHub names it for you.

**3. Work, and commit in small steps.**

```bash
git status                       # see what changed
git add src/CityPicker.jsx       # pick the files to save
git commit -m "Add city picker dropdown"
```

**4. Push your branch to GitHub.**

```bash
git push -u origin 12-city-picker   # first push of this branch
git push                             # every push after that
```

**5. Open a pull request** on GitHub. Write `Closes #12` in the description, then move your card to **Review**.

**6. Fix review comments** on the same branch: commit and push again. The PR updates by itself.

**7. After it's merged**, clean up:

```bash
git switch main
git pull
git branch -d 12-city-picker
```

### Branch names

| Good | Not good |
|---|---|
| `12-city-picker` | `miguel-branch` |
| `15-heat-level-rules` | `fix` |
| `21-fix-rain-chart-labels` | `test123` |

### Commit messages

- Say what the change does, starting with a verb: `Add heat level rules`, `Fix rain chance rounding`.
- Keep it short, about 50 characters.
- One idea per commit. If the message needs "and", it's probably two commits.
- Avoid: `update`, `changes`, `asdf`, `final na talaga`.

### When `main` has moved on (merge conflicts)

Someone merged before you, and now Git needs your help to combine both changes.

```bash
git switch main
git pull
git switch 12-city-picker
git merge main
```

If Git reports a conflict, open the file. You'll see:

```
<<<<<<< HEAD
your version
=======
the version from main
>>>>>>> main
```

Keep the right code, delete the three marker lines, then:

```bash
git add <file>
git commit --no-edit
git push
```

Not sure which version is right? Ask the person who wrote the other change. Don't guess.

Merging `main` into your branch every day or two keeps conflicts small.

### Be careful with

- **`git push --force`**: don't use it. If Git refuses your push, pull first, or ask.
- **Files that don't belong in Git**: `.env`, `node_modules/`, `.venv/`, `__pycache__/`. Our `.gitignore` already skips them. If `git status` shows one, stop and ask.
- **A key committed by mistake**: tell Khair right away. Deleting the file is not enough, because the key stays in the Git history and has to be replaced.
- **`git restore <file>`**: throws away your uncommitted changes to that file for good.

### Quick reference

| I want to... | Command |
|---|---|
| See what changed | `git status` |
| See the exact lines that changed | `git diff` |
| Get the latest `main` | `git switch main` then `git pull` |
| Start a card | `git switch -c 12-short-name` |
| Save my work | `git add <file>` then `git commit -m "..."` |
| Upload my work | `git push` |
| Unstage a file I added by mistake | `git restore --staged <file>` |
| See recent history | `git log --oneline` |

---

## Part 2: Pull requests and reviews

### Opening a PR

- **Title**: what it does, like `Add Alis-Uwi screen`.
- **Description**: what changed, how you tested it, and `Closes #12`. Add a screenshot if it's a screen.
- **Size**: one card's worth. Big PRs get slow, shallow reviews.
- **Before you open it**: it runs, the card's "Done when" line is true, no leftover debug prints, no keys.

### Reviewing someone's PR

- Khair reviews every PR, ideally within a day. Anyone else is welcome to review too. It's the fastest way to learn the other parts of the app.
- Check: does it do what the card says? Can you follow the code? Anything that could break?
- Be kind and specific. "This breaks when a city has no forecast. Can we show the error message here?" helps more than "this is wrong".
- Ask instead of order: "What happens if the API is slow?"
- Comment on the code, not the person.

### Getting your PR reviewed

- Comments are about the code, not about you. Everyone gets them.
- Reply to every comment: fix it, or explain why not.
- Don't merge your own PR before it's approved. We use **Squash and merge**, so each card becomes one clean commit on `main`.

---

## Part 3: Working as a team

### Talk early

- **Daily standup**, a few minutes: what I did, what I'll do, what's blocking me.
- **Blocked?** Say it the same day in the group chat and add the `blocked` label to your card.
- **Not knowing is normal.** Asking early saves everyone time.

### Handoffs

Each part feeds the next one:

```
MJ (data) → Fredelina (facts) → JC (advice) → Miguel (screens)
                                     Joan (designs) → Miguel
```

- **Agree on the format before you build**: field names, types, examples. Write it in the card. Fredelina and JC agree on the advice function's input and output on day one.
- **Changing something others use?** Tell them before you merge, not after.

### Ownership and backups

You own your part, but the code belongs to the team. Anyone can read it and suggest changes.

| Owner | Backup |
|---|---|
| Joan (design) | Miguel |
| Miguel (frontend) | Joan |
| MJ (data) | Fredelina |
| Fredelina (backend) | JC |
| JC (AI) | Fredelina |

Going to be away? Tell your backup what's in progress and where it is.

Roles rotate at the halfway point, so write things down as if someone else will pick up your part, because someone will.

### Meetings

- **Weekly planning**: pick the cards for the week.
- **Friday demo**: show what works, even if it's small.

### Docs

- Changed how to install or run something? Update the README in the same PR.
- Made a decision? Write it in the card or the PR so others can find it later.
