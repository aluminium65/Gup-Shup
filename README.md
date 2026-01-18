---

# Gup Shup 💬

**Gup Shup** is a minimalist, lightweight Python-based chat server designed for simplicity and ease of use. Unlike traditional chat apps, there are no usernames or registration forms. Users are identified solely by their **IP addresses**, making it a "no-frills" communication tool that you can start and leave running on any server.

## Features

* **Ultra-Lightweight:** Written in pure Python with no heavy dependencies.
* **Anonymous & Simple:** No usernames; users are identified by their public/local IP.
* **Private Messaging:** Support for sending direct messages to specific users.
* **Terminal-Based:** Connect instantly using standard networking tools like `netcat` (nc).
* **Persistent:** Designed to be left running as a background service on any server/VPS.

## Getting Started

### 1. Prerequisites

* Python 3.x
* `netcat` (installed by default on most Linux/macOS systems)

### 2. Installation & Setup

Clone the repository to your server:

```bash
git clone https://github.com/aluminium65/Gup-Shup.git
cd Gup-Shup

```

### 3. Running the Server

Start the server by running the Python script. By default, it listens for incoming connections.

```bash
python3 Gup-Shup.py

```

## How to Connect

You don't need a special client to join the chat. Just use `netcat` (nc) from your terminal.

### Connect from your terminal:

Replace `[SERVER_IP]` with the IP address of the machine running the server.

```bash
nc [SERVER_IP] [PORT]

```

*(Default port is usually 5000 or 12345 depending on your script configuration)*

## Usage

* **Public Chat:** Just type your message and hit `Enter`. Everyone connected will see your message prefixed by your IP address.
* **Private Messages:** Enter the reciever's IP address in square brackets followed by a colon then the message.
```text
[TARGET_IP]: [YOUR_MESSAGE]

```



## Why Gup-Shup?

Most chat applications today are bloated with tracking, accounts, and complex UIs. **Gup-Shup** is for those who want a quick, "set it and forget it" communication channel on their own infrastructure.

---

*Created by [aluminium65*](https://www.google.com/search?q=https://github.com/aluminium65)
