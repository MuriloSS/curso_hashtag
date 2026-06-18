def main():
    print("Hello from curso-hashtag!")

    # importar as libs
    import streamlit as st
    import pandas as pd
    import yfinance as yf    

    # criar as funções de carregamento de dados
    @st.cache_data
    def carregar_dados(empresa):
        dados_acao = yf.Ticker(empresa)
        cotacoes_acao = dados_acao.history(start="2025-01-01", end="2026-06-18" ) #"YYYY-MM-DD"
        cotacoes_acao = cotacoes_acao[["Close"]] # [Series do pandas(Array)], [[Dataframe]]
        return cotacoes_acao

    dados = carregar_dados('ITUB4.SA')
    print(dados)

    # preparar as visualizações

    st.write("""
    # App Preço de ações
    O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
             """)#markdown
    
    #Criar o gráfico

    st.line_chart(dados)

    
    
    st.write("""
    # Fim do app
             """)

    # criar a interface




if __name__ == "__main__":
    main()
