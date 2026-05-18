from datetime import date


def avaliar_temperatura(temp: float) -> str:
    if temp < 20:
        return "Frio"
    elif temp < 40:
        return "Ideal"
    elif temp < 70:
        return "Alerta"
    else:
        return "Risco crítico"


def avaliar_cpu(uso: float) -> str:
    if uso < 40:
        return "Normal"
    elif uso <= 80:
        return "Alta"
    else:
        return "Sobrecarga"


def avaliar_memoria(mem: float) -> str:
    if mem < 50:
        return "Confortável"
    elif mem < 85:
        return "Monitorar"
    else:
        return "Crítica"


def classificar_latencia(lat: float) -> str:
    if lat < 10:
        return "Excelente"
    elif lat < 40:
        return "Boa"
    elif lat < 100:
        return "Regular"
    else:
        return "Ruim"


def avaliar_disco(espaco_livre: float) -> str:
    if espaco_livre >= 40:
        return "Seguro"
    elif espaco_livre >= 20:
        return "Atenção"
    else:
        return "Crítico"


def validar_certificado(data_emissao: str, anos: int) -> str:
    dia, mes, ano = map(int, data_emissao.split("/"))
    data_inicio = date(ano, mes, dia)
    data_expiracao = date(data_inicio.year + anos, data_inicio.month, data_inicio.day)
    hoje = date.today()
    if hoje > data_expiracao:
        return "Certificado expirado"
    elif (data_expiracao - hoje).days <= 30:
        return "Certificado expira em breve"
    else:
        return "Certificado válido"


def prever_armazenamento(inicial: float, taxa: float, anos: int) -> tuple:
    final = inicial * ((1 + taxa) ** anos)
    if final < 500:
        status = "Seguro"
    elif final < 2000:
        status = "Monitorar"
    else:
        status = "Upgrade necessário"
    return (round(final, 2), status)


def analisar_trafego(r1, r2, r3) -> tuple:
    media = (r1 + r2 + r3) / 3
    if media < 100:
        status = "Baixo tráfego"
    elif media < 500:
        status = "Tráfego moderado"
    else:
        status = "Tráfego alto"
    return (round(media, 2), status)
