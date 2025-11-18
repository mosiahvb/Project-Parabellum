# 🚀 Simplified Cybersecurity Home Lab: Get Started in 1 Hour!

## 🎯 Your New Game Plan

**The Problem with the Original Plan**: Too much networking setup before you could have fun!

**The NEW Plan**: Get VMs running on ONE simple network, start practicing cybersecurity TODAY, add complexity later.

---

## 📋 What Makes This Simpler?

### Original Plan vs. Simplified Plan

| Original | Simplified |
|----------|-----------|
| Set up 4 different networks | Use 1 network (your existing home network) |
| Configure pfSense firewall | Skip firewall for now |
| Complex network bridges | Use what's already there (vmbr0) |
| Day 1: Still configuring networks | **Day 1: Already hacking!** |

**Important**: You'll still get ALL the same tools and practice. We're just changing the ORDER to get you started faster.

---

## 🏗️ The Simplified Architecture

### What You're Building (Think of it like Lego sets)

**Right Now - Simple Network (Everything on one baseplate)**
```
┌─────────────────────────────────────────────────────┐
│         YOUR HOME NETWORK (172.22.1.x)              │
│         (Everything talks on one network)           │
│                                                      │
│   🖥️ Your Mac          📊 Proxmox Server           │
│   (172.22.1.x)        (172.22.1.22)                │
│                                                      │
│   Inside Proxmox:                                   │
│   ┌────────────────────────────────────────────┐   │
│   │  🎯 Kali Linux    (172.22.1.x)            │   │
│   │  🕷️ Metasploitable (172.22.1.x)          │   │
│   │  🌐 DVWA          (172.22.1.x)            │   │
│   │  📊 Wazuh SIEM    (172.22.1.x)            │   │
│   │  💻 Windows VMs   (172.22.1.x)            │   │
│   └────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**Later - When You're Ready (Multiple baseplates with connections)**
```
We'll add network segmentation and pfSense when you understand 
what you're protecting and why!
```

---

## ⚡ Phase 1: Quick Start (Do This Today!)

**Goal**: Have Kali Linux and a vulnerable target running so you can practice your first attack.

**Time**: 1-2 hours

### Step 1.1: Create Your First VM - Kali Linux

**What is Kali?** Your "hacking toolkit" - it has all the security testing tools built in.

#### Download Kali Linux

**Option A: Pre-built VM (FASTEST - 5 minutes)**
```
1. In Proxmox, click: local (your-server) → ISO Images
2. But wait! We'll use a pre-built VM instead
3. Go to Kali website: https://www.kali.org/get-kali/#kali-virtual-machines
4. Download: "Proxmox" version (about 3GB)
5. Extract the .qcow2 file from the download
```

**Option B: Install from ISO (More practice - 30 minutes)**
```
1. In Proxmox: local → ISO Images → Download from URL
2. URL: https://cdimage.kali.org/kali-2024.3/kali-linux-2024.3-installer-amd64.iso
3. Wait for download
```

#### Create Kali VM

**Using Option A (Pre-built):**
```
In Proxmox Shell (click your node name → Shell):

# Upload the .qcow2 file to Proxmox first (using the Upload feature)
# Then import it:
qm importdisk 300 /path/to/kali.qcow2 local-lvm
qm set 300 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-300-disk-0
qm set 300 --memory 4096
qm set 300 --cores 4
qm set 300 --net0 virtio,bridge=vmbr0
qm set 300 --name kali-linux
```

**Using Option B (ISO Install):**
```
In Proxmox GUI:
1. Click: Create VM
2. Settings:
   - VM ID: 300
   - Name: kali-linux
   - ISO: Select your Kali ISO
   - Disk: 80GB
   - CPU: 4 cores
   - RAM: 4096MB
   - Network: vmbr0 (this is your home network - easy!)
3. Click: Finish
4. Start VM → Console
5. Install Kali:
   - Graphical Install
   - Language: English
   - Location: Your location
   - Keyboard: Your layout
   - Hostname: kali
   - Domain: leave blank
   - Full name: Your name
   - Username: kali
   - Password: kali (or choose your own)
   - Partition: Guided - use entire disk
   - Install GRUB: Yes
   - Wait 15-20 minutes
   - Reboot
```

**Default Login (if using pre-built):**
- Username: `kali`
- Password: `kali`

**✅ Checkpoint**: You can log into Kali Linux and see the desktop!

---

### Step 1.2: Create Your First Target - DVWA

**What is DVWA?** A purposely vulnerable website where you can practice web hacking safely.

#### Quick Setup with Docker (10 minutes)

**Create Ubuntu VM:**
```
In Proxmox:
1. Create VM
2. Settings:
   - VM ID: 301
   - Name: dvwa-target
   - ISO: Ubuntu Server 22.04 (download if needed)
   - Disk: 20GB
   - CPU: 2 cores
   - RAM: 2048MB
   - Network: vmbr0
3. Install Ubuntu:
   - Name: admin
   - Server name: dvwa
   - Username: admin
   - Password: (your choice)
   - Install OpenSSH: YES
   - No other packages
```

**Install DVWA:**
```
After Ubuntu is installed, login and run:

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

# Run DVWA
sudo docker run -d -p 80:80 --name dvwa vulnerables/web-dvwa

# Check it's running
sudo docker ps

# Get the VM's IP address
ip addr show

# You'll see something like: inet 172.22.1.XXX
# Write this down!
```

**Test DVWA:**
```
From your Mac's browser:
http://[the-IP-you-wrote-down]

You should see DVWA login page!
Default login: admin / password
```

**✅ Checkpoint**: You can access DVWA from your Mac's browser!

---

### Step 1.3: Your FIRST Attack! (The Fun Part!)

**Time**: 15 minutes

Now let's do something cool - your first SQL injection attack!

#### From Kali Linux:

1. **Open Firefox** in Kali
2. **Go to**: `http://[your-DVWA-IP]`
3. **Login**: admin / password
4. **Click**: "Create / Reset Database" (bottom of page)
5. **Login again**: admin / password
6. **Click**: "DVWA Security" (left menu)
7. **Set to**: "Low"
8. **Click**: Submit
9. **Click**: "SQL Injection" (left menu)

#### Try Your First Attack:

In the "User ID" box, instead of typing a number, type:
```
' OR '1'='1
```

Click Submit.

**🎉 BOOM! You just performed SQL injection!**

You should see ALL users in the database, not just one!

#### What Just Happened?

The website expected: `SELECT * FROM users WHERE id = '1'`

But you made it: `SELECT * FROM users WHERE id = '' OR '1'='1'`

Since 1 always equals 1, it shows everything!

---

### Step 1.4: Try More Attacks (Practice Time!)

**Now try these in DVWA:**

1. **Command Injection**
   - Click: Command Injection
   - Try: `127.0.0.1; ls -la`
   - You just listed files on the server!

2. **File Upload**
   - Click: File Upload
   - Try uploading a .php file
   - See if you can upload malicious code

3. **XSS (Cross-Site Scripting)**
   - Click: XSS (Reflected)
   - Try: `<script>alert('HACKED!')</script>`
   - You just injected JavaScript!

**Practice these for 30 minutes - 1 hour. Have fun!**

---

## 📊 Phase 2: Add Monitoring (Week 2)

**Goal**: See your attacks being detected by a real security tool!

**Time**: 2-3 hours

### Step 2.1: Install Wazuh SIEM

**What is Wazuh?** The "security camera system" that watches everything and alerts you to threats.

#### Create Wazuh VM:

```
In Proxmox:
1. Create VM
2. Settings:
   - VM ID: 200
   - Name: wazuh-siem
   - ISO: Ubuntu Server 22.04
   - Disk: 100GB (logs need space!)
   - CPU: 4 cores
   - RAM: 8192MB (8GB - important!)
   - Network: vmbr0
```

#### Install Ubuntu (same as before):
```
- Name: admin
- Server name: wazuh
- Username: admin
- Password: (your choice)
- Install OpenSSH: YES
```

#### Install Wazuh:

```
After Ubuntu install, login and run:

# Update system
sudo apt update && sudo apt upgrade -y

# Download Wazuh installer
curl -sO https://packages.wazuh.com/4.9/wazuh-install.sh

# Install everything in one command!
sudo bash ./wazuh-install.sh -a

# This takes 15-20 minutes
# It will show you a password at the end - SAVE IT!
```

**Get your Wazuh IP:**
```
ip addr show
# Write down the IP (172.22.1.XXX)
```

**Access Wazuh:**
```
From your Mac's browser:
https://[your-wazuh-IP]

Username: admin
Password: (from installation output)
```

**✅ Checkpoint**: You see the Wazuh dashboard!

---

### Step 2.2: Connect Your VMs to Wazuh

Now let's make Wazuh monitor your Kali and DVWA!

#### Install Agent on DVWA:

```
SSH into your DVWA VM:
ssh admin@[dvwa-IP]

Then run:
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.9.0-1_amd64.deb

sudo WAZUH_MANAGER="[your-wazuh-IP]" WAZUH_AGENT_NAME="dvwa-target" dpkg -i wazuh-agent_4.9.0-1_amd64.deb

sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

#### Install Agent on Kali:

```
Same process - SSH or open terminal in Kali:
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.9.0-1_amd64.deb

sudo WAZUH_MANAGER="[your-wazuh-IP]" WAZUH_AGENT_NAME="kali-linux" dpkg -i wazuh-agent_4.9.0-1_amd64.deb

sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

**Check Wazuh Dashboard:**
```
In your browser:
- Go to Wazuh
- Click: Agents (top menu)
- You should see: dvwa-target and kali-linux both "Active"!
```

---

### Step 2.3: Watch Your Attacks Get Detected!

#### Perform an Attack:

From Kali, scan DVWA:
```
# Open terminal in Kali
nmap -sV [dvwa-IP]

# This scans for open ports and services
```

#### See It Detected:

```
In Wazuh Dashboard:
1. Click: Security Events
2. Look for alerts from "dvwa-target"
3. You should see: "Multiple connection attempts" or similar!
```

#### Generate More Alerts:

```
Try failed SSH logins:
ssh fakeuser@[dvwa-IP]
(enter wrong password 3 times)

In Wazuh, watch for:
"Multiple failed login attempts" alert!
```

**🎉 You're now doing BOTH red team (attacking) and blue team (defending)!**

---

## 💻 Phase 3: Add Windows (Week 3-4)

**Goal**: Create a mini "company network" to practice Windows security.

**Time**: 3-4 hours

### Step 3.1: Create Windows Server (Domain Controller)

#### Download Windows:
```
Get Windows Server 2022 Evaluation (free 180-day trial)
From: https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022
```

#### Create VM:

```
In Proxmox:
1. Create VM
2. Settings:
   - VM ID: 400
   - Name: dc01-company
   - ISO: Windows Server 2022
   - OS Type: Windows
   - Disk: 60GB
   - CPU: 2 cores
   - RAM: 4096MB
   - Network: vmbr0
```

#### Install Windows:

```
1. Start VM → Console
2. Choose: Windows Server 2022 Standard (Desktop Experience)
3. Custom installation
4. Accept license
5. Set Administrator password (STRONG!)
6. Wait 15-20 minutes
```

#### Make it a Domain Controller:

```
After Windows starts:

1. Open: Server Manager (opens automatically)
2. Click: Add roles and features
3. Next → Next → Next
4. Select: Active Directory Domain Services
5. Add Features → Next → Next → Install
6. Wait 10 minutes
7. After install, click flag icon → "Promote this server..."
8. Add a new forest
9. Domain name: company.local
10. Set DSRM password (STRONG!)
11. Next through everything → Install
12. Server will reboot
```

**✅ Checkpoint**: After reboot, login as company\Administrator

---

### Step 3.2: Create Windows 10 Workstation

#### Download Windows 10:
```
Get Windows 10 Evaluation
From: https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise
```

#### Create VM:
```
In Proxmox:
- VM ID: 410
- Name: ws01-employee
- ISO: Windows 10
- Disk: 60GB
- CPU: 2
- RAM: 4096MB
- Network: vmbr0
```

#### Join to Domain:

```
After installing Windows 10:

1. Set DNS to your DC's IP:
   - Settings → Network → Change adapter options
   - Right-click → Properties → IPv4
   - DNS: [your-DC-IP]

2. Join domain:
   - Right-click This PC → Properties
   - Advanced system settings → Computer Name → Change
   - Domain: company.local
   - Enter Administrator credentials
   - Reboot

3. Login as domain user:
   - company\Administrator
```

---

### Step 3.3: Practice Active Directory Attacks

#### Create Some Users:

On the Domain Controller:
```
1. Open: Active Directory Users and Computers
2. Right-click domain → New → Organizational Unit
   - Name: "Employees"
3. Right-click Employees → New → User
   - Create: john.doe
   - Create: jane.smith
   - Create: bob.johnson
```

#### Attack Scenario 1: Password Spray

From Kali:
```
# Install crackmapexec
sudo apt install crackmapexec -y

# Try common passwords against all users
crackmapexec smb [DC-IP] -u users.txt -p "Password123"
```

**Check Wazuh**: See if it detected the attack!

#### Attack Scenario 2: Kerberoasting

From Kali:
```
# Install impacket
sudo apt install python3-impacket -y

# Try to get service tickets
GetUserSPNs.py company.local/john.doe:Password123 -dc-ip [DC-IP]
```

**Check Wazuh**: Look for Kerberos-related alerts!

---

## 🎯 Practice Scenarios (Do These at Your Own Pace)

### Scenario 1: The Phishing Email
```
Goal: Simulate a user clicking a bad link

1. Create a fake phishing page on DVWA
2. Send link to your "user" (yourself)
3. Enter credentials
4. Watch them get captured
5. See if Wazuh detected anything unusual
```

### Scenario 2: The Insider Threat
```
Goal: Simulate employee accessing unauthorized files

1. On Domain Controller, create a "Finance" folder
2. Set permissions (only HR can access)
3. Try to access from regular user account
4. See the "Access Denied" in Wazuh logs
```

### Scenario 3: The Malware Download
```
Goal: Detect malicious file downloads

1. Download EICAR test file (safe test malware)
2. Put it on DVWA server
3. Download from Windows workstation
4. Watch Wazuh AND Windows Defender alert!
```

### Scenario 4: The Data Exfiltration
```
Goal: Detect someone stealing data

1. Create large file on workstation
2. Use SCP/FTP to transfer to Kali
3. Watch network traffic spike in Wazuh
```

---

## 📈 Phase 4: Expand Your Lab (Month 2+)

Once you're comfortable, add these:

### Option A: More Vulnerable Targets
```
Add:
- Metasploitable 3 (Linux vulnerabilities)
- OWASP Juice Shop (modern web app)
- HackTheBox/TryHackMe boxes
- Vulnerable WordPress site
```

### Option B: More Security Tools
```
Add:
- Suricata IDS (network monitoring)
- TheHive (incident response platform)
- MISP (threat intelligence)
- Velociraptor (endpoint monitoring)
```

### Option C: Cloud Security
```
Add:
- AWS Free Tier account
- Practice cloud security
- S3 bucket misconfigurations
- IAM policies
```

### Option D: NOW Add Network Segmentation
```
Finally add pfSense and create separate networks:
- Management network
- Production network
- Attack range
- DMZ

This is when you'll use the ORIGINAL guide!
```

---

## 🛠️ Quick Reference Commands

### Proxmox Useful Commands:
```bash
# List all VMs
qm list

# Start VM
qm start [VM-ID]

# Stop VM
qm stop [VM-ID]

# Delete VM
qm destroy [VM-ID]

# Check disk usage
df -h

# Check memory usage
free -h
```

### Common Issues & Fixes:

**VM won't start:**
```
- Check disk space: df -h
- Check if already running: qm list
- Try: qm stop [ID] then qm start [ID]
```

**Can't access VM from Mac:**
```
- Check VM is running
- Get VM IP: In VM console, run: ip addr show
- Ping test: ping [VM-IP]
- Check firewall on VM
```

**Wazuh not receiving logs:**
```
On agent VM:
sudo systemctl status wazuh-agent
sudo systemctl restart wazuh-agent

Check logs:
sudo tail -f /var/ossec/logs/ossec.log
```

**Out of disk space:**
```
# Clean up logs
sudo journalctl --vacuum-time=7d

# Remove old snapshots in Proxmox GUI

# Clean apt cache
sudo apt clean
```

---

## 📚 Learning Resources

### Free Practice Platforms:
- **TryHackMe**: Guided rooms for beginners
- **HackTheBox**: CTF challenges
- **OverTheWire**: Command-line challenges
- **PentesterLab**: Web security exercises

### YouTube Channels:
- **NetworkChuck**: Beginner-friendly, fun
- **John Hammond**: Great walkthroughs
- **IppSec**: HackTheBox solutions
- **The Cyber Mentor**: Practical hacking

### Communities:
- Reddit: r/cybersecurity, r/homelab
- Discord: TryHackMe, HackTheBox servers
- Twitter: #infosec, #cybersecurity

---

## 🎓 Your Learning Path

### Week 1: Foundation
```
✓ Install Kali and DVWA
✓ Practice 5 different attacks
✓ Get comfortable with Linux commands
✓ Understand how web vulnerabilities work

Daily: 1-2 hours
```

### Week 2: Monitoring
```
✓ Install Wazuh
✓ Connect your VMs
✓ Generate alerts
✓ Practice investigating logs

Daily: 1-2 hours
```

### Week 3-4: Windows
```
✓ Set up Active Directory
✓ Create users and groups
✓ Join workstations
✓ Practice AD attacks

Daily: 1-2 hours
```

### Month 2: Advanced Topics
```
✓ Add more vulnerable targets
✓ Learn new tools
✓ Practice incident response
✓ Create security documentation

Daily: 1-2 hours
```

### Month 3: Your Choice!
```
Pick your path:
- Penetration Testing (add more targets)
- SOC Analyst (advanced SIEM)
- Security Engineering (network segmentation)
```

---

## 💼 Skills You're Building

### Technical Skills:
✓ Vulnerability scanning (Nmap)
✓ Web application testing (SQL injection, XSS)
✓ SIEM operation (Wazuh)
✓ Log analysis
✓ Active Directory administration
✓ Windows security
✓ Linux administration
✓ Incident response

### Soft Skills:
✓ Problem-solving
✓ Documentation
✓ Analytical thinking
✓ Attention to detail
✓ Patience (important!)

---

## 🎯 Your First Week Goals

### Day 1 (2-3 hours):
- [ ] Install Kali Linux
- [ ] Install DVWA
- [ ] Perform your first SQL injection
- [ ] Try 3 different attacks

### Day 2 (1-2 hours):
- [ ] Practice more DVWA modules
- [ ] Take notes on what you learned
- [ ] Try different security levels in DVWA

### Day 3 (2-3 hours):
- [ ] Install Wazuh SIEM
- [ ] Connect DVWA to Wazuh
- [ ] Generate your first alert

### Day 4 (1-2 hours):
- [ ] Connect Kali to Wazuh
- [ ] Perform attacks and watch detection
- [ ] Practice investigating alerts

### Day 5-7 (1-2 hours each):
- [ ] Review what you learned
- [ ] Document your findings
- [ ] Plan next week's learning

---

## 🆘 When You Get Stuck

**Remember:**

1. **Google is your friend**: Search for specific error messages
2. **Take breaks**: Sometimes stepping away helps
3. **Use snapshots**: Before trying something risky
4. **Document**: Write down what works
5. **Ask for help**: Reddit, Discord communities

**Common Beginner Mistakes:**

❌ Trying to do too much at once
✅ Focus on one thing at a time

❌ Not taking snapshots before changes
✅ Snapshot before every major change

❌ Ignoring error messages
✅ Read and understand errors

❌ Not documenting what you do
✅ Keep a learning journal

---

## 🎉 Celebrate Small Wins!

### You Should Celebrate When:
- ✅ Your first VM boots successfully
- ✅ Your first successful attack
- ✅ Your first detected alert in SIEM
- ✅ Your first Windows domain joins
- ✅ You solve a problem on your own
- ✅ You complete a full attack scenario

**Remember**: Every security professional started where you are. You're building REAL skills that companies pay for!

---

## 🚀 Ready to Start?

### Your Action Plan:

1. **Today**: Install Kali and DVWA (1-2 hours)
2. **Today**: Perform your first attack (30 minutes)
3. **This Week**: Add Wazuh monitoring
4. **Next Week**: Add Windows environment
5. **Month 2**: Advanced scenarios

### Before You Begin:

- [ ] Take a snapshot of your Proxmox host (backup!)
- [ ] Make sure you have enough disk space (100GB+ free)
- [ ] Set aside uninterrupted time
- [ ] Have fun! This is YOUR playground!

---

## 📝 Lab Journal Template

Keep track of your progress:

```markdown
# Date: [Date]

## What I Built:
- 

## What I Learned:
- 

## Cool Things I Discovered:
- 

## Problems I Faced:
- 

## How I Solved Them:
- 

## Tomorrow's Goals:
- 
```

---

## 🎯 Success Metrics

### After 1 Month, You Should:
- ✓ Comfortably navigate Kali Linux
- ✓ Perform 10+ different attack types
- ✓ Operate Wazuh SIEM confidently
- ✓ Understand Windows Active Directory
- ✓ Investigate security alerts
- ✓ Document your findings professionally

### After 3 Months, You Should:
- ✓ Run complex attack scenarios
- ✓ Detect and respond to incidents
- ✓ Manage an Active Directory environment
- ✓ Create custom detection rules
- ✓ Understand defense-in-depth
- ✓ Be ready to apply skills at work!

---

## 💪 You've Got This!

The difference between you and a security professional isn't knowledge - it's just practice time. Every expert was once a beginner who didn't give up.

**Start simple. Practice daily. Build gradually. Have fun!**

---

## 🔄 When to Move to Advanced Network Setup

You're ready for the complex networking (original guide) when:

✅ You've run 20+ attack scenarios
✅ You understand how attacks work
✅ You can investigate alerts confidently
✅ You know WHY you need network segmentation
✅ You're comfortable with Linux and Windows
✅ You want to simulate enterprise environments

**At that point, the network complexity will make SENSE because you'll understand what you're protecting!**

---

**Welcome to your cybersecurity journey! Now stop reading and go install Kali! 🚀**

*Last Updated: November 2, 2025*
*Version: 1.0 - Simplified Quick Start*
*Perfect for: Security+ certified professionals who want hands-on experience FAST*