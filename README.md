# 🏠 Homelab Portfolio

<div align="center">

![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![Updated](https://img.shields.io/badge/updated-daily-blue?style=for-the-badge)
![Labs](https://img.shields.io/badge/labs-building-orange?style=for-the-badge)

**Building Real-World Cybersecurity Skills | One Lab at a Time**

[About](#-about) • [Lab Infrastructure](#-lab-infrastructure) • [Projects](#-projects) • [Skills](#-skills) • [Contact](#-contact)

</div>

---

## 👋 About

Hey! I'm **[YOUR NAME]**, and this is my homelab documentation portfolio. I'm learning cybersecurity by actually **doing** it - building vulnerable environments, testing them, breaking them, and documenting everything along the way.

**Why this exists:**
- 📚 **Learn by doing** - Hands-on practice with real tools
- 📝 **Document everything** - If I learned it, I write about it
- 🔍 **Show my work** - Proof of skills for employers and recruiters
- 🤝 **Help others learn** - Share what I discover with the community

**Currently focusing on:** 
> 🎯 Active Directory security, penetration testing, and building SOC infrastructure

---

## 🏗️ Lab Infrastructure

My homelab is built on **Proxmox** running multiple virtual machines that simulate a real enterprise environment. Think of it as my personal cyber playground where I can safely break things and learn how they work!

### 🖥️ The Setup

```
┌─────────────────────────────────────────────┐
│         Proxmox Hypervisor (Host)           │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────┐  ┌──────────────────┐   │
│  │ Kali Linux   │  │ Windows Server   │   │
│  │ (Attacker)   │  │ 2025 DC          │   │
│  │              │  │ LAB.local        │   │
│  └──────────────┘  └──────────────────┘   │
│                                             │
│  ┌──────────────┐  ┌──────────────────┐   │
│  │Metasploitable│  │ Windows 11       │   │
│  │(Vulnerable)  │  │ (Domain Joined)  │   │
│  │+ DVWA        │  │                  │   │
│  └──────────────┘  └──────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```
![Description of image](assets/images/home_lab_diagram.png)
### 📦 Virtual Machines

| VM | Purpose | Status | Key Features |
|---|---|---|---|
| **🐉 Kali Linux** | Attack platform | 🟢 Running | Penetration testing, security auditing |
| **🎯 Metasploitable 2** | Vulnerable target | 🟢 Running | Practice environment, DVWA hosted |
| **💻 Windows 11** | Domain workstation | 🟢 Running | Joined to LAB.local domain |
| **🏢 Windows Server 2025** | Domain Controller | 🟢 Running | AD DS, AD CS, user management |

### 🌐 Network Details

- **Domain:** `LAB.local`
- **Domain Controller:** Windows Server 2025
- **Test Environment:** Metasploitable 2 @ `http://172.22.1.26/dvwa`

---

## 🎯 What I've Built (So Far!)

### ✅ Active Directory Environment
Built a fully functional Windows domain environment from scratch:
- ✅ Configured Windows Server 2025 as Domain Controller
- ✅ Installed Active Directory Domain Services (AD DS)
- ✅ Installed Active Directory Certificate Services (AD CS)
- ✅ Created domain users (LAB\Wick)
- ✅ Joined Windows 11 workstation to domain

**Why this matters:** Understanding Active Directory is crucial for both defense (securing it) and offense (attacking it). Most enterprise environments use AD, so this gives me real-world experience.

### 🚧 Currently Working On

- [ ] Penetration testing labs using Kali → Metasploitable
- [ ] DVWA challenges and writeups
- [ ] Active Directory attack simulations
- [ ] Building a Security Operations Center (SOC)
- [ ] Network traffic analysis

---

## 🔐 Projects

> 📁 *Project documentation coming soon! Each project will include detailed writeups, screenshots, and lessons learned.*

### Upcoming Projects:
- **SOC Build** - Setting up monitoring and detection
- **AD Attack & Defense** - Red vs Blue team scenarios  
- **Web App Penetration Testing** - DVWA exploitation
- **Network Security** - Firewall rules, segmentation, monitoring

---

## 🛠️ Skills & Tools

**Operating Systems:**
- 🐧 Kali Linux
- 🪟 Windows Server 2025
- 🪟 Windows 11
- 🐧 Linux (Debian-based)

**Security Tools:**
- 🔍 Nmap, Metasploit, Burp Suite
- 🎯 DVWA (Damn Vulnerable Web Application)

**Infrastructure:**
- ☁️ Proxmox VE
- 🌐 Active Directory
- 🔐 Certificate Services

**Currently Learning:**
- Penetration Testing
- Active Directory Security
- Security Operations
- Network Defense

---

## 📊 Lab Statistics

```
🎯 Virtual Machines: 4
⚡ Active Projects: [EXPANDING]
📚 Documentation: In Progress
🔥 Days Active: Daily
```

---

## 🗺️ Roadmap

**Phase 1: Foundation** *(Current)*
- [x] Build Proxmox homelab
- [x] Deploy Windows domain environment
- [x] Set up attack and target VMs
- [ ] Document initial setup

**Phase 2: Security Projects**
- [ ] Complete DVWA challenges
- [ ] Perform penetration tests
- [ ] Document attack chains
- [ ] Build SOC infrastructure

**Phase 3: Advanced Labs**
- [ ] Purple team exercises
- [ ] Threat hunting scenarios
- [ ] Incident response simulations
- [ ] Automation and scripting

---

## 📖 Learning Resources

I document my learning journey and share useful resources:

- 📚 **Research Notes** - Things I've learned and want to remember
- 🎓 **Guides** - Step-by-step tutorials I create
- 🔗 **Resources** - Helpful links and references
- 💡 **TIL (Today I Learned)** - Quick wins and discoveries

*Coming soon to this repo!*

---

## 📬 Contact

Want to connect, collaborate, or chat about homelab stuff?

- 📧 Email: **[your-email]**
- 💼 LinkedIn: **[your-linkedin]**
- 🐙 GitHub: **[your-github]**

---

## 🙏 Acknowledgments

This homelab journey is possible thanks to:
- The cybersecurity community for sharing knowledge
- Open source tools and vulnerable applications for practice
- Everyone who documents their labs and shares their learning

---

<div align="center">

**🚀 This portfolio is actively maintained and updated daily**

*Last Updated: November 2025*

---

⭐ **Found this helpful? Star this repo!** ⭐

</div>
