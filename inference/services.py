# Install transformers from source - only needed for versions <= v4.34
# pip install git+https://github.com/huggingface/transformers.git
# pip install accelerate

from models import PlayerInfo
import torch
from transformers import pipeline, AutoModelForCausalLM,AutoTokenizer
from peft import PeftModel

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

def get_recommandation_prompt_tunig(player_infos: PlayerInfo):
    content = (f"On considere un joueur de football evoluant au post {player_infos.position}, "
    f"qui a joué {player_infos.nbr_matchs_played} matchs "
    f"avec {player_infos.nbr_scored_goals} buts inscrits et {player_infos.nbr_assist} passes decisives."
    f"Peux tu me donner des recomandations pour les questionements suivants: "
    "1) Le poste du joueur est-il adapté par rapport a ses statistiques ? Sinon recommande un poste "
    "2) Quels exercices physique doit-il faire pour améliorer ses statistiques ?")

    # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
    messages = [
        {
            "role": "system",
            "content": "En tant qu'expert en analyse de statistques de football, repond de facon concise aux questionement d'un coach",
        },
        {"role": "user", "content": content},
    ]
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=512, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    output = outputs[0]["generated_text"].split("<|assistant|>")[-1].split("\n")
    print(output)
    return output
    # <|system|>
    # You are a friendly chatbot who always responds in the style of a pirate.</s>
    # <|user|>
    # How many helicopters can a human eat in one sitting?</s>
    # <|assistant|>
    # ...
def get_recommandation_fine_tunig(player_infos: PlayerInfo):
    base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, padding_side="right",)
    tokenizer.pad_token = tokenizer.eos_token

    base_model = AutoModelForCausalLM.from_pretrained(base_model_name)
    model = PeftModel.from_pretrained(base_model,"/workspaces/TestTecnique/finetuning/recomandation_joueur")
    txt = (f"""<|system|>
                En tant qu'expert en analyse de statistques de football dis moi le poste du joueur est adapté et recommande des exercises physique pour ammeliorer ses perfomances.</s>
               <|user|>
                Ce joueur a {player_infos.age} ans et évolue au poste de {player_infos.position}. Il a disputé {player_infos.nbr_matchs_played} matchs, marqué {player_infos.nbr_scored_goals} but(s) et délivré {player_infos.nbr_assist} passe(s) décisive(s).</s>
               <|assistant|>
    
                    """)
    tokens = tokenizer(txt, return_tensors="pt")['input_ids'].to("cpu")
    op = model.generate(tokens, max_new_tokens=200)
    output = tokenizer.decode(op[0]).split("<|assistant|>")[-1].split("\n")
    print(output)
    return output