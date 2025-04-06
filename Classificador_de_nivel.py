nome_heroi = "Bob Esponja"
xp = 0


niveis = {
    "Ferro": "🪨",
    "Bronze": "🥉",
    "Prata": "🥈",
    "Ouro": "🥇",
    "Pratina": "✨",
    "Ascendente": "🚀",
    "Imortal": "💀",
    "Radiante": "🌟"
}


while xp < 11000:
    print(f"\n🎮 {nome_heroi} tem {xp} de XP.")
    
    
    if xp <= 1000:
        nivel_atual = "Ferro"
    elif xp <= 2000:
        nivel_atual = "Bronze"
    elif xp <= 5000:
        nivel_atual = "Prata"
    elif xp <= 7000:
        nivel_atual = "Ouro"
    elif xp <= 8000:
        nivel_atual = "Pratina"
    elif xp <= 9000:
        nivel_atual = "Ascendente"
    elif xp <= 10000:
        nivel_atual = "Imortal"
    elif xp >= 10001:
        nivel_atual = "Radiante"

    
    emoji = niveis[nivel_atual]
    print(f"🏅 Nível atual: {nivel_atual} {emoji}")
    
    
    print("\nMissões:")
    print("1 - Eliminar Slime (+500 XP)")
    print("2 - Coletar ervas (+300 XP)")
    print("3 - Fugir de batalha (+0 XP)")
    
    escolha = input("Escolha uma missão (1, 2 ou 3): ")

    if escolha == "1":
        xp += 500
        print("✅ Você derrotou um Slime e ganhou 500 XP!")
    elif escolha == "2":
        xp += 300
        print("🌿 Você coletou ervas e ganhou 300 XP!")
    elif escolha == "3":
        print("😅 Você fugiu e não ganhou XP.")
    else:
        print("❌ Opção inválida! Tente de novo.")


print(f"\n🌟 O heroi de nome {nome_heroi} está no nível de {nivel_atual} {emoji}")