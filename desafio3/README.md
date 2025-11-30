# Desafio 3 – Docker Compose Orquestrando Serviços

Este desafio usa Docker Compose para subir três containers trabalhando juntos:

- `web`: API Flask.
- `db`: Postgres.
- `cache`: Redis.

## Como rodar

```bash
cd desafio3
docker compose up --build
```

Depois basta acessar `http://localhost:8081/`.  
Cada chamada cria um registro no Postgres e aumenta um contador no Redis; o retorno mostra o total de acessos.

Para parar tudo:

```bash
docker compose down
```
