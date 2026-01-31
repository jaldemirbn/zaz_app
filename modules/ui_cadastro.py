import streamlit as st
import re


# =====================================================
# STATES
# =====================================================
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


# =====================================================
# VALIDAÇÃO (ADICIONADO)
# =====================================================
def email_valido(email: str) -> bool:
    if not email:
        return False
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email) is not None


def senha_valida(senha: str) -> bool:
    return bool(senha and len(senha) >= 4)


# =====================================================
# TERMOS DE USO (COMPLETO — INTACTO)
# =====================================================
@st.dialog("Termos de Uso", width="large")
def dialog_termos():

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

📧 contato@zaz.app

---

**Ao utilizar o zAz, você declara estar de acordo com todos os termos acima.**
    """)

    aceite = st.checkbox("Aceitar termos")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_termos = True
            st.session_state.abrir_termos = False
            st.rerun()


# =====================================================
# POLÍTICA DE PRIVACIDADE (COMPLETA — INTACTA)
# =====================================================
@st.dialog("Política de Privacidade", width="large")
def dialog_privacidade():

    st.markdown("""
## A sua privacidade é importante para nós.  
Esta Política de Privacidade descreve de forma clara e transparente como o **zAz** coleta, utiliza, armazena e protege as informações de seus usuários.

Ao utilizar a plataforma, você concorda com os termos descritos abaixo.

---

## 1. Sobre o zAz

O zAz é uma aplicação web que utiliza inteligência artificial para auxiliar na criação de conteúdos digitais, incluindo:

• ideias de posts  
• headlines  
• descrições visuais  
• legendas  
• imagens conceituais  
• planejamentos estratégicos  

Nosso objetivo é fornecer ferramentas criativas com segurança, simplicidade e eficiência.

---

## 2. Informações coletadas

Coletamos apenas os dados estritamente necessários para o funcionamento do serviço.

Podemos coletar:

• email de cadastro  
• senha criptografada  
• conteúdos criados dentro da plataforma  
• histórico de postagens geradas  
• informações técnicas do navegador e dispositivo  
• dados de sessão (login, tempo de uso, navegação)  

Não coletamos dados sensíveis como documentos, contatos, fotos pessoais ou informações financeiras.

---

## 3. Como utilizamos os dados

As informações são utilizadas exclusivamente para:

• autenticação de login  
• salvar seu histórico de criações  
• personalizar sua experiência  
• melhorar funcionalidades do sistema  
• suporte técnico  
• segurança contra fraudes  

Jamais utilizamos seus dados para fins publicitários ou venda de informações.

---

## 4. Compartilhamento de dados

O zAz **não vende, aluga ou compartilha** dados pessoais com terceiros.

Alguns serviços essenciais podem processar dados para viabilizar a operação da plataforma, como:

• Supabase (banco de dados)  
• hospedagem da aplicação  
• provedores de infraestrutura  

Esses serviços seguem padrões adequados de segurança e confidencialidade.

---

## 5. Login e autenticação

Caso utilize login com email e senha:

• suas credenciais são protegidas  
• não armazenamos senhas em texto simples  
• utilizamos práticas seguras de autenticação  

Caso utilize login com Google (quando disponível):

• recebemos apenas identificação básica (email)  
• não temos acesso à sua senha  
• não acessamos dados privados da sua conta Google  

---

## 6. Armazenamento e segurança

Adotamos medidas técnicas para proteger seus dados, incluindo:

• criptografia  
• autenticação segura  
• controle de acesso  
• proteção contra acessos não autorizados  

Apesar disso, nenhum sistema é 100% invulnerável.

---

## 7. Cookies e sessão

Utilizamos apenas cookies essenciais para:

• manter seu login ativo  
• lembrar preferências  
• melhorar a navegação  

Não utilizamos rastreamento publicitário ou cookies invasivos.

---

## 8. Direitos do usuário

Você pode, a qualquer momento:

• solicitar acesso aos seus dados  
• corrigir informações  
• excluir sua conta  
• solicitar remoção definitiva dos dados  

Basta entrar em contato conosco.

---

## 9. Retenção de dados

Seus dados permanecem armazenados enquanto sua conta estiver ativa.  
Após a exclusão, as informações podem ser removidas permanentemente.

---

## 10. Alterações nesta política

Podemos atualizar esta Política de Privacidade periodicamente.  
O uso contínuo do serviço após alterações indica concordância com a nova versão.

---

## 11. Contato

📧 contato@zaz.app

---

**Ao utilizar o zAz, você concorda com esta Política de Privacidade.**
    """)

    aceite = st.checkbox("Aceitar política")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_privacidade = True
            st.session_state.abrir_privacidade = False
            st.rerun()


# =====================================================
# RENDER
# =====================================================
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

    email_ok = email_valido(email)
    senha_ok = senha_valida(senha)

    pode_criar = (
        email_ok
        and senha_ok
        and st.session_state.aceite_termos
        and st.session_state.aceite_privacidade
    )

    if st.button("Criar conta", use_container_width=True, disabled=not pode_criar):
        criar_usuario(email, senha)
        st.success("Conta criada com sucesso. Faça login.")
