3 componentes principais:
- 3D gaussians
    - [Structure-from-Motion](2.1.SFM.md)- calibrated cameras
- otimizações dos pontos gaussianos
    - 3D position, opacity 𝛼, anisotropic covariance, and spherical harmonic (SH) coefficients
- renderização em tempo real que usa algs de ordenação de GPU inspirados em rasterização baseada em tiles.
real-time rendering solution that uses fast GPU sorting algorithms and is inspired by tile-based rasterization


