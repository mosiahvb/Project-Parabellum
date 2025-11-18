# 🍎 MacBook Pro SOC Analyst Workstation Setup

## 🎯 What You're Building

Your MacBook Pro will become your **Security Operations Center command center** - the machine you use to:
- Monitor security alerts in Wazuh
- Investigate incidents
- Analyze network traffic
- Document findings
- Research threats
- Write reports

**This is the same setup professional SOC analysts use!**

---

## 📋 What Makes a Good SOC Analyst Workstation?

Think of it like a detective's desk - you need different tools for different parts of an investigation:

| Tool Type | What It Does | Real-World Example |
|-----------|--------------|-------------------|
| **Web Browser** | Access SIEM, research threats | Opening Wazuh dashboard |
| **Network Analysis** | Examine traffic, packets | "What did this suspicious connection do?" |
| **Documentation** | Write reports, keep notes | Incident response reports |
| **Terminal** | Run commands, SSH into systems | "Let me check that server" |
| **Screenshots** | Capture evidence | "Here's proof of the attack" |
| **Note-Taking** | Track investigations | Daily log of what you found |

---

## 🚀 Phase 1: Essential Browser Setup (15 minutes)

### Why This Matters:
You'll spend 70% of your time in a browser accessing:
- Wazuh dashboard
- Threat intelligence sites
- Research
- Documentation

### Step 1.1: Install Multiple Browsers

**Why multiple browsers?**
- Different tabs/profiles for different tasks
- Some tools work better in specific browsers
- Separation of concerns

#### Install These Browsers:

**1. Safari** (Already installed)
- Use for: Personal browsing, keeping it clean

**2. Google Chrome** (Primary work browser)
```
Download from: https://www.google.com/chrome/

Use for:
- Wazuh dashboard (primary)
- Threat intelligence research
- Documentation sites
```

**3. Firefox** (Secondary work browser)
```
Download from: https://www.mozilla.org/firefox/

Use for:
- Testing if something doesn't work in Chrome
- Privacy-focused research
- Backup browser
```

---

### Step 1.2: Set Up Chrome for SOC Work

**Create a Dedicated Profile:**

1. Open Chrome
2. Click your profile icon (top right)
3. Click: "Add"
4. Name it: "SOC Analyst Work"
5. Choose an icon color (I like red for security work!)
6. Click: "Done"

**Why?** Keeps work separate from personal browsing.

---

### Step 1.3: Install Essential Browser Extensions

**In your SOC Analyst Work profile, install:**

#### Security & Investigation Extensions:

**1. Wappalyzer**
```
What it does: Identifies technologies on websites
Why you need it: "What is this suspicious site running?"

Chrome Web Store → Search "Wappalyzer" → Add
```

**2. BuiltWith**
```
What it does: Shows website infrastructure
Why you need it: Understanding target websites during investigations

Chrome Web Store → Search "BuiltWith" → Add
```

**3. Shodan Extension**
```
What it does: Quick internet-connected device lookups
Why you need it: "What services are running on this IP?"

Chrome Web Store → Search "Shodan" → Add
(You'll need a free Shodan account)
```

**4. IP Address and Domain Information**
```
What it does: Quick IP/domain lookups
Why you need it: Fast threat investigation

Chrome Web Store → Search "IP Address and Domain Information" → Add
```

**5. User-Agent Switcher**
```
What it does: Changes how your browser identifies itself
Why you need it: Testing different scenarios, investigating web attacks

Chrome Web Store → Search "User-Agent Switcher" → Add
```

#### Productivity Extensions:

**6. OneTab**
```
What it does: Saves all tabs into one list
Why you need it: "I have 50 tabs for this investigation!"

Chrome Web Store → Search "OneTab" → Add
```

**7. Toby for Chrome**
```
What it does: Organizes tabs into collections
Why you need it: Organize investigations by incident

Chrome Web Store → Search "Toby" → Add
```

---

### Step 1.4: Set Up Bookmarks Folder Structure

**Create this folder structure in Chrome Bookmarks:**

```
📁 SOC Work
  └─ 📁 SIEM & Monitoring
      └─ Wazuh Dashboard (add when you install it)
      └─ Proxmox Console (https://172.22.1.22:8006)
  
  └─ 📁 Threat Intelligence
      └─ VirusTotal (https://www.virustotal.com)
      └─ AbuseIPDB (https://www.abuseipdb.com)
      └─ Shodan (https://www.shodan.io)
      └─ AlienVault OTX (https://otx.alienvault.com)
      └─ URLScan.io (https://urlscan.io)
      └─ Hybrid Analysis (https://www.hybrid-analysis.com)
  
  └─ 📁 Security Research
      └─ MITRE ATT&CK (https://attack.mitre.org)
      └─ CVE Database (https://cve.mitre.org)
      └─ Exploit-DB (https://www.exploit-db.com)
      └─ OWASP Top 10 (https://owasp.org/www-project-top-ten/)
  
  └─ 📁 Documentation
      └─ Your incident report templates
      └─ Company security policies
  
  └─ 📁 Learning Resources
      └─ TryHackMe (https://tryhackme.com)
      └─ HackTheBox (https://www.hackthebox.com)
```

**How to create folders:**
1. Bookmarks menu → Bookmark Manager
2. Right-click → Add folder
3. Drag bookmarks into folders

---

## 💻 Phase 2: Terminal Setup (30 minutes)

### Why This Matters:
You'll use the terminal to:
- SSH into your lab VMs
- Run network commands
- Quick investigations
- Automate tasks

### Step 2.1: Set Up iTerm2 (Better than default Terminal)

**Why iTerm2 instead of default Terminal?**
- Split panes (multiple terminals in one window)
- Better search
- More customization
- Tabs management

**Install iTerm2:**
```
1. Go to: https://iterm2.com
2. Download and install
3. Open iTerm2
4. Go to: iTerm2 → Make iTerm2 Default Term
```

---

### Step 2.2: Install Homebrew (Package Manager)

**What is Homebrew?**
Think of it as the "App Store for command-line tools" - makes installing security tools super easy.

**Install:**
```bash
# Open iTerm2 and paste this:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Follow the prompts (enter your Mac password when asked)
# This takes 5-10 minutes
```

**Verify it worked:**
```bash
brew --version
# Should show: Homebrew 4.x.x
```

---

### Step 2.3: Install Essential Terminal Tools

**Install these one by one:**

```bash
# Network analysis tool (like Task Manager for network)
brew install nmap

# DNS lookup tool
brew install dig

# Better version of ping
brew install mtr

# JSON processor (for reading logs)
brew install jq

# YAML processor (for config files)
brew install yq

# Modern replacement for 'cat'
brew install bat

# Modern replacement for 'ls'
brew install exa

# Search tool (better than grep)
brew install ripgrep

# Fancy top replacement
brew install htop

# Network traffic monitor
brew install iftop

# Git (version control)
brew install git

# Curl (already installed, but this is latest)
brew install curl

# Wget (download files)
brew install wget

# Watch (run commands repeatedly)
brew install watch

# Tree (view directory structure)
brew install tree

# SSH client improvements
brew install openssh
```

**What each tool does:**

| Tool | What It Does | Example Use |
|------|-------------|-------------|
| **nmap** | Scans networks for devices/ports | "What's running on this server?" |
| **dig** | DNS queries | "Where does this domain point?" |
| **mtr** | Network path tracing | "Why can't I reach this server?" |
| **jq** | Parse JSON logs | Reading Wazuh logs in terminal |
| **bat** | View files with syntax highlighting | Reading config files nicely |
| **ripgrep** | Fast search | "Find all mentions of this IP in logs" |

---

### Step 2.4: Set Up SSH Keys (For Secure Lab Access)

**Why?** Instead of typing passwords every time you SSH into your lab VMs.

**Create SSH key:**
```bash
# Generate key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter for default location
# Enter a passphrase (or press Enter for none)

# View your public key
cat ~/.ssh/id_ed25519.pub
```

**Later, you'll copy this to your lab VMs for passwordless login!**

---

### Step 2.5: Customize Your Terminal (Optional but Cool!)

**Install Oh My Zsh (makes terminal pretty and useful):**

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**Install Powerlevel10k theme (makes it look professional):**
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Edit your .zshrc
nano ~/.zshrc

# Find the line: ZSH_THEME="robbyrussell"
# Change to: ZSH_THEME="powerlevel10k/powerlevel10k"

# Save and exit (Ctrl+X, Y, Enter)

# Restart terminal
source ~/.zshrc
```

**You'll see a setup wizard - just follow the prompts!**

---

### Step 2.6: Create Useful Aliases

**What are aliases?** Shortcuts for commands you use often.

**Add these to your ~/.zshrc:**

```bash
# Open the file
nano ~/.zshrc

# Scroll to the bottom and add:

# === SOC Analyst Aliases ===

# Quick access to lab
alias lab-ssh="ssh admin@172.22.1.22"
alias wazuh="ssh admin@[your-wazuh-IP]"

# Network shortcuts
alias myip="curl ifconfig.me"
alias ports="netstat -tulanp"
alias listening="lsof -i -P | grep LISTEN"

# Quick scans (replace with your lab IP range)
alias lab-scan="nmap -sn 172.22.1.0/24"

# Better ls
alias ll="exa -la"
alias lt="exa --tree"

# JSON formatting
alias prettyjson="jq '.'"

# Quick notes
alias notes="nano ~/soc-notes.txt"

# Show all IPs on local network
alias ips="arp -a"

# === End SOC Aliases ===

# Save and exit (Ctrl+X, Y, Enter)

# Reload your config
source ~/.zshrc
```

**Now you can type `lab-scan` instead of the full nmap command!**

---

## 📊 Phase 3: Network Analysis Tools (20 minutes)

### Step 3.1: Install Wireshark

**What is Wireshark?**
The #1 tool for analyzing network traffic. Like having X-ray vision for your network.

**Install:**
```bash
brew install --cask wireshark

# Allow running as non-root
sudo dseditgroup -o edit -a $(whoami) -t user access_bpf
```

**Verify:**
- Open Applications → Wireshark
- You should see network interfaces listed

**When to use it:**
- "What data is this suspicious connection sending?"
- "Let me capture this attack in action"
- "What protocols is this malware using?"

---

### Step 3.2: Install Nmap with GUI (Zenmap alternative)

Nmap is already installed, but let's add a GUI for easier use:

```bash
# We'll use Angry IP Scanner instead (works better on Mac)
brew install --cask angry-ip-scanner
```

**What is Angry IP Scanner?**
- Visual network scanner
- See all devices on your network
- Quick port scans
- Easier than command-line for beginners

**When to use it:**
- "What devices are on my lab network?"
- "Is this VM running?"
- Quick reconnaissance

---

## 📝 Phase 4: Documentation & Note-Taking (15 minutes)

### Step 4.1: Set Up Obsidian (Best for SOC Work)

**What is Obsidian?**
A note-taking app perfect for security investigations because:
- Links between notes (like a wiki)
- Markdown support
- Graph view of connections
- Great for tracking complex investigations

**Install:**
```bash
brew install --cask obsidian
```

**Set Up Your SOC Vault:**

1. Open Obsidian
2. Create new vault: "SOC-Lab"
3. Save location: Documents/SOC-Lab

**Create this folder structure:**
```
SOC-Lab/
  ├─ Daily Notes/
  │   └─ 2025-11-02-Lab-Work.md
  ├─ Incidents/
  │   └─ Template-Incident-Report.md
  ├─ Learning/
  │   └─ SQL-Injection-Notes.md
  ├─ Configurations/
  │   └─ Lab-IPs.md
  └─ Resources/
      └─ Useful-Commands.md
```

---

### Step 4.2: Create Investigation Templates

**Incident Report Template:**

Create: `Incidents/Template-Incident-Report.md`

```markdown
# Incident Report: [NAME]

## Incident Details
- **Date Detected**: 
- **Detected By**: 
- **Severity**: Low / Medium / High / Critical
- **Status**: Open / Investigating / Resolved

## Summary
Brief description of what happened

## Timeline
- **[Time]**: Event 1
- **[Time]**: Event 2
- **[Time]**: Event 3

## Technical Details
### Affected Systems
- System 1: IP, hostname
- System 2: IP, hostname

### Indicators of Compromise (IOCs)
- IPs:
- Domains:
- File hashes:
- URLs:

## Investigation Steps
1. What I checked first
2. Tools used
3. Findings

## Evidence
- Screenshot 1: [description]
- Log excerpt 1: [description]

## Root Cause
What actually happened and why

## Remediation Actions
- [ ] Action 1
- [ ] Action 2
- [ ] Action 3

## Lessons Learned
What did I learn? What would I do differently?

## References
- Links to related alerts
- Research articles
- MITRE ATT&CK techniques
```

---

### Step 4.3: Daily Lab Notes Template

Create: `Daily Notes/Template-Daily.md`

```markdown
# Lab Work - [DATE]

## Goals for Today
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## What I Built/Configured
-

## Attacks I Practiced
1. **Attack Name**: 
   - Target: 
   - Tool used:
   - Result:
   - Detection in Wazuh: Yes/No

## Problems I Faced
1. Problem:
   - How I solved it:

## Cool Things I Discovered
-

## Tomorrow's Goals
- [ ] 
- [ ] 

## Time Spent: X hours

## Links
- Related incidents:
- Helpful resources:
```

---

### Step 4.4: Alternative: Apple Notes (Simpler)

If Obsidian feels too complex at first, use Apple Notes:

**Create these folders:**
```
Notes/
  └─ SOC Lab/
      ├─ Daily Work
      ├─ Incident Reports
      ├─ Learning Notes
      └─ Configurations
```

**Advantage:** Already on your Mac, syncs to iPhone
**Disadvantage:** Less powerful for linking complex investigations

---

## 📸 Phase 5: Screenshot & Evidence Collection (10 minutes)

### Step 5.1: Use Built-in Mac Screenshot Tools

**Learn these keyboard shortcuts:**

```
⌘ + Shift + 3  = Capture entire screen
⌘ + Shift + 4  = Select area to capture
⌘ + Shift + 5  = Screenshot tool with options
⌘ + Shift + 6  = Capture Touch Bar (if you have one)
```

**Change default save location:**
1. Press ⌘ + Shift + 5
2. Click "Options"
3. Choose "Save to": Create "Desktop/SOC-Evidence" folder

---

### Step 5.2: Install CleanShot X (Optional - Professional Tool)

**What is CleanShot X?**
Professional screenshot tool used by security professionals for:
- Annotating screenshots
- Recording screen
- Scrolling captures (entire web pages)
- Cloud backup

**Install (free trial):**
```
Download from: https://cleanshot.com
```

**Or use free alternative - Shottr:**
```bash
brew install --cask shottr
```

---

## 📊 Phase 6: Monitoring & Dashboard Setup (10 minutes)

### Step 6.1: Install Stats (System Monitor)

**What is Stats?**
Shows your Mac's performance in the menu bar - useful for:
- Monitoring resource usage during lab work
- Knowing when your Mac is working hard
- Checking network activity

**Install:**
```bash
brew install --cask stats
```

**Configure:**
1. Open Stats
2. Enable: CPU, Memory, Network
3. These will show in your menu bar

**Why you need it:**
When running lab exercises, you'll know if your Mac is struggling or if the slowness is in the VMs.

---

### Step 6.2: Set Up Spaces (Virtual Desktops)

**Create dedicated workspaces for different tasks:**

1. Open System Settings → Desktop & Dock
2. Scroll down to "Mission Control"
3. Check: "Displays have separate Spaces"
4. Press F3 (or swipe up with 3 fingers)
5. Move mouse to top-right → Click "+"

**Create these Spaces:**
- **Space 1: Monitoring** → Chrome with Wazuh dashboard
- **Space 2: Investigation** → Wireshark, iTerm, research tabs
- **Space 3: Documentation** → Obsidian, Notes, reports
- **Space 4: Personal** → Keep work separate

**Switch between spaces:** Ctrl + ← or Ctrl + →

---

## 🔐 Phase 7: Security Tools (30 minutes)

### Step 7.1: Install Security Research Tools

```bash
# SSL/TLS analysis
brew install openssl

# Password generation
brew install pwgen

# Hash generators
brew install md5sha1sum

# Base64 encoding/decoding (already installed but update)
brew install coreutils

# File type identification
brew install file

# Hex viewer
brew install hexyl

# DNS enumeration
brew install dnsmap

# Subdomain enumeration
brew install subfinder
```

---

### Step 7.2: Install Python & Security Libraries

**Install Python 3:**
```bash
brew install python3

# Verify
python3 --version
```

**Install useful Python libraries:**
```bash
# Python package manager
pip3 install --upgrade pip

# For working with APIs
pip3 install requests

# Beautiful output in terminal
pip3 install rich

# IP address manipulation
pip3 install ipaddress

# HTTP library
pip3 install httpx

# For parsing
pip3 install beautifulsoup4

# Excel/CSV handling
pip3 install pandas
```

---

### Step 7.3: Install Docker Desktop (For Running Tools)

**What is Docker?**
Lets you run security tools in containers without installing them directly.

**Install:**
```bash
brew install --cask docker
```

**After installation:**
1. Open Docker Desktop
2. Complete setup wizard
3. Leave it running in background

**Why you need it:**
Some security tools are easier to run in Docker containers. Later you might use:
- Security scanners
- CTF challenges
- Vulnerable web apps for testing

---

## 🎨 Phase 8: UI/UX Optimizations (15 minutes)

### Step 8.1: Set Up Clipboard Manager

**Why?** You'll copy lots of IPs, commands, logs - having history helps!

**Install Maccy:**
```bash
brew install --cask maccy
```

**Configure:**
- Launch Maccy
- Set hotkey: ⌘ + Shift + V
- Set history: 200 items

**Usage:** Press hotkey to see clipboard history!

---

### Step 8.2: Menu Bar Organization

**Install Bartender (or free alternative - Hidden Bar):**

```bash
# Free option
brew install --cask hiddenbar

# Or paid option (better)
brew install --cask bartender
```

**Why?** Your menu bar will get crowded with Stats, Docker, etc. This keeps it clean.

---

### Step 8.3: Window Management

**Install Rectangle (Free window snapping):**

```bash
brew install --cask rectangle
```

**Why?** Quickly organize windows:
- Left half: Terminal
- Right half: Browser
- Quarters: Multiple windows

**Shortcuts:**
- ⌃ + ⌥ + ← = Snap left
- ⌃ + ⌥ + → = Snap right
- ⌃ + ⌥ + F = Fullscreen

---

## 📚 Phase 9: Reference Materials (10 minutes)

### Step 9.1: Create Quick Reference Cheat Sheet

**Save this as a text file on your Desktop: `SOC-Quick-Reference.txt`**

```
=== SOC ANALYST QUICK REFERENCE ===

MY LAB ENVIRONMENT:
- Proxmox: https://172.22.1.22:8006
- Wazuh: https://[IP] (add when installed)
- Kali Linux: [IP]
- DVWA: [IP]

QUICK COMMANDS:
Network Info:
  ifconfig                    # Show network interfaces
  netstat -an | grep LISTEN   # Show listening ports
  lsof -i                     # Show network connections

DNS Lookups:
  dig example.com             # DNS query
  nslookup example.com        # Alternative DNS query
  host example.com            # Simple DNS lookup

Network Scanning:
  nmap -sn 172.22.1.0/24      # Ping scan network
  nmap -sV [IP]               # Service version scan
  nmap -p- [IP]               # All ports scan

SSH:
  ssh user@[IP]               # Connect to server
  ssh -i key.pem user@[IP]    # Connect with key
  scp file.txt user@[IP]:~/   # Copy file to server

INVESTIGATION:
Common Log Locations (when SSH'd into Linux):
  /var/log/auth.log           # Authentication logs
  /var/log/syslog             # System logs
  /var/log/apache2/access.log # Web server logs

Viewing Logs:
  tail -f /var/log/auth.log   # Watch logs live
  grep "failed" /var/log/auth.log # Search logs
  cat file.log | jq '.'       # Pretty print JSON logs

THREAT INTEL WEBSITES:
- VirusTotal: virustotal.com
- AbuseIPDB: abuseipdb.com
- Shodan: shodan.io
- AlienVault OTX: otx.alienvault.com

WAZUH QUICK TIPS:
- Security Events = Your alerts feed
- Agents = Connected monitored systems
- Use filters to find specific events
- Click alerts for full details

===================================
```

---

### Step 9.2: Create Browser Start Page

**Option 1: Use Chrome's "On startup" setting:**
1. Chrome Settings
2. On startup → Open specific pages
3. Add:
   - Your Wazuh dashboard URL
   - Proxmox URL
   - VirusTotal
   - MITRE ATT&CK

**Option 2: Create a local HTML file as start page:**

Create `~/SOC-Dashboard.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>SOC Dashboard</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #1a1a1a;
            color: #fff;
            padding: 40px;
        }
        h1 { color: #4a9eff; }
        .section {
            background: #2a2a2a;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
        }
        a {
            color: #4a9eff;
            text-decoration: none;
            display: block;
            padding: 8px 0;
        }
        a:hover { color: #6ab0ff; }
    </style>
</head>
<body>
    <h1>🛡️ SOC Analyst Dashboard</h1>
    
    <div class="section">
        <h2>My Lab</h2>
        <a href="https://172.22.1.22:8006">Proxmox Console</a>
        <a href="https://[WAZUH-IP]">Wazuh SIEM</a>
        <a href="http://[DVWA-IP]">DVWA Practice Target</a>
    </div>
    
    <div class="section">
        <h2>Threat Intelligence</h2>
        <a href="https://www.virustotal.com">VirusTotal</a>
        <a href="https://www.abuseipdb.com">AbuseIPDB</a>
        <a href="https://www.shodan.io">Shodan</a>
        <a href="https://otx.alienvault.com">AlienVault OTX</a>
    </div>
    
    <div class="section">
        <h2>Research</h2>
        <a href="https://attack.mitre.org">MITRE ATT&CK</a>
        <a href="https://cve.mitre.org">CVE Database</a>
        <a href="https://www.exploit-db.com">Exploit-DB</a>
    </div>
    
    <div class="section">
        <h2>Learning</h2>
        <a href="https://tryhackme.com">TryHackMe</a>
        <a href="https://www.hackthebox.com">HackTheBox</a>
    </div>
</body>
</html>
```

Then set Chrome to open this file on startup!

---

## ✅ Phase 10: Verification & Testing (15 minutes)

### Let's Make Sure Everything Works!

**Checklist:**

```bash
# Test Homebrew
brew --version

# Test terminal tools
nmap --version
jq --version
git --version

# Test Python
python3 --version
pip3 --version

# Test network commands
ifconfig
netstat -an | head

# Test SSH (should show usage)
ssh

# List installed apps
brew list --cask
```

**Test Wireshark:**
1. Open Wireshark
2. Double-click any interface
3. You should see packets scrolling
4. Stop capture (red square)

**Test Screenshots:**
- Press ⌘ + Shift + 4
- Select area
- Check Desktop for screenshot

---

## 🎯 Your Daily SOC Analyst Workflow

### Morning Routine:

**1. Open Your Workspace (5 minutes)**
```
Space 1: Browser with Wazuh dashboard
Space 2: iTerm (ready for investigation)
Space 3: Obsidian (daily note open)
Space 4: Keep for personal stuff
```

**2. Check Your Lab Status**
- Open Proxmox console
- Verify all VMs running
- Check Wazuh dashboard loads

**3. Create Today's Note**
- Open Obsidian
- New note from daily template
- Set today's goals

---

### During Investigation:

**When You Get an Alert in Wazuh:**

**Space 1 (Monitoring):**
1. See alert in Wazuh dashboard
2. Click for details
3. Note the source IP, timestamp, rule

**Space 2 (Investigation):**
1. Switch to iTerm
2. SSH to affected system
3. Run investigation commands:
   ```bash
   # Check recent logins
   last -20
   
   # Check failed logins
   grep "Failed" /var/log/auth.log | tail -20
   
   # Check network connections
   netstat -tulpn
   ```
4. If needed, open Wireshark to capture traffic

**Space 3 (Documentation):**
1. Switch to Obsidian
2. Create incident note from template
3. Document findings in real-time
4. Take screenshots as evidence

---

### Evening Routine:

**1. Review What You Learned (10 minutes)**
- Update daily note
- Document any new commands learned
- Save interesting findings

**2. Clean Up**
- Close unnecessary browser tabs (use OneTab)
- Save investigation notes
- Take VM snapshots if you made changes

**3. Plan Tomorrow**
- Write tomorrow's goals
- Note any unfinished investigations

---

## 📊 Keyboard Shortcuts Master List

### Critical Shortcuts for SOC Work:

**Browser (Chrome):**
```
⌘ + T         = New tab
⌘ + W         = Close tab
⌘ + Shift + T = Reopen closed tab
⌘ + F         = Find on page
⌘ + L         = Jump to address bar
⌘ + Option + → = Next tab
⌘ + Option + ← = Previous tab
```

**iTerm2:**
```
⌘ + T         = New tab
⌘ + D         = Split pane vertically
⌘ + Shift + D = Split pane horizontally
⌘ + [         = Previous pane
⌘ + ]         = Next pane
⌘ + F         = Search
⌘ + K         = Clear screen
```

**Window Management (Rectangle):**
```
⌃ + ⌥ + ←     = Left half
⌃ + ⌥ + →     = Right half
⌃ + ⌥ + ↑     = Top half
⌃ + ⌥ + ↓     = Bottom half
⌃ + ⌥ + F     = Fullscreen
```

**Screenshots:**
```
⌘ + Shift + 3 = Full screen
⌘ + Shift + 4 = Selection
⌘ + Shift + 5 = Screenshot tool
```

**System:**
```
⌘ + Space     = Spotlight (quick app launch)
⌘ + Tab       = Switch apps
⌃ + ←/→       = Switch Spaces
F3            = Mission Control (see all windows)
```

---

## 🔧 Advanced Configuration (Optional)

### For Power Users:

**Install Visual Studio Code (for editing configs/scripts):**
```bash
brew install --cask visual-studio-code
```

**Install Postman (for API testing):**
```bash
brew install --cask postman
```

**Install Burp Suite Community (web app testing):**
```bash
brew install --cask burp-suite
```

---

## 🎓 Learning Your Tools

### Week 1: Browser & Basics
- [ ] Learn browser extensions
- [ ] Set up bookmarks
- [ ] Practice screenshot workflow
- [ ] Get comfortable with Spaces

### Week 2: Terminal Mastery
- [ ] Practice SSH to lab VMs
- [ ] Learn basic commands
- [ ] Try aliases
- [ ] Get comfortable with iTerm

### Week 3: Investigation Tools
- [ ] Practice with Wireshark
- [ ] Use nmap for scans
- [ ] Try network analysis
- [ ] Document in Obsidian

### Week 4: Full Workflow
- [ ] Complete investigation start to finish
- [ ] Use all tools together
- [ ] Create professional report
- [ ] Review and optimize workflow

---

## 📝 Customization Ideas

### Make It Yours:

**Desktop Wallpaper Ideas:**
- Security-themed wallpaper
- Minimalist dark theme (helps with long sessions)
- Or set your lab network diagram as wallpaper!

**Menu Bar:**
- Keep it clean - only show what you need
- Clock (with seconds - good for timestamps)
- Stats (monitor resources)
- WiFi, Battery

**Dock:**
- Chrome (SOC profile)
- iTerm2
- Obsidian
- Wireshark
- Keep it minimal!

---

## ⚡ Pro Tips

### Efficiency Hacks:

**1. Create Text Snippets**
Use macOS Text Replacement (System Settings → Keyboard → Text Replacements):
- Type: `@wazuh` → Expands to: Your Wazuh URL
- Type: `@prox` → Expands to: Your Proxmox URL
- Type: `@sshdvwa` → Expands to: `ssh admin@[DVWA-IP]`

**2. Use Clipboard History**
- With Maccy, you never lose copied IPs, commands, etc.
- Press ⌘ + Shift + V to see history

**3. Tab Organization**
- Use OneTab to save "Investigation sets"
- Example: Save all tabs related to one incident
- Reopen later to continue investigation

**4. Terminal Profiles**
In iTerm2, create profiles for:
- "Lab Work" (connects to Proxmox)
- "Wazuh" (connects to SIEM)
- "Investigation" (your working terminal)

---

## 🎯 Real-World SOC Analyst Comparison

**Your Setup vs. Professional SOC:**

| Your Mac | Professional SOC Workstation |
|----------|---------------------------|
| MacBook Pro | Windows/Linux workstation |
| Chrome + extensions | Same browsers + extensions |
| Wazuh access | Splunk/QRadar/Sentinel access |
| iTerm2 | SecureCRT/PuTTY |
| Obsidian notes | Ticketing system (ServiceNow) |
| Wireshark | Same Wireshark |
| Python tools | Same Python tools |

**What's the same:** 80% of your tools and workflow!
**What's different:** Company specifics (SIEM brand, ticketing system)

---

## ✅ Final Setup Checklist

**Go through this list to make sure you're ready:**

### Browsers & Extensions:
- [ ] Chrome with SOC profile installed
- [ ] Security extensions installed
- [ ] Bookmarks organized
- [ ] Start page configured

### Terminal:
- [ ] iTerm2 installed
- [ ] Homebrew working
- [ ] All CLI tools installed
- [ ] Aliases configured
- [ ] SSH keys generated

### Analysis Tools:
- [ ] Wireshark installed and tested
- [ ] Network scanning tools ready
- [ ] Python and libraries installed

### Documentation:
- [ ] Obsidian or Notes set up
- [ ] Templates created
- [ ] Folder structure ready

### Productivity:
- [ ] Spaces configured
- [ ] Rectangle window management working
- [ ] Clipboard manager installed
- [ ] Menu bar organized

### Reference Materials:
- [ ] Quick reference file created
- [ ] Start page bookmarked
- [ ] Keyboard shortcuts learned

---

## 🚀 You're Ready!

Your MacBook Pro is now a professional-grade SOC analyst workstation!

**What You Have:**
✅ Professional browser setup for investigations
✅ Powerful terminal with security tools
✅ Network analysis capabilities
✅ Documentation system
✅ Efficient workflow with hotkeys
✅ All the tools a real SOC analyst uses

**Next Steps:**
1. Get your lab VMs running (follow simplified guide)
2. Add your lab IPs to bookmarks and notes
3. Start your first investigation
4. Use these tools to become confident!

---

## 🆘 Troubleshooting

**Homebrew issues:**
```bash
# Fix permissions
sudo chown -R $(whoami) /usr/local/Homebrew

# Update Homebrew
brew update

# Check for problems
brew doctor
```

**iTerm2 not opening:**
- System Settings → Privacy & Security → Allow iTerm2

**Can't SSH to lab VMs:**
- Check VM is running in Proxmox
- Verify IP address: `ping [VM-IP]`
- Check SSH is installed on VM

**Wireshark no interfaces:**
- Reinstall with: `brew reinstall --cask wireshark`
- Run: `sudo dseditgroup -o edit -a $(whoami) -t user access_bpf`

---

## 📚 Keep Learning

**Master Your Tools:**
- YouTube: "Wireshark tutorial"
- YouTube: "Terminal tips for beginners"
- Practice daily with your lab!

**Remember:** Every professional SOC analyst started where you are. The tools on your Mac right now are THE SAME tools they use every day!

---

**Now go build your lab and start investigating! 🕵️‍♂️**

*Your MacBook Pro is ready to be your security operations command center!*
