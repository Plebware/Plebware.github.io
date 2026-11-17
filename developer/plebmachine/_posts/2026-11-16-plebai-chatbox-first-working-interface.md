---
layout: post
title: "PlebAI ChatBox — The First Working Local AI Interface!"
date: 2026-11-16
description: "Development milestone documenting the installation of Ollama and the creation of a custom Python desktop chat interface for locally operated AI models."
category: "plebmachine"
tags: [PlebMachine, PlebAI, PlebWare, Offline AI, Local AI, Ollama, Python, Qwen, DeepSeek, Linux, Development]
mode: "developer"
author: Otto Brinkmeier
---

<!-- PLEBVOX:START -->

# 🤖 PlebAI ChatBox — Building an AI Interface That Works for Me.

**From installing a local AI engine to creating a desktop interface designed around the user's needs.**

Sometimes the best way to develop software is to discover what doesn't work first.

On 15 November 2026, we began establishing a local artificial intelligence environment on the Lenovo development machine. The objective was to bring AI processing closer to the desktop, reducing dependence on cloud services and providing an opportunity to experiment with locally operated language models.

The first milestone was installing the AI engine.

The second was finding a suitable interface.

The third, and perhaps most interesting, was deciding that instead of adapting to somebody else's interface, we could build one ourselves.

That decision led to the first working prototype of **PlebAI ChatBox**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧠 Stage One — Installing the AI Engine.

The foundation of the project is **Ollama**, which provides the local environment for downloading, managing and running language models.

The installation was completed on MX Linux, with Ollama reporting version 0.40.16.

Our initial model selection was Qwen 3.5 0.8B.

This is a relatively small language model, selected with the available hardware resources in mind.

However, our first experiments revealed an interesting problem.

The original model did not behave as expected when tested through the Chatbox application.

Rather than abandoning the project, we investigated the model configuration and created a separate no-draft variant.

The resulting model was:

`qwen3.5:0.8b-nodraft`

Its configuration disabled draft prediction and set a conservative output limit.

A direct API test against the local Ollama service returned the expected response:

**Local AI is connected.**

That was our first successful confirmation that the local engine could receive a request and generate a response.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🖥️ Stage Two — The Search for a Suitable Interface.

Our next experiment involved downloading and testing Chatbox.

Although the application provided an interface for connecting to Ollama, it wasn't the experience we wanted.

There is nothing particularly wrong with using an existing application. However, the purpose of PlebMachine is to provide a working environment that suits the person using it.

We wanted something simpler.

We wanted a normal desktop window, without unnecessary complications or features that would get in the way of an ordinary conversation.

Instead of spending more time trying to adapt Chatbox to our requirements, we decided to build a small Python application.

DeepSeek was brought into the development process to help design and implement the interface.

The result was a working desktop application.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔧 Stage Three — Building PlebAI ChatBox.

The first prototype is deliberately uncomplicated.

It uses a conventional desktop window with a chat area, model selection controls and a small collection of practical buttons.

The objective is straightforward: open the application, select a model, type a message and communicate with the local AI engine.

### 💬 The Chat Window.

The main area provides the conversation interface.

Messages can be entered and sent to the locally running Ollama service.

The application receives the generated response and displays it in the conversation.

### 🧠 Model Selection.

A model selection control allows the user to choose between the currently available models.

The first two choices are:

- `qwen3.5:0.8b`
- `qwen3.5:0.8b-nodraft`

A **Refresh** button allows the model list to be refreshed.

This is particularly useful as the project develops and additional models become available.

### 🛠️ Conversation Controls.

The interface currently includes:

- **Refresh:** Refreshes the available model selection.
- **New Chat:** Starts a fresh conversation.
- **Copy Conversation:** Copies the conversation for reuse or archiving.
- **Send:** Sends the current message to the selected model.
- **Stop:** Provides a control for stopping generation.

These are ordinary features, but they are precisely the features we wanted.

No unnecessary menus, complicated configuration screens or distractions.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📡 Stage Four — Connection Status and Feedback.

One of the small details I particularly wanted was a status bar at the bottom of the window.

It provides immediate information about the local AI environment.

The current interface reports:

- **Engine:** Ollama connected.
- **Version:** 0.40.16.
- **Selected model:** Qwen 3.5 0.8B — No Draft.

This provides a convenient way of checking which engine is connected and which model is selected.

The application is not simply a graphical shell. It communicates with the local AI service and provides the user with useful feedback about that connection.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## ✅ Stage Five — Testing the Interface.

Once the initial interface had been assembled, we went through its controls.

The model selection was tested.

The refresh function was tested.

New Chat was tested.

Copy Conversation was tested.

The Send and Stop controls were tested.

The connection status was also checked.

The result was encouraging.

The interface worked as intended during our initial tests.

Everything was tickety-boo!

More importantly, we now had a usable starting point for further development.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔑 Why Build Our Own Interface?

There is a bigger lesson here.

Software developers sometimes assume that users must adapt to the applications they are given.

PlebMachine approaches this differently.

The user should be able to decide what is useful, what is unnecessary and how an application should fit into an existing working environment.

PlebAI ChatBox is a small example of that philosophy.

We did not need an elaborate application.

We needed a practical interface that allowed us to communicate with a local AI model without getting lost in unnecessary controls.

Python provided the means to create that interface, while Ollama provided the underlying model-running service.

DeepSeek assisted with the development, and the resulting application was tested against the actual local engine.

Different AI systems can contribute to a common development project without having to replace one another.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🚀 The Next Development Objective — A Model Installer.

With the basic chat interface working, the next logical development task is a dedicated model installer and manager.

At present, the interface can select between the models already available locally.

However, we would like to take this a step further.

A future model-management component could allow the user to:

- Browse suitable models.
- Download selected models through Ollama.
- Display installed models.
- Switch between available models.
- Remove models that are no longer required.
- Refresh the available model list.

This is a proposed development objective, not an implemented feature.

Model selection and installation should remain separate from the basic chat interface wherever practical.

That would allow PlebAI ChatBox to remain lightweight while providing a more capable model-management facility.

We must also continue considering available memory, storage capacity and processor performance before adding models.

There is no advantage in installing an enormous collection of models if the computer cannot comfortably run them.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🏁 Development Milestone — A Working Beginning.

The first stage of PlebAI has now moved beyond an installation proposal.

We have:

1. Installed the Ollama local AI engine.
2. Downloaded and configured a small Qwen language model.
3. Created a no-draft model variant.
4. Tested communication through the local API.
5. Experimented with an existing desktop chat application.
6. Designed and implemented our own Python chat interface with DeepSeek.
7. Tested the interface controls and connection feedback.

The next objective is to develop a model installer and gradually expand the capabilities of the local AI environment.

This is still an early prototype. Offline operation with the network disconnected, longer conversations, model resource consumption and broader reliability testing remain part of the work ahead.

Nevertheless, we have achieved something useful.

We now have a local AI engine and a desktop interface that we actually want to use.

And that is a far better starting point than trying to make ourselves comfortable with software that doesn't suit our needs.

**Technology Must Serve Humanity, Not The Other Way Around.**

*Convenience is the objective. Empowerment is the outcome. Human freedom remains the safeguard.*

<!-- PLEBVOX:END -->

---

**✍️ Otto Brinkmeier**

*PlebWare — Accessible. Repairable. Understandable Technology.*
