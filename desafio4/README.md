# Desafio 4 – Microsserviços Independentes

Este desafio separa a lógica em dois microsserviços HTTP distintos:

- **Microsserviço A** (`service_a`): expõe uma lista de usuários em formato JSON.
- **Microsserviço B** (`service_b`): consome o serviço A e gera um relatório textual.

Cada serviço tem seu próprio Dockerfile e pode ser construído e executado separadamente.

## Execução com rede Docker

```bash
cd desafio4
./run.sh
```

O script:

- Cria a rede `desafio4-net` (se ainda não existir).
- Constrói as imagens `desafio4-service-a` e `desafio4-service-b`.
- Inicia o serviço A mapeando `localhost:5000` para a API de usuários.
- Inicia o serviço B mapeando `localhost:5001` e apontando a variável `SERVICE_A_HOST` para `service-a`.

Testes rápidos:

- `curl http://localhost:5000/users` → retorna a lista de usuários.
- `curl http://localhost:5001/report` → retorna mensagens como “Usuário X ativo desde ...”.
