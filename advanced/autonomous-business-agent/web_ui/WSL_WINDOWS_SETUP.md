# Accessing Web UI from Windows (WSL2 Setup)

## Configuration Complete ✅

The application is now configured to be accessible from Windows while running in WSL2.

## How to Access

### Option 1: Using localhost (Recommended)
WSL2 automatically forwards ports to Windows. After starting the servers in WSL, access from Windows browser:

- **Frontend**: `http://localhost:3002`
- **Backend API**: `http://localhost:8000`

### Option 2: Using WSL IP Address
If localhost doesn't work, find your WSL IP address:

```bash
# In WSL terminal
ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'
```

Then access using that IP:
- **Frontend**: `http://<WSL_IP>:3002`
- **Backend API**: `http://<WSL_IP>:8000`

## Starting the Application

### From WSL Terminal:

```bash
cd /mnt/d/Code/Agentic\ AI/Internship\ Tasks/nexe-agent-internship/advanced/autonomous-business-agent/web-ui

# Make sure you're in the virtual environment
source ../.venv/bin/activate

# Start both servers
./start.sh
```

### Or start them separately:

**Terminal 1 - Backend:**
```bash
cd api
python main.py
```

**Terminal 2 - Frontend:**
```bash
npm run dev
```

## What Was Changed

1. **Backend (FastAPI)**: Already bound to `0.0.0.0:8000` - accessible from anywhere
2. **Frontend (Next.js)**: Now bound to `0.0.0.0:3002` with `-H 0.0.0.0` flag
3. **CORS**: Updated to allow requests from localhost, 127.0.0.1, and 0.0.0.0

## Troubleshooting

### If localhost doesn't work:

1. **Check Windows Firewall**: Make sure ports 3002 and 8000 are allowed
2. **Check WSL version**: Run `wsl --version` (WSL2 required for automatic port forwarding)
3. **Manual port forwarding**: If using WSL1, you'll need to manually forward ports

### Manual Port Forwarding (if needed):

Run in Windows PowerShell as Administrator:
```powershell
netsh interface portproxy add v4tov4 listenport=3002 listenaddress=0.0.0.0 connectport=3002 connectaddress=<WSL_IP>
netsh interface portproxy add v4tov4 listenport=8000 listenaddress=0.0.0.0 connectport=8000 connectaddress=<WSL_IP>
```

To remove port forwarding:
```powershell
netsh interface portproxy delete v4tov4 listenport=3002 listenaddress=0.0.0.0
netsh interface portproxy delete v4tov4 listenport=8000 listenaddress=0.0.0.0
```

## Testing

1. Start the servers in WSL
2. Open Windows browser
3. Navigate to `http://localhost:3002`
4. You should see the Autonomous Business Agent chat interface

## Notes

- Both servers are now bound to `0.0.0.0`, making them accessible from Windows
- CORS is configured to accept requests from multiple origins
- WSL2 handles port forwarding automatically in most cases
- The application will work seamlessly between WSL and Windows
