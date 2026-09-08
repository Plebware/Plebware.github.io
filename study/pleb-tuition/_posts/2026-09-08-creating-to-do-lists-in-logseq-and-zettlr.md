---
layout: post
title: "Creating To-Do Lists in Logseq and Zettlr"
date: 2026-09-08
categories: [study, pleb-tuition]
tags: [logseq, zettlr, markdown, todo-lists, productivity, note-taking, plebware]
---
<!-- PLEBVOX:START -->

# 📋 Creating To-Do Lists in Logseq and Zettlr.

A to-do list sounds like one of the simplest things in computing.

Write down what needs doing.

Tick it off when it is finished.

But different applications approach this simple idea in very different ways.

Two particularly useful tools for Markdown-based work are **Logseq** and **Zettlr**.

Both can handle tasks, but they are designed around different philosophies.

Logseq is much more task-oriented.

Zettlr is much more focused on writing and ordinary Markdown.

Understanding the difference makes it easier to decide which tool should handle which part of your workflow.

---

## 🔑 1. Creating Tasks in Logseq.

Logseq treats tasks as blocks.

A simple task can be written like this:

```text
TODO Write the PlebMachine article
```

You can create several tasks:

```text
TODO Write today's article
TODO Check the GitHub repository
TODO Update the PlebVox markers
TODO Back up important files
```

Logseq can then track the state of those tasks.

A typical workflow can look like:

```text
TODO → DOING → DONE
```

This makes Logseq particularly useful when your notes and your tasks are closely connected.

---

## 🔑 2. Changing a Task's Status.

In Logseq, a task can move through different states as the work progresses.

For example:

```text
TODO Write the PlebMachine article
```

can become:

```text
DOING Write the PlebMachine article
```

and eventually:

```text
DONE Write the PlebMachine article
```

Logseq also supports other task states and workflows.

This is one of the major advantages of Logseq over a basic Markdown checklist.

You are not simply marking something with a tick.

You are recording the state of the work.

---

## 🔑 3. Adding Priorities in Logseq.

Logseq can also assign priorities to tasks.

For example:

```text
TODO [#A] Publish the PlebMachine article
TODO [#B] Clean up old notes
TODO [#C] Read the documentation
```

The letters indicate different levels of priority.

A simple system might be:

**A** — Important.

**B** — Normal.

**C** — Low priority.

This can be useful when a to-do list starts becoming larger than your working memory.

---

## 🔑 4. Using the Logseq Journal.

One of Logseq's most useful features is its Journal.

Instead of keeping every task in a separate master list, you can record tasks on the day you actually think of them.

For example:

```text
## Tuesday, 8 September 2026

TODO [#A] Publish the Sleep and Wellbeing article
TODO Check PlebVox markers
TODO Review Fitness Pro report

Notes:
- Investigate Zettlr task management.
- Update PlebMachine documentation.
```

Now the task is associated with that day's notes.

This creates a useful combination of diary, notebook, research system, and task manager.

---

## 🔑 5. Creating To-Do Lists in Zettlr.

Zettlr takes a simpler approach.

Instead of using Logseq's special task states, Zettlr uses ordinary Markdown checkboxes.

An unfinished task looks like this:

```markdown
- [ ] Write the PlebMachine article
```

A completed task looks like this:

```markdown
- [x] Write the PlebMachine article
```

A complete list might therefore look like this:

```markdown
- [ ] Write the PlebMachine article
- [ ] Check the GitHub repository
- [ ] Update PlebVox
- [x] Publish the Sleep article
```

This is standard Markdown.

That means the checklist remains readable even if you open the file in another Markdown editor.

---

## 🔑 6. Creating Nested Tasks in Zettlr.

Markdown checklists can also be organised into projects.

For example:

```markdown
# PlebMachine Release.

- [ ] Prepare release.
  - [ ] Check installation script.
  - [ ] Check wallpapers.
  - [ ] Check Mission Control.
  - [ ] Test on old computer.
- [ ] Build the Debian package.
- [ ] Create the GitHub release.
- [ ] Write release notes.
- [ ] Publish announcement.
```

This creates a simple hierarchy.

The main task describes the project.

The indented tasks describe the individual jobs required to complete it.

---

## 🔑 7. Logseq or Zettlr?

Neither application is necessarily better.

They are simply better suited to different jobs.

| Feature | Logseq | Zettlr |
|---|---|---|
| Basic checklist | Yes | Yes |
| TODO / DOING / DONE | Yes | No |
| Task priorities | Yes | Manual |
| Journal integration | Excellent | Manual |
| Task queries | Powerful | Limited |
| Plain Markdown | Extended Markdown | Excellent |
| Writing long documents | Good | Excellent |
| Task management | Excellent | Basic |

If your main question is:

**"What do I need to do?"**

Logseq is probably the stronger choice.

If your main question is:

**"What am I writing?"**

Zettlr is probably the stronger choice.

---

## 🔑 8. A Practical PlebWare Workflow.

For a PlebWare workflow, the two applications can complement each other rather than compete with each other.

Think of them as different stations in the same workshop.

### 🧠 Logseq — The Command Centre.

Use Logseq for things that need doing.

```text
TODO PlebMachine
  TODO Fix wallpaper switching
  TODO Test Cognitive Mode
  TODO Investigate Stretchly
  TODO Update documentation

TODO PlebWare Website
  TODO Write article
  TODO Add PlebVox markers
  TODO Test article
  TODO Publish

TODO Writing
  TODO Science-fiction project
  TODO Christian writing
  TODO News articles
```

Logseq becomes the place where you ask:

**What must I do?**

### ✍️ Zettlr — The Writing Workshop.

Use Zettlr for writing the actual Markdown documents.

For example:

```markdown
---
layout: post
title: "Sleep and Wellbeing."
date: 2026-09-08
---

<!-- PLEBVOX:START -->

# Sleep Is Not Wasted Time.

Your article goes here.

<!-- PLEBVOX:END -->
```

Zettlr can also contain publication checklists:

```markdown
## Publication Checklist.

- [x] Write article.
- [x] Proofread.
- [x] Add PlebVox markers.
- [ ] Test locally.
- [ ] Commit to GitHub.
- [ ] Publish.
```

---

## 🔑 9. The Three-Stage PlebWare Workshop.

The distinction becomes especially useful when combined with GitHub.

Think of the workflow as three stations:

**Logseq → What must I do?**

**Zettlr → What am I writing?**

**GitHub → What have I published?**

That gives you a simple progression:

```text
IDEA
  ↓
LOGSEQ
What needs doing?
  ↓
ZETTLR
Write and edit the Markdown.
  ↓
GITHUB
Commit and publish.
  ↓
PLEBWARE
The finished article appears on the website.
```

The tools therefore have different responsibilities.

You don't need to force one application to do everything.

---

## 🔑 10. Why Markdown Makes This Possible.

There is another important advantage to this approach.

Markdown is plain text.

A task such as:

```markdown
- [ ] Write the article.
```

is not locked inside a proprietary database.

It is simply text.

The same file can be opened, edited, copied, backed up, version-controlled, and published using different tools.

That is particularly valuable for PlebWare because Markdown is already part of the publishing system.

The same basic language can therefore serve as the bridge between:

**Notes.**

**Tasks.**

**Articles.**

**Documentation.**

**GitHub.**

And ultimately:

**The PlebWare website.**

---

## 🔑 Quick Reference.

### Logseq.

Use:

```text
TODO Task
DOING Task
DONE Task
```

For priority:

```text
TODO [#A] Important task
TODO [#B] Normal task
TODO [#C] Low-priority task
```

### Zettlr.

Use:

```markdown
- [ ] Unfinished task.
- [x] Finished task.
```

For nested tasks:

```markdown
- [ ] Main project.
  - [ ] First task.
  - [ ] Second task.
  - [ ] Third task.
```

The basic rule is simple:

**Logseq is excellent for managing the work.**

**Zettlr is excellent for writing the work.**

And Markdown provides the common language that keeps the whole system portable.

---

## 🔑 Final Thought.

A good productivity system should not make life more complicated.

It should make complicated work easier to understand.

Logseq gives you a way to see the work that needs doing.

Zettlr gives you a clean environment in which to write.

GitHub gives you version control and a publishing platform.

Together, they form a surprisingly powerful little workshop.

And like any good workshop, the goal isn't to admire the tools.

The goal is to **build something with them.**

<!-- PLEBVOX:END -->
