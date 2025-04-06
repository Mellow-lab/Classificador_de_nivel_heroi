# 🛡️ Classificador de Nível de Herói

Projeto de desafio prático da **DIO (Digital Innovation One)**, com o objetivo de aplicar os conceitos fundamentais da programação: **variáveis**, **operações matemáticas**, **laços de repetição** e **estruturas de decisão**.  

O projeto na qual eu fiz umas pequenas alterações simula um pequeno jogo de RPG, onde um herói ganha **XP (experiência)** realizando missões e sobe de nível de acordo com sua pontuação.

---

## 💻 Tecnologias usadas

- Linguagem: **Python 3**
- Execução: Terminal / Console

---

## 📌 Regras do sistema de níveis

| Faixa de XP     | Nível       | Emoji   |
|----------------|-------------|---------|
| 0 - 1000       | Ferro       | 🪨      |
| 1001 - 2000    | Bronze      | 🥉      |
| 2001 - 5000    | Prata       | 🥈      |
| 5001 - 7000    | Ouro        | 🥇      |
| 7001 - 8000    | Pratina     | ✨      |
| 8001 - 9000    | Ascendente  | 🚀      |
| 9001 - 10000    | Imortal     | 💀      |
| 10001+          | Radiante    | 🌟      |

---

## 🎮 Como funciona

- O usuário inicia com XP igual a 0.
- Em cada rodada, ele escolhe uma missão:
  - Eliminar Slime → +500 XP
  - Coletar ervas → +300 XP
  - Fugir da batalha → +0 XP
- O jogo continua até o herói atingir o nível máximo (Radiante).

---

## 📷 Exemplo de execução

```bash
🎮 Bob esponja tem 1500 de XP.
🏅 Nível atual: Bronze 🥉

Missões:
1 - Eliminar Slime (+500 XP)
2 - Coletar ervas (+300 XP)
3 - Fugir de batalha (+0 XP)

Escolha uma missão (1, 2 ou 3):
 
