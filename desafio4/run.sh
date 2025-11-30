#!/bin/sh
set -e

NETWORK_NAME="desafio4-net"

echo "Criando rede Docker (se necessário): $NETWORK_NAME"
if ! docker network ls --format '{{.Name}}' | grep -q "^${NETWORK_NAME}\$"; then
  docker network create "$NETWORK_NAME"
fi

echo "Construindo imagens dos serviços..."
docker build -t desafio4-service-a ./service_a
docker build -t desafio4-service-b ./service_b

echo "Iniciando Microsserviço A (lista de usuários)..."
docker run -d --rm --name service-a --network "$NETWORK_NAME" -p 5000:5000 desafio4-service-a

echo "Iniciando Microsserviço B (relatório)..."
docker run --rm --name service-b --network "$NETWORK_NAME" -p 5001:5001 \
  -e SERVICE_A_HOST=service-a \
  desafio4-service-b

