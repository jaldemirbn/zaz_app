import streamlit as st


# ===============================
# STATES
# ===============================
def _init_states():

    defaults = {
        "aceite_termos": False,
        "aceite_privacidade": False,
        "abrir_termos": False,
        "abrir_privacidade": False,
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ===============================
# DIALOGS
# ===============================
@st.dialog("Termos de Uso", width="large")
def dialog_termos():



    #===========================================
    # TERMO DE USO
    #===========================================
    st.markdown("""
    ## Bem-vindo ao **zAz**.

Estes Termos de Uso estabelecem as regras, direitos e responsabilidades aplicáveis ao acesso e utilização da plataforma.

Ao criar uma conta ou utilizar o sistema, você declara que leu, compreendeu e concorda integralmente com os termos abaixo.

Se você não concordar, não utilize o serviço.

---

## 1. Sobre o serviço

O zAz é uma aplicação web que utiliza inteligência artificial para auxiliar na criação de conteúdo digital, incluindo:

• geração de ideias  
• headlines  
• descrições visuais  
• legendas  
• imagens conceituais  
• planejamento estratégico de conteúdo  

O serviço é fornecido como ferramenta de apoio criativo.

---

## 2. Aceitação dos termos

Ao acessar, cadastrar-se ou utilizar o zAz, o usuário concorda automaticamente com:

• estes Termos de Uso  
• a Política de Privacidade  

O uso contínuo do sistema implica aceitação total das condições estabelecidas.

---

## 3. Cadastro e conta

Para utilizar a plataforma, o usuário deve:

• criar uma conta com email e senha válidos  
ou  
• utilizar métodos de autenticação disponibilizados pela plataforma  

O usuário é responsável por:

• manter suas credenciais seguras  
• não compartilhar sua conta  
• todas as ações realizadas em seu login  

O zAz não se responsabiliza por acessos indevidos decorrentes de negligência do usuário.

---

## 4. Uso permitido

Você concorda em utilizar o zAz apenas para fins legais e éticos.

É proibido:

• explorar falhas de segurança  
• tentar acessar contas ou dados de outros usuários  
• copiar, revender ou redistribuir a plataforma  
• utilizar o sistema para atividades ilícitas  
• sobrecarregar ou prejudicar o funcionamento do serviço  

O descumprimento pode resultar em suspensão ou encerramento da conta.

---

## 5. Conteúdo gerado

Todo conteúdo criado pelo usuário dentro da plataforma é de sua responsabilidade.

O zAz:

• não reivindica propriedade sobre o conteúdo criado  
• não se responsabiliza pelo uso feito pelo usuário  
• não garante resultados comerciais ou de desempenho  

O usuário deve respeitar direitos autorais e legislações aplicáveis.

---

## 6. Limitação de responsabilidade

O zAz é fornecido “como está”.

Não garantimos:

• resultados específicos  
• aumento de seguidores  
• conversões  
• vendas  
• desempenho financeiro  

O zAz não se responsabiliza por:

• perdas financeiras  
• decisões tomadas com base no conteúdo gerado  
• falhas temporárias  
• indisponibilidade do serviço  
• perda de dados  

O uso é de responsabilidade exclusiva do usuário.

---

## 7. Disponibilidade do serviço

A plataforma pode sofrer:

• manutenções  
• atualizações  
• melhorias  
• interrupções temporárias  

Não garantimos funcionamento contínuo e ininterrupto.

---

## 8. Propriedade intelectual

Todo o código, design, marca, identidade visual e estrutura do zAz são protegidos por direitos autorais.

É proibida:

• reprodução  
• modificação  
• distribuição  
• engenharia reversa  

sem autorização expressa.

---

## 9. Privacidade

O tratamento de dados pessoais é regido pela Política de Privacidade do zAz.

Recomendamos a leitura integral desse documento.

---

## 10. Suspensão ou encerramento de conta

O zAz poderá suspender ou encerrar contas que:

• violem estes termos  
• pratiquem uso abusivo  
• realizem atividades ilegais  
• comprometam a segurança da plataforma  

Sem necessidade de aviso prévio.

---

## 11. Alterações nos termos

Estes Termos podem ser modificados a qualquer momento para melhoria do serviço ou adequação legal.

A versão atualizada substituirá automaticamente a anterior.

O uso contínuo após alterações indica concordância.

---

## 12. Contato

Para dúvidas, suporte ou solicitações:

📧 contato@zaz.app

---

**Ao utilizar o zAz, você declara estar de acordo com todos os termos acima.
    """)

    aceite = st.checkbox("Aceitar termos")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_termos = True
            st.session_state.abrir_termos = False
            st.rerun()


@st.dialog("Política de Privacidade", width="large")
def dialog_privacidade():

    st.markdown("""
    ## Política de Privacidade

    Cole aqui o texto completo.
    """)

    aceite = st.checkbox("Aceitar política")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_privacidade = True
            st.session_state.abrir_privacidade = False
            st.rerun()


# ===============================
# RENDER
# ===============================
def render_cadastro(criar_usuario):

    _init_states()

    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.aceite_termos:
            st.success("✅ Termos aceitos")
        elif st.button("Aceitar os Termos de Uso"):
            st.session_state.abrir_termos = True

    with col2:
        if st.session_state.aceite_privacidade:
            st.success("✅ Política aceita")
        elif st.button("Aceitar a Política de Privacidade"):
            st.session_state.abrir_privacidade = True


    if st.session_state.abrir_termos:
        dialog_termos()

    if st.session_state.abrir_privacidade:
        dialog_privacidade()


    st.markdown("---")

    pode_criar = (
        st.session_state.aceite_termos
        and
        st.session_state.aceite_privacidade
    )

    if st.button("Criar conta", use_container_width=True, disabled=not pode_criar):
        criar_usuario(email, senha)
        st.success("Conta criada com sucesso. Faça login.")

