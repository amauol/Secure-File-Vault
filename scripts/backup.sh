#!/bin/bash
BACKUP_DIR="/var/backups/secure-vault"
SRC="/var/lib/secure-vault"

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/backup-$(date =%F_%H%M).tar.gz" "$SRC"
