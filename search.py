import requests
import argparse

def buscar_dados_ip(ip, city=False, country=False, all_data=False):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()

            if all_data or (not city and not country):
                for chave, valor in dados.items():
                    print(f"{chave.capitalize()}: {valor}")
            else:
                if city:
                    print(f"Cidade: {dados.get('city', 'Não encontrada')}")
                if country:
                    print(f"País: {dados.get('country', 'Não encontrado')}")
        else:
            print(f"Erro: {resposta.status_code} - Não foi possível obter os dados do IP.")
    except Exception as e:
        print(f"Erro ao fazer requisição: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consulta informações de um endereço IP.")
    parser.add_argument("ip", help="Endereço IP a ser consultado")
    parser.add_argument("-c", "--city", action="store_true", help="Mostra apenas a cidade do IP")
    parser.add_argument("-ct", "--country", action="store_true", help="Mostra apenas o país do IP")
    parser.add_argument("-a", "--all", action="store_true", help="Mostra todos os dados do IP")
    args = parser.parse_args()

    buscar_dados_ip(args.ip, args.city, args.country, args.all)
