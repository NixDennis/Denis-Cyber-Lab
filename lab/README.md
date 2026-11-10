# Home lab

My practice environment in VirtualBox. Everything here runs on my own machine, on an isolated network.

## Machines

| Machine | Role | Status |
| ------- | ---- | ------ |
| Kali Linux | Attacker machine with security tools | Planned |
| Metasploitable | Intentionally vulnerable target | Planned |

## Setup checklist

- [ ] Install VirtualBox
- [ ] Create the Kali Linux VM
- [ ] Create the Metasploitable VM
- [ ] Put both on a host-only network so the vulnerable VM is never exposed to the internet
- [ ] First test: scan Metasploitable from Kali

## Experiments

One file per experiment, for example `01-first-scan.md`: what I tried, the commands I ran, what I found and what I learned.
