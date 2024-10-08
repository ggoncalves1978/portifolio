import streamlit as st

# Cabeçalho

div1, div2, div3 = st.columns([1, 2, 10])

with div1:
    st.image('Foto.jpg', width=150)

with div3:
    st.title('Gabriel Gonçalves')
    st.write(
        """
        Olá, bem-vindo ao meu portfólio de projetos. Aqui apresento as minhas habilidades na construção de dashboards 
        e/ou aplicação web, bem como a resolução de problemas.
        """
    )

    # Seção de links sociais
    st.write("###### Me encontre em:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/gabrielgoncalves78//" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20"/>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.write("LinkedIn")

    with col2:
        st.markdown(
            """
            <a href="https://github.com/ggoncalves1978?tab=repositories" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="20"/>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.write("GitHub")

    with col3:
        st.markdown(
            """
            <a href="mailto:gabrielgoncalves@msn.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="20"/>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.write("E-mail")
    
    with col4:
        st.markdown(
            """
            <a href="https://wa.me/5511982120200" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="20"/>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.write("WhatsApp")

st.divider()

# Portifólio
st.header('Portifólio')
st.subheader('Sobre mim')
st.write(
    """
    Atualmente, estou aprofundando meus estudos em Machine Learning, Análise de Dados e construção de Dashboards para aplicações web. 
    Com um sólido conhecimento em estatística e matemática, sou graduado em Logística e pós-graduado em Supply Chain, acumulando mais de 18 anos de experiência
    em Planejamento de Demanda e gestão de estoque na área da saúde. Durante minha carreira, desenvolvi um grande interesse por dados ao perceber o impacto que análises avançadas 
    podem ter na otimização de processos. Meu objetivo é ajudar as empresas a aprimorar sua tomada de decisões, fornecendo soluções baseadas em dados que 
    transformem informações em insights valiosos para promover o crescimento e a inovação.
"""
    )
st.markdown('**Habilidades Técnicas:**')
import streamlit as st

st.markdown("""
- Linguagem de programação: Python
- Análise de dados: Excel / Python: utilizando Pandas, Numpy entre outras.
- Dashboard: Power BI / Python utilizando Streamlit e Plotly Dash.
""")


st.divider()

# Projetos
st.header('Projetos')
st.subheader('Dashboard - aplicações web')

# Câmara dos Deputados
with st.expander('## Dash - Câmara dos Deputados'):
    col11, col22 = st.columns([0.25, 0.75])
    with col11:
        logo_camara = st.image('image/logo_camara.png', width=150)
    
    with col22:
        foto_camara = st.image('image/foto_camara.png', width=280, use_column_width=True)
    
    st.markdown("""
    ### Câmara dos Deputados - Aplicação Web
    
    Este projeto consiste na construção de uma aplicação web interativa utilizando o framework [Streamlit](https://streamlit.io), 
    com dados extraídos da [API Dados Abertos da Câmara dos Deputados](https://dadosabertos.camara.leg.br/). 
    O principal objetivo da aplicação é permitir o acompanhamento detalhado dos gastos de cada partido e parlamentar, 
    com a flexibilidade de aplicar filtros por ano, partido e deputado.
    """)

    st.markdown("""
    ### Funcionalidades
    
    - **Visualização Dinâmica de Gastos**: Acompanhe os gastos por partido e/ou parlamentar com gráficos interativos.
    - **Filtros Inteligentes**: Ao selecionar um partido, o filtro de deputados exibe automaticamente apenas os parlamentares pertencentes ao partido escolhido, proporcionando uma experiência de navegação mais ágil e precisa.
    - **Gráficos Interativos**: Os gráficos foram criados utilizando a biblioteca [Plotly Express](https://plotly.com/python/plotly-express/), garantindo máxima interatividade e visualização rica em detalhes.
    - **Personalização de Estilo**: Incluímos um arquivo CSS para permitir a customização da paleta de cores, adaptando o design da aplicação às preferências do usuário.
    """)

    st.markdown("""
    ### Análise de Dados
    
    Todo o processo de extração, análise, formatação e exploração dos dados (EDA - Análise Exploratória de Dados) 
    foi realizado no notebook `Analise_cdf.ipynb`, que está disponível neste repositório. Nele, você pode acompanhar cada etapa 
    do tratamento dos dados e entender as principais decisões que guiaram o desenvolvimento da aplicação.
    """)

    st.markdown("""
    ### Estrutura do Projeto
    
    - `app.py`: Código principal da aplicação Streamlit.
    - `Analise_cdf.ipynb`: Notebook com a análise de dados, limpeza, transformação e criação de insights.
    - `style.css`: Arquivo CSS que permite a personalização da paleta de cores da aplicação.
    - `requirements.txt`: Lista das dependências necessárias para a execução do projeto.
    """)

    st.markdown("""
    ### Fonte de Dados
                
    - `API Dados Abertos da Câmara dos Deputados`: Todos os dados utilizados nesta aplicação foram obtidos através da API oficial da Câmara dos Deputados. 
            Para mais informações, consulte a documentação oficial em https://dadosabertos.camara.leg.br/.
    """)

    st.markdown('Visualize o projeto: [clique aqui](https://ggoncalves1978-camara-deputados-app-deputados-baeaah.streamlit.app/)')
    st.markdown('Github: [clique aqui](https://github.com/ggoncalves1978/camara_deputados/tree/main)')

# Balança comercial
with st.expander('## Dash - COMEX | Balança Comercial'):
    col11, col22 = st.columns([0.25, 0.5])
    with col11:
        logo_camara = st.image('image/brasao.png', width=150)
    
    with col22:
        foto_camara = st.image('image/OIP.jpg', width=220, use_column_width=True)

    # Título e descrição do projeto
    
    st.markdown("""
    ### Dash_Comex
    Aplicação web interativa, construída com Streamlit e Python, para visualização e análise da balança comercial brasileira. 
    O projeto utiliza dados abertos e permite explorar indicadores como exportações, importações e saldo comercial ao longo do tempo.
    """)

    st.markdown("""
    ### COMEX - Análise da Balança Comercial Brasileira
    Este projeto tem como objetivo fornecer uma análise detalhada da balança comercial brasileira, utilizando dados históricos e ferramentas de visualização de dados. 
    Através de uma interface web interativa, desenvolvida com o Streamlit, é possível explorar os principais indicadores do comércio exterior brasileiro, como:
    """)

    st.markdown("""
    - **Evolução da balança comercial ao longo do tempo**: Gráficos de linha e barras que demonstram a variação percentual entre exportações e importações, além do saldo da balança comercial.
    - **Composição do comércio exterior**: Tabelas detalhadas que apresentam os principais produtos exportados e importados, agrupados por NCM (Nomenclatura Comum do Mercosul).
    - **Filtros interativos**: O usuário pode selecionar diferentes períodos para analisar a evolução dos indicadores ao longo do tempo.
    """)

    # Tecnologias utilizadas
    st.markdown("""
    ### Tecnologias Utilizadas
    - **Python**: Linguagem de programação para análise de dados e desenvolvimento web.
    - **Pandas**: Biblioteca para manipulação e análise de dados.
    - **Streamlit**: Framework para criação de aplicações web interativas.
    - **Plotly**: Biblioteca para criação de gráficos interativos.
    """)

    st.markdown('Visualize o projeto: [clique aqui](https://ggoncalves1978-dash-comex-balanca-comercial-zyzunr.streamlit.app//)')
    st.markdown('Github: [clique aqui](https://github.com/ggoncalves1978/Dash_Comex/tree/main)')

st.divider()
st.subheader('Machine Learning')
with st.expander('Em desenvolvimento'):
    st.subheader('xxx')

st.divider()
st.subheader('Outros Projetos')
with st.expander('Em desenvolvimento'):
    st.subheader('xxx')