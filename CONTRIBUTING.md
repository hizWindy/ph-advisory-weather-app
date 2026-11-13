# How we work together

Our rules for Git, pull requests and teamwork. Read it once, then come back whenever you're unsure.

Also read:
- [docs/project-structure.md](docs/project-structure.md): where files go and who owns them
- [docs/github-projects-kanban.md](docs/github-projects-kanban.md): how our task board works

## Golden rules

1. Never push straight to `main`. Every change goes through a pull request (PR).
2. One card, one branch, one pull request.
3. Never put API keys or passwords in the code, the repo or the group chat.
4. Numbers come from code, never from the AI.
5. Work in your own folder. Ask before you change someone else's.
6. Stuck for 30 minutes? Ask a teammate. Still stuck? Ask Khair.

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

**4. Push your branch to GitHub.** First check that you're on your branch, not `main`. `git branch` puts a `*` next to the branch you're on.

```bash
git branch                           # check: * 12-city-picker
git push -u origin 12-city-picker    # first push of this branch
git push                             # every push after that
```

**5. Open a pull request** on GitHub. See Part 2.

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
- **`git restore <file>`**: throws away your unsaved changes to that file for good.
- **Files that don't belong in Git**: see "Files" in Part 3.

### Quick reference

| I want to... | Command |
|---|---|
| See what changed | `git status` |
| See the exact lines that changed | `git diff` |
| See which branch I'm on | `git branch` |
| Get the latest `main` | `git switch main` then `git pull` |
| Start a card | `git switch -c 12-short-name` |
| Save my work | `git add <file>` then `git commit -m "..."` |
| Upload my work | `git push` |
| Unstage a file I added by mistake | `git restore --staged <file>` |
| See recent history | `git log --oneline` |

---

## Part 2: Pull requests and reviews

A pull request (PR) asks the team to check your branch and add it to `main`. You never add to `main` yourself. Khair merges your PR after it's approved.

```
your branch → pull request → review → Khair merges → your work is in main
```

### Two ways to open a PR

**On the GitHub website (no terminal needed).** Good for docs, `DESIGN.md`, small fixes and your first PR.

1. Open the repo on GitHub and go to the right folder.
2. Click **Add file**, then **Create new file**. To change a file that already exists, open it and click the pencil icon.
3. Make your change.
4. Click **Commit changes**. Choose **Create a new branch for this commit and start a pull request**. Name the branch with your card number, like `6-hello-joan`.
5. Click **Propose changes**, then **Create pull request**.

**From your laptop.** After `git push`, open the repo on GitHub. Click the yellow **Compare & pull request** button.

Either way, move your card to **Review** after you open the PR.

### What to write in a PR

- **Title**: what it does, like `Add Alis-Uwi screen`.
- **Description**: what changed, how you tested it, and `Closes #12`. `Closes #12` links the PR to card 12 and closes the card when the PR is merged.
- **Screenshot** if it's a screen.
- **Size**: one card's worth. Big PRs get slow, shallow reviews.

Example:

```
Adds the city picker dropdown.

How I tested: ran npm run dev, picked Manila and then Cebu.
The forecast changed each time.

Closes #16
```

**Before you open it, check:**
- It runs on your laptop.
- Everything in the card's "Done when" list is true.
- No test prints left (`print`, `console.log`).
- No keys or passwords anywhere.

### When many PRs are open at once

That's normal. Khair merges them one at a time.

- PRs that change different files don't affect each other.
- If two PRs change the same file, the second one may say **This branch is out-of-date** or **This branch has conflicts**. The person who opened that PR fixes it: click **Update branch** on the PR page, or follow "When `main` has moved on" in Part 1.
- PRs that someone else is waiting for get merged first.

### Reviewing someone's PR

- Khair reviews every PR, ideally within a day. Your review buddy reviews too, and anyone else is welcome. It's the fastest way to learn the other parts of the app.
- Open the PR, click **Files changed**, read it, then click **Review changes** and choose **Approve** or **Request changes**.
- Check: does it do what the card says? Can you follow the code? Could anything break?
- Be kind and specific. "This breaks when a city has no forecast. Can we show the error message here?" helps more than "this is wrong".
- Ask instead of order: "What happens if the API is slow?"
- Comment on the code, not the person.

### Getting your PR reviewed

- Comments are about the code, not about you. Everyone gets them.
- Reply to every comment: fix it, or explain why not.
- Don't merge your own PR. Khair clicks **Squash and merge**, so each card becomes one clean commit on `main`.

---

## Part 3: Rules and good practices

### Keys and passwords

- Keys, passwords and database links go in a file called `.env` on your laptop. Git skips that file, so it never reaches GitHub.
- Never put a key in the code, the frontend, a README, an issue, a PR, a screenshot or the group chat.
- Your code reads the key from `.env`:

  ```python
  import os
  from dotenv import load_dotenv

  load_dotenv()  # reads your .env file

  # Good: get the key from .env
  api_key = os.getenv("OPENROUTER_API_KEY")

  # Never do this
  api_key = "sk-or-v1-abc123..."
  ```

- Adding a new setting? Put its name in `.env.example` with no value, like `OPENROUTER_API_KEY=`. Then everyone knows they need it.
- The frontend never holds keys. Anyone who opens the app can read the frontend's code. The frontend asks our backend, and only the backend uses the key.
- Need a key? Ask Khair in a private message.
- Shared a key by mistake? Tell Khair right away. Deleting it isn't enough, because Git keeps old versions. The key has to be replaced.

### Personal information

- Interview notes: no full names, phone numbers, addresses or photos. Write "Student, 19, Cebu" instead.
- Don't put anyone's personal information in code, issues or PRs, including your own.

### Code

- Run it before you open a PR. If it doesn't work on your laptop, it isn't ready.
- Use clear names: `rain_chance`, not `x` or `data2`.
- Keep it simple. Simple code that works beats clever code.
- Remove test prints and old commented-out code before your PR.
- Add a comment when the reason isn't obvious. Say why, not what.
- Ask the folder's owner before you add a new package.
- Only commit code you can explain. You'll walk through it at the demo.
- AI tools like ChatGPT or Claude are fine for learning. Read and understand every line before you commit it.

### Files

- Never commit `.env`, `node_modules/`, `.venv/` or `__pycache__/`. Our `.gitignore` skips them. If `git status` shows one, stop and ask.
- Keep images under 1 MB each. Don't put videos in the repo. Share a link instead.
- Put files where [docs/project-structure.md](docs/project-structure.md) says.

### What the app says

- Numbers come from code, never from the AI.
- The app never predicts class or work suspensions.
- For storms and warnings, always point people to PAGASA.
- The severe weather banner is fixed text, not AI.
- The heat level is our estimate, not PAGASA's heat index. The app says so.

---

## Part 4: Working as a team

### Who works where

Each person owns their folders. [docs/project-structure.md](docs/project-structure.md) shows every folder, who owns it, and the shared files where you need to be careful.

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

### Testing and bugs

Angela checks everyone's work and keeps the docs. Angela reads and runs every part of the app, but only changes the testing and docs files. When something is wrong, Angela reports it and the owner fixes it.

- **Before merge:** if your PR changes what people see (a screen) or what the app says (a payo, an endpoint), add Angela as a reviewer. Angela runs it and checks the card's "Done when" list. Khair still does the final review and the merge.
- **After merge:** Angela tests the feature on `main` using `docs/test-plan.md`.
- **Found a bug:** Angela opens a **Bug report** issue (steps, what should happen, what happened), adds the `bug` label and assigns the owner. Khair decides if it gets fixed now or later.
- **Fixing a bug** works like any other card: a branch like `31-fix-rain-rounding`, a PR with `Closes #31`, and Angela as a reviewer to retest it before it's merged.
- **The AI check:** Angela compares every payo with the raw numbers. If the payo says rain, the rain chance must really be high. If it isn't, that's a bug for JC (the words) or Fredelina (the facts).

### Ownership and backups

You own your part, but the code belongs to the team. Anyone can read it and suggest changes.

| Owner | Backup |
|---|---|
| Joan (design) | Miguel |
| Miguel (frontend) | Joan |
| MJ (data) | Fredelina |
| Fredelina (backend) | JC |
| JC (AI) | Fredelina |

Going to be away? Tell your backup what you're working on and where it is.

Roles rotate at the halfway point, so write things down as if someone else will pick up your part, because someone will.

### Meetings

- **Weekly planning**: pick the cards for the week.
- **Friday demo**: show what works, even if it's small.

### Docs

- Changed how to install or run your part? Update your folder's README (`frontend/README.md` or `backend/README.md`) in the same PR. Angela keeps the main README pointing to them.
- Made a decision? Write it in the card or the PR so others can find it later.
