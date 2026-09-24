# PlebMachine AI Instructions

## PlebMachine AI Manifesto

These instructions govern AI assistants working on the design, development, testing, maintenance, documentation, and evolution of PlebMachine.

The AI is an assistant to the human designer. It is not the owner of PlebMachine, the computer, the repository, or the project direction.

**PlebMachine provides context. The user provides purpose.**

---

# PART I — MANDATORY RULES

## 1. Human Authority Comes First

The human designer has final authority over PlebMachine.

AI may analyse, propose, explain, implement, test, document, and identify problems, but it must not replace the designer's decisions or silently redefine the project.

## 2. PlebMachine Is a State-Driven Linux Desktop Orchestration System

PlebMachine is a state-driven Linux desktop orchestration system.

Its purpose is to provide context through the desktop environment, applications, workspaces, configuration, and supporting resources so that the computer can better reflect the user's current purpose.

## 3. User Ownership and Control

The user owns the computer.

PlebMachine must never behave as though it owns the computer or has unrestricted authority over it.

The user must remain able to understand, control, recover, and use the underlying Linux system.

## 4. PlebMachine Must Never Uninstall Non-PlebMachine Software

PlebMachine must **never uninstall, remove, or deliberately delete software that is not a PlebMachine component**.

PlebMachine may uninstall a PlebMachine component only when that component is part of the **original Debian package from which that PlebMachine component was installed**.

PlebMachine must not remove user applications, unrelated software, system software, arbitrary dependencies, or other software merely because it is unused, inconvenient, or no longer required by a PlebMachine component.

Package ownership and installation origin must be established before any PlebMachine uninstall operation.

## 5. PlebMachine Is Not a Monolith

PlebMachine is a collection of cooperating components.

Major PlebMachine components must be treated as standalone applications, even when they communicate with or pass information to other PlebMachine components.

Communication does not make separate components one application.

## 6. PlebMachine Component Design Order

The established component design order is:

1. **PlebDecide** — importance 9/10
2. **PlebControler — Mission Control** — importance 9/10
3. **PlebGizmo** — importance 7/10
4. **PlebBeaks** — importance 8/10
5. **PlebTools** — importance 10/10

Design order and importance rating are separate concepts.

AI must not reorder the development sequence merely because a component has a higher or lower importance rating.

## 7. PlebControler — Mission Control

PlebControler, Mission Control, is the coordinating heart of PlebMachine.

Mission Control coordinates. It does not own.

It may coordinate states, modes, desktop configuration, workspaces, wallpapers, application launching, and communication between components, but it must not become a monolithic owner of unrelated functionality.

## 8. PlebMachine States

PlebMachine has an OFF condition and three active states:

- **COGNITIVE**
- **AUTOMATIC**
- **ADVANCED**

OFF is the absence of an active PlebMachine operating state, rather than one of the three active states.

Cognitive Mode is a pause or speed-bump, not a lockdown. Normal desktop facilities such as the right-click menu and Start Menu must remain usable.

## 9. PlebMachine Modes

PlebMachine provides twelve established modes:

1. Everyday
2. Author
3. Study
4. Research
5. Graphics
6. Music
7. Video
8. Broadcast
9. AI Helpers
10. Developer
11. Accounting
12. Leisure

These modes provide context for the desktop and its working environment.

## 10. Desktop Baseline and Recovery

The PlebMachine baseline primarily concerns the desktop environment.

It includes desktop elements such as XFCE panels, launchers, wallpaper, workspaces, and managed desktop settings.

The baseline must not be interpreted as ownership or control of everything on the computer.

PlebMachine must support recovery of the managed desktop state.

## 11. State and Configuration

PlebMachine state and configuration must be explicit, inspectable, and recoverable.

Configuration should remain understandable to the user and must not be hidden inside unnecessary mechanisms.

User-writable configuration should remain user-writable and must not require unnecessary administrative privilege.

## 12. Dynamic Application Discovery

Where appropriate, PlebMachine should discover available applications dynamically rather than relying on unnecessarily rigid lists.

Discovery must respect the distinction between applications that exist, applications that are available, applications that are configured, and applications that PlebMachine itself manages.

## 13. Setup Must Be Rerunnable

PlebMachine setup must be safely rerunnable.

Running setup again should repair or complete an installation rather than assuming that the system is permanently in its first-install state.

Setup must avoid unnecessary duplication and destructive behaviour.

## 14. Filesystem Architecture

The filesystem architecture must preserve the established separation of responsibilities.

Major executable PlebMachine scripts and runtimes are located under `/opt`.

Shared resources such as wallpapers, icon sets, sounds, and similar assets belong under the appropriate `/usr` or `/usr/local/share` locations.

Do not invent new filesystem conventions without a design reason and approval.

## 15. Repository Architecture

The repository architecture should reflect the actual PlebMachine filesystem architecture where appropriate.

In particular, `opt/` and `usr/` are meaningful parts of the project's architecture and must not be treated as arbitrary directory names.

## 16. Legacy Code Is Evidence, Not Automatically Current Code

Legacy code must be examined and classified individually.

Legacy material may be:

- retained,
- adapted,
- replaced,
- rejected,
- experimental,
- deprecated,
- or confirmed as working.

Legacy code must not be promoted into the current architecture merely because it already exists.

## 17. Protect Working Code

Working code must be protected.

AI must distinguish between code that:

- exists,
- runs,
- has been tested,
- has been verified,
- is experimental,
- is proposed,
- is deprecated,
- or is legacy.

A working component must not be casually replaced by an untested alternative.

## 18. Development Workflow

The established development workflow is:

**Understand → Inspect → Discuss → Design → Implement → Test → Document → Verify**

AI should follow this sequence unless the human designer explicitly directs otherwise.

## 19. Testing Is Part of Development

Testing is not an optional final decoration.

AI must distinguish between code that has merely been written and code that has actually been run and tested.

Where possible, testing must occur on the intended supported Linux environments.

## 20. Dependencies

PlebMachine should use the minimum appropriate dependencies.

Dependencies must have a reason to exist.

Do not introduce dependencies merely for convenience when an existing system facility or simpler solution is sufficient.

## 21. Security and Privilege

Avoid unnecessary privilege escalation.

PlebMachine must not use administrative privileges where ordinary user privileges are sufficient.

Operations requiring privilege must have a clear reason and must be constrained to their intended purpose.

## 22. No Silent Architectural Changes

AI must not silently change the architecture.

If an implementation requires an architectural change, the change must be identified and discussed with the human designer before it is treated as the new architecture.

## 23. No Feature Creep

Do not introduce feature creep.

A useful idea is not automatically an approved requirement.

New functionality must remain within the agreed scope unless the human designer approves the expansion.

## 24. Documentation

Documentation must describe what actually exists and what has actually been tested.

Do not document proposals as though they were implemented features.

Do not claim a feature works merely because code for it exists.

## 25. Git and Repository Discipline

Inspect the repository before making significant changes.

Preserve working material.

Use version control deliberately.

Do not perform mass changes merely for convenience.

When repository publication or modification is requested, make the actual change and verify the result before claiming it has been published.

## 26. Fact, Design, Proposal, Implementation, and Test Result

AI must distinguish clearly between:

- established fact,
- approved design,
- proposal,
- implementation,
- test result,
- and experimental work.

These categories must not be blurred.

## 27. Do Not Invent Missing Architecture

If an architectural detail is missing, do not invent it and present it as established fact.

Inspect the repository, existing code, documentation, and configuration where possible.

If the answer is still unknown, identify the uncertainty and ask the human designer where a decision is required.

## 28. Recovery Is a First-Class Requirement

Recovery is part of the design.

PlebMachine must be designed so that configuration mistakes, failed setup, failed component changes, or other problems can be diagnosed and recovered from.

## 29. Preserve the Project's Human Direction

PlebMachine is a human-directed project.

AI must preserve the project's established purpose, terminology, architecture, and design decisions unless the human designer deliberately changes them.

## 30. The PlebMachine AI Golden Rules

The following rules summarize the mandatory principles:

1. **Check first. Never guess.**
2. **The user owns the computer.**
3. **PlebMachine provides context. The user provides purpose.**
4. **Mission Control coordinates; it does not own.**
5. **PlebMachine must never uninstall anything other than a PlebMachine component belonging to its original Debian package.**
6. **Major PlebMachine components remain standalone applications.**
7. **Protect working code.**
8. **Legacy code is evidence, not automatically current code.**
9. **Test what is built. Do not assume it works.**
10. **Do not silently change the architecture.**
11. **Do not introduce feature creep.**
12. **Do not invent missing requirements.**
13. **Recovery is part of the design.**
14. **The AI assists the designer; it does not replace the designer.**

---

# PART II — GUIDANCE

## 31. Prefer Modular Architecture

Prefer small, understandable, independently testable components over unnecessary monolithic structures.

A component may communicate with other components without losing its identity as a standalone application.

## 32. Use the Established Development Workflow

When beginning or changing a component, establish what already exists before writing replacement code.

The development sequence should normally remain:

**Understand → Inspect → Discuss → Design → Implement → Test → Document → Verify**

## 33. Prefer Dynamic Discovery

Where dynamic discovery is appropriate, use the Linux desktop's available information rather than maintaining unnecessary hard-coded assumptions.

Discovery should remain predictable, inspectable, and recoverable.

## 34. Treat the Desktop Baseline as a Desktop Baseline

The desktop baseline is about the managed desktop environment.

It is not a declaration that PlebMachine owns every application, package, file, or system service on the computer.

## 35. PlebMachine States

The three active states serve different levels of automation and interaction:

- **COGNITIVE** provides a deliberate pause or speed-bump.
- **AUTOMATIC** provides automated launching and contextual setup for users who want more automation.
- **ADVANCED** provides greater user choice and control over application selection and interaction.

The OFF condition disables active PlebMachine orchestration.

## 36. PlebMachine Modes

The twelve modes provide contextual working environments rather than separate computers or separate operating systems.

Mode changes may alter the desktop context, workspace arrangement, wallpaper, and selected applications or tools as designed.

## 37. Prefer Evidence Over Assumption

Repository contents, existing code, actual system behaviour, logs, package information, and test results are stronger evidence than assumptions.

When evidence is available, inspect it.

## 38. Preserve Human Direction

The AI should help the designer see possibilities, identify problems, and implement agreed solutions.

It should not turn its own suggestions into requirements.

## 39. Core Principle

**PlebMachine provides context. The user provides purpose.**

The computer remains the user's computer.

PlebMachine exists to help organise the desktop around what the user is trying to do, while preserving user control, recoverability, modularity, and transparency.
