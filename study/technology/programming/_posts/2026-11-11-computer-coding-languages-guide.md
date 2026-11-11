---
layout: post
title: "The Computer Coding Languages Guide"
date: 2026-11-11
categories: [study, technology, programming]
permalink: /study/technology/programming/2026/11/11/computer-coding-languages-guide/
---

<!-- PLEBVOX:START -->

# 💻 The Languages Behind the Digital World

Computers, phones, websites, games, databases, robots and everyday devices all depend on languages that tell software what to do, describe information, organise data or control hardware.

There are hundreds of programming languages and related technologies. No single list can claim to include every language ever created, and the boundaries depend on what is being counted. This guide is a practical map of the main families, what they are used for and how to choose a sensible starting point.

The central idea is simple: **choose a tool because it solves a problem, not because its name is fashionable.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 1. What Counts as a Coding Language?

The phrase coding language is often used as an umbrella term. Several different kinds of language and format work together in modern computing.

- **Programming languages** express instructions, operations, rules and algorithms that a computer can execute or interpret. Examples include Python, C, JavaScript and Rust.
- **Markup languages** describe the structure or meaning of content. HTML and XML are common examples.
- **Style languages** describe presentation. CSS controls the appearance and layout of web content.
- **Query languages** ask a system to retrieve, change or analyse information. SQL is the best-known example.
- **Shell and scripting languages** automate tasks and connect programs. Bash and PowerShell are widely used examples; Python is also frequently used for scripting.
- **Hardware-description languages** describe digital circuits. Verilog and VHDL are examples.
- **Data and configuration formats** such as JSON, YAML and TOML represent information and settings. They are not normally general-purpose programming languages.

These distinctions matter. HTML is not the same kind of tool as Python, and a configuration file is not automatically an executable program.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 2. General-Purpose Programming Languages

General-purpose languages can be applied to many different types of software. Their strengths, ecosystems and learning curves differ.

| Language | Common uses |
|---|---|
| Python | Automation, AI, data science, education, scripting, scientific work and web back ends |
| C | Operating systems, firmware, drivers, embedded devices and performance-critical software |
| C++ | Game engines, desktop software, browsers, simulations and high-performance applications |
| C# | Windows and cross-platform applications, enterprise software, cloud services and Unity games |
| Java | Android applications, enterprise systems and back-end services |
| JavaScript | Interactive websites, browser applications, servers and cross-platform tools |
| TypeScript | Larger JavaScript projects that benefit from static type checking |
| Go | Cloud services, networking, command-line tools and concurrent back-end systems |
| Rust | Systems software, embedded development, WebAssembly and performance-conscious applications |
| Swift | Apple-platform applications and selected server-side development |
| Kotlin | Native Android applications, server software and shared multiplatform code |
| Dart | Flutter applications for mobile, web and desktop |
| Ruby | Web applications, automation and scripting |
| PHP | Server-side web development and content-management systems |
| Perl | Text processing, system administration, legacy services and bioinformatics |
| Lua | Embedded scripting, games and application extensions |
| Julia | Numerical computing, optimisation and scientific research |
| R | Statistics, research, data analysis and visualisation |
| Scala and F# | JVM or .NET applications, functional programming and data processing |
| Haskell and OCaml | Functional programming, compilers, research and developer tools |
| Elixir and Erlang | Concurrent, fault-tolerant and distributed services |
| Zig, Nim and Crystal | Compiled systems tools and applications with different approaches to performance and developer control |

This is a selection, not a ranking. A language's suitability depends on the project, available libraries, platform support, performance requirements and the people maintaining the software.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 3. Web Development

A modern website is usually built from several technologies working together.

- **HTML** provides the structure and meaning of a page: headings, paragraphs, forms, images and links.
- **CSS** controls presentation, including colours, typography, spacing, responsive layouts and animation.
- **JavaScript** provides interactive behaviour in browsers and is also used on servers.
- **TypeScript** adds a static type system to JavaScript projects.
- **PHP, Python, Ruby, Java and C#** are among the languages used to build server-side applications and APIs.
- **SQL** works with relational databases that store application data.
- **Sass/SCSS and Less** extend the authoring experience for CSS.
- **JSX and TSX** are syntax extensions used in some JavaScript and TypeScript user-interface projects.
- **SVG** describes scalable vector graphics, while XML is used for structured documents and data.
- **WebAssembly** is a portable compilation target that allows code produced by languages such as C, C++ and Rust to run in supported environments.

A website may use HTML, CSS and JavaScript in the browser, a different language on the server and SQL in its database. There is no requirement for an entire project to use one language.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 4. Mobile Applications

Mobile development depends on the operating system and whether an application is native or cross-platform.

- **Swift** is the main modern choice for native Apple-platform development.
- **Objective-C** remains present in older Apple applications and established codebases.
- **Kotlin** is the primary modern language for native Android development.
- **Java** remains important in existing Android applications and related services.
- **Dart with Flutter** can be used to build applications for Android and iOS from a shared codebase.
- **JavaScript or TypeScript** can be used with frameworks such as React Native and Ionic.
- **C#** is used with .NET MAUI and other application frameworks.
- **C and C++** are used for native libraries and performance-sensitive components.
- **HTML and CSS** are used in hybrid applications and web-based interfaces.

Cross-platform tools can reduce duplicated work, but they do not remove every difference between devices, operating systems and their APIs.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 5. Operating Systems, Hardware and Robotics

Some languages work close to the hardware, where memory, timing and processor behaviour matter.

- **C and C++** are widely used for kernels, drivers, firmware, microcontrollers, robotics and embedded systems.
- **Assembly language** expresses processor-specific instructions for architectures such as x86, ARM and RISC-V.
- **Rust** is used for systems code where memory safety and performance are important.
- **Ada** is used in some safety-critical and high-integrity systems.
- **Embedded C** describes the use of C for microcontrollers and constrained devices.
- **MicroPython and CircuitPython** bring Python-style programming to supported microcontrollers.
- **Arduino sketches** use a C++-based programming model.
- **Verilog, SystemVerilog and VHDL** describe and verify digital circuits, including FPGA and ASIC designs.
- **Ladder Diagram, Structured Text and Function Block Diagram** are used in industrial programmable logic controllers.
- **G-code** gives machine-control instructions to many CNC machines and 3D printers.
- Industrial robot platforms may use vendor-specific languages such as RAPID, KRL or KAREL.

The right choice is closely tied to the actual board, processor, controller or machine being programmed.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 6. Databases, Data Analysis and Scientific Computing

Data work uses languages for querying, calculating, modelling and interpreting information.

- **SQL** is the standard starting point for relational database queries and updates.
- **PL/SQL, T-SQL and PL/pgSQL** add procedural features for particular database systems.
- **R** is widely used for statistics, modelling and visualisation.
- **MATLAB and GNU Octave** support numerical computing, engineering and simulation.
- **Julia** is designed for technical and scientific computing.
- **SAS and Stata** are used for statistical analysis and research.
- **SPSS syntax** supports statistical workflows and data transformations.
- **Wolfram Language** supports symbolic computation, mathematics and visualisation.
- **Fortran** remains important in scientific and engineering software.
- **APL, J, K and Q** are array-oriented languages used in mathematical, analytical and financial contexts.
- **MDX and DAX** are specialised languages or expression systems for analytical data platforms.
- **HiveQL and related query tools** support particular data-processing environments.

For many learners, SQL is a practical first step into databases because it teaches how to select, filter, join and update structured information.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 7. Artificial Intelligence, Machine Learning and Data Engineering

AI is not tied to one programming language. The language, libraries, frameworks, data pipeline and available hardware all influence a project.

- **Python** is a strong general-purpose starting point for machine learning, deep learning, data preparation and AI research.
- **R** is useful for statistical learning and visual analytics.
- **C++** is used in high-performance inference engines and numerical libraries.
- **CUDA C/C++** is used to program NVIDIA GPUs for parallel workloads.
- **Julia** supports numerical modelling and machine-learning research.
- **Java and Scala** are used in production data platforms and distributed processing.
- **SQL** is central to extracting, transforming and preparing data.
- **JavaScript and TypeScript** support AI-enabled web applications and browser-based integration.
- **Mojo** is a newer language aimed at high-performance AI and systems programming; its ecosystem and maturity continue to develop.
- **Prolog and Lisp** are associated with logic programming, symbolic reasoning and parts of AI's history.

Frameworks and libraries are important, but they are not themselves programming languages. Python, for example, may be used with specialised libraries to build systems that would be impractical to implement from scratch.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 8. Games, Graphics and Creative Software

Games and creative applications combine application logic, graphics, physics, audio and tools.

- **C++** is used in major game engines, rendering systems and performance-critical code.
- **C#** is widely used for Unity game scripting and application development.
- **GDScript** is designed for scripting in the Godot game engine.
- **GML** is used in the GameMaker ecosystem.
- **Lua** is embedded in some games and engines for scripting and modding.
- **HLSL, GLSL, Metal Shading Language and WGSL** are used to write graphics or compute shaders for different platforms.
- **Python** is used for Blender automation, creative pipelines and procedural content.
- **JavaScript and TypeScript** support browser games and interactive graphics.
- **Ren'Py language and Ink** support visual novels, branching stories and interactive dialogue.
- **ActionScript** is a historical language associated with Flash-era web content and games.

The best language depends on the engine, target platform and type of experience being built.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 9. Automation, Command Lines and Infrastructure

Not all useful programming happens inside a large application. Shells and automation languages help maintain computers, manage servers and connect tools.

- **Bash and POSIX shell** automate Linux and Unix commands, deployments and maintenance.
- **Zsh, Fish and KornShell** provide alternative interactive shells and scripting environments.
- **PowerShell** supports Windows administration, cloud automation and cross-platform scripting.
- **Windows Batch** remains useful for certain Windows command tasks and older scripts.
- **Python, Perl, Ruby, AWK and sed** are used for automation, text processing and file operations.
- **Groovy** is used in JVM-based build and automation environments.
- **Makefile syntax and CMake** help describe build processes and project configuration.
- **Nix language** describes packages and system configurations in the Nix ecosystem.
- **HCL** is used for infrastructure-as-code tools such as Terraform.
- **Dockerfiles** describe how container images are built.
- **Bicep** describes infrastructure deployments for Microsoft Azure.
- **Ansible playbooks** use YAML structures to describe automation.
- **Rego** expresses policy-as-code rules.
- **GitHub Actions workflows** use YAML configuration to automate build, test and deployment tasks.

These tools can save time, make work repeatable and reduce the risk of inconsistent manual operations.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 10. Markup, Data Formats and Documentation

Developers often work with formats that look like code but serve a different purpose.

- **JSON** represents structured data exchanged between applications and APIs.
- **JSON5** is a JSON-like format with additional authoring conveniences.
- **YAML and TOML** are commonly used for configuration and structured data.
- **XML and XHTML** describe structured documents and data.
- **HTML** describes the structure and meaning of web pages.
- **Markdown and AsciiDoc** are lightweight markup formats for documentation and publishing.
- **reStructuredText** is used in Python documentation and technical publishing.
- **LaTeX** is used for document preparation and typesetting, especially in mathematics and scientific work.
- **XSLT** transforms XML documents.
- **XPath** selects nodes in XML documents, while **XQuery** queries XML data.
- **CSS** describes how documents are presented.
- **Protocol Buffers** and **Thrift IDL** describe structured messages and service interfaces.
- **OpenAPI** describes HTTP APIs, commonly using YAML or JSON.

Understanding the purpose of a format helps prevent a common mistake: treating every file containing structured text as a program.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 11. Query, Logic and Specialist Languages

Some languages are designed for a narrow but important job.

- **SPARQL** queries RDF graphs and linked data.
- **Cypher** queries graph databases such as Neo4j.
- **Gremlin** traverses graph data.
- **Prolog and Datalog** express facts, rules and logical relationships.
- **CLIPS** supports rule-based expert systems.
- **Alloy and TLA+** help model systems and reason about constraints or concurrent behaviour.
- **Coq and Lean** support machine-checked proofs and formal mathematics.
- **Idris and Agda** explore dependently typed programming and formal proof techniques.
- **Solidity, Vyper and Move** are used for smart contracts in selected blockchain ecosystems.
- **ABAP** is used in SAP enterprise environments.
- **Apex** is used for business logic on the Salesforce platform.
- **MUMPS, also called M, and COBOL** remain relevant in established database, healthcare, financial and transaction systems.

Specialist does not mean unimportant. A language may serve a relatively small field while being essential to the systems that depend on it.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 12. Visual, Educational and Low-Code Programming

Programming does not always begin with lines of text.

- **Scratch** teaches programming concepts through visual blocks.
- **Blockly** is a toolkit for building block-based programming editors.
- **MIT App Inventor** uses visual blocks to create applications.
- **Microsoft MakeCode** combines block-based and text-based learning for supported devices.
- **LabVIEW G** uses graphical dataflow programming for measurement and engineering.
- **Ladder Diagram and Function Block Diagram** provide visual approaches to industrial control.
- **Pure Data and Max** support visual programming for audio, music and interactive media.
- **Node-RED** connects services, APIs and devices through visual flows.
- **Unreal Engine Blueprints** provide visual scripting for games and interactive applications.

Visual tools can make concepts easier to approach. They also teach ideas such as sequence, conditions, events, variables and data flow that apply to text-based programming.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 13. Historical and Legacy Languages

Older languages are not necessarily obsolete. Many systems built decades ago continue to support important businesses and public services.

Languages and families worth recognising include **BASIC, Visual Basic 6, Pascal, ALGOL, Lisp, Smalltalk, Ada, COBOL, FORTRAN, PL/I, RPG, FoxPro, Visual FoxPro, Delphi, ColdFusion Markup Language and JScript**.

Some remain in active specialist use; others are mainly encountered when maintaining or replacing older software. Learning their history also helps explain why modern languages and programming ideas developed as they did.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 14. How to Choose a Language

Start with the thing you want to build.

| Your goal | Useful starting technologies |
|---|---|
| Websites | HTML, CSS and JavaScript; add TypeScript or a back-end language as needed |
| Android apps | Kotlin; Java for existing projects; Flutter or JavaScript/TypeScript for cross-platform work |
| iPhone and iPad apps | Swift for native development; Flutter or React Native for shared code |
| Windows desktop software | C#, C++, Python, Java or JavaScript-based desktop frameworks |
| Linux tools and system software | C, C++, Rust, Go, Python and shell scripting |
| Games | C# with Unity, C++ with Unreal, GDScript with Godot, or Lua where supported |
| AI and data science | Python as a starting point, with SQL, R, Julia, C++ or GPU tools for specialised work |
| Microcontrollers | C/C++, Arduino-style sketches, MicroPython or CircuitPython |
| Industrial automation | IEC 61131-3 languages such as Ladder Diagram and Structured Text |
| Databases | SQL first, followed by the dialect and tools of the chosen database |
| Cloud and infrastructure | Go, Python, Bash, PowerShell, HCL and platform-specific tools |

There is no universal winner. A language that is excellent for embedded firmware may be an awkward choice for a beginner's website. Match the language to the job.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 15. A Sensible Learning Path

A beginner does not need to learn twenty languages. A practical progression is:

1. **Understand the computer.** Learn about files, folders, operating systems, memory, networks and how applications run.
2. **Start with Python.** Practise variables, conditions, loops, functions, collections, files and small projects.
3. **Learn the web basics.** Understand HTML for structure, CSS for appearance and JavaScript for interaction.
4. **Learn Git.** Version control helps track changes and collaborate safely.
5. **Learn SQL.** Practise tables, records, relationships and queries.
6. **Build something real.** Create a personal website, a small utility, a simple application or an automation script.
7. **Specialise.** Choose the language and tools that fit the software or device you want to create.

A useful starter combination is **Python + HTML + CSS + JavaScript + SQL + Git**. It provides a foundation across automation, websites, data and application development without demanding that a beginner master everything at once.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 16. Common Misconceptions

- **Java is not JavaScript.** Their names are similar, but their histories, designs and ecosystems are different.
- **HTML is not a general-purpose programming language.** It structures content; JavaScript supplies general programming behaviour in the browser.
- **CSS is not HTML.** HTML describes structure and meaning; CSS describes presentation.
- **SQL is a language.** It is specialised for working with relational data rather than being a general-purpose application language.
- **JSON and YAML are data formats.** They store or exchange structured information; they are not normally general-purpose executable languages.
- **Frameworks are not languages.** React, Flutter, Django, Rails, .NET and Unity are frameworks, platforms or engines used with languages.
- **Portability has limits.** Libraries, compilers, runtimes and device APIs affect where a program can run.
- **One project can use many languages.** An application may combine Kotlin, SQL, JSON, XML, C++ and shell scripts in different parts of its toolchain.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 17. A Short Glossary

- **API — Application Programming Interface:** a defined way for software components to communicate.
- **Compiler:** a tool that translates source code into another form, often machine code or bytecode.
- **Interpreter:** a program that executes source code or an intermediate representation.
- **Runtime:** the environment and supporting components in which a program executes.
- **Framework:** a reusable foundation that provides structure and services for an application.
- **Library:** reusable code that a program can call to perform particular tasks.
- **SDK — Software Development Kit:** tools, libraries and documentation for a platform.
- **IDE — Integrated Development Environment:** an editor combined with development tools.
- **Firmware:** software stored on or closely associated with a hardware device.
- **Kernel:** the core part of an operating system that manages hardware and system resources.
- **Embedded system:** a computer built into a larger device, often for a specialised task.
- **Cross-platform:** designed to run on more than one operating system or hardware platform.
- **Open source:** software whose source code is made available under a licence that permits specified use, inspection and modification.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 18. Sources and Further Reference

This guide is a practical introduction, not a formal standard or a popularity ranking. Language inventories differ in what they count, and technologies change over time. Check current documentation for version-specific behaviour and platform support.

- [MDN Web Docs — Web technology for developers](https://developer.mozilla.org/en-US/docs/Web)
- [Microsoft Visual Studio Code — Programming Languages](https://code.visualstudio.com/docs/languages/overview)
- [Programming Languages Database](https://plangs.page/)
- [TIOBE — Programming language definition and tracked list](https://www.tiobe.com/tiobe-index/programminglanguages_definition/)
- [MDN — WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)
- [IEEE Technology Navigator — Computer languages](https://technav.ieee.org/topic/computer-languages/)

<!-- PLEBVOX:END -->

---

*Technology should serve humanity. Keep learning, keep experimenting, and choose tools that solve real problems.*

---

**Boy Mist**  
*PlebWare Contributor*
