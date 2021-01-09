import streamlit as st
import pandas as pd

alimentos = pd.read_csv('alimentos.csv')
description = alimentos['description'].unique()

atv_fisica = pd.read_csv('atividades.csv')

st.title('Athetic Fit')

st.title('Um pouco sobre voce:')

idade = st.number_input('Qual e a sua idade?', value=0)

peso = st.number_input('Qual o seu peso ?', value=0)

altura = st.number_input('Qual e a sua altura?', value=0)

sexo = st.selectbox('Qual e o seu sexo?', ['F', 'M'])

def repouso(idade, peso, altura, sexo):
    repouso = 0

    if sexo == 'F':
        if idade >= 10 and idade < 18:
            repouso = 12.2 * peso + 746
        elif idade >= 18 and idade < 30:
            repouso = 14.7 * peso + 496
        elif idade >= 30 and idade < 60:
            repouso = 8.7 * peso + 829
        elif idade >= 60:
            repouso = 10.5 * peso + 596
            
    elif sexo == 'M':
        if idade >= 10 and idade < 18:
            repouso = 17.5 * peso + 651
        elif idade >= 18 and idade < 30:
            repouso = 15.3 * peso + 679
        elif idade >= 30 and idade < 60:
            repouso = 8.7 * peso + 879
        elif idade >= 60:
            repouso = 13.5 * peso + 487
    
    return repouso

calorias_repouso = repouso(idade, peso, altura, sexo)
st.write(calorias_repouso)

st.title('Como voce se alimentou hoje ?')

options = st.multiselect('Selecione o seu cafe da manha:', description)
mask = alimentos['description'].isin(options)
kcal = 0
kcal += alimentos.loc[mask, 'kcal'].sum()
kcal

st.write('You selected:', options)

options = st.multiselect('Selecione o seu almoco:', description)
mask = alimentos['description'].isin(options)
kcal += alimentos.loc[mask, 'kcal'].sum()
kcal

st.write('You selected:', options)

options = st.multiselect('Selecione o seu lanche da tarde:', description)
mask = alimentos['description'].isin(options)
kcal += alimentos.loc[mask, 'kcal'].sum()
kcal

st.write('You selected:', options)

options = st.multiselect('Selecione o seu jantar:', description)
mask = alimentos['description'].isin(options)
kcal += alimentos.loc[mask, 'kcal'].sum()
kcal

st.write('You selected:', options)
st.write('Soma de calorias:', kcal)


diferenca = kcal - calorias_repouso
if diferenca < 0:
   st.title(f' Parabéns você economizou {-diferenca} calorias') 
elif diferenca == 0:
    st.title('Parabéns você consumiu extamente as calorias necessárias')
elif diferenca > 0:

    st.title('Ops, calorias sobrando ?')
    st.write(f' Existe {diferenca} calorias ingeridas a mais')



st.title('Calma, vamos praticar exercicios ?')

Atividade = st.selectbox('Atividade',['Correr', 'Andar de bicicleta', 'nadar'])

def convert_hour (hour):
    return f'{int(hour)}h:{int(round((hour%1)*60))}'

atv_fisica['calorias'] = atv_fisica['calorias'].apply(lambda x: float(x.replace(',', '.').replace (' kcal/min', '')))   

if st.button('atualizar'):
    nome_atv = atv_fisica.sample(1)['atv_fisica'].values[0]
    calorias_atv = atv_fisica.sample(1)['calorias'].values[0]
    horas =convert_hour( (diferenca/60)/calorias_atv)

    st.write (f' Você precisa realizar {horas} de {nome_atv}')

st.sidebar.title('Athletic Fit')

st.sidebar.selectbox('O Athletic Fit foi construido para ajudar a queimar as calorias extras e a manter a sua saude em equilibrio', ['Saiba mais', 'Entre em contato'])
