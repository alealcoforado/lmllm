import time

try:
    from openai import AzureOpenAI
    openai_client = AzureOpenAI(
        azure_endpoint = 'YOUR_AZURE_ENDPOINT',
        api_key = 'YOUR_AZURE_API_KEY',
        api_version = 'YOUR_API_VERSION',
    )
except:
    print("Could not connect to Azure OpenAI client.")

def call_Assistants_API(messages, tools, model='gpt-35-turbo'):
    if tools is not None:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice='auto',
        )
    else:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools
        )
    return response


try:
    import anthropic
    anthropic_client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key= 'YOUR_API_ANTHROPIC' #
    )
except:
    print("Could not connect to Anthropic client.")

def call_Claude_API(mapped_messages,max_tokens=2000,temperature=0.7,model="claude-3-haiku-20240307"):
    try:
        response = anthropic_client.messages.create(
            system="""Estamos jogando um jogo chamado "caça ao tesouro" da Escola Politécnica da USP, onde recebemos uma pista em formato de enigma e devemos decodifidar a mensagem da pista, que geralmente remete a conceitos e/ou direto a localizações dentro da USP, no campus CUASO localizado no Butantã-SP. Nós passamos de etapa no jogo quando encontramos um pequeno papel, cujo conteúdo será a próxima pista, em um lugar da USP. Costumamos chamar o local de "macro"  (por exemplo, Rua do Matão, Prédio da História e Geografia da FFLCH, Centro de Difusão Internacional (CDI)...), e o local específico onde o papel será encontrado de "micro" (por ex, extintor de incêndio, Praça do Cavalo, ou o "totem" que contém o nome do Instituto).  É muito comum que partes da resolução da pista remetam a eventos ou personagens históricos ou fictícios. Há vários métodos de resolução para as pistas: alguns exemplos são associações com elementos de cultura "pop", isto é, elementos que sejam reconhecíveis por adultos de 20 a 25 anos; elementos ou fatos históricos, do Brasil, do mundo ou da Universidade de São Paulo, ou com mitologia (incluindo mitologia cristã/bíblia etc); jogos de palavras e/ou sons, desambiguação de siglas, ou referências diretas a localidades e/ou obras de arte internas ou externas à Cidade Universitária da USP (Butantã). Quando necessário, você deve buscar na web por informações históricas de pessoas, eventos ou lugares para tentar estabelecer essa relação ou analogia com a USP.""",
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=mapped_messages
        )
        return response
    except anthropic.APIConnectionError as e:
        print("The server could not be reached")
        print("Cause", e.__cause__)  # an underlying Exception, likely raised within httpx.
        return False
    except anthropic.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
        time.sleep(30)
        return call_Claude_API(mapped_messages)
    except anthropic.APIStatusError as e:
        print("Another non-200-range status code was received")
        print("Code", e.status_code)
        print("Message:", e.response)
        return False

def call_model(messages,interface='anthropic'):
    if interface=='anthropic':
        return call_Claude_API(messages)
    elif interface=='openai':
        return call_Assistants_API(messages)
    