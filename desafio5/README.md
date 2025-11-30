# Desafio 5 – Microsserviços com API Gateway

Nesta pasta existem três serviços HTTP encapsulados em containers:

- `users-service`: fornece informações de usuários.
- `orders-service`: retorna pedidos associados a usuários.
- `gateway`: atua como ponto de entrada único e repassa as chamadas para os dois serviços.

## Subindo o ambiente

```bash
cd desafio5
docker compose up --build
```

Quando todos os containers estiverem prontos:

- Verificar saúde do gateway:
  - `curl http://localhost:8082/health`
- Listar usuários via gateway:
  - `curl http://localhost:8082/users`
- Listar pedidos via gateway:
  - `curl http://localhost:8082/orders`

O gateway acessa internamente os serviços `users-service` e `orders-service` pela rede interna definida no `docker-compose.yml`, mantendo um único endpoint exposto externamente.
