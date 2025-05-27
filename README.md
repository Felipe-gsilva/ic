# Investigação de técnicas de geração de imagens para melhor eficiência em NeRF’s aplicados a dados histológicos

## 1 Introdução

A renderização 3D de dados médicos facilita a visualização integrada de estruturas complexas, como órgãos, vasos sanguíneos ou tecidos, em perspectivas dinâmicas, aprimorando a compreensão de relações espaciais críticas para diagnósticos e planejamentos cirúrgicos. Além disso, modelos 3D personalizados, gerados a partir de dados de pacientes, podem simular intervenções médicas com maior segurança, servir como ferramenta educativa para treinamento de profissionais e até apoiar a criação de próteses ou implantes sob medida. Existem diversas metodologias e técnicas para se alcançar bons resultados e modelos 3D, seja através da modelagem a partir de um artista ou, de maneira avançada, obter modelos a partir de imagens 2D.

Em dissonância a métodos tradicionais de síntese de imagens, os campos de radiação neural, os _NeRF’s_, utilizam-se de técnicas de renderização volumétricas comuns, apoiando-se nas redes neurais artificiais MLP’s (multilayer perceptron) para processar a entrada de coordenadas 5D ((x, y, z, θ, φ), compreendido como um vetor 3D de posições (x, y, z) computado com o ângulo e direção de câmera correspondentes (θ, φ)) em pontos de densidade volumétrica (σ(x)) e cor (c = (r, g, b)), capazes de posteriormente se transformarem em um objeto 3D convencional [1]. Porém, para conseguir modelos tri-dimensionais de alta confiabilidade, o NeRF depende de um conjunto consideravelmente grande de imagens e diferentes rotações dos ângulos da câmera do objeto/ambiente de referência.

Considerando-se a necessidade de grandes volumes de dados mencionada, vários autores buscaram aprimorar seus datasets com inúmeras técnicas. Por exemplo, pesquisadores utilizaram-se do SFM (Structure from Motion), uma técnica de imagem de alcance fotogramétrico, para se capturar imagens do ambiente em questão com maior precisão e qualidade, como no método de gaussianos 3D [2], ou mesmo o MVS (multi-view stereo), escolhido pelo uso subsequente de CNN’s (convolutional neural network) [3]. Estas técnicas, conquanto fiéis a suas referências, ora são computacionalmente caras, ora, ainda, demandam de uma quantidade exacerbada de imagens do item a ser renderizado. Datasets histológicos, entretanto, costumam não possuir tamanha diversidade ou redundância de ângulos necessária, devido a desafios como a complexidade estrutural dos tecidos e restrições éticas na coleta de amostras [4].

Apesar de sua fidelidade, no entanto, os trabalhos supracitados demandam um alto poder computacional, não tendo sua replicabilidade altamente assegurada. Consonantemente, neste trabalho, buscar-se-á possibilidades de se minimizar a distância entre um dataset ideal (repleto de redundância e ângulos de câmera distintos) e os datasets comuns na histologia. Para tal, seguindo trabalhos similares, se faz necessária uma investigação sobre a viabilidade de se utilizar técnicas de geração de imagem como GAN’s (generative adversarial network) [5] aplicadas em dados histológicos, como feito previamente por Rozendo [6] em imagens bi-dimensionais. Os _GAN’s_ se baseiam nas técnicas de deep learning. Espera-se, portanto, promover a redução da dependência de datasets extensos de NeRF’s.

---

## 2 Objetivos

Neste projeto, tem-se como objetivo investigar e aplicar métodos de geração de imagem para aumentar um dataset limitado na histologia. Para tal, pretende-se:

- Investigar a viabilidade de se aumentar um dataset histológico ou não para o uso em NeRF.

Considerando o previsto em Edital PROPe Unesp Nº 08/2025 - PIBIC, esta proposta tem aderência plena com as áreas Prioritárias do Ministério da Ciência, Tecnologia, Inovações e Comunicações (estabelecidas na Portaria MCTIC nº 1.122/2020, com texto alterado pela Portaria MCTIC nº 1.329/2020), especificamente com as Áreas de Tecnologias para Qualidade de Vida (Saúde) e Tecnologias Habilitadoras (Inteligência Artificial). No que tange à lista dos Objetivos do Desenvolvimento Sustentável (ODS), esta pesquisa apresenta aderência direta com a ODS 9 (indústria, inovação e infraestrutura).

---

## 3 Metodologia

A pesquisa será conduzida em cinco etapas principais, dispostas a seguir.

### 3.1 Etapa 1 - Revisão Bibliográfica

Esta etapa permite o levantamento bibliográfico necessário para manter o projeto atualizado, proporcionar uma fundamentação teórica sólida e subsidiar a exploração proposta.

### 3.2 Etapa 2 - Processar input (adaptar dataset para input padrão NeRF)

Processamento do dataset para adequação aos requisitos de entrada do NeRF.

### 3.3 Etapa 3 - Geração de imagens com GAN’s

Implementação e aplicação de GANs para aumento do dataset histológico.

### 3.4 Etapa 4 - Treinamento do modelo NeRF

Treinamento do modelo NeRF utilizando o dataset original e o aumentado.

### 3.5 Etapa 5 - Verificar métricas de validação de modelos 3D e imagens

Avaliação quantitativa e qualitativa dos resultados obtidos.

---

## 4 Plano de Trabalho e Cronograma de Execução

**Tabela 1:** Proposta de Cronograma para o atendimento das etapas previstas no escopo do projeto, considerando o período de 12 meses.

| Etapas | Ano 1: 2024-2025 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|--------|-------------------|---|---|---|---|---|---|---|---|---|---|----|----|
| 1      | x | x |   | x |   | x |   | x |   |   |    |    |
| 2      | x | x | x |   |   |   |   |   |   |   |    |    |
| 3      |   |   |   | x | x |   |   |   |   |   |    |    |
| 4      |   |   |   |   |   | x | x |   |   |   |    |    |
| 5      |   |   |   |   |   |   |   | x | x | x |    |    |
| **Escrita: Processos e Resultados** |   | x |   | x |   | x |   | x |   | x | x |    |

---

## 5 Resultados Esperados

Este projeto visa investigar a aplicabilidade de métodos convencionais de Deep Learning em dados histológicos. O objetivo principal é explorar técnicas como GANs (Generative Adversarial Networks) e NeRFs (Neural Radiance Fields) para superar desafios como a escassez de dados e a complexidade estrutural de tecidos biológicos.

---

## Referências

[1] B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoorthi, and R. Ng, "Nerf: Representing scenes as neural radiance fields for view synthesis," 2020.  
[2] B. Kerbl, G. Kopanas, T. Leimkuhler, and G. Drettakis, "3d gaussian splatting for real-time radiance field rendering," _ACM Transactions on Graphics_, vol. 42, July 2023.  
[3] A. Chen, Z. Xu, F. Zhao, X. Zhang, F. Xiang, J. Yu, and H. Su, "Mvsnerf: Fast generalizable radiance field reconstruction from multi-view stereo," 2021.  
[4] Y. Xue, J. Ye, Q. Zhou, L. R. Long, S. Antani, Z. Xue, C. Cornwell, R. Zaino, K. C. Cheng, and X. Huang, "Selective synthetic augmentation with histogram for improved histopathology image classification," _Medical Image Analysis_, vol. 67, p. 101816, 2021.  
[5] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, "Generative adversarial networks," 2014.  
[6] G. B. Rozendo, B. L. d. O. Garcia, V. A. T. Borgue, A. Lumini, T. A. A. Tosta, M. Z. d. Nascimento, and L. A. Neves, "Data augmentation in histopathological classification: An analysis exploring gans with xai and vision transformers," _Applied Sciences_, vol. 14, no. 18, 2024.
