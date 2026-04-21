#!/bin/bash
# ATOM-SG Pilot Playwright Test Monitor
# Runs every 5 minutes to check test status

REPO="seanfzc/atom-sg"
LOG_FILE="/Users/zcaeth/.openclaw/workspace/playwright_monitor.log"

echo "========================================" >> "$LOG_FILE"
echo "$(date): Checking Playwright test status" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

# Get latest run status
cd /Users/zcaeth/.openclaw/workspace/ATOM-SG\ Pilot
RUN_STATUS=$(gh run list --repo "$REPO" --limit 1 --json status,conclusion,headBranch,createdAt 2>/dev/null)

if [ -z "$RUN_STATUS" ]; then
    echo "$(date): ERROR - Could not fetch run status" >> "$LOG_FILE"
    exit 1
fi

echo "$(date): Latest run status: $RUN_STATUS" >> "$LOG_FILE"

# Check if there are any failed runs
FAILED_RUNS=$(gh run list --repo "$REPO" --limit 5 --json databaseId,status,conclusion | jq -r '.[] | select(.conclusion == "failure") | .databaseId')

if [ -n "$FAILED_RUNS" ]; then
    echo "$(date): ALERT - Failed runs detected: $FAILED_RUNS" >> "$LOG_FILE"
    
    for RUN_ID in $FAILED_RUNS; do
        echo "$(date): Investigating run $RUN_ID..." >> "$LOG_FILE"
        gh run view "$RUN_ID" --repo "$REPO" >> "$LOG_FILE" 2>&1
        echo "" >> "$LOG_FILE"
        echo "Failed jobs log:" >> "$LOG_FILE"
        gh run view "$RUN_ID" --log-failed --repo "$REPO" 2>&1 | head -100 >> "$LOG_FILE"
        echo "---" >> "$LOG_FILE"
    done
else
    echo "$(date): No failed runs in last 5 checks" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
