---
layout: post
title: "Metro Fibre Internet Stability — Evidence and Reporting Note"
date: 2026-09-20
---

# 🛜 Metro Fibre Internet Stability — A Note for Otto and Juelz

<!-- PLEBVOX:START -->

## 📝 Why This Note Exists

This note is a reminder for **Otto** to prepare a detailed, evidence-based report for **Metro Fibre** regarding the recurring internet instability we have been experiencing.

Otto and Juelz have been communicating about the problem for **almost two weeks**, yet the underlying issue has still not been resolved.

The concern is not simply that the internet occasionally feels slow. The problem is **network stability and reliability**, and we need to document the evidence properly so that technical support has something concrete to investigate.

Technical support has also been a continuing source of frustration. The response over a prolonged period has not resulted in a satisfactory resolution, and the repeated delays have put unnecessary strain on Otto and Juelz.

This morning, the frustration finally boiled over into a serious argument. The underlying message from Juelz was that repeated reminders to contact Metro Fibre had been going on for months, while Otto's response was that previous attempts seemed to result in being ignored or not properly resolving the problem.

The language used during the argument is deliberately **not reproduced here**. The important point is that both people are frustrated because the technical problem remains unresolved.

**The purpose of this note is therefore not to assign blame. It is to create evidence.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🎯 What We Need to Establish

The report should distinguish between:

- **Internet speed**
- **Latency**
- **Ping response time**
- **Packet loss**
- **Connection stability**
- **DNS performance**
- **Routing problems**
- **Local Ethernet/link problems**
- **Problems that occur only with particular websites or services**
- **Problems that affect the entire connection**

A single speed test showing good download and upload speeds does **not** necessarily prove that the connection is healthy.

A connection can deliver excellent throughput while still suffering from intermittent packet loss, latency spikes, routing problems, or short interruptions.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔬 Internet Tests Otto Can Perform

Run tests at different times of day, especially when the connection is behaving badly.

### 1. Speed Test

Use:

- <a href="https://www.speedtest.net/" target="_blank" rel="noopener">Ookla Speedtest</a>
- <a href="https://fast.com/" target="_blank" rel="noopener">Fast.com</a>

Record:

- Date and time
- Download speed
- Upload speed
- Reported latency
- Test server, where shown
- Whether the connection felt normal or unstable during the test

**Important:** Do not run only one speed test. Repeat the test when the connection is working normally and again when the problem is occurring.

### 2. Ping Test

On Linux, open a terminal and test a reliable external host:

```bash
ping -c 20 1.1.1.1
```

Then:

```bash
ping -c 20 8.8.8.8
```

Record:

- Minimum latency
- Average latency
- Maximum latency
- Packet loss

A useful comparison is to test the router as well, if its local address is known:

```bash
ping -c 20 192.168.1.1
```

Replace `192.168.1.1` with the actual router/gateway address if different.

### 3. Continuous Ping During an Outage

When the connection starts misbehaving:

```bash
ping 1.1.1.1
```

Leave it running for several minutes.

Look for:

- `Request timeout`
- Increasing latency
- Sudden latency spikes
- Packet loss
- Long gaps between replies

Press **Ctrl+C** to stop and record the final statistics.

### 4. Ping Several Destinations

Testing more than one destination can help establish whether the problem is general or destination-specific.

For example:

```bash
ping -c 20 1.1.1.1
ping -c 20 8.8.8.8
ping -c 20 google.com
```

If IP addresses respond normally but a domain name does not, DNS may deserve investigation.

### 5. Packet-Loss Test

Packet loss is particularly important because it can cause interruptions even when speed tests look good.

Run:

```bash
ping -c 100 1.1.1.1
```

Record the final packet-loss percentage.

Repeat the test at different times.

### 6. Traceroute

Traceroute can show where latency or routing problems may be appearing.

On Linux:

```bash
traceroute 1.1.1.1
```

If traceroute is not installed:

```bash
sudo apt install traceroute
```

Also test:

```bash
traceroute 8.8.8.8
```

Do not automatically assume that a single slow or non-responsive hop proves that hop is faulty. Some routers deliberately deprioritise or block traceroute responses.

### 7. MTR — Longer-Term Routing Test

MTR combines ping and traceroute and can be particularly useful for recurring instability.

If installed:

```bash
mtr -rwzc 100 1.1.1.1
```

And:

```bash
mtr -rwzc 100 8.8.8.8
```

This provides a much better picture than a single traceroute because it collects repeated observations.

### 8. DNS Test

Test DNS resolution:

```bash
dig google.com
```

Also:

```bash
dig @1.1.1.1 google.com
```

And:

```bash
dig @8.8.8.8 google.com
```

Record whether the response is immediate or unusually slow.

### 9. Browser-Based DNS and Connectivity Checks

Useful online resources include:

- <a href="https://www.dnsleaktest.com/" target="_blank" rel="noopener">DNS Leak Test</a>
- <a href="https://www.cloudflare.com/ssl/encrypted-sni/" target="_blank" rel="noopener">Cloudflare connectivity resources</a>

These are supplementary tests rather than replacements for ping, packet-loss, and routing evidence.

### 10. Check the Ethernet Interface

Because the computer is connected by LAN cable, check the Ethernet interface directly.

On Linux:

```bash
ip link
```

Then identify the Ethernet interface and run:

```bash
ip -s link show <interface>
```

Look for increasing:

- RX errors
- TX errors
- Dropped packets
- Other interface errors

For example:

```bash
ip -s link show enp3s0
```

The actual interface name may be different.

### 11. Check Link Negotiation

If `ethtool` is available:

```bash
sudo ethtool <interface>
```

Check:

- Link detected
- Speed
- Duplex
- Auto-negotiation

For example:

```bash
sudo ethtool enp3s0
```

### 12. Record the Physical Link Indicators

The network card currently shows **green and orange activity/link lights**, even with a new Cat5 LAN cable.

Photographing the lights is not proof of an ISP fault, but it can be recorded as part of the troubleshooting history.

The important evidence is what the operating system reports about the Ethernet interface and what the external network tests show.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📊 What to Record for Every Test

Use a simple table or log:

| Date | Time | Test | Result | Connection Condition |
|---|---|---|---|---|
| 2026-09-20 | 08:00 | Speedtest | Download / Upload / Latency | Normal |
| 2026-09-20 | 08:15 | Ping 1.1.1.1 | Average / Loss | Unstable |
| 2026-09-20 | 08:20 | Ping 8.8.8.8 | Average / Loss | Unstable |
| 2026-09-20 | 08:30 | MTR | Results | Unstable |

Do not record only the tests that look bad.

**Good results are evidence too.**

If speed is excellent while packet loss or latency is problematic, that distinction may be important to the technician.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## ⏱️ Build a Two- or Three-Day Evidence Log

For the next few days, record tests at approximately:

- Morning
- Midday
- Late afternoon
- Evening
- During an actual failure or period of instability

Also record ordinary observations such as:

- Websites taking unusually long to load
- Video buffering
- Pages intermittently failing
- Online services disconnecting
- Sudden latency increases
- Short periods where the connection appears to disappear
- Whether other devices experience the same problem

If multiple devices are affected at the same time, record that as well.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📄 What the Metro Fibre Report Should Contain

The final report should be calm, factual, and chronological.

### 1. Customer and Service Details

Include the relevant account or service reference information, but do not publish sensitive account numbers on the public PlebWare site.

### 2. Problem Summary

State clearly:

> The fibre internet connection has experienced recurring instability for an extended period. Communication regarding the problem has continued for almost two weeks without a satisfactory resolution.

### 3. History

List:

- When the instability was first noticed
- When Metro Fibre was contacted
- Dates of follow-up communication
- Responses received
- Any troubleshooting already performed
- Any technician visits, if applicable
- Whether the problem remains unresolved

### 4. Technical Evidence

Attach or summarise:

- Speed-test results
- Ping results
- Packet-loss results
- MTR results
- Traceroute results
- DNS observations
- Ethernet-interface statistics
- Link-speed and duplex information
- Relevant screenshots

### 5. Important Contradiction to Highlight

The connection can produce acceptable results on conventional online speed tests while still showing symptoms of instability.

Therefore:

**Good speed-test throughput should not be treated as proof that the service is stable.**

### 6. Requested Action

Ask Metro Fibre to investigate the connection for:

- Intermittent packet loss
- Latency spikes
- Fibre/ONT issues
- Router or termination issues
- Port or link negotiation problems
- Local access-network problems
- Routing instability
- Any other faults visible from their network side

The report should ask for a **technical investigation and a clear explanation of the findings**, rather than simply another speed test.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧭 The Main Rule for Otto

Do not let frustration become the report.

Let the **evidence speak**.

The argument this morning is a sign that the situation has become frustrating for both Otto and Juelz, but that frustration is not the technical case we need to present to Metro Fibre.

The technical case is:

**Repeated instability + documented symptoms + repeated communication + no satisfactory resolution.**

Now we need to turn that into a clean evidence package that technical support cannot simply answer with, "Your speed test is fine."

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📌 Action List

- [ ] Start a dated troubleshooting log.
- [ ] Run Speedtest and Fast.com at different times.
- [ ] Record download, upload, and latency.
- [ ] Run 20-packet pings to 1.1.1.1 and 8.8.8.8.
- [ ] Run 100-packet tests when instability occurs.
- [ ] Record packet loss.
- [ ] Run traceroute.
- [ ] Run MTR where available.
- [ ] Check DNS response.
- [ ] Check Ethernet interface statistics.
- [ ] Check link speed and duplex with `ethtool`.
- [ ] Record the physical LAN-link indicators.
- [ ] Take screenshots of important results.
- [ ] Keep copies of Metro Fibre correspondence.
- [ ] Build a chronological incident history.
- [ ] Prepare one consolidated report for Metro Fibre.
- [ ] Request a technical investigation rather than another basic speed test.

<!-- PLEBVOX:END -->
