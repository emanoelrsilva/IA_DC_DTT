# Modulo 1
from google import genai
from api_key import GEMINIAPIKEY
from prompt import prompt_agent_module_1

client = genai.Client(api_key=GEMINIAPIKEY)


print("Bem Vindo ao Assitente ASP!!!")
request = input("Digite sua dúvida (ou 'sair' para encerrar) => ")

while request.lower() != "sair":
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=request,
        config={
                "system_instruction": (
                    prompt_agent_module_1
                ),
                "temperature": 0.6,
                #"max_output_tokens": 200
                }
    )
    print(response.text)
    request = input("Digite sua dúvida (ou 'sair' para encerrar) => ")

print("Até Mais!")


