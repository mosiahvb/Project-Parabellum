# 🏰 Your Cybersecurity Home Lab: From Zero to Security Engineer

## 📋 Table of Contents
1. [Welcome to Your Security Journey](#welcome)
2. [The Big Picture: What We're Building](#big-picture)
3. [Your Hardware: The Foundation](#hardware)
4. [Understanding the Pieces (Like Lego Instructions)](#understanding-pieces)
5. [Phase 1: Building the Foundation](#phase-1)
6. [Phase 2: Adding Security Monitoring](#phase-2)
7. [Phase 3: Creating Attack & Defense Labs](#phase-3)
8. [Phase 4: Enterprise Simulation](#phase-4)
9. [Real-World Job Tasks You'll Practice](#job-tasks)
10. [Your Learning Roadmap](#roadmap)
11. [Troubleshooting & Maintenance](#troubleshooting)

---

## 🎯 Welcome to Your Security Journey {#welcome}

Hey! I'm excited you're building this home lab. This isn't just about playing with computers - you're building **real experience** that will make you confident as a security engineer.

### What This Lab Will Do For You
- **Build Confidence**: Practice solving real security problems without fear of breaking anything
- **Gain Experience**: Simulate actual security department tasks
- **Prepare for Your Job**: Learn how to set up security from scratch at your workplace
- **Portfolio Material**: Show potential employers or your boss what you can do

### How to Use This Guide
Think of this like building with Legos:
1. **Step 1**: We'll show you each piece and what it does
2. **Step 2**: We'll show you how pieces connect together
3. **Step 3**: We'll build section by section
4. **Step 4**: Test everything works

**Important**: Don't rush! Build one section, test it, understand it, then move to the next.

---

## 🏗️ The Big Picture: What We're Building {#big-picture}

### The Blueprint (Imagine This Like a Lego Box Picture)

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR PROXMOX SERVER                          │
│  (The Big Lego Baseplate Everything Sits On)                   │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │         🌐 INTERNET CONNECTION                           │  │
│  │                     ↓                                    │  │
│  │    ┌────────────────────────────────┐                  │  │
│  │    │   🛡️ pfSense Firewall         │  ← Your Router   │  │
│  │    │   (The Security Gate)          │                  │  │
│  │    └────────────┬───────────────────┘                  │  │
│  │                 │                                       │  │
│  │    ┌────────────┴───────────────┐                     │  │
│  │    │                             │                     │  │
│  ├────▼────────────────┬───────────▼─────────────────────┤  │
│  │                     │                                   │  │
│  │  🔒 SECURE ZONE    │    ⚠️ PRACTICE ZONE              │  │
│  │  (Blue Team)       │    (Red Team)                     │  │
│  │  ─────────────     │    ─────────────                  │  │
│  │                     │                                   │  │
│  │  📊 Wazuh SIEM     │    🎯 Kali Linux                 │  │
│  │  (Security Brain)   │    (Attack Tools)                │  │
│  │                     │                                   │  │
│  │  📡 Suricata IDS   │    🕷️ Metasploitable            │  │
│  │  (Network Guard)    │    (Vulnerable Target)           │  │
│  │                     │                                   │  │
│  │  💼 Windows AD     │    🌐 DVWA                       │  │
│  │  (Business Network) │    (Web Vulnerabilities)         │  │
│  │                     │                                   │  │
│  │  🖥️ Windows PCs    │    🧪 CTF Boxes                  │  │
│  │  (Employees)        │    (Practice Challenges)         │  │
│  │                     │                                   │  │
│  └─────────────────────┴───────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### What Each Part Does (Like Lego Instruction Descriptions)

**🛡️ pfSense Firewall** - Think of this as the security guard at your building's entrance. It controls who can go where.

**📊 Wazuh SIEM** - This is like security cameras + a smart computer that watches everything and alerts you when something suspicious happens.

**📡 Suricata IDS** - Like a metal detector at the airport - it scans all network traffic for dangerous patterns.

**💼 Windows Active Directory** - This simulates a real company network where employees log in and access files.

**🎯 Kali Linux** - Your "hacker toolkit" - but used for good! This is where you'll practice finding vulnerabilities.

**🕷️ Metasploitable & DVWA** - Intentionally vulnerable computers where you can practice attacking (legally and safely).

---

## 💪 Your Hardware: The Foundation {#hardware}

### What You Have (This Is AWESOME!)

| Component | Your Specs | What This Means |
|-----------|-----------|-----------------|
| **CPU** | Intel Xeon E5-2670 (16 cores) | You can run 10-15 virtual machines at once! |
| **RAM** | 64GB | Plenty of memory for all your labs |
| **Storage** | 2x NVMe SSDs + 2x SATA | Super fast drives for your VMs |
| **Network** | IP: 172.22.1.22 | Already connected to your home network |

**Translation**: Your hardware is more than enough. Most professionals would be jealous of this setup!

---

## 🧩 Understanding the Pieces (Like Lego Instructions) {#understanding-pieces}

Before we build, let's understand what each piece does in **real-world terms**.

### 1. Virtual Machines (VMs) - The Lego Bricks

**What is it?** 
A VM is like having a complete computer inside your computer. You can turn it on, turn it off, break it, and start fresh - all without affecting your actual computer.

**Real-World Example**:
Imagine you have a sandbox in your backyard. You can build sandcastles, knock them down, and rebuild without affecting your actual house. VMs are the same - safe places to experiment.

**Why Security Engineers Need This**:
- Test security tools without risking real systems
- Practice incident response
- Simulate attacks safely
- Reset everything after each practice session

---

### 2. Networks - The Lego Baseplates

**What is it?**
Networks are how computers talk to each other. In your lab, we'll create separate networks (like separate Lego baseplates) so different activities stay isolated.

**Real-World Example**:
Think of your home with different rooms:
- **Living Room** (Secure Zone): Where you do normal, safe activities
- **Workshop** (Practice Zone): Where you do messy work and experiments
- **Front Door** (Firewall): Controls who comes in and which room they can access

**Network Layout We'll Create**:

```
Home Network (172.22.1.0/24)
    ↓
[pfSense Firewall]
    ├─→ Management Network (10.0.0.0/24)    - For accessing your SIEM/monitoring
    ├─→ Secure Network (10.0.10.0/24)        - Simulates your company network
    └─→ Attack Range (10.0.50.0/24)          - Where vulnerable targets live
```

---

### 3. Firewall (pfSense) - The Security Guard

**What is it?**
A firewall controls what traffic is allowed between networks. It's like a security guard who checks IDs and decides who can go where.

**Real-World Job Task**:
In a real company, you'll configure firewalls to:
- Block dangerous websites
- Prevent hackers from accessing internal systems
- Allow employees to access what they need
- Log who's accessing what for security audits

**What You'll Learn**:
- Creating firewall rules
- Network segmentation
- VPN setup for remote access
- Traffic monitoring and logging

---

### 4. SIEM (Wazuh) - The Security Brain

**What is it?**
SIEM stands for "Security Information and Event Management." It's a system that collects logs from all your computers and networks, analyzes them, and alerts you when something suspicious happens.

**Real-World Example**:
Imagine you have cameras throughout your house (computers/servers), and a security system that:
1. Records everything from all cameras
2. Knows what "normal" looks like
3. Alerts you if something unusual happens (like a door opening at 3 AM)
4. Keeps records for investigation

**Real-World Job Task**:
Security engineers spend a lot of time:
- Setting up log collection
- Creating alert rules
- Investigating alerts (Is this a real threat or false alarm?)
- Creating security dashboards for management
- Responding to incidents

---

### 5. IDS/IPS (Suricata) - The Network Guard

**What is it?**
IDS = Intrusion Detection System. It monitors network traffic and looks for signs of attacks.
IPS = Intrusion Prevention System. Same thing, but can also block attacks automatically.

**Real-World Example**:
This is like having a smart security system that:
- Watches all the traffic going in and out
- Recognizes attack patterns (like someone trying passwords repeatedly)
- Alerts you to suspicious behavior
- Can automatically block the attacker

**What You'll Learn**:
- Network traffic analysis
- Creating detection rules
- Identifying attack patterns
- Tuning alerts to reduce false positives

---

### 6. Active Directory - The Business Network

**What is it?**
Active Directory (AD) is how Windows manages users, computers, and permissions in a company.

**Real-World Example**:
Think of a company building:
- **Employees** have ID badges with different access levels
- **IT Department** can enter server rooms
- **HR** can access employee records
- **Regular Employees** can only access their workstations

Active Directory is the system that controls all of this.

**Real-World Job Task**:
Security engineers need to:
- Understand how AD works (it's in 90% of companies)
- Secure AD from attacks
- Monitor for suspicious logins
- Detect when an account is compromised
- Implement security policies

---

### 7. Vulnerable Targets - The Practice Dummies

**What is it?**
These are intentionally insecure systems built for practice. It's like having crash test dummies - they're meant to be "attacked" safely.

**Types We'll Use**:
- **Metasploitable**: A Linux system full of vulnerabilities
- **DVWA**: A web application with common security flaws
- **Juice Shop**: A modern vulnerable web app
- **Vulnerable Windows machines**: For practicing Windows attacks

**Why This Matters**:
You can't legally practice hacking on real systems. These give you a safe, legal way to:
- Learn how attacks work
- Practice using security tools
- Understand vulnerabilities
- Test your defensive measures

---

## 🏗️ Phase 1: Building the Foundation {#phase-1}

### Step 1.1: Set Up Network Bridges in Proxmox

**What We're Doing**: Creating separate "roads" for different types of traffic.

**Think of it like**: Building separate Lego baseplates before adding buildings.

#### Instructions (Follow Each Step):

1. **Log into Proxmox**
   - Open your web browser
   - Go to: `https://172.22.1.22:8006`
   - Login with your credentials

2. **Create Management Bridge (vmbr1)**
   ```
   Click: Your server name → System → Network → Create → Linux Bridge
   
   Settings:
   - Name: vmbr1
   - IPv4/CIDR: 10.0.0.1/24
   - Comment: "Management Network - For monitoring tools"
   - Click: Create
   ```
   
   **What this does**: Creates a network for your security monitoring tools.

3. **Create Secure Network Bridge (vmbr2)**
   ```
   Click: Create → Linux Bridge
   
   Settings:
   - Name: vmbr2
   - IPv4/CIDR: 10.0.10.1/24
   - Comment: "Secure Zone - Company network simulation"
   - Click: Create
   ```
   
   **What this does**: Creates a network that simulates your company's internal network.

4. **Create Attack Range Bridge (vmbr3)**
   ```
   Click: Create → Linux Bridge
   
   Settings:
   - Name: vmbr3
   - IPv4/CIDR: 10.0.50.1/24
   - Comment: "Attack Range - Vulnerable targets"
   - Click: Create
   ```
   
   **What this does**: Creates an isolated network for vulnerable machines you'll practice on.

**✅ Checkpoint**: You should now see 4 network bridges:
- vmbr0 (your existing home network connection)
- vmbr1 (Management Network)
- vmbr2 (Secure Zone)
- vmbr3 (Attack Range)

---

### Step 1.2: Install pfSense Firewall

**What We're Doing**: Installing the "security guard" that controls traffic between networks.

#### Instructions:

1. **Download pfSense**
   - In Proxmox, click: local (your-server) → ISO Images → Download from URL
   - URL: Go to pfSense website and get the latest CE ISO URL
   - Wait for download to complete

2. **Create pfSense VM**
   ```
   Click: Create VM (top right)
   
   Settings:
   - VM ID: 100 (easy to remember - this is your firewall)
   - Name: pfsense-firewall
   - ISO: Select the pfSense ISO you downloaded
   ```

3. **Configure Hardware**
   ```
   System Tab:
   - Leave defaults
   
   Disk Tab:
   - Storage: Select your fast NVMe drive
   - Disk size: 32GB (plenty for a firewall)
   
   CPU Tab:
   - Cores: 2 (firewalls need a bit of processing power)
   
   Memory Tab:
   - RAM: 2048MB (2GB is enough)
   
   Network Tab:
   - Bridge: vmbr0 (WAN - connects to internet)
   - Model: VirtIO (faster)
   ```

4. **Add Additional Network Interfaces**
   ```
   After creating the VM:
   - Click: Hardware → Add → Network Device
   - Bridge: vmbr1 (Management)
   - Click: Add
   
   Repeat for:
   - vmbr2 (Secure Zone)
   - vmbr3 (Attack Range)
   ```

5. **Install pfSense**
   ```
   - Start the VM
   - Click: Console
   - Follow installation wizard:
     * Accept defaults
     * Choose "Quick/Easy Install"
     * Wait for installation (5-10 minutes)
     * When done, choose "Reboot"
   ```

6. **Basic Configuration**
   ```
   After reboot, pfSense will ask questions:
   
   Should VLANs be set up? → n (we're using bridges instead)
   
   WAN interface: vtnet0 (this should be auto-detected)
   LAN interface: vtnet1 (this should be auto-detected)
   
   Enter to proceed
   ```

7. **Access Web Interface**
   ```
   - pfSense will display its LAN IP (should be 10.0.0.1)
   - From your computer, open browser
   - Go to: https://10.0.0.1
   - Username: admin
   - Password: pfsense
   - Complete the setup wizard
   ```

**✅ Checkpoint**: 
- You can access pfSense web interface
- You see a dashboard with interface status
- All network interfaces show as "up"

**Real-World Connection**: In a real company, this is exactly how you'd set up a firewall to segment different network zones (like separating employee network from server network).

---

### Step 1.3: Configure pfSense Network Rules

**What We're Doing**: Creating rules that control traffic flow between your networks.

**Think of it like**: Programming the security guard's instructions for who can go where.

#### Basic Firewall Rules:

1. **Management Network Rules (vmbr1)**
   ```
   Go to: Firewall → Rules → LAN (or Management interface)
   
   Click: Add (with up arrow)
   
   Rule 1: Allow SIEM to collect logs from all networks
   - Action: Pass
   - Interface: Management
   - Protocol: Any
   - Source: Management net
   - Destination: Any
   - Description: "Allow SIEM to collect logs"
   - Click: Save
   ```

2. **Secure Zone Rules (vmbr2)**
   ```
   Rule 1: Allow internal communication
   - Action: Pass
   - Interface: Secure Zone
   - Protocol: Any
   - Source: Secure Zone net
   - Destination: Secure Zone net
   - Description: "Allow internal company communication"
   
   Rule 2: Block access to Attack Range
   - Action: Block
   - Interface: Secure Zone
   - Protocol: Any
   - Source: Secure Zone net
   - Destination: Attack Range net
   - Description: "Prevent company network from accessing vulnerable systems"
   ```

3. **Attack Range Rules (vmbr3)**
   ```
   Rule 1: Isolate from everything except monitoring
   - Action: Block
   - Protocol: Any
   - Source: Attack Range net
   - Destination: Any
   - Description: "Isolate vulnerable systems"
   ```

**✅ Checkpoint**: Your networks are now properly segmented. Secure zone can't accidentally connect to vulnerable targets.

---

## 🔍 Phase 2: Adding Security Monitoring {#phase-2}

### Step 2.1: Install Wazuh SIEM

**What We're Doing**: Setting up your "security brain" that will monitor everything.

**Real-World Context**: In a real security operations center (SOC), the SIEM is the most important tool. It's always running, collecting logs, and alerting on threats.

#### Instructions:

1. **Create Ubuntu VM for Wazuh**
   ```
   Click: Create VM
   
   Settings:
   - VM ID: 200
   - Name: wazuh-siem
   - ISO: Ubuntu Server 22.04 LTS (download if needed)
   
   Hardware:
   - Disk: 100GB (logs take space)
   - CPU: 4 cores (SIEM needs processing power)
   - RAM: 8192MB (8GB - this is important!)
   - Network: vmbr1 (Management network)
   ```

2. **Install Ubuntu**
   ```
   - Start VM and open console
   - Follow Ubuntu installation:
     * Choose English
     * Update to new installer: Yes
     * Keyboard: Your layout
     * Network: Use DHCP (it'll get 10.0.0.x address)
     * Proxy: Leave blank
     * Mirror: Default
     * Storage: Use entire disk
     * Profile:
       - Name: admin
       - Server name: wazuh-siem
       - Username: admin
       - Password: (choose strong password)
     * Install OpenSSH: Yes
     * Featured snaps: None
   - Wait for installation (10-15 minutes)
   - Reboot when prompted
   ```

3. **Install Wazuh**
   ```
   Log in and run these commands:
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Download Wazuh installation script
   curl -sO https://packages.wazuh.com/4.9/wazuh-install.sh
   
   # Run all-in-one installation
   sudo bash ./wazuh-install.sh -a
   
   # This will take 15-20 minutes
   # At the end, save the password it shows you!
   ```

4. **Access Wazuh Dashboard**
   ```
   - In your browser, go to: https://10.0.0.x (your VM's IP)
   - Username: admin
   - Password: (the one from installation output)
   - You'll see the Wazuh dashboard!
   ```

**✅ Checkpoint**: 
- Wazuh dashboard is accessible
- You see a clean dashboard with no agents yet
- Main dashboard shows "0 agents connected"

---

### Step 2.2: Install Suricata IDS

**What We're Doing**: Setting up network monitoring to detect attacks.

#### Instructions:

1. **Create Suricata VM**
   ```
   Create VM:
   - VM ID: 201
   - Name: suricata-ids
   - ISO: Ubuntu Server 22.04
   - Disk: 50GB
   - CPU: 2 cores
   - RAM: 4096MB (4GB)
   - Network 1: vmbr1 (Management)
   - Network 2: vmbr2 (Monitor secure zone)
   - Network 3: vmbr3 (Monitor attack range)
   ```

2. **Install Ubuntu** (same process as before)

3. **Install Suricata**
   ```
   sudo apt update
   sudo apt install suricata -y
   sudo apt install jq -y  # Helpful tool for logs
   ```

4. **Configure Suricata**
   ```
   sudo nano /etc/suricata/suricata.yaml
   
   Find "HOME_NET" and change to:
   HOME_NET: "[10.0.0.0/24,10.0.10.0/24,10.0.50.0/24]"
   
   Find "EXTERNAL_NET" and change to:
   EXTERNAL_NET: "!$HOME_NET"
   
   Save and exit (Ctrl+X, Y, Enter)
   ```

5. **Start Suricata**
   ```
   sudo systemctl enable suricata
   sudo systemctl start suricata
   sudo systemctl status suricata
   ```

6. **Install Wazuh Agent on Suricata**
   ```
   # This connects Suricata to your SIEM
   # Download agent package
   wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.9.0-1_amd64.deb
   
   # Install agent
   sudo WAZUH_MANAGER="10.0.0.x" WAZUH_AGENT_NAME="suricata-ids" dpkg -i wazuh-agent_4.9.0-1_amd64.deb
   
   # Start agent
   sudo systemctl daemon-reload
   sudo systemctl enable wazuh-agent
   sudo systemctl start wazuh-agent
   ```

**✅ Checkpoint**:
- Go to Wazuh dashboard
- Click: Agents
- You should see "suricata-ids" as connected!

---

### Step 2.3: Understanding SIEM Alerts (The Fun Part!)

**What We're Doing**: Learning to read and respond to security alerts.

**Real-World Context**: This is 50% of a security engineer's job - investigating alerts and deciding what's a real threat.

#### Setting Up Your First Alert:

1. **Create a Test Rule in Wazuh**
   ```
   In Wazuh Dashboard:
   - Click: Management → Rules
   - Click: Manage rule files
   - Click: Custom rules
   - Add this rule:
   
   <group name="custom,">
     <rule id="100100" level="10">
       <if_sid>5710</if_sid>
       <description>Test Alert: Multiple Failed SSH Login Attempts</description>
     </rule>
   </group>
   ```

2. **Trigger the Alert** (This is practice!)
   ```
   From another machine, try to SSH to Suricata with wrong password 3 times
   
   ssh fakeuser@10.0.0.x
   (enter wrong password)
   (try 3 times)
   ```

3. **Investigate in SIEM**
   ```
   In Wazuh Dashboard:
   - Click: Security Events
   - You should see alerts for "Multiple Failed SSH Attempts"
   - Click on an alert to see details
   ```

**🎓 Learning Moment**: 
This is exactly what you'll do in a real SOC! You'll:
1. See an alert
2. Investigate the details (who, what, when, where)
3. Decide if it's a real threat or false alarm
4. Take action (block IP, investigate further, etc.)

---

## ⚔️ Phase 3: Creating Attack & Defense Labs {#phase-3}

### Step 3.1: Install Kali Linux (Your Attack Platform)

**What We're Doing**: Setting up your ethical hacking toolkit.

**Real-World Context**: Security engineers use these same tools to test their company's security.

#### Instructions:

1. **Download Kali Linux**
   ```
   In Proxmox:
   - Go to: local → ISO Images
   - Download from URL: https://cdimage.kali.org/kali-2024.3/kali-linux-2024.3-installer-amd64.iso
   ```

2. **Create Kali VM**
   ```
   Create VM:
   - VM ID: 300
   - Name: kali-attack
   - ISO: Kali Linux ISO
   - Disk: 80GB (tools need space)
   - CPU: 4 cores
   - RAM: 4096MB (4GB)
   - Network: vmbr3 (Attack Range)
   ```

3. **Install Kali**
   ```
   - Graphical Install
   - Language: English
   - Location: Your country
   - Keyboard: Your layout
   - Hostname: kali-attack
   - Domain: (leave blank)
   - Full name: Your name
   - Username: kali
   - Password: (choose strong one)
   - Partition: Guided - use entire disk
   - Install GRUB: Yes
   - Wait for installation (15 minutes)
   - Reboot
   ```

4. **Update Kali**
   ```
   After login:
   Open terminal and run:
   
   sudo apt update
   sudo apt full-upgrade -y
   sudo apt autoremove -y
   ```

**✅ Checkpoint**: You can log into Kali and see the desktop environment with all the hacking tools.

---

### Step 3.2: Set Up Vulnerable Targets

**What We're Doing**: Creating safe targets to practice on.

#### Option A: Metasploitable 3 (Linux Target)

1. **Download**
   ```
   - Search for "Metasploitable 3" 
   - Download the OVA file
   - Upload to Proxmox storage
   ```

2. **Import to Proxmox**
   ```
   Using command line on Proxmox:
   qm importovf 301 /path/to/metasploitable.ova local-lvm
   
   Then:
   - VM ID: 301
   - Name: metasploitable
   - Network: vmbr3 (Attack Range)
   - RAM: 2048MB
   - Start VM
   ```

#### Option B: DVWA (Web Application Target)

1. **Create Ubuntu VM**
   ```
   Create VM:
   - VM ID: 302
   - Name: dvwa-webapp
   - ISO: Ubuntu Server 22.04
   - Disk: 20GB
   - CPU: 2 cores
   - RAM: 2048MB
   - Network: vmbr3
   ```

2. **Install DVWA Using Docker**
   ```
   sudo apt update
   sudo apt install docker.io -y
   sudo systemctl start docker
   sudo systemctl enable docker
   
   # Run DVWA
   sudo docker run --rm -it -p 80:80 vulnerables/web-dvwa
   
   # Access in browser: http://[VM IP]
   # Default login: admin/password
   ```

#### Option C: OWASP Juice Shop (Modern Web App)

```
Create LXC Container in Proxmox:
- ID: 303
- Template: Ubuntu 22.04
- Name: juice-shop
- Disk: 8GB
- CPU: 1 core
- RAM: 1024MB
- Network: vmbr3

Then install:
sudo apt update
sudo apt install docker.io -y
sudo docker run -d -p 3000:3000 bkimminich/juice-shop
```

**✅ Checkpoint**: 
- You have at least 2 vulnerable targets
- You can access them from Kali Linux
- They are isolated in Attack Range (can't reach your secure network)

---

### Step 3.3: Your First Attack & Detection Exercise

**What We're Doing**: Practicing the complete cycle - Attack → Detect → Respond

**Real-World Context**: This is exactly what penetration testers and security analysts do!

#### Exercise 1: Port Scanning & Detection

**Part A: Perform the Attack (Red Team)**

1. **From Kali Linux**
   ```
   # Open terminal
   # Find your targets
   nmap -sn 10.0.50.0/24
   
   # This shows all devices on the Attack Range
   # You should see: Metasploitable, DVWA, Juice Shop
   ```

2. **Detailed Scan**
   ```
   # Pick a target (e.g., Metasploitable at 10.0.50.101)
   nmap -sV -sC 10.0.50.101
   
   # -sV = Find versions of services
   # -sC = Run default scripts
   
   # This will take 2-3 minutes
   # You'll see open ports, services, versions
   ```

3. **Document Your Findings**
   ```
   Create a file: scan-results.txt
   Write down:
   - What ports are open?
   - What services are running?
   - What versions do you see?
   - Any obvious vulnerabilities?
   ```

**Part B: Detect the Attack (Blue Team)**

1. **Check Suricata Alerts**
   ```
   On Suricata VM:
   sudo tail -f /var/log/suricata/fast.log
   
   You should see alerts about port scanning!
   ```

2. **Check Wazuh Dashboard**
   ```
   Go to: Wazuh Dashboard → Security Events
   Filter by: "suricata"
   
   You should see alerts for:
   - Port scan detected
   - Multiple connection attempts
   - Suspicious network activity
   ```

3. **Investigate the Alert**
   ```
   Click on an alert
   You'll see:
   - Source IP: 10.0.50.x (your Kali machine)
   - Destination IP: 10.0.50.101 (target)
   - Rule that triggered
   - Severity level
   - Timestamp
   ```

**Part C: Respond (Security Engineer)**

This is where you decide:
- **Is this a threat?** In this case, you know it's you practicing, but in real life, you'd investigate
- **Should we block it?** You could create a firewall rule to block that IP
- **What's the pattern?** Multiple targets? Just one port? Helps identify the threat

**🎓 What You Just Learned**:
- How to use Nmap (industry standard tool)
- How IDS detects suspicious activity
- How SIEM correlates and displays alerts
- How to investigate security events
- The attacker vs. defender perspective

---

#### Exercise 2: SQL Injection Attack & Detection

**Part A: Perform the Attack**

1. **Access DVWA**
   ```
   From Kali, open Firefox
   Go to: http://10.0.50.102
   Login: admin / password
   
   Click: DVWA Security → Set to "Low"
   Click: SQL Injection
   ```

2. **Try a Simple Injection**
   ```
   In the User ID field, enter:
   ' or '1'='1
   
   Click Submit
   
   What happened? 
   - You should see all users in the database!
   - This is because the query becomes:
     SELECT * FROM users WHERE user_id = '' or '1'='1'
   - Since 1=1 is always true, it shows everything!
   ```

3. **Try More Advanced Injection**
   ```
   ' or 1=1 UNION SELECT null, table_name FROM information_schema.tables #
   
   This reveals database table names!
   ```

**Part B: Detect and Respond**

1. **Check Web Server Logs**
   ```
   On DVWA server:
   sudo docker logs [container-name]
   
   You'll see the malicious queries!
   ```

2. **Check Wazuh**
   ```
   Wazuh should detect:
   - Unusual SQL patterns
   - Multiple failed attempts
   - Suspicious characters in web requests
   ```

3. **Fix the Vulnerability**
   ```
   In DVWA:
   - Change security level to "Medium" or "High"
   - Try your attacks again
   - See how proper input validation stops the attack!
   ```

**🎓 What You Learned**:
- How SQL Injection works
- Why input validation is critical
- How web application firewalls help
- The importance of logging
- Defense in depth (multiple security layers)

---

## 🏢 Phase 4: Enterprise Simulation {#phase-4}

### Step 4.1: Set Up Windows Active Directory

**What We're Doing**: Creating a realistic company network.

**Real-World Context**: 90% of companies use Active Directory. Understanding it is crucial for security engineers.

#### The Setup:

```
You'll create:
- 1 Domain Controller (the "boss" of the network)
- 2-3 Windows 10 workstations (employees)
- File shares (like company drives)
- Security policies
```

#### Step-by-Step:

1. **Download Windows Server**
   ```
   - Get Windows Server 2022 Evaluation ISO
   - Available from Microsoft for free (180 day trial)
   - Upload to Proxmox storage
   ```

2. **Create Domain Controller VM**
   ```
   Create VM:
   - VM ID: 400
   - Name: dc01-contoso
   - ISO: Windows Server 2022
   - Disk: 60GB
   - CPU: 2 cores
   - RAM: 4096MB (4GB minimum for Windows)
   - Network: vmbr2 (Secure Zone)
   - OS Type: Windows
   ```

3. **Install Windows Server**
   ```
   - Boot VM
   - Choose: Windows Server 2022 Standard (Desktop Experience)
   - Custom installation
   - Accept license
   - Set Administrator password (strong!)
   - Wait for installation (15 minutes)
   ```

4. **Configure Domain Controller**
   ```
   After Windows starts:
   
   Step 1: Set Static IP
   - Open: Settings → Network → Change adapter
   - Right-click → Properties
   - IPv4 Properties:
     * IP: 10.0.10.10
     * Subnet: 255.255.255.0
     * Gateway: 10.0.10.1
     * DNS: 10.0.10.10 (itself)
   
   Step 2: Install AD Role
   - Open: Server Manager
   - Click: Add roles and features
   - Next → Next → Next
   - Select: Active Directory Domain Services
   - Add Features
   - Next → Next → Install
   - Wait for installation (10 minutes)
   
   Step 3: Promote to Domain Controller
   - After installation, click flag icon → "Promote this server to a domain controller"
   - Add a new forest
   - Root domain name: contoso.local
   - Forest functional level: Windows Server 2016 or higher
   - Domain Controller capabilities: Both DNS and GC
   - DSRM Password: (choose strong one)
   - Next through rest
   - Install
   - Server will reboot
   ```

**✅ Checkpoint**: After reboot, you can log in as CONTOSO\Administrator

---

5. **Create Users and Groups**

**Real-World Context**: This simulates your company's employee structure.

```
In Active Directory Users and Computers:

1. Create Organizational Units (like departments)
   Right-click domain → New → Organizational Unit
   Create:
   - IT Department
   - Security Team
   - Finance
   - HR
   - Regular Users

2. Create User Accounts
   Right-click OU → New → User
   
   Create these users:
   - john.doe (IT Administrator)
   - jane.smith (Security Analyst)
   - bob.johnson (Regular User)
   - alice.williams (HR Manager)
   
3. Create Security Groups
   Right-click OU → New → Group
   Create:
   - IT-Admins (give admin rights)
   - Security-Team
   - File-Share-Access
```

---

6. **Create Windows 10 Workstations**

**What We're Doing**: Adding employee computers to the domain.

```
Create 2 Windows 10 VMs:

VM 1:
- ID: 410
- Name: ws01-user
- ISO: Windows 10 ISO
- Disk: 60GB
- CPU: 2 cores
- RAM: 4096MB
- Network: vmbr2

VM 2:
- ID: 411
- Name: ws02-user
- Same specs as above
```

**Join to Domain**:
```
After installing Windows 10:
1. Set DNS to 10.0.10.10 (your DC)
2. Right-click This PC → Properties
3. Change settings → Change
4. Domain: contoso.local
5. Enter Administrator credentials
6. Reboot
7. Log in as domain user (john.doe@contoso.local)
```

**✅ Checkpoint**: 
- Users can log into workstations with domain accounts
- You see computers in Active Directory
- File shares are accessible

---

### Step 4.2: Security Monitoring for AD

**What We're Doing**: Monitoring your "company network" for threats.

#### Installing Wazuh Agents on Windows:

1. **On Domain Controller**
   ```
   From Wazuh Dashboard:
   - Click: Agents → Deploy new agent
   - Operating System: Windows
   - Server Address: 10.0.0.200 (your Wazuh server)
   - Agent Name: dc01-contoso
   - Copy the PowerShell command shown
   
   On DC01:
   - Open PowerShell as Administrator
   - Paste and run the command
   - Wait for installation
   ```

2. **On Each Workstation** (repeat above process)

3. **Configure Windows Event Log Collection**
   ```
   On each Windows machine:
   Edit: C:\Program Files (x86)\ossec-agent\ossec.conf
   
   Add after <ossec_config>:
   <localfile>
     <location>Security</location>
     <log_format>eventchannel</log_format>
   </localfile>
   <localfile>
     <location>System</location>
     <log_format>eventchannel</log_format>
   </localfile>
   
   Restart Wazuh agent service
   ```

**✅ Checkpoint**: 
- All Windows machines show "Active" in Wazuh
- You see Windows events in Security Events dashboard

---

### Step 4.3: Simulate Real Security Scenarios

#### Scenario 1: Brute Force Attack Detection

**The Attack**:
```
From Kali (you'll need to allow this temporarily):
hydra -l john.doe -P /usr/share/wordlists/rockyou.txt rdp://10.0.10.11

This tries many passwords on Remote Desktop
```

**The Detection**:
```
In Wazuh:
- Alert: "Multiple failed login attempts"
- Alert: "Windows Security Event ID 4625" (failed login)
- Alert: "Possible brute force attack"
```

**Your Response** (as Security Engineer):
```
1. Investigate the alert
2. Identify the source IP (Kali machine)
3. Check: Is this a real attack?
4. Action: Block the IP in pfSense
5. Create rule: "If >5 failed logins in 1 minute → block IP for 1 hour"
```

---

#### Scenario 2: Lateral Movement Detection

**The Attack**:
```
Simulate an attacker who compromised one user, trying to access other systems

From WS01 (as compromised user):
- Try to access admin shares on DC01
- Try to enumerate other users
- Try to access restricted folders
```

**The Detection**:
```
Wazuh Alerts:
- "User accessed privileged share from unauthorized system"
- "Account enumeration detected"
- "Privilege escalation attempt"
```

**Your Response**:
```
1. Isolate the compromised workstation
2. Reset user password
3. Check what data was accessed
4. Investigate how compromise happened
5. Strengthen security policies
```

---

#### Scenario 3: Malicious File Detection

**The Attack**:
```
Download a test malware file (EICAR test file - safe for testing):
From any Windows machine:
Invoke-WebRequest -Uri "https://secure.eicar.org/eicar.com" -OutFile "C:\temp\test.exe"
```

**The Detection**:
```
Wazuh Alerts:
- "File integrity monitoring alert"
- "Suspicious file downloaded"
- "Windows Defender alert" (if enabled)
```

**Your Response**:
```
1. Quarantine the file
2. Scan the system
3. Check: Where did it come from?
4. Block the download source
5. Alert the user
```

---

## 💼 Real-World Job Tasks You'll Practice {#job-tasks}

Let's map what you're doing in your lab to actual security engineer responsibilities:

### 1. Security Monitoring & Analysis

**In Your Lab**:
- Monitor Wazuh dashboard
- Investigate alerts
- Tune detection rules
- Create custom alerts

**Real Job Task**:
- Monitor SIEM (Splunk, QRadar, Azure Sentinel)
- Triage security alerts (50-200 per day)
- Identify false positives
- Escalate real threats

**Skills You're Building**:
- Log analysis
- Pattern recognition
- Incident triage
- Tool expertise

---

### 2. Vulnerability Management

**In Your Lab**:
- Scan systems with Nmap, Nessus
- Identify vulnerabilities
- Test exploits
- Recommend fixes

**Real Job Task**:
- Run vulnerability scans weekly
- Prioritize findings by risk
- Work with IT to patch systems
- Verify fixes

**Skills You're Building**:
- Vulnerability assessment
- Risk prioritization
- Remediation planning
- Communication with IT teams

---

### 3. Incident Response

**In Your Lab**:
- Detect attacks in SIEM
- Investigate compromised systems
- Contain threats
- Document everything

**Real Job Task**:
- Respond to security incidents 24/7
- Investigate breaches
- Contain malware outbreaks
- Recover systems
- Write incident reports

**Skills You're Building**:
- Forensic analysis
- Quick decision making
- Documentation
- Crisis management

---

### 4. Security Architecture

**In Your Lab**:
- Design network segmentation
- Configure firewalls
- Implement monitoring
- Create security policies

**Real Job Task**:
- Design security solutions
- Review architecture for security
- Implement defense-in-depth
- Create security standards

**Skills You're Building**:
- Network security design
- Defense strategy
- Security frameworks
- Best practices implementation

---

### 5. Identity & Access Management

**In Your Lab**:
- Manage Active Directory
- Create security groups
- Implement policies
- Monitor privileged access

**Real Job Task**:
- Manage user access
- Review permissions
- Implement least privilege
- Audit access logs
- Manage service accounts

**Skills You're Building**:
- AD administration
- Access control
- Policy enforcement
- Compliance

---

## 🗺️ Your Learning Roadmap {#roadmap}

### Month 1: Foundation

**Week 1-2: Build the Infrastructure**
```
✓ Set up all networks
✓ Install pfSense
✓ Configure basic firewall rules
✓ Install Wazuh SIEM
✓ Install Suricata IDS

Daily Time: 2-3 hours
Goal: Working monitoring environment
```

**Week 3-4: Basic Attack & Defense**
```
✓ Install Kali Linux
✓ Set up vulnerable targets
✓ Practice basic scans
✓ Learn to read SIEM alerts
✓ Do 5 exercises from Phase 3

Daily Time: 2-3 hours
Goal: Understand attack → detect → respond cycle
```

---

### Month 2: Active Directory & Enterprise

**Week 1-2: Windows Infrastructure**
```
✓ Set up Domain Controller
✓ Add workstations to domain
✓ Create users and groups
✓ Set up file shares
✓ Configure Group Policy

Daily Time: 2-3 hours
Goal: Working enterprise environment
```

**Week 3-4: AD Security**
```
✓ Monitor AD events
✓ Practice detecting attacks
✓ Implement security policies
✓ Test privilege escalation
✓ Practice incident response

Daily Time: 2-3 hours
Goal: Secure and monitor AD
```

---

### Month 3: Advanced Scenarios

**Week 1: Web Application Security**
```
✓ Deep dive into DVWA
✓ Learn all OWASP Top 10
✓ Practice web attacks
✓ Configure WAF rules
✓ Detect web attacks in SIEM

Daily Time: 2-3 hours
Goal: Web security expertise
```

**Week 2: Network Security**
```
✓ Advanced firewall rules
✓ VPN configuration
✓ IPS mode for Suricata
✓ Network forensics
✓ Traffic analysis

Daily Time: 2-3 hours
Goal: Network security mastery
```

**Week 3-4: Real-World Simulations**
```
✓ Full attack chain exercises
✓ Incident response drills
✓ Create security runbooks
✓ Build detection rules
✓ Practice documentation

Daily Time: 2-3 hours
Goal: Job-ready skills
```

---

### Month 4+: Specialize & Expand

**Choose Your Path**:

**Path A: Penetration Testing Focus**
```
- Add more vulnerable targets
- Learn advanced exploitation
- Practice report writing
- Try HackTheBox/TryHackMe
- Get OSCP certification
```

**Path B: SOC Analyst Focus**
```
- Build playbooks
- Advanced SIEM queries
- Threat hunting
- SOAR automation
- Get Security+ certification
```

**Path C: Security Engineering Focus**
```
- Infrastructure as Code
- Cloud security (AWS/Azure lab)
- Container security (Docker/K8s)
- CI/CD security
- Get CISSP certification
```

---

## 🔧 Troubleshooting & Maintenance {#troubleshooting}

### Common Issues & Solutions

#### Issue 1: "VMs are slow"

**Diagnosis**:
```
In Proxmox:
- Check CPU usage
- Check RAM usage
- Check disk I/O
```

**Solutions**:
```
1. Too many VMs running at once
   → Shut down VMs you're not using
   → Use snapshots, power off base VMs

2. Not enough RAM allocated
   → Check Task Manager in VMs
   → Adjust RAM allocation
   → Use Linux containers instead of VMs where possible

3. Disk bottleneck
   → Move VMs to faster NVMe drives
   → Check disk usage with 'iostat -x 1'
```

---

#### Issue 2: "Can't connect to VMs"

**Diagnosis**:
```
1. Check VM is running
2. Check network settings
3. Ping test:
   ping [VM-IP]
```

**Solutions**:
```
1. Wrong network bridge
   → VM Settings → Network → Select correct vmbr

2. Firewall blocking
   → Check pfSense rules
   → Check VM firewall (Windows/Linux)

3. DHCP not working
   → Check pfSense DHCP server
   → Set static IP manually
```

---

#### Issue 3: "Wazuh not receiving logs"

**Diagnosis**:
```
On agent:
systemctl status wazuh-agent

Check logs:
tail -f /var/ossec/logs/ossec.log
```

**Solutions**:
```
1. Agent not connected
   → Check agent configuration
   → Verify Wazuh manager IP
   → Restart agent: systemctl restart wazuh-agent

2. Firewall blocking
   → Allow ports 1514, 1515
   → Check pfSense rules

3. Agent not enrolled
   → Re-run agent installation
   → Check manager can reach agent
```

---

#### Issue 4: "Running out of disk space"

**Solutions**:
```
1. Clean up logs:
   sudo journalctl --vacuum-time=7d
   
2. Remove old snapshots in Proxmox

3. Clean up apt cache:
   sudo apt clean
   sudo apt autoclean

4. Use log rotation:
   Configure /etc/logrotate.d/
```

---

### Regular Maintenance Tasks

**Weekly**:
```
✓ Update all systems:
  - Proxmox: apt update && apt upgrade
  - Kali: apt update && apt full-upgrade
  - Windows: Windows Update
  - Wazuh: Check for updates

✓ Check disk space:
  df -h

✓ Review SIEM alerts

✓ Back up important configs
```

**Monthly**:
```
✓ Update Suricata rules:
  sudo suricata-update

✓ Review firewall rules

✓ Test backup restoration

✓ Clean up old VMs/snapshots

✓ Update vulnerable targets
```

---

### Snapshot Strategy

**When to Take Snapshots**:
```
1. Before major changes
   "clean-install" → Before installing new software
   "before-attack" → Before running attacks
   "working-config" → When something works perfectly

2. Name them descriptively:
   ✓ Good: "ws01-clean-domain-joined-2024-11-02"
   ✗ Bad: "snapshot1"

3. Delete old ones regularly
   Keep: Clean install, working configs
   Delete: Experimental, broken states
```

---

## 🎓 Building Your Security Department at Work

Now let's talk about applying this to build your company's security department!

### Phase 1: Assessment (Weeks 1-2)

**What to Do**:
```
1. Inventory everything:
   - What systems do you have?
   - What data needs protection?
   - Who has access to what?
   - What security tools exist (if any)?

2. Identify risks:
   - Biggest threats to your company?
   - Most critical systems?
   - Compliance requirements?

3. Document current state:
   - Network diagram
   - Asset inventory
   - Current security measures
```

**Use Your Lab**:
```
Practice creating:
- Network documentation
- Asset inventories
- Risk assessments
- Security policy templates
```

---

### Phase 2: Quick Wins (Months 1-2)

**Priority Actions**:
```
1. Basic Hygiene:
   ✓ Implement password policy
   ✓ Enable MFA on critical systems
   ✓ Regular backups
   ✓ Patch management process

2. Visibility:
   ✓ Deploy SIEM (like Wazuh)
   ✓ Centralized logging
   ✓ Monitor critical systems
   ✓ Basic alerting

3. Access Control:
   ✓ Review user permissions
   ✓ Implement least privilege
   ✓ Remove old accounts
   ✓ Audit admin access
```

**Practice in Your Lab**:
```
- Set up the same tools
- Create policies
- Test implementations
- Document procedures
```

---

### Phase 3: Build the Foundation (Months 3-6)

**What to Implement**:
```
1. Network Security:
   - Firewall rules
   - Network segmentation
   - VPN for remote access
   - IDS/IPS

2. Endpoint Security:
   - Antivirus/EDR
   - Patch management
   - Application whitelisting
   - Device encryption

3. Identity Security:
   - Active Directory cleanup
   - Privileged access management
   - Service account management
   - Access reviews
```

---

### Phase 4: Mature Security (Months 6-12)

**Advanced Capabilities**:
```
1. Security Operations:
   - 24/7 monitoring (or MSSP)
   - Incident response plan
   - Security playbooks
   - Regular security reviews

2. Compliance:
   - Meet regulatory requirements
   - Security awareness training
   - Policy documentation
   - Audit preparation

3. Proactive Security:
   - Vulnerability management
   - Penetration testing
   - Threat hunting
   - Security metrics
```

---

### Building Your Team

**Start Small**:
```
Year 1: Just You
- Focus on fundamentals
- Implement basic security
- Build processes
- Document everything

Year 2: Hire Your First Team Member
- SOC Analyst or Security Engineer
- Someone who can help monitor
- Complement your skills

Year 3+: Grow the Team
- Additional analysts
- Specialized roles (IAM, Cloud Security)
- Maybe a SOC manager
```

**Skills to Look For**:
```
Must Have:
✓ Security fundamentals (like Security+)
✓ Network knowledge
✓ Problem-solving
✓ Communication

Nice to Have:
✓ SIEM experience
✓ Scripting (Python, PowerShell)
✓ Incident response
✓ Cloud security
```

---

## 🚀 Next Steps

### This Week:
```
Day 1-2: Complete Phase 1 (Network setup)
Day 3-4: Complete Phase 2 (Monitoring setup)
Day 5-6: Complete first attack/defense exercise
Day 7: Review and document what you learned
```

### This Month:
```
Week 1: Complete infrastructure build
Week 2: Practice basic attacks and detection
Week 3: Set up AD environment
Week 4: Practice real-world scenarios
```

### This Quarter:
```
Month 1: Build everything in this guide
Month 2: Advanced exercises and scenarios
Month 3: Start applying knowledge at work
```

---

## 📚 Resources for Continued Learning

### Free Online Labs:
- **TryHackMe**: Guided cybersecurity lessons
- **HackTheBox**: CTF challenges
- **PentesterLab**: Web security exercises
- **OWASP WebGoat**: Learn web vulnerabilities

### YouTube Channels:
- **NetworkChuck**: Fun, beginner-friendly tutorials
- **IppSec**: HackTheBox walkthroughs
- **John Hammond**: Security tutorials
- **The Cyber Mentor**: Practical hacking

### Communities:
- **Reddit**: r/cybersecurity, r/netsec, r/homelab
- **Discord**: Find security-focused servers
- **LinkedIn**: Connect with security professionals
- **Twitter/X**: Follow security researchers

### Books (When You're Ready):
- "Blue Team Handbook" by Don Murdoch
- "Practical Malware Analysis" - Learn threat analysis
- "The Hacker Playbook 3" - Red team tactics
- "Security Operations Center Guidebook" - SOC building

---

## 🎯 Final Thoughts

Remember:

**It's okay to break things** - That's what snapshots are for!

**Go at your own pace** - Don't rush. Understanding is more important than speed.

**Document everything** - Future you will thank present you.

**Ask for help** - The security community is friendly and helpful.

**Practice regularly** - 30 minutes a day is better than 5 hours once a week.

**Have fun!** - This is your playground. Experiment. Try crazy things. Learn.

---

## 📝 Your Lab Journal Template

Keep a journal of what you learn! Here's a template:

```markdown
# Date: [Today's Date]

## What I Built Today:
- 

## What I Learned:
- 

## Challenges I Faced:
- 

## How I Solved Them:
- 

## Tomorrow's Goals:
- 

## Cool Thing I Discovered:
- 
```

---

## 🆘 Need Help?

**If You Get Stuck**:
1. Check the troubleshooting section above
2. Google the specific error message
3. Check Proxmox/tool documentation
4. Ask in Reddit communities
5. Take a break and come back fresh

**Remember**: Every security professional has been where you are. We all started as beginners. You're building real, valuable skills!

---

## ✅ Lab Completion Checklist

Use this to track your progress:

### Phase 1: Foundation
- [ ] Proxmox networks configured
- [ ] pfSense installed and working
- [ ] Basic firewall rules created
- [ ] Can access pfSense web interface

### Phase 2: Monitoring
- [ ] Wazuh SIEM installed
- [ ] Wazuh dashboard accessible
- [ ] Suricata IDS installed
- [ ] First test alert received
- [ ] Can investigate alerts

### Phase 3: Attack Lab
- [ ] Kali Linux installed
- [ ] Metasploitable or DVWA working
- [ ] Juice Shop installed
- [ ] Completed port scan exercise
- [ ] Completed SQL injection exercise

### Phase 4: Enterprise
- [ ] Windows Domain Controller set up
- [ ] Active Directory functional
- [ ] Workstations joined to domain
- [ ] Users can log in
- [ ] Wazuh monitoring AD events

### Mastery
- [ ] Can respond to incidents
- [ ] Created custom detection rules
- [ ] Documented security procedures
- [ ] Practiced 10+ attack scenarios
- [ ] Built security playbooks

---

**Congratulations on starting this journey! You're on your way to becoming a confident security engineer with real, hands-on experience. Keep building, keep learning, and most importantly - have fun!**

**Remember: The best security engineers aren't the ones who never make mistakes - they're the ones who learn from every experiment in their home lab.** 🎉

---

*Last Updated: November 2, 2025*
*Version: 1.0*
*Created for: Security+ certified professionals building enterprise security experience*