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

## 2. Test Environment

**Testing system:** Linux desktop  
**Connection:** Ethernet/LAN cable  
**Router/Gateway:** 192.168.1.254  
**External test destinations:** Cloudflare DNS (1.1.1.1), Google DNS (8.8.8.8), Google services.

A new Cat5 LAN cable is currently being used.

The network interface also shows normal green/orange link and activity indicators.

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

## 6. Important Technical Observation

The testing demonstrates why the investigation should not rely exclusively on conventional speed testing.

During the recorded baseline period:

- Latency to major public DNS services was low.
- DNS resolution was successful.
- Packet loss was 0% on the initial MTR to 1.1.1.1.
- A subsequent MTR to 8.8.8.8 reported 1% loss at the final destination.
- Occasional higher latency values were observable even while the connection otherwise appeared healthy.

These results are valuable because they establish what the connection looks like when it is functioning normally.

The same measurements should be taken when the connection is actually unstable.

---

## 7. What We Are Asking Metro Fibre to Investigate

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

## 8. Requested Technical Response

We would appreciate a technical investigation rather than another basic speed test alone.

Please advise:

1. Whether Metro Fibre can see any packet loss, errors, optical degradation, link flaps, or other abnormal behaviour on the service.
2. Whether the ONT/fibre termination and associated network port are reporting normally.
3. Whether there are any relevant faults or incidents affecting the access network.
4. Whether the observed intermittent instability can be correlated with Metro Fibre network-side monitoring.
5. What corrective action is recommended if an issue is found.

---

## 9. Evidence Available

The following evidence can be supplied to support the investigation:

- MTR results.
- Ping results.
- DNS test results.
- Speed-test results.
- Screenshots.
- Ethernet interface statistics.
- Link-speed and duplex information.
- Chronological records of incidents.
- Previous communication regarding the fault.

Further tests will be recorded during periods of actual instability so that they can be compared directly with this baseline.

---

## 10. Summary for Technical Support

**The issue being reported is recurring internet instability, not simply inadequate internet speed.**

The connection can produce good performance during normal periods, while intermittent symptoms may occur at other times.

A technical investigation using Metro Fibre's network-side monitoring, together with the customer-side evidence above, should provide a better opportunity to identify the underlying cause.

**Please investigate the service for intermittent instability and provide the technical findings.**

---

**Prepared for:** Metro Fibre Technical Support  
**Date:** 20 September 2026  
**Document type:** Customer technical evidence report
