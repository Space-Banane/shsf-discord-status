# SHSF Discord Status

A Discord bot that checks and caches the online status of a specific Discord user using Redis for caching.

## Overview

This application monitors a target Discord user's status (online, idle, dnd, offline) and caches the result in Redis to minimize API calls and improve response times.

## Features

- 🔍 Fetches Discord user status across all mutual guilds
- ⚡ Redis caching with 5-minute expiration to reduce Discord API calls
- 🎯 Targets a specific user by ID
- 🔄 Automatic fallback to live fetch when cache expires

## Prerequisites

- Python 3.9 (tested)
- Discord Bot Token
- Redis instance
- Discord bot with proper intents enabled

## Installation

1. Make a new Function in your SHSF instance.
2. Configure it to your needs.
3. Make a requirements.txt file with the following content:

```txt
discord
redis
``` 
4. Configure your .env file with the necessary environment variables (see Configuration section).

The function returns a dictionary with the user's status: 

```python
{"status": "online"}  # or "idle", "dnd", "offline"
```

## Configuration

Set the following environment variables: 

| Variable | Description |
|----------|-------------|
| `BOB` | Your Discord bot token |
| `TARGET` | Discord user ID to monitor |
| `HOST` | Redis server hostname |
| `REDID` | Redis password |

## How It Works

1. **Cache Check**: First checks Redis for a cached status
2. **Live Fetch**: If no cache exists, connects to Discord and searches for the target user across all guilds
3. **Cache Update**: Stores the fetched status in Redis with a 500-second (5-minute) expiration
4. **Return**: Returns the status as a dictionary

## Discord Bot Setup

Your Discord bot needs the following intents enabled in the [Discord Developer Portal](https://discord.com/developers/applications):

- ✅ Server Members Intent
- ✅ Presence Intent
- ✅ Message Content Intent (if using message features)

## Redis Configuration

The application connects to Redis on port `12003` with:
- Username: `default`
- Password: From `REDID` environment variable
- Decode responses:  Enabled (UTF-8)

## Redis Note
You can also you Database Communication within SHSF instead of setting up your own Redis instance. Read the doc for that though!

## License

This project is open source and available under the MIT License. 
