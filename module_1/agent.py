# Modulo 1
from google import genai
from api_key import GEMINIAPIKEY

client = genai.Client(api_key=GEMINIAPIKEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Como fazer check in no sistema ASFFGT da empresa?",
    config={
            "system_instruction": (
                "Você é um assistente corporativo com tom formal e objetivo."
                " Responda sempre em português do Brasil, de forma objetiva."
                " Não invente informações."
            ),
            "temperature": 0.6,
            #"max_output_tokens": 200
            }
)

print(response.text)
