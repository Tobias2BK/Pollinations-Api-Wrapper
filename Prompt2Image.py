import tls_client
import random
from urllib.parse import quote_plus
import base64

class Client:
    def __init__(self):
        self.session = tls_client.Session(
            client_identifier="chrome112",
            random_tls_extension_order=True
        )

    def generate_image(
        self,
        model: str = 'dall-e-3',
        prompt: str = None,
        size: str = '1024x1024',
        seed: int = None,
        nologo: bool = True,
        private: bool = False,
        enhance: bool = False,
        safe: bool = False,
        response_format: str = 'url',
        **kwargs
    ):  
        if not prompt:
            return ("Please input a prompt")
        
        if seed is None:
            seed = random.randint(int(1e8), int(1e10) - 1)

        if model not in ["dall-e-3",'flux-pro','sdxl-turbo']:
            print(f"Unable Model: {model}\n"
                  "Falling back to 'dall-e-3' model.")
            model = 'dall-e-3'
        
        prompt = quote_plus(prompt.strip())

        try:
            width,height = map(int,size.split('x'))
        except ValueError:
            return "Invalid size. Format must be 'WIDTHxHEIGHT' (eg 1024x1024)"
        
        url = (
            f"https://image.pollinations.ai/prompt/{prompt}"
            f"?width={width}&height={height}&model={model}"
            f"&nologo={str(nologo).lower()}"
            f"&private={str(private).lower()}"
            f"&enhance={str(enhance).lower()}"
            f"&safe={str(safe).lower()}"
            f"&seed={seed}"
        )

        try:
            r = self.session.get(url)
            if r.status_code == 200:
                if response_format == 'b64_json':
                    return {"b64_json": base64.b64encode(r.content).decode('utf-8')}
                return url
        except Exception as e:
            return f"Fail to fetch image: {str(e)}"

    
print(Client().generate_image(prompt="A adult girl hold a board that say 'I Love Tobi Mitchell'"))