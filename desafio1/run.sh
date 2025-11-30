#!/bin/sh
set -e

NETWORK_NAME="desafio1-net"
SERVER_IMAGE="desafio1-server"
CLIENT_IMAGE="desafio1-client"

echo "Criando rede Docker : $NETWORK_NAME"
if ! docker network ls --format '{{.Name}}' | grep -q "^${NETWORK_NAME}\$"; then
  docker network create "$NETWORK_NAME"
fi

echo "Construindo imagens"
docker build -t "$SERVER_IMAGE" ./server
docker build -t "$CLIENT_IMAGE" ./client

echo "Iniciando servidor"
docker run -d --rm --name server --network "$NETWORK_NAME" -p 8080:8080 "$SERVER_IMAGE"

echo "Iniciando cliente"
docker run --rm --name client --network "$NETWORK_NAME" \
  -e SERVER_HOST=server \
  "$CLIENT_IMAGE"

