# diario-oficial-rag

Perguntas e respostas sobre diários oficiais: o projeto baixa as publicações, extrai as informações que estão soltas no meio do texto e permite perguntar sobre elas em linguagem natural.

> **Status:** em construção. É um projeto de aprendizado — o objetivo é ter o fluxo completo funcionando de ponta a ponta.

---

## O problema

Diário oficial é público, mas é publicado como um bloco corrido de texto, sem formatação consistente. Achar uma nomeação, um contrato ou uma decisão específica significa ler página por página na mão.

Este projeto transforma esse texto bruto em algo pesquisável.

---

## Como funciona

1. **Coleta** — baixa as publicações e guarda o texto bruto
2. **Extração** — identifica campos estruturados (datas, nomes, número do ato, categoria) com expressões regulares
3. **Divisão e indexação** — quebra o texto em trechos menores e guarda cada um em um banco vetorial, que permite buscar por significado e não só por palavra exata
4. **Resposta** — recupera os trechos relacionados à pergunta e entrega ao modelo de linguagem, que redige a resposta citando a publicação de origem

As etapas 2 e 3 são o que tornam a etapa 4 confiável: o modelo responde apenas a partir do texto que foi recuperado, em vez de inventar.

---

## Tecnologias

| | |
| --- | --- |
| Linguagem | Python |
| API | FastAPI |
| Banco vetorial | Qdrant |
| Container | Docker |

---

## Roadmap

- [ ] Coleta e armazenamento do texto bruto
- [ ] Extração de campos com regex
- [ ] Divisão do texto e indexação no banco vetorial
- [ ] Endpoint de busca
- [ ] Endpoint de pergunta e resposta com citação da fonte
- [ ] Configuração com Docker
- [ ] Testes

---

## Rodando localmente

As instruções entram aqui quando a primeira versão estiver funcionando de ponta a ponta.

---

## Licença

MIT
