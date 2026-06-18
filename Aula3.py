# importar as libs

from datetime import timedelta
import streamlit as st
import pandas as pd
import yfinance as yf 


def main():
    print("Hello from curso-hashtag!") 
       

    # criar as funções de carregamento de dados
    @st.cache_data
    def carregar_dados(empresas):
        texto_tickers = " ".join(empresas)
        dados_acao = yf.Tickers(texto_tickers)
        cotacoes_acao = dados_acao.history(start="2025-01-01", end="2026-06-18" ) #"YYYY-MM-DD"
        print(cotacoes_acao)
        cotacoes_acao = cotacoes_acao["Close"] #a função tickers já retorna um Dataframe
        return cotacoes_acao

    acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "WEGE3.SA"]

    dados = carregar_dados(acoes)
    print(dados)

    # preparar as visualizações

    st.write("""
    # App Preço de ações
    O gráfico abaixo representa a evolução do preço das ações ao longo dos anos
             """)#markdown
    
    #prepara as vizualizações = filtro
    st.sidebar.header("Filtros")

    #Filtro de ações
    lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", dados.columns)
    print(lista_acoes)
    if lista_acoes:
        dados = dados[lista_acoes]
        if lista_acoes.__len__() ==1:
            acao_unica = lista_acoes[0]
            dados = dados.rename(columns={acao_unica: 'Close'})

    #filtro de Datas
    data_inicial = dados.index.min().to_pydatetime()
    data_final = dados.index.max().to_pydatetime()
    intervalo_data = st.sidebar.slider("Selecione o período", min_value=data_inicial , max_value=data_final, value=(data_inicial, data_final), step=timedelta(days=1))
    print(intervalo_data)

    dados = dados.loc[intervalo_data[0]: intervalo_data[1]]

    #Criar o gráfico

    st.line_chart(dados)

    
    
    st.write("""
    # Fim do app
             """)

    # criar a interface




if __name__ == "__main__":
    main()
