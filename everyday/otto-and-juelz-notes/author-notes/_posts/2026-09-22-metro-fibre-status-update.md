---
layout: post
title: "Metro Fibre Status Update — 22 September 2026"
date: 2026-09-22
---

# Metro Fibre Connection — Customer-Side Test Results

**📰 Field Report — 22 September 2026**

## Morning Observation

On the morning of **22 September 2026**, both LAN Card status lights were observed to be **green**.

This was after they had been displaying **Green and Orange** for a couple of months; they were observed as **both green** this morning.

This is recorded as a factual observation only. No conclusion is being made regarding the cause of the change.

The service indicators remain relevant to the ongoing incident record because they had previously shown a different condition. The timing of this change may therefore be useful when compared with Metro Fibre's technical records and any work performed on the service.

## Customer-Side Network Testing

After returning home from work, I performed a customer-side network test at approximately **14:54–14:57 SAST on 22 September 2026**.

The test included the local router, Cloudflare, Google, a 100-packet MTR test, and DNS queries through the router, Cloudflare DNS, and Google DNS.

### Local Router — 192.168.1.254

- **20 packets transmitted.**
- **20 packets received.**
- **0% packet loss.**
- Minimum latency: **1.596 ms**.
- Average latency: **2.006 ms**.
- Maximum latency: **3.062 ms**.

The local connection to the router was therefore responding consistently during this test.

### Cloudflare — 1.1.1.1

- **20 packets transmitted.**
- **20 packets received.**
- **0% packet loss.**
- Minimum latency: **5.354 ms**.
- Average latency: **6.294 ms**.
- Maximum latency: **10.328 ms**.

### Google — 8.8.8.8

- **20 packets transmitted.**
- **20 packets received.**
- **0% packet loss.**
- Minimum latency: **5.467 ms**.
- Average latency: **6.185 ms**.
- Maximum latency: **7.871 ms**.

### MTR — Google 8.8.8.8

A **100-packet MTR test** was performed.

The recorded route showed:

- Local router: **0.0% loss**, average **1.9 ms**.
- First upstream hop: **0.0% loss**, average **6.1 ms**.
- Second upstream hop: **0.0% loss**, average **6.2 ms**.
- Google destination: **0.0% loss**, average **6.9 ms**.

The MTR therefore recorded **0% packet loss across all reported hops and at the destination during this test**.

### DNS Testing

DNS resolution was successful through all three tested DNS paths:

- Router DNS — **192.168.1.254:** google.com resolved successfully; query time **4 ms**.
- Cloudflare DNS — **1.1.1.1:** google.com resolved successfully; query time **8 ms**.
- Google DNS — **8.8.8.8:** google.com resolved successfully; query time **8 ms**.

## Technical Record

The customer-side test performed on the afternoon of **22 September 2026** recorded:

- Both LAN Card status lights observed green in the morning.
- Local router connectivity: **0% packet loss**.
- Cloudflare connectivity: **0% packet loss**.
- Google connectivity: **0% packet loss**.
- 100-packet MTR to Google: **0% packet loss on all reported hops and destination**.
- DNS resolution through the router, Cloudflare, and Google: **successful**.

These results document the condition of the connection at the time of testing. They do not establish the cause of the earlier service problems or the reason for the change in indicator-light status.

The results are being added to the existing technical evidence record so that the sequence of events and customer-side observations remain documented accurately.

---

**Prepared for:** Metro Fibre Technical Support  
**Status:** Customer-side testing completed and recorded.  
**Test period:** Approximately 14:54–14:57 SAST, 22 September 2026.  
**Result:** Connectivity and DNS tests completed successfully with 0% packet loss in the recorded tests.
