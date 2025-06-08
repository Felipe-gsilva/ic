# Investigação de técnicas de geração de imagens para melhor eficiência em NeRF’s aplicados a dados histológicos

## 1 Introdução

A renderização 3D, especialmente aplicada sobre dados médicos, facilita a visualização integrada de estruturas complexas, como órgãos, vasos sanguíneos ou tecidos orgânicos com perspectivas dinâmicas, aprimorando a compreensão de relações espaciais críticas para diagnósticos e planejamentos cirúrgicos. Além disso, modelos 3D personalizados, gerados a partir de dados de pacientes, podem simular intervenções médicas com maior segurança, servir como ferramenta educativa para treinamento de profissionais e até apoiar a criação de próteses ou implantes sob medida. Existem diversos metodologias e técnicas para se alcançar bons resultados e modelos 3D, seja através da modelagem a partir de um artista ou, de maneira avançada, obter modelos a partir de imagens 2D.

Em dissonância a métodos tradicionais de síntese de imagens, os campos de radiação neural (NeRF’s) utilizam-se de técnicas de renderização volumétricas comuns, apoiando-se nas redes neurais artificiais MLP’s (multilayer perceptron) para processar a entrada de coordanadas 5D ((x, y, z, θ, ϕ), compreendido como um vetor 3D de posições (x, y, z) computado com o ângulo e direção de câmera correspondentes (θ, ϕ)) em pontos de densidade volumétrica (σ(x)) e cor (c = (r, g, b)), capazes de posteriormente se transformarem em um objeto 3D convencional [1].

Porém, para conseguir modelos tri-dimensionais de alta confiabilidade, o NeRF depende de um conjunto consideravelmente grande de imagens e diferentes rotações dos ângulos da câmera do objeto/ambiente de referência.

Considerando-se a necessidade de grandes volumes de dados mencionada, vários autores buscaram aprimorar seus datasets com inúmeras técnicas, sempre na intenção de qualificar mais e mais os dados e obter imagens mais próximas do ground-truth. Por exemplo, pesquisadores utilizaram-se do SFM (Structure from Motion), uma técnica de imagem de alcance fotogramétrico, para se capturar imagens do ambiente em questão com maior precisão e qualidade, como no método de gaussianos 3D [2], ou mesmo o MVS (multi-view stereo), escolhido pelo uso subsequente de CNN’s (convulutional neural network) [3]. Estas técnicas, conquanto fiéis às suas referências, são, ora, computacionalmente caras, ora, ainda, demandantes de uma quantidade exacerbada de imagens do item a ser renderizado. Datasets histológicos, entretanto, costumam não possuir tamanha diversidade ou redundância de ângulos necessária, devido a desafios como a complexidade estrutural dos tecidos e restrições éticas na coleta de amostras [4].

Apesar de sua fidelidade, no entanto, os trabalhos supracitados demandam um alto poder computacional, não tendo sua replicabilidade altamente assegurada. Consonantemente, neste trabalho, buscar-se-á possibilidades de se minimizar a distância entre um dataset ideal (repleto de redundância e ângulos de câmera distintos) e os datasets comuns na histologia. Para tal, seguindo trabalhos similares, se faz necessária uma investigação sobre a viabilidade de se utilizar técnicas de geração de imagem como GAN’s (generative adversarie network) aplicadas em dados histológicos, como feito previamente por Rozendo [5] em imagens bi-dimensionais. GAN’s permitem a criação de imagens através de duas redes neurais treinadas para competição mutua (G - gerador e D - discriminador). G tenta criar imagens que emulam o pertencimento ao domínio de D, enquanto este o avalia, classificando-o como pertencente ou não. Eventualmente, G e D atingem um estado de equilíbrio (chamado de equilíbrio de Nesh), no qual, mesmo após maiores treinamentos, a diferença se estabiliza [6]. Ao utilizar-se deste conceito, espera-se, portanto, promover a redução da dependência de datasets extensos de NeRF’s, enquanto mantem-se sua qualidade instrínseca.
## 2 Objetivos

Neste projeto, tem-se como objetivo investigar e aplicar métodos de geração de imagem para aumentar um dataset limitado na histologia. Para tal, pretende-se:

- Adaptar entradas de imagens para se adequarem ao uso oficial de NeRF’s
- Explorar o uso do modelo GAN's como técnica comparativa de aumento de dados, a fim de avaliar sua eficácia relativa em relação ao uso em NeRF’s
- Investigar a viabilidade de se aumentar um dataset histológico para o uso em nerf
- Definir as principais associações e limites observados no contexto aqui explorado

Considerando o previsto em Edital PROPe Unesp Nº 08/2025 - PIBIC, esta proposta tem aderência plena com as áreas Prioritárias do Ministério da Ciência, Tecnologia, Inovações e Comunicações (estabelecidas na Portaria MCTIC nº 1.122/2020, com texto alterado pela Portaria MCTIC nº 1.329/2020), especificamente com as Áreas de Tecnologias para Qualidade de Vida (Saúde) e Tecnologias Habilitadoras (Inteligência Artificial). No que tange à lista dos Objetivos do Desenvolvimento Sustentável (ODS), esta pesquisa apresenta aderência direta com a ODS 9 (indústria, inovação e infraestrutura).

## 3 Metodologia

A pesquisa será conduzida em cinco etapas principais, dispostas a seguir.

### 3.1 Etapa 1 - Revisão Bibliográfica

Esta etapa permite o levantamento bibliográfico necessário para manter o projeto atualizado, proporcionar uma fundamentação teórica sólida e subsidiar a exploração proposta.

### 3.2 Etapa 2 - Pré-processamento dataset de imanges histológicas

Dado um conjunto de imagens fornecido pelo, observa-se 2 embróglios principais: a necessidade de pré-processamento das imagens e a organização do conjunto de dados em grupos distintos.

Os NerF’s requerem os dados sobre a pose da câmera para cada imagem, ou seja, a posição e orientação da câmera no momento da captura da imagem. Para tal, é necessário que as imagens sejam organizadas em grupos, os quais contenham, individualmente, imagens de um único tecido e pose. Consonantemente, o **pré-processamento das imagens se torna essencial para garantir-se** o formato adequado para o treinamento do modelo. Isso inclui técnicas como a normalização das imagens, a remoção de ruídos e artefatos e a padronização do tamanho e resolução das imagens, nos casos onde se faça necessário.

Além disso, para efeito de treinamento do modelo, é necessário que sejam estabelecidos subconjuntos de imagens, cada qual usado em diferentes contextos. Serão criados 3 conjuntos principais: Treinamento, Validação e Teste, sendo, em específico, o conjunto de treinamento, novamente, subdividido. Pretende-se que, ao fazê-lo, os resultados percam possíveis viéses e, ademais, seja possível determinar os resultados de forma mais precisa.

### 3.3 Etapa 3 - Treinamento e Geração de imanges

Nesta etapa, um modelo GAN será treinado para gerar novas imagens histológicas a partir do conjunto de dados pré-processado. O modelo GAN deverá aprender as características dos tecidos histológicos presentes no dataset, permitindo, assim, a geração de imagens que preservem as propriedades visuais e estruturais dos tecidos.

### 3.4 Etapa 4 - Treinamento do modelo NeRF e Criação dos volumes 3D

O treinamento do modelo NeRF será realizado utilizando as imagens geradas pelo modelo GAN e, paralelamente, com subconjuntos do grupo de treinamento, supracitado. Desta forma, poder-se-á compreender a relação entre as imagens 2D e a reconstrução 3D dos tecidos histológicos. A partir do modelo NeRF treinado, serão obtidos volumes 3D dos tecidos histológicos, permitindo a visualização das estruturas internas dos tecidos com alta fidelidade. Esses volumes serão futuramente avaliados quanto à sua qualidade e fidelidade em relação às imagens originais do dataset na etapa de validação.

### 3.5 Etapa 5 - Validação dos resultados

Para obter-se resultados precisos, factíveis e replicáveis, este projeto buscará utilizar-se de métricas de validação dos modelos 3D reconstruídos, seja pela comparação com modelos de referência ou pela análise de poses específicas, ou seja, imagens 2D tiradas sobre o modelo.

- **Validação de imangens 2D**: Serão empregados, no campo das imagens bidimensionais, tanto o PSNR (Peak Signal-To-Noise Ratio) quanto o SSIM (Structural Similarity Index). O PSNR faz uma comparação direta entre 2 imagens e consegue descrever o ruído discrepante entre estas, utilizando-se de uma razão sinal-ruído em escala logarítmica. Já o SSIM trabalha com a estrutura da imagem em si, ou seja, nos agrupamentos dos pixels da referência quando comparados à imagem gerada pela arquitetura GAN, capturando melhor a percepção humana de qualidade visual do que o PSNR.

- **Validação de modelos 3D**: Para o domínio das reconstruções 3D, utilizar-se-á o Volumetric Intersection over Union (IoU Volumétrico). Esta métrica calcula a razão entre o volume da interseção e o volume da união do modelo reconstruído e do modelo de referência, fornecendo uma medida direta da sobreposição espacial dos volumes.

Essas métricas fornecerão uma base quantitativa robusta para avaliar e comparar a qualidade dos modelos testados, dimensionando uma alta fidelidade ao obter-se valores elevados de PSNR e SSIM e de IoU Volumétrico.

## 4 Plano de Trabalho e Cronograma de Execução

O plano de trabalho consiste em realizar as etapas descritas na seção 3:  
1. Etapa 1 - Revisão Bibliográfica  
2. Etapa 2 - Pré-processamento dataset de imanges histológicas  
3. Etapa 3 - Treinamento e Geração de imanges  
4. Etapa 4 - Treinamento do modelo NeRF e Criação dos volumes 3D  
5. Etapa 5 - Validação dos resultados  

**Tabela 1**: Proposta de Cronograma para o atendimento das etapas previstas no escopo do projeto, considerando o período de 12 meses.

| Etapas                              | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 |
|-------------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
| 1 - Revisão Bibliográfica           | x  | x  |    | x  |    | x  |    | x  |    |    |    |    |
| 2 - Pré-processamento               | x  | x  | x  |    |    |    |    |    |    |    |    |    |
| 3 - Treinamento/Geração GAN         |    |    |    | x  | x  |    |    |    |    |    |    |    |
| 4 - Treinamento NeRF/Volumes 3D     |    |    |    |    |    | x  | x  |    |    |    |    |    |
| 5 - Validação                       |    |    |    |    |    |    |    | x  | x  | x  |    |    |
| Escrita: Processos e Resultados     |    | x  |    | x  |    | x  |    | x  |    | x  | x  |    |

## 5 Resultados Esperados

Este projeto visa investigar a aplicabilidade de métodos convencionais de Deep Learning em dados histológicos, ao gerar imagens histológicas sintéticas e reconstruir volumes 3D a partir dessas imagens. Os resultados esperados incluem a avaliação da qualidade dessas imagens e dos volumes 3D reconstruídos e a contribuição para a área de pesquisa em imagens médicas, ao concluir a viabilidade de se utilizar GAN’s associados a NeRF’s.

## References

1. **B. Mildenhall et al.**, "Nerf: Representing scenes as neural radiance fields for view synthesis," 2020.  
2. **B. Kerbl et al.**, "3d gaussian splatting for real-time radiance field rendering," *ACM Transactions on Graphics*, vol. 42, July 2023.  
3. **A. Chen et al.**, "Mvsnerf: Fast generalizable radiance field reconstruction from multi-view stereo," 2021.  
4. **Y. Xue et al.**, "Selective synthetic augmentation with histogram for improved histopathology image classification," *Medical Image Analysis*, vol. 67, p. 101816, 2021.  
5. **G. B. Rozendo et al.**, "Data augmentation in histopathological classification: An analysis exploring gans with xai and vision transformers," *Applied Sciences*, vol. 14, no. 18, 2024.  
6. **I. J. Goodfellow et al.**, "Generative adversarial networks," 2014.
