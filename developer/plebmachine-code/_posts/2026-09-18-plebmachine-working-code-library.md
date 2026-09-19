---
layout: post
title: "PlebMachine Working Code Library — Explainer and Recovery Guide."
date: 2026-09-18
---

<!-- PLEBVOX:START -->

# PlebMachine Working Code: The Safe Way Back.

<!-- PLEBVOX:END -->

PlebMachine is continuously being developed.

That means code gets changed, improved, replaced, tested, and sometimes broken.

That is normal software development.

The problem is not experimentation.

The problem is losing a working version while experimenting.

The **PlebMachine Working Code Library** exists to prevent that.

Its governing principle is simple:

> **If it works, preserve it before experimenting.**

<!-- PLEBVOX:START -->

## 🔑 Working Code Catalogue.

**[Open the PlebMachine Working Code Catalogue](https://plebware.github.io/developer/plebmachine-code/)**

This is the online catalogue of documented, tested, known-good PlebMachine code.


<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## What Is the Working Code Library?

The Working Code Library is an online catalogue of **known-good PlebMachine code**.

It is not a collection of ideas.

It is not a collection of unfinished experiments.

It is not a place to store code merely because it has been written.

Code belongs here because it has been tested and confirmed to work.

The purpose is straightforward:

**When an experiment goes wrong, retrieve the working version and restore it.**

Instead of trying to remember what the previous version looked like, the developer can return to the catalogue, locate the required file, copy the known-good code, and overwrite the experimental version.


<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Three PlebMachine Development Layers.

PlebMachine development can be separated into three distinct areas.

### GitHub — The Workshop.

GitHub is the PlebMachine development workshop.

This is where code is created, modified, committed, tested, and developed.

Changes are expected here.

Experimental work belongs here.

Git history provides an additional record of development.

### Working Code Library — The Safe Shelf.

The Working Code Library contains versions that have been tested and confirmed as working.

These versions are deliberately preserved.

This is the recovery shelf.

### Local PlebMachine — The Test Environment.

The actual PlebMachine installation is where code is executed and tested.

New experimental versions can be installed and tested without destroying the preserved working version.

If the experiment succeeds, it can eventually become the new working version.

If it fails, the known-good version can be restored.


<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Every Working File Gets a Record.

A working file should not simply appear as an unexplained block of code.

Each preserved file should have a clear record describing exactly what it is.

For example:

### `mission-control.py`

- 🔑 **Status:** **WORKING**
- 📅 **Verified:** 2026-09-18
- 💻 **Tested on:** MX Linux / SparkyLinux
- 🧩 **Language:** Python
- 📍 **Installed path:** `/opt/plebmachine/mission-control.py`
- 📝 **Purpose:** Main PlebMachine Mission Control interface
- ⚠️ **Experimental versions:** Keep out of this section.

Then comes the most important part:

> **📋 COPY WORKING CODE**

The complete known-good code follows.

This makes the page useful not only as documentation, but as a practical recovery resource.


<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## What Does “WORKING” Mean?

The **WORKING** status has a specific meaning.

It means the code has been tested in the intended PlebMachine environment and has been confirmed to perform its intended function.

Writing code is not the same as proving that code works.

A script may look correct and still fail when it interacts with:

- The Linux desktop.
- Configuration files.
- Other PlebMachine scripts.
- Installed applications.
- Workspace configuration.
- Display settings.
- Dependencies.
- Another supported Linux distribution.

The Working Code Library therefore records **tested code**, not merely proposed code.


<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Experimental Code Stays Experimental.

Experimental code is an important part of PlebMachine development.

However, experimental code must remain clearly separated from known-good code.

The distinction is:

🟢 **WORKING** — Tested and confirmed.

🟡 **EXPERIMENTAL** — Currently being developed or tested.

🔴 **RETIRED** — Previously used but no longer part of the current working system.

Only **WORKING** code belongs in the Working Code Library.

Experimental versions can continue to exist in the development environment without contaminating the recovery library.

---

## The Recovery Checklist.

When an experimental version breaks a PlebMachine component, use this checklist.

### 🔧 PlebMachine Code Recovery.

- [ ] **Stop experimenting.**
- [ ] **Identify the broken component.**
- [ ] **Identify the exact installed file path.**
- [ ] **Open the [PlebMachine Working Code Catalogue](https://plebware.github.io/developer/plebmachine-code/).**
- [ ] **Locate the matching working file.**
- [ ] **Confirm that the catalogue entry says `Status: WORKING`.**
- [ ] **Check the verification date.**
- [ ] **Check the tested Linux distribution or environment.**
- [ ] **Open `📋 COPY WORKING CODE`.**
- [ ] **Copy the complete preserved working code.**
- [ ] **Back up the currently broken experimental file, if practical.**
- [ ] **Overwrite the experimental file with the known-good code.**
- [ ] **Save the restored file.**
- [ ] **Check file permissions and ownership if applicable.**
- [ ] **Run or restart the affected PlebMachine component.**
- [ ] **Test the component.**
- [ ] **Confirm that PlebMachine is working again.**
- [ ] **Only then resume experimentation.**

### ✅ Recovery Complete.

Once the component has been successfully restored:

- [ ] Confirm the restored version is functioning.
- [ ] Record any useful information about what caused the failure.
- [ ] Keep the restored working version untouched.
- [ ] Continue development from the known-good state.

> **The objective is not to avoid breaking things.**
>
> **The objective is to make breaking things recoverable.**

---

## Working Code Is a Recovery Mechanism.

The Working Code Library is more than documentation.

It is a practical recovery mechanism.

PlebMachine is designed around the idea of known system states and controlled changes.

The same principle applies to its development.

A known-good version gives us a known-good starting point.

That means experimentation becomes safer.

We can make changes.

We can test new ideas.

We can introduce bugs.

And when something goes wrong, we have a documented way back.

---

## The Rule.

The PlebMachine development rule is:

> **If it works, preserve it before experimenting.**

A working version should be:

1. Tested.
2. Verified.
3. Documented.
4. Preserved.
5. Clearly identified as **WORKING**.

Only after that should further experimentation replace or modify it.

This creates a simple development discipline:

**Build → Test → Verify → Preserve → Experiment.**

If the experiment succeeds, the new version can eventually be verified and preserved.

If the experiment fails:

**Restore → Test → Continue.**

---

## What Should Be Preserved?

The library can eventually contain every important PlebMachine component that has reached a known-good state.

Examples include:

- `mission-control.py`
- `splash.py`
- `plebmachine-tools.sh`
- Mode scripts.
- Configuration files.
- State-management scripts.
- Dependency-management scripts.
- User Setup components.
- Desktop integration scripts.
- Recovery utilities.

The same documentation principle should apply to each one.

**What is it?**

**Where does it belong?**

**What does it do?**

**When was it verified?**

**Where has it been tested?**

**Can the complete working code be copied from this page?**

---

## Copy Working Code.

The most important feature of a preserved entry is the complete working source.

The developer should be able to locate the file and immediately see:

**📋 COPY WORKING CODE**

The code presented beneath that heading must represent the preserved working version.

It should not contain experimental modifications.

It should not contain unfinished ideas.

It should not be mixed with unrelated versions.

The purpose is simple:

**Copy it. Replace the broken version. Test it. Continue developing.**

---

## GitHub and the Working Code Library.

GitHub remains the PlebMachine workshop and development repository.

The Working Code Library serves a different purpose.

Git records development history.

The Working Code Library identifies **known-good working states** in a form that is easy to find and use.

These two systems therefore complement one another.

**GitHub tells us where the project has been.**

**The Working Code Library tells us which working code we can safely return to.**

---

## The Goal.

The goal is not to prevent experimentation.

The opposite is true.

The goal is to make experimentation safer.

A developer should be able to try something new without worrying that one failed experiment has destroyed the previous working state.

PlebMachine should always have a reliable way back.

That is what this library provides.

---

## PlebMachine Working Code Catalogue.

### 🔑 Open the Catalogue.

**[PlebMachine Working Code Catalogue](https://plebware.github.io/developer/plebmachine-code/)**

This is the place to find the preserved, known-good PlebMachine code.

As PlebMachine grows, this catalogue will grow with it.

Every important component that reaches a properly tested and verified state can be preserved here.

The principle remains unchanged:

> **If it works, preserve it before experimenting.**

**Known-good code is not just documentation.**

**Known-good code is a recovery tool.**



<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔧 Developer Maintenance Note: Tools Script DRY Refactoring Opportunity.

The PlebMachine tools architecture contains a clear **DRY — Don't Repeat Yourself — maintenance opportunity**.

The older design used approximately twelve mode-specific application-dispatch scripts. Although each script serves a different mode, much of its internal structure is identical: environment initialisation, PlebMachine state parsing, AUTOMATIC versus COGNITIVE handling, Zenity rendering, application dispatch, and common error handling.

The duplication is therefore largely in the **system logic**, while the genuinely different information is the **mode configuration**.

This is a valid refactoring opportunity, but it is a **Low Priority / Maintenance** item. Stability takes precedence over code reduction.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Original Twelve-Script Pattern.

The older architecture can be represented as twelve mode-specific tools scripts: author-tools.sh, study-tools.sh, research-tools.sh, graphics-tools.sh, music-tools.sh, video-tools.sh, broadcast-tools.sh, ai-helpers-tools.sh, developer-tools.sh, accounting-tools.sh, leisure-tools.sh, and everyday-tools.sh.

Each script contains its own copy of the general dispatch machinery. The mode-specific data changes, but much of the processing logic does not.

One important example is the mode-specific case block defining DEFAULT_APP and ZENITY_ITEMS. Another is filename self-inspection, where the script derives the active mode from its own execution name.

The filename mechanism is conceptually:

    SCRIPT_NAME=$(basename "$0" .sh)
    MODE=${SCRIPT_NAME%-tools}

For example, author-tools.sh becomes the author mode.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## From Twelve Implementations to One Common Engine.

The preferred long-term direction is a common tools engine such as /opt/plebmachine/plebmachine-tools.sh.

The common engine would contain the shared system logic: environment initialisation, state loading, mode detection, AUTOMATIC handling, COGNITIVE handling, Zenity interaction, application dispatch, error handling, logging, and common validation.

The mode-specific differences can then become configuration.

Conceptually:

    PlebMachine Tools Engine
              │
              ▼
    plebmachine-tools.sh
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
    Author Graphics Developer
       │      │      │
       └──────┼──────┘
              ▼
       Mode Configuration

This separates **system logic** from **mode configuration**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Symlink Standardization.

A possible implementation is to provide familiar mode-specific entry points as symbolic links to the common engine.

> **One implementation. Multiple entry points.**

However, this must remain a proposal until tested. The installation must confirm that $0 produces the expected mode name, basename behaves correctly, mode detection remains reliable, executable permissions are preserved, packaging preserves the links, and recovery remains straightforward.

A symlink is not automatically safe merely because it points to the correct file.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Where Should Mode Data Live?

There are three practical approaches.

### Option A — One Central Case Block.

Keep one central case block in the common engine. This is already a substantial improvement because the common logic exists only once.

### Option B — Configuration Files.

Move mode-specific information into configuration, such as author.default_app=libreoffice or graphics.default_app=gimp.

### Option C — Hybrid Configuration.

Keep core behaviour in the common engine while configuration supplies default applications, application lists, Zenity menu entries, mode-specific options, and optional tools.

The hybrid approach is consistent with separating stable system logic from user or mode configuration.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Why DRY Matters.

The purpose is not simply to make the source code shorter.

The real benefit is consistency. If a bug exists in common Zenity handling, twelve duplicated scripts potentially have to be inspected and updated. With one common engine, the common logic can be corrected once and the affected modes can then be tested.

The maintenance surface becomes smaller, and the risk of one mode retaining an outdated copy of common logic is reduced.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Refactoring Must Not Break Working Code.

The Working Code Library changes how this refactor should be approached.

A cleaner implementation is not automatically a better implementation if it breaks working behaviour.

The safe sequence is:

    WORKING
       ↓
    PRESERVE
       ↓
    EXPERIMENT
       ↓
    TEST
       ↓
    VERIFY
       ↓
    PROMOTE

If the refactor fails:

    EXPERIMENT
       ↓
      FAIL
       ↓
    RESTORE
       ↓
      TEST
       ↓
    WORKING

The existing working scripts must therefore be preserved before the common engine replaces them.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Proposed Refactoring Sequence.

### Stage 1 — Preserve.

- [ ] Preserve every currently working tools script.
- [ ] Record its verification status and installed path.
- [ ] Record tested environments.
- [ ] Preserve the complete working source.

### Stage 2 — Identify Common Logic.

- [ ] Compare the existing scripts.
- [ ] Identify common functions and state handling.
- [ ] Identify common Zenity and error handling.
- [ ] Separate mode-specific configuration.

### Stage 3 — Build the Common Engine.

Create or verify plebmachine-tools.sh.

### Stage 4 — Test.

- [ ] Test AUTOMATIC.
- [ ] Test COGNITIVE.
- [ ] Test mode detection.
- [ ] Test application dispatch.
- [ ] Test Zenity behaviour.
- [ ] Test configuration loading.
- [ ] Test every supported mode.

### Stage 5 — Test Entry Points.

If symlinks are introduced, test every mode-specific entry point and confirm that $0 is interpreted correctly.

### Stage 6 — Promote.

Only after successful verification should the refactored implementation become the new WORKING version.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## What Must Not Be Lost.

The refactor must preserve AUTOMATIC mode behaviour, COGNITIVE mode behaviour, mode identification, application launching, Zenity menus, existing configuration paths, application mappings, error handling, permissions, supported distributions, installation behaviour, and recovery procedures.

The objective is not:

> Make the script smaller.

The objective is:

> **Remove unnecessary duplication without changing the behaviour that already works.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Developer Decision.

The duplicated mode-specific tools scripts represent a valid **Low Priority / Maintenance** refactoring opportunity.

There is no reason to destabilise a working system merely to remove duplication. The refactor becomes worthwhile when a tools-system change requires touching multiple scripts, a common bug must be corrected, packaging is revised, configuration is redesigned, more modes are introduced, or long-term maintenance becomes unnecessarily difficult.

The preferred direction is one common PlebMachine Tools Engine with mode-specific configuration and, where appropriate, familiar mode-specific entry points provided through symbolic links.

The implementation remains subject to testing.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Rule for This Refactor.

> **If it works, preserve it before experimenting.**

Then:

> **Refactor one controlled component at a time.**

Then:

> **Test before promoting.**

And finally:

> **If the refactor fails, restore the known-good version.**

That turns refactoring into a controlled engineering process rather than a risky replacement exercise.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Build → Test → Verify → Preserve → Refactor.

    BUILD
      ↓
    TEST
      ↓
    VERIFY
      ↓
    PRESERVE
      ↓
    REFACTOR
      ↓
    TEST
      ↓
    VERIFY
      ↓
    PROMOTE

If the refactor fails:

    FAIL
      ↓
    RESTORE
      ↓
    TEST
      ↓
    WORKING

The Working Code Library does not stop development.

**It makes development recoverable.**

<!-- PLEBVOX:END -->
