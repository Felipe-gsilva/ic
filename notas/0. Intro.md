# neural rendering accelerator
## NeRF (campos de radiação neural)

usadas para reconstruir cenas tridimensionais complexas a partir de um conjunto parcial de imagens bidimensionais
https://ieeexplore.ieee.org/abstract/document/10967345

Usam MLP (perceptron multicamada)

- PixelNeRF
- Mega-NeRD
- NSVF
- Plenoptic Voxel

### gaussian splatting
https://ieeexplore.ieee.org/abstract/document/10908905

## redes adversarias generativas 
GAN's -> 2 redes (uma rede geradora, outra rede discriminadora) as quais exercem exatamente a função a si cunhada. Uma gera imagens distinas baseando-se em uma base de dados conhecida, enquanto o outro os aceita ou não. Enquanto a rede geradora tenta se aproximar de um valor aceitado pela rede aceitadora, esta não altera seu comportamento, apenas não conseguirá, eventualmente, identificar a diferença entra uma imagem no dataset e outra gerada.
usos:
- Gerar imagens
- Gerar modelos 3D a partir de dados 2D

Existem alguns tipos:
- StyleGAN, CycleGAN e discoGAN, por exemplo.

