# Agente Recruiter Specialist

Este repositório contém o código (flow exportado do LangFlow) e a síntese técnica da live sobre a criação de um Agente de IA Recruiter Specialist, realizada durante a [Community Week da DIO](https://pages.dio.me/lp-community-week2). Este agente foi desenvolvido para ajudar profissionais de tecnologia a otimizar seus currículos com base em seu perfil público na plataforma DIO e descrições de vagas reais.

## 🔗 Links Rápidos

- **[DIO](https://www.dio.me)** - Conheça ecossistema educacional da DIO 
- **[LangFlow (GitHub)](https://github.com/langflow-ai/langflow)** - Plataforma open-source utilizada no projeto
- **[DataStax](https://www.datastax.com)** - Acesso gratuito ao LangFlow online após cadastro
- **[Azure OpenAI Service](https://azure.microsoft.com/pt-br/products/ai-services/openai-service)** - Provedor de LLM usado na demonstração
- **[Job Board DIO](https://web.dio.me/job-board)** - Encontre vagas reais para testar o agente
- **[Exemplo de Perfil DIO](https://www.dio.me/users/falvojr)** - Perfil de exemplo para teste

## 🚀 Objetivos

Este projeto, parte da [Community Week da DIO](https://pages.dio.me/lp-community-week2), teve como foco demonstrar o potencial da Inteligência Artificial (IA) e dos agentes inteligentes para revolucionar o futuro do trabalho. Especificamente, o objetivo principal foi **criar um agente de IA, o "Recruiter Specialist"**, capaz de:
*   Analisar o perfil público de um profissional na plataforma DIO.
*   Comparar as habilidades e conquistas do profissional com os requisitos de uma descrição de vaga específica.
*   Gerar um resumo otimizado para currículo.
*   Identificar pontos fortes e lacunas no perfil do candidato para a vaga desejada.
*   Sugerir caminhos de aprendizado para aumentar as chances de sucesso na aplicação.

A intenção é transformar as _skills_ adquiridas na DIO em elementos palpáveis para o currículo e ajudar na jornada de aplicação para vagas.

## 🛠️ Conhecendo o LangFlow

Para construir nosso agente, utilizamos o **[LangFlow](https://github.com/langflow-ai/langflow)**. O LangFlow é uma ferramenta **open-source e visual (low-code/no-code)** para construir e implantar agentes empoderados por IA.

*   **Origem Brasileira:** Nascido de uma startup brasileira, foi adquirido pela DataStax, empresa do Vale do Silício agora parte dos investimentos em IA da IBM.
*   **Interface Visual:** Permite criar "flows" (fluxos de trabalho) conectando componentes prontos como inputs, outputs, prompts, modelos de linguagem (LLMs) e ferramentas (tools).
*   **Flexibilidade:** Suporta diversas fontes de dados (URL, arquivos, APIs, etc.) e integrações com os principais provedores de LLMs do mercado.
*   **Código Editável:** Embora seja low-code, permite editar o código Python por trás dos componentes para customização avançada.
*   **Deployment Facilitado:** Flows podem ser publicados como APIs ou embedados como chat widgets em sites.
*   **Execução:** Pode ser rodado localmente (open-source) ou utilizado na plataforma online gratuita da DataStax.

Utilizamos a plataforma da DataStax durante a live por sua facilidade de uso e ambiente online.

## 🤖 Criando Nosso Primeiro Agente de IA

Começamos construindo um flow básico no LangFlow:
1.  Adicionamos um componente **Chat Input** para receber a entrada do usuário.
2.  Adicionamos um componente **Agent** para processar a informação utilizando uma LLM.
3.  Conectamos o Chat Input ao Agent.
4.  Adicionamos um componente **Chat Output** para exibir a resposta.
5.  Conectamos o Agent ao Chat Output.

Dentro do componente Agent, configuramos o provedor de LLM. Na live, utilizamos o **Azure OpenAI**, aproveitando modelos como o GPT-4o. Foi ressaltada a importância de configurar corretamente as chaves de API e *endpoints*, idealmente usando variáveis de ambiente seguras dentro do LangFlow. Mencionamos que outros provedores como OpenAI, Antropic, Google AI Studio, etc., também estão disponíveis e podem ser utilizados.

As instruções iniciais do agente foram definidas no campo `Agent Instructions`, indicando que ele seria um assistente útil.

## ✨ Refinando Prompts

Para tornar o agente "Recruiter Specialist" realmente útil, refinamos a forma como ele recebe e processa as informações usando o componente **Prompt**.

*   **Componente Prompt:** Permite estruturar o texto de entrada para a LLM, incluindo variáveis.
*   **Variáveis do Prompt:** Definimos variáveis para os `DADOS_CANDIDATO` e a `DESCRICAO_VAGA`.
*   **Fonte dos Dados do Candidato:** Utilizamos o componente **URL** para buscar informações diretamente do perfil público da DIO do usuário. A URL do perfil foi passada como entrada para este componente.
*   **Fonte da Descrição da Vaga:** A descrição da vaga foi definida para vir do **Chat Input**, digitada pelo usuário.
*   **Conexão no Flow:** Conectamos o componente URL à variável `DADOS_CANDIDATO` no Prompt e o Chat Input à variável `DESCRICAO_VAGA` no Prompt. O Prompt resultante foi conectado como input para o Agent.
*   **Web Scraping/Crawling:** Inicialmente, o componente URL estava configurado para buscar apenas texto. Isso resultou na perda de informações importantes no perfil da DIO, como conquistas, certificações e links. Ao alterar a configuração do componente URL para buscar o **HTML** da página, conseguimos extrair uma quantidade muito maior de dados, permitindo ao agente identificar e utilizar informações antes "invisíveis".
*   **Instruções do Agente:** As instruções globais do agente (`Agent Instructions`) foram aprimoradas para garantir que ele use *exclusivamente* as informações fornecidas, evitando "inventar" ou deduzir. Também definimos um tom de voz profissional, conciso e factual, evitando adjetivos exagerados.
*   **Formato de Saída:** No corpo do Prompt, instruímos a LLM a formatar a resposta em **Markdown** para facilitar a leitura e eventual conversão para PDF. Definimos a estrutura detalhada da saída, incluindo nome, resumo, skills, conquistas/certificações, artigos e uma análise das chances para a vaga com recomendações de aprendizado.

Testamos o agente utilizando diferentes perfis da DIO e descrições de vagas, observando a melhoria significativa na qualidade da resposta ao mudar a fonte de dados de texto para HTML.

## 🎯 Agora é a Sua Vez!

A live demonstrou como é possível criar um agente de IA funcional e útil em pouco tempo utilizando o LangFlow. O flow "Recruiter Specialist" que construímos é um ponto de partida poderoso.

**Este repositório contém o flow exportado (arquivo JSON) que foi criado durante a live.**

**Nosso desafio para você é o seguinte:**

1.  **Faça um Fork** deste repositório para a sua conta no GitHub.
2.  **Importe o flow JSON** para a sua instância do LangFlow (local ou na DataStax).
3.  **Experimente!** Utilize seu próprio perfil da DIO, diferentes descrições de vagas, e veja como o agente se comporta.
4.  **Personalize!** Vá além do que foi feito na live, algumas ideias:
    *   Refine os prompts para que a saída seja ainda mais alinhada com suas necessidades.
    *   Explore outros componentes do LangFlow, como a leitura de **arquivos (PDFs, etc.)** para analisar seu currículo tradicional ou perfil do LinkedIn exportado.
    *   Tente implementar a busca de URL como uma **Tool** dinâmica acionada pelo agente.
    *   Teste diferentes **provedores de LLMs** (OpenAI, Google AI Studio, etc.) e compare os resultados.

Lembre-se sempre de **estar atento à precificação** dos modelos de LLM que você escolher utilizar. Muitos oferecem créditos gratuitos iniciais ou tiers de uso baixo custo.

## 💡 Conclusão

A IA serve para nos ajudar a sermos mais produtivos e focarmos no que realmente importa. Use este projeto como um trampolim para criar suas próprias soluções inteligentes!

Compartilhe suas criações e aprendizados com a comunidade DIO! Use as hashtags **#DIOAiAgents** e **#CommunityWeekAiAgents** nas redes sociais.

Estamos ansiosos para ver o que você vai construir 🚀
