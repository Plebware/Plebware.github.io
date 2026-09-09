---
layout: post
title: "PlebMachine Master Class — Relearning Systems Coding With AI"
date: 2026-09-09
categories: [study, pleb-tuition]
tags: [plebmachine, ai, coding, linux, xfce, bash, python, systems-architecture, relearning, plebware]
---
<!-- PLEBVOX:START -->

# 🧠 PlebMachine Master Class: Relearning to Code With AI.

Returning to programming after years away can feel rather strange.

The computer has not become simpler.

In fact, it has become considerably more complicated.

But something else has changed.

You now have access to artificial intelligence that can explain code, generate code, inspect errors, suggest solutions, and help you rebuild knowledge that may have gone rusty.

That changes the game.

This Master Class explores how to use AI without surrendering control of the system you are building.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 The Real Subject of This Master Class.

This is not really a lesson about Bash.

It is not really a lesson about Python.

It is not even really a lesson about PlebMachine.

The deeper subject is **how to think about software when working alongside an AI assistant**.

The central principle is simple:

**The AI can be the worker, but the human must remain the architect.**

If the architecture is vague, the AI can make technically plausible changes that damage the system.

If the architecture is clearly defined, the AI becomes an extraordinarily useful development partner.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 1. What Is PlebMachine?

PlebMachine is a lightweight desktop management system designed around the XFCE desktop environment.

Instead of creating one enormous application that controls everything, PlebMachine divides responsibility between small components.

Each component has a specific job.

The graphical interface handles interaction.

Shell scripts handle system operations.

A state file records the current operating state.

Mission Control coordinates the pieces.

This is **modularity**.

And modularity is one of the most important ideas in this entire Master Class.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧩 2. Think in Components, Not in One Giant Program.

Imagine asking an AI:

> "Fix PlebMachine."

That sounds reasonable.

It is actually a dangerous request.

The AI does not automatically know which parts of PlebMachine are sacred, which are experimental, which are deprecated, and which are deliberately separated.

It may decide that the easiest solution is to rewrite several components.

That can produce a system that appears better while quietly destroying the architecture.

A better approach is:

**"Fix this one component while preserving these boundaries."**

That changes everything.

<!-- PLEBVOX:END -->

---

## 🔄 3. Component Interaction Flow.

```text
[ Desktop Launcher / CLI ]
           │
           ▼
[ /opt/plebmachine/ui/splash.py ]
           │
           │ Lock Check & Dependencies
           ▼
         Launch
           │
           ▼
[ mission-control.py ]
           │
           ↕
[ ~/.config/plebmachine/state.conf ]
           │
           │ Mode Selected
           ▼
[ on-mode-change <mode> ]
           │
     ┌─────┼───────────────────────┐
     ▼     ▼                       ▼
mode-     mode-                <mode>-
switch.sh wallpaper.sh         tools.sh
     │     │                       │
     ▼     ▼                       ▼
wmctrl   Wallpaper              Apps /
workspace  engine                Zenity
```

<!-- PLEBVOX:START -->

The important thing is not the individual filenames.

The important thing is the direction of responsibility.

The launcher starts the interface.

The interface communicates with Mission Control.

Mission Control reads and writes persistent state.

The mode-change orchestrator coordinates the actual transition.

Individual shell scripts perform individual jobs.

That is a chain of responsibility.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 4. The Golden Rule: Define the Boundary.

Before asking an AI to modify code, define what that component is **allowed to do**.

For example:

The Python interface may display a window.

It may collect user input.

It may launch a shell command.

But it should not suddenly absorb all of the workspace management logic.

The workspace script has a job.

The wallpaper script has a job.

The mode-tools script has a job.

When each component remains inside its boundary, the entire system becomes easier to understand and repair.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🤖 5. AI-Assisted Relearning.

When returning to programming with an LLM, one of the greatest dangers is not bad syntax.

It is **hallucinated context**.

An AI may know a great deal about Linux.

It may know Bash.

It may know Python.

It may know XFCE.

But that does not mean it knows *your* PlebMachine.

Your directory structure.

Your state model.

Your design decisions.

Your deliberately chosen limitations.

Those things must be supplied by you.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔐 6. The Master System Prompt Guardrail.

A powerful way of preventing architectural drift is to establish a technical constraint envelope before asking the AI to work.

The following prompt can be reused when beginning a serious PlebMachine development session.

<!-- PLEBVOX:END -->

```text
Act as a Principal Linux Systems Architect specializing in
Debian, XFCE4, PyQt/PyGTK, and POSIX shell scripting.

You are assisting with PlebMachine:
a lightweight desktop manager.

Strict Architectural Constraints:

1. Python UI code is restricted to:
   /opt/plebmachine/ui/
   /opt/plebmachine/control-center/

2. Backend execution, workspace switching,
   wallpaper setting, and application triggering
   must remain modular POSIX/Bash shell scripts
   under:
   /opt/plebmachine/bin/

3. Persistent state is maintained solely in:
   ~/.config/plebmachine/state.conf

   Important variables include:
   PM_STATE
   MODE

4. Use native XFCE utilities where appropriate:
   xfconf-query
   wmctrl

5. Use standard dialog tools where appropriate:
   zenity
   yad

6. Do not introduce external Python daemons.

7. Do not introduce heavy external dependencies.

8. Preserve the existing component boundaries.

9. Modify only the component explicitly requested
   unless a dependency requires another change.

10. Before changing architecture, explain why the
    architectural change is necessary.
```

<!-- PLEBVOX:START -->

## 🔑 Why This Prompt Matters.

This prompt does not magically make an AI infallible.

What it does is establish a **contract**.

The AI now has a much smaller area in which it is expected to operate.

That reduces the temptation to solve every problem by rewriting everything.

It also gives you something important when reviewing AI-generated code:

**You can compare the proposed solution against the architectural rules.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧱 7. Component Isolation Strategy.

Never ask an AI:

> "Can you fix this whole system?"

Instead, isolate the component.

Every component should be considered through three questions.

**Input Contract.**

What arguments, variables, files, or state does this component receive?

**Execution Boundary.**

What single job is this component responsible for?

**Output Contract.**

What state change, result, or exit status must it produce?

These three questions turn vague programming problems into engineering problems.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 8. The Input Contract.

The input contract defines what enters a component.

For example:

```text
on-mode-change <mode-id>
```

The script expects a mode identifier.

That gives the AI something concrete to work with.

Instead of:

> "Make mode switching work."

you can say:

> "The script receives one mode ID as argument one. Validate that argument without changing the existing interface."

That is much safer.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 9. The Execution Boundary.

The execution boundary defines what the component actually does.

For `on-mode-change`, the responsibility is orchestration.

It should coordinate:

- State checking.
- Cognitive pause handling.
- Workspace switching.
- Wallpaper application.
- State updating.
- Mode-specific tool launching.

It should not quietly become the entire graphical interface.

It should not replace the state-management system.

It should not absorb unrelated application logic.

One component.

One responsibility.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 10. The Output Contract.

The output contract describes what happens after the component finishes.

That may be:

- A changed workspace.
- A changed wallpaper.
- An updated `MODE`.
- A launched tool suite.
- A successful exit status.
- Or a deliberate failure.

A good AI request therefore describes not merely what should happen, but also what **must remain unchanged**.

That final part is often forgotten.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 💾 11. The State File: PlebMachine's Memory.

PlebMachine needs a persistent representation of its current operating state.

That responsibility belongs to:

```text
~/.config/plebmachine/state.conf
```

A simple state file can look like this.

<!-- PLEBVOX:END -->

```bash
# PlebMachine Dynamic State Configuration
# Updated automatically by Mission Control and on-mode-change

PM_STATE="AUTOMATIC"
MODE="author"
USER_EXPERIENCE="DEFAULT"
```

<!-- PLEBVOX:START -->

The important concept is **single source of truth**.

If one script thinks PlebMachine is in `AUTOMATIC` mode while another thinks it is in `COGNITIVE` mode, the system becomes unpredictable.

A shared state file gives the components a common reference.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## ⚙️ 12. The Three PlebMachine States.

The state model provides three broad operating conditions.

**AUTOMATIC.**

PlebMachine performs normal orchestration without stopping for additional user confirmation.

**COGNITIVE.**

PlebMachine introduces a deliberate pause or confirmation point before important transitions.

This gives the human operator an opportunity to think.

**OFF.**

PlebMachine does not perform automatic mode orchestration.

This is particularly important because an `OFF` state should mean something operationally meaningful.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔀 13. The Orchestrator.

The central mode-change entry point is:

```text
/opt/plebmachine/bin/on-mode-change
```

Its job is not to perform every operation itself.

Its job is to **coordinate the pipeline**.

That distinction is fundamental.

The orchestrator tells the appropriate components what to do.

The individual components do the work.

<!-- PLEBVOX:END -->

---

```bash
#!/usr/bin/env bash
# /opt/plebmachine/bin/on-mode-change
# Central entry point for mode switching.

set -euo pipefail

MODE_ID="${1:-}"
STATE_FILE="${HOME}/.config/plebmachine/state.conf"

if [[ -z "$MODE_ID" ]]; then
    echo "Usage: $0 <mode-id>" >&2
    exit 1
fi

if [[ -f "$STATE_FILE" ]]; then
    source "$STATE_FILE"
else
    PM_STATE="AUTOMATIC"
fi

if [[ "${PM_STATE}" == "OFF" ]]; then
    echo "PlebMachine state is OFF. Aborting mode switch."
    exit 0
fi

if [[ "${PM_STATE}" == "COGNITIVE" ]]; then
    if ! /opt/plebmachine/bin/cognitive-pause.sh; then
        echo "Mode switch cancelled by user."
        exit 0
    fi
fi

/opt/plebmachine/bin/mode-switch.sh "$MODE_ID"
/opt/plebmachine/bin/mode-wallpaper.sh "$MODE_ID"

sed -i "s/^MODE=.*/MODE=\"${MODE_ID}\"/" "$STATE_FILE"

TOOL_SCRIPT="/opt/plebmachine/bin/${MODE_ID}-tools.sh"

if [[ -x "$TOOL_SCRIPT" ]]; then
    "$TOOL_SCRIPT" "$PM_STATE" &
fi
```

<!-- PLEBVOX:START -->

## 🧠 What We Learn From the Orchestrator.

Notice what this script does not do.

It does not contain the entire workspace-switching implementation.

It does not contain the wallpaper-selection algorithm.

It does not contain every application launcher.

Instead, it calls specialised components.

This is exactly what modular architecture is supposed to accomplish.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🖼️ 14. The Wallpaper Engine.

Wallpaper management is another excellent example of component isolation.

The wallpaper engine receives an image path.

Its job is to apply that image.

It should not need to know why a particular mode was selected.

It should not need to know which applications belong to that mode.

It should simply perform its defined task.

<!-- PLEBVOX:END -->

---

```bash
#!/usr/bin/env bash
# /opt/plebmachine/bin/wallpaper-apply.sh
# Applies wallpaper via xfconf-query with feh fallback.

WALLPAPER_PATH="${1:-}"

if [[ ! -f "$WALLPAPER_PATH" ]]; then
    echo "Error: Image file not found: $WALLPAPER_PATH" >&2
    exit 1
fi

if command -v xfconf-query &>/dev/null; then
    MONITORS=$(xfconf-query -c xfce4-desktop -l |
        grep "last-image" || true)

    if [[ -n "$MONITORS" ]]; then
        while read -r prop; do
            xfconf-query -c xfce4-desktop \
                -p "$prop" \
                -s "$WALLPAPER_PATH"
        done <<< "$MONITORS"

        exit 0
    fi
fi

if command -v feh &>/dev/null; then
    feh --bg-fill "$WALLPAPER_PATH"
else
    echo "Error: Neither xfconf-query nor feh could set the wallpaper." >&2
    exit 1
fi
```

<!-- PLEBVOX:START -->

## 🔑 The Important Lesson.

This is a good example of defensive programming.

First, the script checks whether the requested image actually exists.

Then it tries the native XFCE mechanism.

If that is unavailable, it has a fallback.

If neither mechanism exists, it reports a meaningful error.

The component therefore has a clear beginning, middle, and end.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🐧 15. Why POSIX and Bash Components Matter.

PlebMachine deliberately keeps much of its backend logic in shell scripts.

That is not an accident.

Shell scripts are particularly useful for operations involving:

- Files.
- Processes.
- Desktop utilities.
- Environment variables.
- Command-line tools.
- Exit statuses.
- Linux system operations.

A small shell script can therefore perform one system-level operation without requiring a permanent Python service.

That keeps PlebMachine lightweight.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🐍 16. Why Python Still Has a Place.

Python is not being rejected.

It is being **given a defined role**.

PlebMachine can use Python for interfaces and control-centre functions where a richer graphical interaction is useful.

For example:

```text
/opt/plebmachine/ui/
```

and:

```text
/opt/plebmachine/control-center/
```

can contain the graphical interface components.

The important principle is not:

> "Python is bad."

The principle is:

> **Use the right tool for the right layer.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🚫 17. Resist the AI's Favourite Solution: More Code.

One of the easiest traps when working with an AI is accepting complexity simply because the AI can generate it.

You ask for a small fix.

The AI proposes:

- A new Python service.
- A configuration database.
- A background daemon.
- Several new dependencies.
- A new abstraction layer.
- A complete rewrite.

It may all work.

But should it exist?

That is a different question.

PlebMachine's philosophy is deliberately conservative.

**If a small shell script can solve the problem, do not automatically create a new software subsystem.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧪 18. How to Ask AI to Fix a Component.

A strong technical request can follow this pattern.

First, identify the component.

Second, state its current purpose.

Third, describe the observed failure.

Fourth, define what must not change.

Fifth, request the smallest safe modification.

For example:

> "Inspect `mode-wallpaper.sh`. Its responsibility is limited to selecting and applying the wallpaper for a supplied mode ID. Do not modify Mission Control, state management, workspace switching, or the UI. Identify the fault, explain it, and provide the smallest correction."

That is a dramatically better engineering request than:

> "The wallpaper isn't working. Fix PlebMachine."

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔍 19. The Five-Step AI Debugging Method.

When something breaks, use this sequence.

**1. Observe.**

What exactly failed?

**2. Isolate.**

Which component owns that behaviour?

**3. Inspect.**

What inputs does the component receive?

**4. Test.**

Can the component be tested independently?

**5. Modify.**

Only after understanding the failure should the code be changed.

This prevents the classic AI-development mistake of changing five things because one thing failed.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 20. Ask the AI to Explain Before It Changes.

One of the most useful habits when relearning programming is this:

**Ask the AI to explain the existing code before asking it to rewrite the code.**

You can say:

> "Explain this script line by line. Do not modify it."

Then:

> "Identify the likely failure point."

Then:

> "Suggest the smallest possible correction."

Only then:

> "Provide the corrected version."

This sequence turns the AI from a code vending machine into a teaching assistant.

And that is much more valuable when your real objective is to relearn.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧠 21. The Human Still Has to Understand the Machine.

AI makes it tempting to stop learning.

Why learn Bash if the AI can write Bash?

Why learn Python if the AI can write Python?

Why understand Linux if the AI can explain Linux?

Because the moment something goes wrong, someone still has to decide whether the proposed solution makes sense.

The person who understands the architecture can evaluate the AI.

The person who does not understand the architecture can only hope the AI is correct.

That is a very different position.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🛠️ 22. PlebMachine Development Roadmap.

PlebMachine has already established several important foundations.

### Completed.

- [x] Defined the core 12-workspace operational matrix.
- [x] Built modular POSIX shell hooks for workspace manipulation.
- [x] Established the use of `wmctrl`.
- [x] Established the use of `xfconf-query`.
- [x] Established the `state.conf` single-source-of-truth structure.
- [x] Separated interface logic from backend operations.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🚧 23. Present Development Tasks.

Several areas remain suitable for refinement.

- [ ] Refine `mission-control.py` event handling.
- [ ] Use non-blocking `QProcess` execution where appropriate.
- [ ] Standardise Zenity/YAD interfaces across the mode tool scripts.
- [ ] Continue refining `COGNITIVE` mode behaviour.
- [ ] Implement a system-tray indicator for rapid state switching.

These are not reasons to abandon the architecture.

They are opportunities to strengthen it.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🚀 24. Future Development.

The architecture also leaves room for future expansion.

Possible developments include:

### Hardware Profile Awareness.

PlebMachine could detect conditions such as battery state or connected external monitors and respond accordingly.

### PlebWare Integration.

Installation scripts could eventually make deploying PlebMachine and its mode-specific tool suites easier on fresh Debian-based systems.

### Local Productivity Analytics.

Optional, telemetry-free local logging could provide information about workspace usage without sending personal productivity data to an external service.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔐 25. The Principle of Telemetry-Free Design.

There is another lesson hiding inside the roadmap.

Useful analytics do not automatically require cloud analytics.

A local machine can record information for its owner without transmitting that information elsewhere.

For a personal productivity system, that can be an important design principle.

**Collect only what is useful. Keep it local where possible.**

That keeps the system simpler and respects the operator's control over their own information.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🎓 26. What Relearning Programming Really Means.

When you return to programming after a long absence, you may discover that syntax is not actually the biggest problem.

The bigger challenge is rebuilding your mental model.

You need to remember how programs communicate.

You need to understand processes.

You need to understand state.

You need to understand interfaces.

You need to understand failure.

And you need to know where one component should stop and another should begin.

AI can help you rebuild all of that.

But you must remain involved in the reasoning.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 27. The Architect and the Worker.

This is perhaps the most important concept in the entire Master Class.

Think of the relationship this way.

**The human is the architect.**

The human defines:

- The purpose.
- The boundaries.
- The constraints.
- The acceptable dependencies.
- The system state.
- The desired result.

**The AI is the implementation worker.**

The AI can:

- Explain.
- Generate.
- Refactor.
- Compare.
- Debug.
- Document.
- Suggest alternatives.

But the AI should not quietly redefine the architecture.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧰 28. The Master Class Quick Reference.

When working with AI on PlebMachine, remember:

🔑 **Define the architecture first.**

🔑 **Give the AI explicit boundaries.**

🔑 **Work on one component at a time.**

🔑 **Define input, execution, and output contracts.**

🔑 **Ask for explanations before accepting rewrites.**

🔑 **Prefer the smallest safe change.**

🔑 **Do not introduce dependencies without a reason.**

🔑 **Preserve the single source of truth.**

🔑 **Test components independently.**

🔑 **Never confuse working code with good architecture.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧭 29. The Bigger Lesson.

PlebMachine is a practical example of a much larger change taking place in software development.

Programming is becoming increasingly conversational.

You can describe what you want.

An AI can produce a first implementation.

You can test it.

You can explain what went wrong.

The AI can help analyse the failure.

Then you iterate.

But the fundamental engineering questions have not disappeared.

What should this component do?

What should it not do?

Where is the state stored?

Who owns the operation?

What happens when something fails?

What dependencies are acceptable?

Those questions still belong to the architect.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

# 🏁 Conclusion: Keep Your Hands on the Steering Wheel.

Relearning to code in the age of AI is not about memorising every command.

It is about learning how to **think clearly enough to direct the machine**.

PlebMachine demonstrates that principle in a practical way.

Small components.

Clear boundaries.

Persistent state.

Simple tools.

Modular scripts.

A controlled interface.

And an AI that works inside the boundaries established by the human developer.

The result is not merely faster coding.

It is a different way of learning.

You do not have to remember everything.

You need to understand enough to ask the right questions, recognise a dangerous answer, test the result, and maintain control of the architecture.

That is the real skill.

**The AI may write the code.

The architect decides what the code is allowed to become.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 📚 Master Class Principle.

**Design the system.

Define the boundaries.

Isolate the components.

Use AI intelligently.

Test everything.

Keep learning.**

That is how a returning programmer can turn an AI from a shortcut into a genuine development partner.

<!-- PLEBVOX:END -->

---

**PlebWare — Technology should remain connected to humanity.**

**Otto — The Keyboard Is Mightier Than The Pen.**
