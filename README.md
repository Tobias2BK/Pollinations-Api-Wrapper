# 🖼️ Prompt2Image

**Prompt2Image** is a lightweight Python client that generates AI images from text prompts using the [Pollinations API](https://pollinations.ai/).  
It supports models like `dall-e-3`, `flux-pro`, and `sdxl-turbo`, and includes features like base64 encoding, resolution control, random seed support, and more.

---

## 🚀 Features

- 🔄 Support for multiple models: `dall-e-3`, `flux-pro`, `sdxl-turbo`
- 📝 Clean and easy-to-use API
- 🧠 Random seed generation (or customizable)
- 🖼️ Output as image URL or Base64 JSON
- 🧪 No need for API key or OAuth
- ✅ Works with `tls-client` for better compatibility

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Tobias2BK/Pollinations-Api-Wrapper.git prompt2image
cd prompt2image
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
tls-client
```

---

## 💡 Usage

### 🔹 Basic Example

```python
from prompt2image import Client

client = Client()

url = client.generate_image(
    prompt="I Love Tobi Mitchell",
    model="sdxl-turbo",
    size="1024x1024"
)

print("Image URL:", url)
```

> 📷 **Example Output:**
>
> ![Example](./image/example.jpg)

---

### 🔹 Return Base64 Image

```python
from prompt2image import Client
import base64

client = Client()

image_data = client.generate_image(
    prompt="A magical forest with glowing mushrooms",
    model="flux-pro",
    response_format="b64_json"
)

```

---

### 🔹 Custom Options

```python
url = client.generate_image(
    prompt="A cyberpunk cat ",
    model="dall-e-3",
    size="512x512",
    seed=123456789,
    nologo=True,
    enhance=True,
    private=False
)
```

---

## ⚠️ Notes

- Only these models are currently supported: `dall-e-3`, `flux-pro`, `sdxl-turbo`
- Size must be in format `WIDTHxHEIGHT` (e.g., `1024x1024`)
- If no seed is provided, a random one is generated
- The API does **not** require authentication

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests are welcome! If you find bugs or want to add improvements, feel free to open an issue or submit a PR.

---

## 🌐 Links

- 🔗 [Pollinations AI](https://pollinations.ai/)
- 💬 Feel free to fork and share!
