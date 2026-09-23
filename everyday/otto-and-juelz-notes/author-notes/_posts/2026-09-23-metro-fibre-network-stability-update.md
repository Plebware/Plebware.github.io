---
layout: post
title: "Metro Fibre Network Stability Update — 23 September 2026"
date: 2026-09-23
---

# Metro Fibre Connection — Recurrence of Network Instability

**📰 Field Report — 23 September 2026**

## Incident Summary

On the morning of **23 September 2026**, Jullian reported that the LAN Card status lights had reverted to the previously observed **Green and Orange** condition.

At the same time, the network was experiencing major instability and repeated network errors. The connection became sufficiently unstable that the modem/router had to be rebooted before connectivity could be restored.

This report records the new incident and compares it with the customer-side test results obtained on 22 September.

## Previous Status — 22 September 2026

On the morning of **22 September 2026**, both LAN Card status lights were observed to be **green**.

Customer-side testing later that afternoon, approximately **14:54–14:57 SAST**, recorded:

- Local router: **0% packet loss**.
- Cloudflare: **0% packet loss**.
- Google: **0% packet loss**.
- 100-packet MTR to Google: **0% packet loss** across all reported hops and destination.
- DNS resolution through the router, Cloudflare, and Google: **successful**.

The complete customer-side test results are documented in the previous report.

## Recurrence — 23 September 2026

This morning, the LAN indicators have again changed to:

**Green + Orange.**

The change coincides with a significant deterioration in network behaviour.

Jullian reported:

- Major network errors.
- Severe network instability.
- Loss of reliable connectivity.
- The need to reboot the modem/router to restore service.

The recurrence is particularly relevant because the previous day's customer-side testing had recorded a clean baseline with 0% packet loss.

## Sequence of Observed Conditions

| Date | LAN Indicator Condition | Observed Network Condition |
|---|---|---|
| Previous period | Green + Orange | Recurring instability reported. |
| 20 September | Green + Orange | Network instability documented during the ongoing investigation. |
| 22 September | Green + Green | Customer-side tests recorded 0% packet loss and successful DNS resolution. |
| 23 September | Green + Orange | Major instability and network errors reported; modem/router reboot required. |

This table records observations rather than assigning a cause.

## Physical Intervention

There has been no known physical intervention on the router that would explain the change in indicator status.

No Metro Fibre technician has attended the property.

The Green + Orange condition had previously remained present for an extended period. It subsequently changed to Green + Green without a known physical intervention, and has now reverted to Green + Orange.

## Technical Significance

The available observations document different network states occurring at different times:

**22 September:** Green + Green, followed by clean customer-side testing.

**23 September:** Green + Orange, accompanied by severe network instability.

This correlation is worth adding to Metro Fibre's technical investigation. It does not, by itself, establish the cause of the indicator-light change or the network failures.

Further testing should be performed while the fault is active where practical, so that the network condition can be compared with the previous clean baseline.

## Current Status

As of the morning of **23 September 2026**, the network problem has recurred.

The latest customer report and the return of the Green + Orange LAN indication have been recorded as part of the ongoing incident history.

---

**Prepared for:** Metro Fibre Technical Support  
**Author:** Otto Brinkmeier  
**Date:** 23 September 2026  
**Status:** Active incident — recurrence reported.
