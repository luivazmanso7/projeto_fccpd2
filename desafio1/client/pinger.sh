#!/bin/sh

SERVER_HOST="${SERVER_HOST:-server}"
SERVER_PORT="${SERVER_PORT:-8080}"
INTERVAL_SECONDS="${INTERVAL_SECONDS:-5}"

echo "Iniciando cliente HTTP. Alvo: http://$SERVER_HOST:$SERVER_PORT/"

while true; do
  echo "---- $(date -u +"%Y-%m-%dT%H:%M:%SZ") ----"
  if curl -s "http://$SERVER_HOST:$SERVER_PORT/"; then
    echo ""
  else
    echo "Falha ao contatar o servidor"
  fi
  sleep "$INTERVAL_SECONDS"
done

