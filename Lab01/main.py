from chatbot import ChatBot


# Funcao para iniciar a conversa com chatbot, solicitacao de pergunta ao usuario com resposta, verificacao se a intencao
# é despedir para encerrrar conversa
def iniciar_conversa(chatbot):
    print("+~~~~~~~~~~~~~~~~~~~~~+")
    print("+Bem-vindo ao ChatBot!+")
    print("+~~~~~~~~~~~~~~~~~~~~~+")

    while True:
        pergunta = input("\nChatBot: Bem vindo! Como posso ajudar?\n")
        resposta, intencao = chatbot.chatbot_response(pergunta)

        if intencao[0]['intent'] == "Despedida":
            print("ChatBot: Espero ter ajudado! Volte se surgirem mais dúvidas!")
            break

        if intencao[0]['intent'] == "EtapasPIPE":
            print("ChatBot: " + resposta + " [" + intencao[0]['intent'] + "]")
            etapas = input("Gostaria de saber mais sobre qual fase? \n Digite 1) Fase 1\n Digite 2) Fase 2\n Digite 3) "
                           "Fase 3 \n")
            if etapas == "1":
                resposta = ("Fase 1: é destinada à verificação da viabilidade técnico-científica da proposta, (duração "
                            "de até 9 meses e orçamento de até R$ 300.000, mais Reserva Técnica e Benefícios "
                            "Complementares).\n Essa fase não é obrigatória, a empresa pode submeter uma proposta "
                            "diretamente para a Fase 2.")
            elif etapas == "2":
                resposta = (" Fase 2: destina-se à execução da pesquisa propriamente dita (duração de até 24 meses e "
                            "orçamento de até R$ 1.500.000, mais Reserva Técnica e Benefícios Complementares);.\nA "
                            "empresa pode submeter uma proposta diretamente para essa fase. ")
            elif etapas == "3":
                resposta = (" Fase 3: Desenvolvimento comercial e industrial dos produtos, processos, sistemas e/ou "
                            "serviços inovadores obtidos a partir de pesquisas anteriores realizadas pela pequena "
                            "empresa sem o apoio da FAPESP ou a partir de pesquisa apoiada no âmbito do PIPE ")
            else:
                resposta = "Desculpe, não entendi o que você quis dizer."

        print("ChatBot: " + resposta + " [" + intencao[0]['intent'] + "]")


# Funcao principal para execucao do chatbot, criando uma instancia, modelo do chatbot e chamando funcao iniciar_conversa
def main():
    myChatBot = ChatBot()
    myChatBot.createModel()

    iniciar_conversa(myChatBot)


if __name__ == "__main__":
    main()