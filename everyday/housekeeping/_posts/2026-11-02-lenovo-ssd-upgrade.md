---
layout: post
title: "The Lenovo SSD Upgrade: Making Better Use of What We Have"
date: 2026-11-02
---

<!-- PLEBVOX:START -->

# 🚀 A New Lease on Life: The Lenovo SSD Upgrade.

<div style="text-align: center; margin: 1.25rem auto;">
  <img src="{{ '/assets/images/PlebServices.webp' | relative_url }}"
       alt="PlebWare Services banner created by Juelz"
       loading="lazy"
       decoding="async"
       style="width: 100%; height: auto;">
  <p><em>Banner created by Juelz. Thank you for the contribution!</em></p>
</div>

Sometimes the best computer upgrade isn't buying a new computer. It's recognising that the machine you already own still has plenty of life left in it — provided you give it the resources it needs.

On Monday, 2 November 2026, I finally tackled a job I had been postponing for months: upgrading the storage in my Lenovo IdeaPad 130-15IKB.

It was a necessary upgrade, and one that had become increasingly difficult to ignore.

But this story isn't simply about installing a larger SSD. It's about making practical use of available resources, learning new skills and extending the useful life of existing equipment.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 💻 Why the Upgrade Was Necessary.

My Lenovo was running a dual-boot configuration with Windows 11 and MX Linux.

Both operating systems shared a 250GB-class Kingmax SSD.

Over time, available storage had become a serious concern. Both Windows and Linux were approaching 90% capacity.

Windows was running short of breathing room, while Linux was also becoming increasingly cramped.

I had wanted to upgrade for months, but financial constraints meant postponing the expense.

Fortunately, I already had another drive available: a Western Digital WD Blue 500GB SSD.

I had not purchased a new SSD for this project. The WD Blue was already in my possession, waiting to be put to good use.

Rather than spend money unnecessarily, I decided to reuse the hardware I already owned.

Sometimes the best solution isn't something you buy. It's something you already have.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔧 The Hardware and Equipment.

The upgrade involved two drives:

- **Original drive:** Kingmax 240GB SSD, approximately 223.6GB usable.
- **Replacement drive:** Existing Western Digital WD Blue 500GB SSD, approximately 465.8GB usable.

The additional equipment included:

- USB 3.0 IDE/SATA universal external drive adapter.
- Ventoy USB drive.
- Rescuezilla ISO.
- Lenovo IdeaPad 130-15IKB laptop.

The objective was straightforward: preserve both operating systems, their existing installations and the dual-boot arrangement.

I didn't want to reinstall everything from scratch if I could safely migrate the existing installation.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🛠️ The Cloning Operation.

Rather than reinstalling Windows and Linux separately, I chose a disk-to-disk cloning operation using Clonezilla through the Rescuezilla environment.

The original Kingmax SSD was selected as the source, and the WD Blue was selected as the destination.

One particularly important decision concerned the partition table.

I selected **K1 — proportional partition resizing**.

This allowed the partition layout to expand proportionally to use the larger destination drive, rather than simply copying the original partition sizes and leaving the additional capacity unused.

The cloning process reported all six original partitions successfully copied.

Clonezilla then performed additional filesystem processing, including checking and updating the Linux environment.

It also updated the Linux initramfs and generated the boot image for kernel 6.1.0-54-amd64.

Based on the estimated start time of approximately 13:42 and the recorded shutdown at 14:17, the cloning operation took about 35 minutes.

That was an encouraging result.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🛡️ Protecting the Original Installation.

Before opening the laptop, I performed an important final test.

I disconnected the external cloning equipment and booted the Lenovo from its original Kingmax SSD.

Both operating systems started successfully.

MX Linux loaded, and Windows 11 also booted normally.

This confirmed that the original installation was still working before I proceeded with the physical replacement.

I then shut the laptop down properly, disconnected the power and opened the casing.

The original SSD was secured inside a small drive cage. After removing the mounting screws, I transferred the cage and installed the WD Blue.

Once everything was secured and the laptop reassembled, it was time for the moment of truth.

The original Kingmax was retained as a backup. It was not erased or repurposed.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🚀 The Moment of Truth.

I powered up the Lenovo.

The GRUB boot menu appeared!

First, I selected MX Linux.

The system started successfully from the newly installed WD Blue.

That was the first major confirmation that the cloned Linux installation was bootable.

Next came the Windows test.

I restarted the laptop and selected Windows Boot Manager.

The Lenovo splash screen appeared. Windows began loading, followed by the usual spinning loading indicator.

Then came the password screen.

I entered my password.

And there it was!

The familiar Bing wallpaper featuring polar bears appeared on the Windows desktop.

**Windows 11 had successfully loaded from the new SSD!**

Houston, we had liftoff!

🐻‍❄️🚀

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📊 The Final Storage Results.

After successfully booting both operating systems, I checked the new partition layout using MX Linux terminal commands.

The WD Blue was identified as a 465.8GB drive.

**Windows 11:**

- Total C: capacity: approximately 301.1GB.
- Available free space: approximately 170GB.
- Used space: approximately 131GB.

**MX Linux:**

The Linux `df -hT` command confirmed the following filesystem figures:

| Filesystem | Total | Used | Available | Usage |
|---|---:|---:|---:|---:|
| Root `/` | 91GB | 40GB | 47GB | 46% |
| Home `/home` | 70GB | 15GB | 52GB | 23% |
| EFI `/boot/efi` | 96MB | 32MB | 65MB | 34% |

The partition information from `lsblk` showed:

- EFI boot partition: 100MB.
- Windows 11 partition: 301.1GB.
- Windows recovery partition: 864MB.
- MX Linux root partition: 92.6GB.
- MX Linux home partition: 71GB.

The difference between the partition sizes and the filesystem figures is normal: the filesystem reports its usable formatted capacity.

**Linux now has approximately 99GB of available space across root and home.**

The system also uses a 2GB zram swap device rather than a dedicated swap partition.

Most importantly, both operating systems are now running successfully from the WD Blue, and the additional storage is available.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔑 More Than a Hardware Upgrade.

This exercise was important for another reason.

I have been considering a small computer support service for 2027, together with Julian.

One of the proposed services is helping people extend the useful life of their existing computers through:

- SSD upgrades.
- Operating-system migration.
- Data transfers.
- Dual-boot installations.
- Basic computer maintenance.
- Photo and data recovery.

There is a considerable difference between reading about a procedure and actually performing it.

This upgrade gave me practical experience with:

- Identifying source and destination drives.
- Disk-to-disk cloning.
- Partition resizing.
- Filesystem processing.
- Physical drive replacement.
- Bootloader and operating-system verification.

It also reminded me of something important: a successful computer upgrade requires patience, preparation and a reliable backup plan.

Keeping the original drive untouched gave me a recovery option throughout the process.

This was not a commercial customer installation, but it was a valuable practical exercise and an important step towards developing a responsible service.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 💙 Technology Should Serve Humanity.

At PlebWare, one of our guiding principles is:

**Your computer should serve you — not the other way around.**

Replacing an entire laptop isn't always necessary. Sometimes a carefully planned upgrade can extend the useful life of the equipment you already own.

This project wasn't about chasing the newest hardware or spending money for the sake of spending money.

It was about making better use of what I had, solving a genuine problem and learning something valuable along the way.

The WD Blue was already available. The Lenovo was still capable. The solution was to bring the two together.

And perhaps, in the process, take another small step towards building a service that can help others do the same.

**Convenience is the objective. Empowerment is the outcome. Human freedom remains the safeguard.**

<!-- PLEBVOX:END -->

---

✍️ **Otto Brinkmeier**
*PlebWare Contributor*

*Sanguine et Igne Veritas Revelata.*
