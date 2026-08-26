---
layout: post
title: "Make PlebMachine Run on Your Debian"
date: 2026-08-26
category: "plebmachine"
tags: [plebmachine, MX Linux, Debian, Ubuntu, XFCE, Linux Mint, tag7]
mode: "developer"
author: Otto Brinkmeier
---
<!-- PLEBVOX:START -->

# So You Want to Try PlebMachine

## Installing XFCE Desktop

Yes, you can install the XFCE desktop environment on all the Debian-based Linux distributions we discussed . For most of them, it's a simple process, as they either offer an XFCE version or it can be installed with a single command.

Here’s how it works on the main distributions mentioned:

### 🐧 Confirmed Distributions that Can Run XFCE
Distribution	How to Get XFCE
**MX Linux**	XFCE is the default desktop environment, so it comes preinstalled.
**Debian** & **Ubuntu**	You can either choose XFCE during installation or install it later on an existing system using the command: **sudo apt install xfce4 xfce4-goodies**
<!-- PLEBVOX:END -->

```
sudo apt install xfce4 xfce4-goodies
```
<!-- PLEBVOX:START -->

## **Which Known Distros Support XFCE**

**Linux Mint & Zorin OS**	Officially support **XFCE**. Linux Mint has a specific "Xfce Edition" you can download and install directly.
Pop!_OS & elementary OS	XFCE is not the default, but you can install it manually using the apt command. You can then select it from the login screen.

## ⚙️ One Key Detail
Please note that if you are installing XFCE on a distribution that ships with a different default desktop 
(like **Pop! OS** with GNOME or **Ubuntu** with GNOME), your system will have **multiple desktop environments** installed side-by-side. 
You will be able to choose which one to use at the login screen.
<!-- PLEBVOX:END -->


## 💡 **Simple Installation Command**
On any Ubuntu or Debian-based system, the standard command to install a full XFCE desktop is :
```
bash
sudo apt update && sudo apt install xfce4 xfce4-goodies
```
Running this will install XFCE alongside your current environment if you have one.
