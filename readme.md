# API RESTful: Casa Inteligente (Sensores de Clima)
## unibh -- campus Estoril
Esta é uma API educacional desenvolvida em Python com o micro-framework Flask. O projeto simula o *backend* de uma arquitetura de Internet das Coisas (IoT), gerenciando o recebimento e a consulta de dados de sensores de clima distribuídos.

Para fins didáticos, esta versão utiliza **armazenamento em memória** (estruturas de lista do Python). Os registros não são persistidos em banco de dados e serão reiniciados sempre que o servidor for desligado.

## 🛠️ Tecnologias e Pré-requisitos

* **Python 3.x**
* **Flask** (Micro-framework web)

## ⚙️ Como configurar e executar

1. Clone ou baixe este repositório para a sua máquina local.
2. (Opcional) Crie e ative um ambiente virtual para isolar as dependências:
   ```bash
   python -m venv venv
   # No Windows: venv\Scripts\activate
   # No Linux/Mac: source venv/bin/activate
