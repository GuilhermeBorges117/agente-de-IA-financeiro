def recomendar_investimentos(perfil, produtos):
    perfil_usuario = perfil['perfil_investidor']
    
    recomendados = []
    
    for p in produtos:
        if perfil_usuario == "moderado" and p['risco'] in ["baixo", "medio"]:
            recomendados.append(p['nome'])
    
    return recomendados
