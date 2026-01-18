
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

  * Python 3.x -> On Server
  * `netcat` -> ON Client (installed by default on most Linux/macOS systems)

  ### 2. Installation & Setup

  Clone the repository to your server:

  ```bash
  git clone [https://github.com/aluminium65/Gup-Shup.git](https://github.com/aluminium65/Gup-Shup.git)
  cd Gup-Shup
