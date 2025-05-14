# Beta Power Network\nPlaceholder
# Beta Power Network

A decentralized YouTube ecosystem empowering consumers, creators, and advertisers.

## Overview
- **Consumers**: Vote on age recommendations and ad quality, building reputation signatures.
- **Advertisers**: Earn BETA tokens for short ads or creative content, competing as creators.
- **Creators**: Rewarded for mediation quality, not just popularity.

## Setup
1. Install dependencies: `pip install google-api-python-client google-auth-oauthlib`.
2. Configure YouTube API: Replace `YOUR_API_KEY` in `follower_bot.py`, `backend.py`.
3. Run DApp: Load `userscript.js` in Tampermonkey, start `follower_bot.py`.

## Files
- `follower-bot/`: Tracks actions and votes.
- `notification-addon/`: DApp UI and backend.
- `blockchain/`: BETA token contract.
