---
layout: post
title: "Metro Fibre Service Stability — Technical Evidence Report"
date: 2026-09-20
---

# Metro Fibre Internet Stability — Technical Evidence for Support

**Prepared:** 20 September 2026  
**Purpose:** Provide Metro Fibre technical support with a concise record of observed network behaviour and tests performed from the customer premises.

---

## 1. Reason for This Report

The fibre internet connection has experienced recurring instability over an extended period.

Communication regarding the problem has continued for almost two weeks without a satisfactory resolution.

This report is intended to provide technical evidence for investigation rather than simply report that the connection is "slow."

The connection can sometimes produce normal or very good performance while instability is not occurring. Therefore, individual speed tests should not be considered sufficient evidence that the service is consistently stable.

---
<div style="text-align: center;">
  <img src="/assets/images/golfclash-crash.webp"
       alt="Alt Text - Golf Clash Crash"
       style="width: 70%; max-width: 100%; height: auto;">
</div>

**This Fault Occurred at 06:02 SAST**
-----
<div style="text-align: center;">
  <img src="/assets/images/playdemic-ea-crash.webp"
       alt="Alt Text - Playdemic Crash"
       style="width: 70%; max-width: 100%; height: auto;">
</div>

**This Fault Occurred at 06:29 SAST**
-----
<div style="text-align: center;">
  <img src="/assets/images/Raid Crash.webp"
       alt="Alt Text - Raid Shadow Legends Crash"
       style="width: 70%; max-width: 100%; height: auto;">
</div>

**This Fault Occurred at 7:29 SAST**
-----
Took a break to calm down; Otto was angry!
**Had to reset the modem** by unplugging it for 5min **before getting internet back to run tests**.

-----
## 2. Test Environment

**Testing system:** Lenovo laptop  
**Operating systems used:** Linux and Windows 11 Pro  
**Connection:** Wi-Fi only  
**Router/Gateway:** 192.168.1.254  
**External test destinations:** Cloudflare DNS (1.1.1.1), Google DNS (8.8.8.8), Google services.

**Important:** All tests recorded in this report were performed from the Lenovo laptop over **Wi-Fi**. None of the tests were performed using a LAN/Ethernet cable.

---

## 3. Baseline Testing

### 20 September 2026 — Approximately 08:06

The connection appeared to be behaving normally during the initial baseline testing.

Recorded results included:

- Router: average **1.995 ms**, maximum **4.089 ms**
- 8.8.8.8: average **5.777 ms**, maximum **7.683 ms**
- 1.1.1.1: average **4.624 ms**, maximum **6.598 ms**
- Google: average **9.796 ms**, maximum **56.804 ms**
- Earlier 1.1.1.1 test: average **9.726 ms**, maximum **62.664 ms**
- 100-packet MTR to 1.1.1.1: **0.0% loss** at every reported hop
- Final-hop MTR to 1.1.1.1: average **8.6 ms**, maximum **94.9 ms**

These results establish a useful baseline during a period when the connection appeared normal.

---

## 4. MTR Test to Google DNS

### 20 September 2026 — 08:08

Command used:

```bash
mtr -rwzc 100 8.8.8.8
```

Results:

- **100 packets sent**
- Hops 1–3: **0.0% packet loss**
- Final destination: **1.0% reported packet loss**
- Final destination average: **7.1 ms**
- Best: **4.6 ms**
- Worst: **37.6 ms**
- Standard deviation: **5.7 ms**

The 1% loss reported at the final destination is recorded as an observation. It is not, by itself, proof of an ISP fault, particularly because the intermediate hops reported 0% loss.

The result should be compared with repeated tests during an actual period of instability.

---

## 5. DNS Testing

### Local Router DNS

Command:

```bash
dig google.com
```

Result:

- DNS server: **192.168.1.254**
- Query status: **NOERROR**
- Query time: **8 ms**
- Successful Google A record returned.

### Cloudflare DNS

Command:

```bash
dig @1.1.1.1 google.com
```

Result:

- DNS server: **1.1.1.1**
- Query status: **NOERROR**
- Query time: **4 ms**
- Successful Google A record returned.

### Google DNS

Command:

```bash
dig @8.8.8.8 google.com
```

Result:

- DNS server: **8.8.8.8**
- Query status: **NOERROR**
- Query time: **8 ms**
- Successful Google A record returned.

### DNS Conclusion

DNS resolution was functioning normally during these tests.

All three DNS queries completed successfully and quickly.

Different Google IP addresses were returned by the different resolvers. This is normal behaviour for a large distributed service and does not, by itself, indicate a problem.


---

## 6. Follow-Up Test — 20 September 2026

### 08:23–08:26 SAST

A second complete test batch was performed using the same combined terminal command.

#### Router — 192.168.1.254

- **20 packets transmitted**
- **0% packet loss**
- Average: **7.463 ms**
- Minimum: **1.341 ms**
- Maximum: **77.547 ms**
- Standard deviation: **16.991 ms**

Notable individual latency spikes:
- Packet 6: **77.5 ms**
- Packet 17: **15.1 ms**
- Packet 18: **24.0 ms**

#### Cloudflare — 1.1.1.1

- **20 packets transmitted**
- **0% packet loss**
- Average: **16.744 ms**
- Minimum: **3.589 ms**
- Maximum: **77.542 ms**
- Standard deviation: **25.571 ms**

Notable individual latency spikes:
- Packet 1: **62.8 ms**
- Packet 6: **63.5 ms**
- Packet 11: **66.5 ms**
- Packet 16: **77.5 ms**

#### Google — 8.8.8.8

- **20 packets transmitted**
- **0% packet loss**
- Average: **9.359 ms**
- Minimum: **4.734 ms**
- Maximum: **41.069 ms**
- Standard deviation: **8.823 ms**

Notable individual latency spikes:
- Packet 2: **22.0 ms**
- Packet 7: **22.4 ms**
- Packet 17: **41.1 ms**

#### MTR — 8.8.8.8

100-packet MTR:

- Hop 1: **0.0% loss**
- Hop 2: **0.0% loss**
- Hop 3: **0.0% loss**
- Final destination: **1.0% reported loss**
- Final average: **6.5 ms**
- Best: **4.5 ms**
- Worst: **32.9 ms**
- Standard deviation: **3.7 ms**

#### DNS

All three DNS tests completed successfully:

- Router DNS `192.168.1.254`: **NOERROR**, **8 ms**
- Cloudflare `1.1.1.1`: **NOERROR**, **4 ms**
- Google `8.8.8.8`: **NOERROR**, **8 ms**

Different Google IP addresses were returned by the resolvers, which is normal for a distributed service.

### Observation

This second test batch is particularly useful because the **router itself recorded a 77.547 ms maximum response**, despite **0% packet loss**.

Similar latency spikes were also visible when testing external destinations.

At this stage, these results should be treated as evidence of **intermittent latency variation**, not as proof of a specific fault location. Repeated tests at different times, especially during a period when the internet is visibly unstable, will help establish whether the pattern is persistent.

---

## 7. Incident and Follow-Up Test — 20 September 2026

### Connection Error Immediately Before Testing — 10:50 SAST

A further connection error was experienced immediately before this test batch was run. The full automated test was then started at **10:50:24 SAST**.

### Router — 192.168.1.254

- **20 packets transmitted**
- **19 packets received**
- **5% packet loss**
- Average: **7.616 ms**
- Minimum: **1.716 ms**
- Maximum: **108.006 ms**
- Standard deviation: **23.667 ms**

One packet did not receive a reply. Packet 16 recorded a **108 ms** response.

### Cloudflare — 1.1.1.1

- **20 packets transmitted**
- **20 received**
- **0% packet loss**
- Average: **10.702 ms**
- Minimum: **3.634 ms**
- Maximum: **69.466 ms**
- Standard deviation: **16.528 ms**

Notable latency spikes included **46.6 ms**, **69.5 ms**, and **18.7 ms**.

### Google — 8.8.8.8

- **20 packets transmitted**
- **20 received**
- **0% packet loss**
- Average: **5.570 ms**
- Minimum: **4.472 ms**
- Maximum: **8.801 ms**
- Standard deviation: **1.148 ms**

This was comparatively stable, with all recorded responses below 9 ms.

### MTR — 8.8.8.8

100-packet MTR:

- Hop 1: **0.0% loss**
- Hop 2: **0.0% loss**
- Hop 3: **0.0% loss**
- Final destination: **0.0% reported loss**
- Final average: **7.9 ms**
- Best: **4.5 ms**
- Worst: **72.3 ms**
- Standard deviation: **9.2 ms**

Although MTR reported no packet loss, latency variation was visible across the route, with a worst reported value of **72.3 ms** at the final destination.

### DNS

All three DNS tests completed successfully:

- Router DNS `192.168.1.254`: **NOERROR**, **4 ms**
- Cloudflare `1.1.1.1`: **NOERROR**, **4 ms**
- Google `8.8.8.8`: **NOERROR**, **8 ms**

### Observation

This test is significant because it was performed **immediately after another connection error** and recorded **5% packet loss to the local router itself**, together with a **108.006 ms maximum router response**.

The external tests did not show packet loss during this particular batch, although Cloudflare also showed substantial latency variation.

The results do not by themselves identify the fault location. However, the combination of a reported connection error immediately beforehand and packet loss to the local gateway provides useful evidence for comparison with future incidents and Metro Fibre's network-side monitoring.

---

## 8. Latest Test — 20 September 2026

### 12:30–12:33 SAST

A further complete test batch was performed after the earlier instability and reset. The test timestamp was **12:30:36 SAST**, with the 100-packet MTR beginning at **12:31:33 SAST**. DNS tests completed at **12:33:19 SAST**.

### Router — 192.168.1.254

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Average: **2.267 ms**
- Minimum: **1.489 ms**
- Maximum: **6.159 ms**
- Standard deviation: **1.239 ms**

The router response was stable overall, with all 20 replies below 7 ms.

### Cloudflare — 1.1.1.1

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Average: **8.495 ms**
- Minimum: **3.628 ms**
- Maximum: **87.200 ms**
- Standard deviation: **18.069 ms**

One significant latency spike occurred at packet 18: **87.2 ms**. The other responses were generally between approximately 3.6 and 5.9 ms.

### Google — 8.8.8.8

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Average: **5.470 ms**
- Minimum: **4.726 ms**
- Maximum: **7.439 ms**
- Standard deviation: **0.740 ms**

This was comparatively stable, with all recorded responses below 7.5 ms.

### MTR — 8.8.8.8

100-packet MTR:

- Hop 1: **0.0% loss**
- Hop 2: **0.0% loss**
- Hop 3: **0.0% loss**
- Final destination: **0.0% reported loss**
- Final average: **6.5 ms**
- Best: **4.6 ms**
- Worst: **47.6 ms**
- Standard deviation: **5.7 ms**

The MTR showed no reported packet loss across the four reported hops. However, latency variation was still visible, including a worst value of **47.6 ms** at the final destination.

### DNS

All three DNS tests completed successfully:

- Router DNS `192.168.1.254`: **NOERROR**, **4 ms**
- Cloudflare `1.1.1.1`: **NOERROR**, **4 ms**
- Google `8.8.8.8`: **NOERROR**, **4 ms**

The DNS tests were therefore successful and responsive during this batch.

### Observation

This latest batch shows a useful contrast with the earlier **10:50 SAST incident test**, where the local router recorded **5% packet loss** and a **108.006 ms** maximum response immediately after a connection error.

At 12:30 SAST, the local router was responding normally with **0% packet loss** and a maximum of only **6.159 ms**. Google DNS was also very stable. However, Cloudflare still recorded a single **87.2 ms** latency spike despite 0% packet loss.

This supports the value of continued time-correlated testing: the connection can appear normal at one moment while isolated latency spikes remain visible at another destination. These results do not identify the fault location by themselves, but they provide additional evidence for comparison against future incidents and Metro Fibre's network-side monitoring.


---

## 9. Windows 11 Cross-Platform Test — 20 September 2026

### 12:49:55 SAST

A further test batch was performed from **Windows 11 Pro** over Wi-Fi. This provides a useful cross-platform comparison with the earlier Linux testing.

### Local Router — 192.168.1.254

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Minimum: **2 ms**
- Maximum: **4 ms**
- Average: **2 ms**

All 20 router responses were between 2 and 4 ms.

### Cloudflare — 1.1.1.1

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Minimum: **4 ms**
- Maximum: **20 ms**
- Average: **5 ms**

One response reached **20 ms**, while most responses were between 4 and 9 ms.

### Google — 8.8.8.8

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Minimum: **4 ms**
- Maximum: **8 ms**
- Average: **5 ms**

This was comparatively stable, with all responses below 9 ms.

### Route to Google

Windows tracert reported four hops:

- Hop 1: **192.168.1.254**
- Hop 2: **196.50.234.64**
- Hop 3: **102.33.29.245**
- Hop 4: **8.8.8.8**

The route completed successfully without displayed timeouts.

### DNS

The Windows DNS tests produced the following results:

- Router DNS 192.168.1.254: successful response.
- Cloudflare DNS 1.1.1.1: **DNS request timed out after 2 seconds**, followed by a successful answer for google.com.
- Google DNS 8.8.8.8: successful response.

The Cloudflare result is worth recording because the resolver eventually returned an answer but Windows reported a timeout first. This is an observation of intermittent DNS response behaviour, not proof of a Metro Fibre fault.

### Windows Network Configuration

The Windows system was connected through:

- **Realtek 8821CE Wireless LAN 802.11ac**
- IPv4 address: **192.168.1.109**
- Default gateway: **192.168.1.254**
- DHCP server: **192.168.1.254**

The physical Ethernet adapter was reported as disconnected during this test, so this particular Windows test was conducted over **Wi-Fi**, rather than the Ethernet connection used for the earlier Linux measurements.

### Observation

This Windows test represents a **stable snapshot** at 12:49:55 SAST:

- Local router: **0% loss**, maximum **4 ms**
- Cloudflare: **0% loss**, maximum **20 ms**
- Google: **0% loss**, maximum **8 ms**
- DNS generally successful, with one Cloudflare timeout followed by a successful response.

This contrasts with the **10:50 SAST incident test**, when the router recorded **5% packet loss** and a **108.006 ms** maximum response immediately after a connection error.

Because all tests recorded in this report were performed over Wi-Fi from the Lenovo laptop, the results should be interpreted as observations of the fibre service as experienced through the same local wireless path. The Linux and Windows results are therefore useful as cross-platform and cross-time observations, but they do not provide an Ethernet-versus-Wi-Fi comparison. Continued testing during actual connection failures remains the most valuable evidence.


---

## 10. Important Technical Observation

The testing demonstrates why the investigation should not rely exclusively on conventional speed testing.

Across the recorded test batches:

- Latency to major public DNS services is generally low.
- DNS resolution has been successful.
- Packet loss has varied between **0% and 5%** in customer-side tests, depending on the time and destination.
- MTR has shown both **0% and 1% reported final-destination loss** in different tests.
- Significant isolated latency spikes have been observed, including **108.006 ms to the local router**, **87.2 ms to Cloudflare**, and other elevated values during earlier batches.

These results are valuable because they establish what the connection looks like both during apparently normal operation and around reported incidents.

The same measurements should continue to be taken when the connection is actually unstable.

---

## 11. What We Are Asking Metro Fibre to Investigate

Please investigate the service for possible intermittent problems that may not be visible during a single speed test, including:

- Intermittent packet loss.
- Latency spikes.
- Fibre/ONT or optical-link issues.
- Router or termination issues.
- Port or link negotiation problems.
- Local access-network problems.
- Routing instability.
- Any errors, alarms, or degradation visible from the Metro Fibre network side.

Please also check whether the service shows any historical or intermittent faults that may not be present at the exact moment a technician performs a speed test.

---

## 12. Requested Technical Response

We would appreciate a technical investigation rather than another basic speed test alone.

Please advise:

1. Whether Metro Fibre can see any packet loss, errors, optical degradation, link flaps, or other abnormal behaviour on the service.
2. Whether the ONT/fibre termination and associated network port are reporting normally.
3. Whether there are any relevant faults or incidents affecting the access network.
4. Whether the observed intermittent instability can be correlated with Metro Fibre network-side monitoring.
5. What corrective action is recommended if an issue is found.

---

## 13. Evidence Available

The following evidence can be supplied to support the investigation:

- MTR results.
- Ping results.
- DNS test results.
- Speed-test results.
- Screenshots.
- Network interface and Wi-Fi configuration information.
- Chronological records of incidents.
- Previous communication regarding the fault.

Further tests will be recorded during periods of actual instability so that they can be compared directly with this baseline.

---

## 14. Summary for Technical Support

**The issue being reported is recurring internet instability, not simply inadequate internet speed.**

The connection can produce good performance during normal periods, while intermittent symptoms may occur at other times.

A technical investigation using Metro Fibre's network-side monitoring, together with the customer-side evidence above, should provide a better opportunity to identify the underlying cause.

**Please investigate the service for intermittent instability and provide the technical findings.**

---

## 15. Evening Test — 20 September 2026

### 20:21–20:24 SAST

A further complete test batch was performed from the Lenovo laptop running MX Linux over Wi-Fi.

### Router — 192.168.1.254

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Average: **2.458 ms**
- Minimum: **1.583 ms**
- Maximum: **12.634 ms**
- Standard deviation: **2.365 ms**

Most responses were approximately 1.6–2.0 ms. One response reached **12.6 ms**, with another at **3.32 ms**.

### Cloudflare — 1.1.1.1

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Average: **4.863 ms**
- Minimum: **3.597 ms**
- Maximum: **15.657 ms**
- Standard deviation: **2.550 ms**

Most responses were below 6 ms, with one response reaching **15.7 ms**.

### Google — 8.8.8.8

- **20 packets transmitted**
- **20 packets received**
- **0% packet loss**
- Average: **9.499 ms**
- Minimum: **4.560 ms**
- Maximum: **50.396 ms**
- Standard deviation: **10.605 ms**

Notable latency spikes included:

- Packet 4: **24.4 ms**
- Packet 13: **50.4 ms**
- Packet 19: **19.0 ms**

### MTR — 8.8.8.8

100-packet MTR:

- Hop 1: **0.0% loss**
- Hop 2: **0.0% loss**
- Hop 3: **0.0% loss**
- Final destination: **0.0% reported loss**
- Final average: **5.7 ms**
- Best: **4.6 ms**
- Worst: **25.3 ms**
- Standard deviation: **2.1 ms**

The MTR showed **0% reported packet loss at every reported hop**. The second hop nevertheless recorded a worst response of **49.1 ms**, while the final destination recorded a worst response of **25.3 ms**.

### DNS

All three DNS tests completed successfully:

- Router DNS 192.168.1.254: **NOERROR**, **4 ms**
- Cloudflare 1.1.1.1: **NOERROR**, **4 ms**
- Google 8.8.8.8: **NOERROR**, **4 ms**

### Observation

This evening test shows **stable connectivity with 0% packet loss**, but measurable intermittent latency variation remains visible.

The local router was generally responding around 1.6–2.0 ms, but reached **12.634 ms**. Cloudflare reached **15.657 ms**, while Google recorded a larger **50.396 ms** maximum.

The result should not be interpreted as proof of a specific fault location. It is another useful time-stamped data point showing that the connection can have no packet loss while isolated latency spikes remain present.

Compared with the earlier **10:50 SAST incident test**, this is a materially different condition: the 10:50 test recorded **5% packet loss to the local router and a 108.006 ms maximum router response**, whereas the 20:21 test recorded **0% loss and a 12.634 ms router maximum**.

---

## 16. Updated Overall Observation

The additional evening test strengthens the value of maintaining a chronological record of the connection rather than relying on one-off speed tests.

The recorded data now includes periods showing:

- **0% packet loss with low and stable latency**.
- **0% packet loss with isolated latency spikes**.
- **1% reported final-destination loss in some MTR tests**.
- **5% packet loss to the local router immediately after a reported connection error**.
- A local-router maximum response of **108.006 ms** during that incident test.

This variation is consistent with an intermittent problem requiring time-correlated investigation. The customer-side tests alone do not establish where the fault originates, but they provide measurable evidence that can be compared against Metro Fibre's network-side monitoring and historical service records.

---

**Prepared for:** Metro Fibre Technical Support  
**Date:** 20 September 2026  
**Document type:** Customer technical evidence report


---

## 17. Service Status Update — 22 September 2026

### Morning Observation

On the morning of **22 September 2026**, the two Metro Fibre status lights that had previously indicated the service condition were observed to be **green**.

The change is recorded as an observation only. The customer is not currently at the premises and therefore **no network tests can be performed at this time**.

The fact that the status lights are now green is nevertheless relevant to the incident timeline. It should be recorded alongside the earlier reports of instability so that the timing can be compared with Metro Fibre's network-side records and any remote corrective action that may have occurred.

This report does **not** make any allegation about the cause of the change. It simply records that the indicators were previously not showing the normal condition and are now both green.

Further customer-side testing will be performed when access to the premises is available.

---

**Status update:** 22 September 2026  
**Current observation:** Both Metro Fibre status lights green.  
**Network testing:** Not possible at present because the customer is away from the premises.
