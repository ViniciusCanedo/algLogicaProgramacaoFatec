def verificar_endereco_ip(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or int(parte) < 0 or int(parte) > 255:
            return False
    return True


arquivo_entrada = "entrada.txt"
arquivo_saida = "relatorio_enderecos_ip.txt"

enderecos_validos = []
enderecos_invalidos = []

with open(arquivo_entrada, "r") as file:
    for linha in file:
        ip = linha.strip()
        if verificar_endereco_ip(ip):
            enderecos_validos.append(ip)
        else:
            enderecos_invalidos.append(ip)

with open(arquivo_saida, "w") as file:
    file.write("[Endereços válidos:]\n")
    for endereco in enderecos_validos:
        file.write(endereco + "\n")
    file.write("\n[Endereços inválidos:]\n")
    for endereco in enderecos_invalidos:
        file.write(endereco + "\n")

print("Relatório gerado com sucesso no arquivo:", arquivo_saida)
