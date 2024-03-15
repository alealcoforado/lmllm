import random
import csv

def get_method_resolution(resolution_method_file: str):
    method_file = open(resolution_method_file, newline='')
    description = method_file.read()
    method_file.close()
        
    return description


def get_train_clues(resolution_method_name: str, amount: int):
    train_clues = []
    with open('base.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            if row[resolution_method_name] == "1":
                train_clues.append(row["prompt"])
    
    return random.sample(train_clues, amount)

def first_prompt(clue: str):
    text = "Estamos jogando um jogo chamado ''caça ao tesouro'' da Escola Politécnica da USP, onde recebemos uma pista em formato de enigma e devemos decodifidar a mensagem da pista, que geralmente remete a conceitos e/ou direto a localizações dentro da USP (campus CUASO). Nós passamos de etapa no jogo quando encontramos um pequeno papel, cujo conteúdo será a próxima pista, em um lugar da USP. Costumamos chamar o local de ''macro''  (por exemplo, Rua do Matão, Prédio da História e Geografia da FFLCH, Centro de Difusão Internacional (CDI)...), e o local específico onde o papel será encontrado de ""micro"" (por ex, extintor de incêndio, Praça do Cavalo, ou o ""totem"" que contém o nome do Instituto).  É muito comum que partes da resolução da pista remetam a eventos ou personagens históricos ou fictícios. Em geral, as associações serão com elementos de cultura ''pop'', isto é, elementos que sejam reconhecíveis por adultos de 20 a 25 anos, principal faixa dos participantes da caça ao tesouro. Quando necessário, você deve buscar na web por informações históricas de pessoas, eventos ou lugares que tenham alguma relação com a USP.\n"
    text += "Abaixo estarão algumas pistas e o exemplo de resolução da pista, junto com o macro e o micro onde o papel seguinte foi encontrado.\n"
    text += "||Pista: やめて！これが私の家, え? そうではない! | Explicação: やめて！ = Pare! ; これが私の家, え? = Kore ga watashinoie, e? > Jogo sonoro para IEE ao final da frase. そうではない! é uma negação, dizendo que não, esta não é minha casa (ou seja, não é CCJ) | Macro: IEE | Micro: Placa de Pare\n"
    text += "||Pista: O meu irmão vive junto ao descobridor, já eu tenho uma grande paixão pelo mar | Explicação: Descobridor = Pedro Alvares Cabral - Na avenida Pedro Alvares tem o MAC - USP do ibirapuera. Paixão pelo mar = ultramarinho (obra no mac). | Macro: MAC | Micro: Ultramarino\n"
    text += "||Pista: Se o peixe do sr. hacker fosse nativo brasileiro ele entenderia ecgh>iecfaei | Explicação: Sr. Hacker -> Mr. Robot, o peixe dele chama QWERTY. Existe um teclado chamado BR-Nativo. Fazendo a conversão da ''sobre as ondas''. (podemos mudar o lugar se quiser) | Macro: Bio | Micro: Edificio ''Sobre as Ondas''\n"
    text += "||Pista: Entre o marechal e a república, ele nos deu a obra de sua linha do seu ritmo e vibração | Explicação: Entre as estações Marechal Deodoro e Republica é a estação Santa Cecilia do metro. Trilho, Ritmo e Vibração é uma arte do Caciporé Torres nesta estação. Rei é para indicar que é a escultura do Torres que esta na Reitoria. | Macro: Reitoria Nova | Micro: ''AConstrução''/Caciporé Torres\n"
    text += "||Pista: Olhando a família e educação é notável que uma Boa Ideia do MEC passou a infância e adolescência entre a capital e a bela chuva | Explicação: Boa ideia leva a 51. O 51º ministro do MEC é José Mendonça B. Filho. Olhando o perfil dele no wikipedia na seção ''famila e edcucação'' a frase está ''viveu entre a capitão e belo jardim''. Jardim + Chuva | Macro: Hidráulica | Micro: Jardim de Chuva\n"
    text += "||Pista: casoEnsolarado | Explicação: A pista está escrita em camelCase, Ensolarado leva a FAU. Camelo é sinonimo para bicicleta em vários estados do Brasil. | Macro: FAU | Micro: Bicicletário\n"
    text += "||Pista: Zero a esquerda e 1308 donas? Menos... com um zero a esquerda só cinquenta bastam | Explicação: 01308-050 CEP - Rua Dona Adma Jafet - > Auditório na Física | Macro: IF | Micro: Auditório Adma Jafet\n"
    text += "A pista atual está abaixo. Raciocine passo-a-passo, buscando informações na web se julgar necessário, e vamos tentar gerar uma explicação que remeta a um Macro e um Micro onde deveremos procurar o papel com a próxima pista. Lembre-se que é incomum que haja redundância nos trechos da pista. Ou seja, se uma parte da pista remete ao Macro, provavelmente essa mesma parte não remete também ao Micro. Da mesma forma se uma parte já remete ao Macro, a outra parte provavelmente remete ao Micro ou a uma info auxiliar que confirme o Macro. Se precisar, pode me fazer perguntas para que eu explique algumas siglas ou qualquer outra coisa que achar necessário.\n"
    
    text += f"||Pista: {clue}"
    
    return text


def second_prompt(clue: str, resolution_index: int):
    resolution_method_details = resolution_methods[resolution_index]
    description = get_method_resolution(resolution_method_details["method_file"])
    train_clues = get_train_clues(resolution_method_details["column"], 5)
    
    text = "Vamos aprofundar nosso raciocínio. Baseado no que falamos anteriormente, vamos investigar o método de resolução abaixo:"
    text += description
    text += "\nAbaixo, seguem alguns exemplos que usam este mesmo método de resolução"
    text += "\n".join(train_clues)
    text += "A pista atual está abaixo. Raciocine passo-a-passo, buscando informações na web se julgar necessário, e vamos tentar gerar uma explicação que remeta a um Macro e um Micro onde deveremos procurar o papel com a próxima pista. Lembre-se que é incomum que haja redundância nos trechos da pista. Ou seja, se uma parte da pista remete ao Macro, provavelmente essa mesma parte não remete também ao Micro. Da mesma forma se uma parte já remete ao Macro, a outra parte provavelmente remete ao Micro ou a uma info auxiliar que confirme o Macro. Se precisar, pode me fazer perguntas para que eu explique algumas siglas ou qualquer outra coisa que achar necessário.\n"
    text += f"||Pista: {clue}"
    
    return text

def third_prompt():
    text = "Sintetize as hipóteses levantadas até aqui, e escreva SOMENTE um vetor (python list) de JSONs com chaves 'macro', 'explicação' (resumida) e 'micro' (quando houver)"
    
    return text

resolution_methods = [
    {
        "column": "1-jogo-de-palavras-anagrama-cacofonia", 
        "method_file": "methods/method_0.txt",
        "result_file": "results/jogo-de-palavras.txt"
    },
    {
        "column": "2-ref-visual-observavel-team-rua", 
        "method_file": "methods/method_1.txt",
        "result_file": "results/ref-visual.txt"
    },
    # {
    #     "column": "3-criptografia", 
    #     "method_file": "methods/method_2.txt",
    #     "result_file": "results/criptografia.txt"
    # },
    {
        "column": "4-ref-historica-mitologia", 
        "method_file": "methods/method_3.txt",
        "result_file": "results/ref-historica.txt"
    },
    {
        "column": "5-cultura-pop-conhecimento-geral", 
        "method_file": "methods/method_4.txt",
        "result_file": "results/cultura-pop.txt"
    },
    {
        "column": "6-ref-interna-cidade-universitaria", 
        "method_file": "methods/method_5.txt",
        "result_file": "results/ref-interna.txt"
    },
    {
        "column": "7-ref-externa-campus", 
        "method_file": "methods/method_6.txt",
        "result_file": "results/ref-externa.txt"
    },
    {
        "column": "8-caminho-trajetória-roteiro", 
        "method_file": "methods/method_7.txt",
        "result_file": "results/caminho.txt"
    },
    {
        "column": "10-busca-listas-elencaçoes-clusters", 
        "method_file": "methods/method_9.txt",
        "result_file": "results/listas.txt"
    },
    # {
    #     "column": "11-links-site-integra-daquele-ano", 
    #     "method_file": "methods/method_10.txt",
    #     "result_file": "results/site.txt"
    # }
]



def get_prompt(clue: str, resolution_index: int, position: int):
    if position == 0:
        return first_prompt(clue)
    if position == 1:
        return second_prompt(clue, resolution_index)
    if position == 2:
        return third_prompt()
    return third_prompt()


def mount_user_prompt(clue, resolution_index, i,interface='anthropic'):
    if interface=='anthropic':
        
        return {
            "role": "user",
        "content": [
            {
                "type": "text",
                "text": get_prompt(clue, resolution_index, i)
            }
        ]
        }
    elif interface=='openai':
        mess = {'role': 'user', 'content': get_prompt(clue, resolution_index, i)}
        return mess



def mount_assistant_prompt(new_response,interface='anthropic'):
    if interface=='anthropic':
            
        return {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": get_response_text(new_response)
                }
            ]
        }
    elif interface=='openai':
        mess = {'role': 'assistant', 'content': get_response_text(new_response)}
        return mess



def get_response_text(response,interface='anthropic'):
    if interface=='anthropic':
        return response.content[0].text
    elif interface=='openai':
        return response.choices[0].message.content



# def get_prompt_dict_text_answer(prompt):
#     if (isinstance(prompt, str)):
#         return prompt
#     return prompt["content"][0]["text"]