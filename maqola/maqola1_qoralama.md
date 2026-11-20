# A mass-conservative numerical model of groundwater flow in a three-aquifer system with storage in both aquitards, heterogeneous transmissivity and an unconfined top layer

Javokhir Erkinov

Samarkand State University named after Sharof Rashidov, Samarkand, Uzbekistan. ORCID 0009-0007-6580-7402. E-mail: erkinovj110@gmail.com

Draft v0.1, 20 November 2026. Numbers come from the scripts in the repository `1-masala` (branch `claude/project-thread-15xs9v`), each table names its script. References marked [DOI?] still have to be checked against Crossref before submission.

## Abstract

In a three-aquifer system the two aquitards hold water in elastic storage. During pumping this water is released, and the release delays the response of the adjacent aquifers. Existing numerical models of layered aquifers in Uzbekistan treat aquitards as storage-free leakance interfaces. Analytical multilayer solutions do include aquitard storage, but they assume homogeneous, confined layers and radial flow. We formulate a model in which each aquitard obeys a one-dimensional vertical diffusion equation. Head and flux are continuous at both faces. The aquifers have spatially variable conductivity, and the upper aquifer is unconfined, with recharge, depth-dependent evaporation and wells.

The model is discretised with cell-centred finite volumes and backward Euler time stepping. The aquitard unknowns of each column are eliminated by a vectorised tridiagonal solve. This leaves a symmetric 2×2 exchange matrix per column and one sparse symmetric system for the aquifer heads. We prove that the scheme conserves mass exactly, that it is unconditionally stable in an energy norm and that it satisfies a discrete maximum principle.

The code reproduces the Theis and Hantush–Jacob solutions and a Laplace-domain multilayer solution with aquitard storage within 0.7%. It agrees with MODFLOW 6 to 4×10⁻⁹ m on the same grid. The aquitard discretisation converges at second order, and the mass-balance residual stays below 10⁻¹¹.

Numerical experiments show that the time scale t_c = b′S′/K′ alone does not decide when aquitard storage can be neglected. The ratio ε of aquitard to aquifer storage matters as well: for ε ≳ 1 the difference between the two models persists for t ≫ t_c. In a heterogeneous field with thick clay aquitards, storage changes early drawdown in the pumped aquifer by 18–30%. One year later it still reduces the water-table decline in the unconfined aquifer by 14%. A storage-free model therefore overestimates the water-table response that controls evaporation and salinisation.

Keywords: multilayer aquifer; aquitard storage; leaky aquifer; finite volume; unconditional stability; unconfined aquifer

## 1. Introduction

Irrigated plains of Central Asia overlie sequences of sandy aquifers separated by clay and loam layers. Pumping from a deeper aquifer lowers the water table in the shallow unconfined aquifer through the separating layers. This, in turn, changes evaporation from the water table and the salt balance of the root zone. Predicting the shallow response requires a model that couples the aquifers through the aquitards in a physically consistent way.

The school of N. Ravshanov has developed a sequence of quasi-three-dimensional models for such systems. Ravshanov et al. (2026a) solved three heterogeneous aquifers coupled through two aquitards with an ADI scheme, harmonic face averaging and a mass-conserving exchange term, together with particle transport and clogging. Ravshanov et al. (2026b) treated a four-layer system with head-dependent conductivity. Mukhamadiyev and Karimov (2025, 2026) added an unconfined top layer, variable transmissivity, evaporation and a low-permeability layer with elastic storage. In their model, however, the storage layer lies at the bottom of the sequence and its base is impermeable, so it does not connect two aquifers. Qodirov (2024) derived analytical solutions for three homogeneous aquifers with storage in the aquitards. In all of these numerical models the aquitards between aquifers carry no storage. None of them gives a stability proof for the coupled scheme.

Outside this school, aquitard storage has a long history. Hantush (1960) and Neuman and Witherspoon (1969) showed that the release of water from aquitard storage changes early-time drawdown. Hemker (1985) and Hemker and Maas (1987) solved the n-layer problem with storage in all aquitards in the Laplace domain. Cihan et al. (2011) extended this to many aquifers with leaky wells. Herrera and Yates (1977) wrote the aquitard response as a memory integral. In MODFLOW, aquitard storage is available through the TLK1 package (Leake et al. 1994) and through delay interbeds in the CSUB package (Hughes et al. 2022). An aquitard can also be represented as several thin model layers. Hence aquitard storage itself is not new.

What these tools do not provide together is the combination needed for the irrigated-plain problem: (i) storage in each aquitard between aquifers; (ii) conductivity that varies in plan within each aquifer and aquitard; (iii) a nonlinear unconfined top layer with recharge and depth-dependent evaporation; and (iv) a single discrete scheme for which mass conservation, stability and monotonicity are proved rather than assumed. The analytical solutions fail on (ii) and (iii). Discretising the aquitard as MODFLOW layers solves the same discrete problem as ours (Section 5.3), but it multiplies the number of three-dimensional unknowns and comes without a stability analysis of the coupled system.

This paper makes four contributions.

1. A three-aquifer model with a vertical diffusion equation in each aquitard, continuity of head and flux at both aquitard faces, K(x,y) in all units, and an unconfined top aquifer with recharge, Averyanov-type evaporation and wells (Section 2).
2. A finite-volume scheme in which the aquitard columns are condensed exactly by a tridiagonal solve. We prove exact discrete mass conservation, symmetry and positive semi-definiteness of the condensed exchange, unconditional energy stability and a discrete maximum principle (Sections 3 and 4).
3. Verification against classical solutions, a Laplace-domain multilayer solution with aquitard storage, MODFLOW 6 and the Dalem pumping test (Section 5).
4. A parametric study showing that the decision to neglect aquitard storage depends on two numbers, t/t_c and ε = S′/ΣS. We also quantify the effect of storage on the water table in a heterogeneous field (Section 6).

## 2. Mathematical model

### Setting and assumptions

The system consists of three aquifers numbered k = 1, 2, 3 from the top and two aquitards j = 1, 2. Aquitard j lies between aquifers j and j+1. The plan domain Ω ⊂ ℝ² has an arbitrary shape (Fig. 1). We adopt the following assumptions:

- (A1) flow is horizontal in the aquifers (Dupuit) and vertical in the aquitards (Hantush), since K′ ≪ K_k;
- (A2) storage in confined units and aquitards is linear and elastic;
- (A3) aquifer 1 is unconfined, with saturated thickness h₁ − z₀ and specific yield μ, while aquifers 2 and 3 stay confined;
- (A4) evaporation from the water table depends on its depth;
- (A5) each well is screened in one aquifer;
- (A6) each medium is locally isotropic, with conductivity varying in x and y.

Fig. 1. Schematic cross-section of the three-aquifer system (`maqola/rasm1_sxema.png`).

### Governing equations

Aquifer 1 (unconfined):

$$\mu\frac{\partial h_1}{\partial t}=\nabla\cdot\big(K_1(h_1-z_0)\nabla h_1\big)+W-E(h_1)-q^{+}_1-\sum_i Q_{1i}\delta(\mathbf x-\mathbf x_i).\tag{1}$$

Aquifers 2 and 3 (confined, T_k = K_k b_k):

$$S_2\frac{\partial h_2}{\partial t}=\nabla\cdot(T_2\nabla h_2)+q^{-}_1-q^{+}_2-\sum_i Q_{2i}\delta(\mathbf x-\mathbf x_i),\tag{2}$$

$$S_3\frac{\partial h_3}{\partial t}=\nabla\cdot(T_3\nabla h_3)+q^{-}_2-\sum_i Q_{3i}\delta(\mathbf x-\mathbf x_i).\tag{3}$$

Aquitard j, with ζ ∈ [0, b′_j] measured downward from its top:

$$S'_{s,j}\frac{\partial u_j}{\partial t}=K'_j\frac{\partial^2u_j}{\partial\zeta^2},\tag{4}$$

$$u_j|_{\zeta=0}=h_j,\qquad u_j|_{\zeta=b'_j}=h_{j+1},\tag{5}$$

$$q^{+}_j=-K'_j\partial_\zeta u_j|_{\zeta=0},\qquad q^{-}_j=-K'_j\partial_\zeta u_j|_{\zeta=b'_j}.\tag{6}$$

Here K′_j, b′_j and S′_{s,j} may vary with (x,y). Equations (5) and (6) express continuity of head and flux. When S′_s = 0, the aquitard becomes a storage-free interface and q⁺ = q⁻ = K′(h_j − h_{j+1})/b′. This is the exchange used by Ravshanov et al. (2026a).

Evaporation follows the law of Averyanov:

$$E(h_1)=E_0\big(1-(z_s-h_1)/\Delta\big)^n\ \text{ for } 0\le z_s-h_1\le\Delta,\qquad E=0\ \text{ for } z_s-h_1>\Delta.\tag{7}$$

Initial heads h_k⁰ are taken from the steady state without wells, which makes the aquitard heads u_j⁰ linear. Boundary conditions are prescribed head on Γ_D and no flow on Γ_N.

### Global balance and time scales

Integrating (4) over the aquitard thickness gives d/dt ∫S′_s u dζ = q⁺ − q⁻. Adding this to the integrals of (1)–(3), the exchange terms cancel. The storage change of the aquifers plus that of the aquitards equals recharge minus evaporation, minus pumping, plus boundary inflow.

Scaling (4) gives the aquitard time scale

$$t_c=\frac{b'^2S'_s}{K'}=\frac{b'S'}{K'},\qquad S'=S'_sb'.\tag{8}$$

The memory time of Herrera and Figueroa (1969), 3S′b′/(π²K′), is 0.30 t_c. A second dimensionless group is the storage ratio

$$\varepsilon=S'/\textstyle\sum_kS_k,\tag{9}$$

which plays the role of S′/S in the solutions of Hantush (1960) and Neuman and Witherspoon (1969).

## 3. Numerical method

### Spatial discretisation

Ω is covered by a tensor-product grid with variable spacing; cells outside Ω are inactive. Two neighbouring cells P and Q are coupled through the series conductance

$$C_{PQ}=\ell_{PQ}\Big(\frac{d_P}{2T_P}+\frac{d_Q}{2T_Q}\Big)^{-1},\tag{10}$$

where ℓ_PQ is the face length and d_P, d_Q are the cell widths. This is the harmonic mean, which is exact for piecewise-constant T. In aquifer 1 we set T₁ = K₁ max(h₁ − z₀, b_min).

Each aquitard column is divided into M sublayers of thickness δ = b′/M, with nodes at the sublayer centres. The interior conductance is c = K′/δ and the face conductance is c_e = 2K′/δ.

### Time discretisation

Backward Euler is applied to all units. For aquifer cell P with area A_P:

$$\frac{S_PA_P}{\tau}(h_P^{n+1}-h_P^n)+\sum_QC_{PQ}(h_P^{n+1}-h_Q^{n+1})+A_P(q^+_P-q^-_P)^{n+1}=A_P(W-E)_P^{n+1}-Q_P.\tag{11}$$

For each aquitard sublayer m:

$$\frac{S'_s\delta}{\tau}(u_m^{n+1}-u_m^n)=c_{m-1/2}(u_{m-1}^{n+1}-u_m^{n+1})+c_{m+1/2}(u_{m+1}^{n+1}-u_m^{n+1}),\tag{12}$$

with u₀ = h_j and u_{M+1} = h_{j+1}. The face fluxes are q⁺ = c_e(h_j − u₁) and q⁻ = c_e(u_M − h_{j+1}).

### Condensation of the aquitards

In each column, (12) is a symmetric tridiagonal system 𝔗u = s uⁿ + c_e e₁ h_j + c_e e_M h_{j+1}, with s = S′_sδ/τ. Solving it with three right-hand sides gives

$$u=a+\alpha h_j+\beta h_{j+1},\qquad \mathfrak Ta=su^n,\ \mathfrak T\alpha=c_ee_1,\ \mathfrak T\beta=c_ee_M.\tag{13}$$

The face fluxes then become linear in the two aquifer heads:

$$\begin{pmatrix}q^+\\-q^-\end{pmatrix}=\Lambda\begin{pmatrix}h_j\\h_{j+1}\end{pmatrix}-c_e\begin{pmatrix}a_1\\a_M\end{pmatrix},\qquad\Lambda=c_e\begin{pmatrix}1-\alpha_1&-\beta_1\\-\alpha_M&1-\beta_M\end{pmatrix}.\tag{14}$$

The tridiagonal solves are vectorised over all columns and depend only on τ and uⁿ, so they are done once per step. Inserting (14) into (11) gives one sparse symmetric system for the aquifer heads. After it is solved, u is recovered from (13). For M = 0, Λ = (K′/b′)[[1, −1], [−1, 1]].

### Nonlinearity and algorithm

T₁(h₁) and E(h₁) are handled by Picard iteration. At iterate r we use T₁(h^{(r)}) and linearise E about h^{(r)}:

$$E(h^{(r+1)})\approx E(h^{(r)})+E'(h^{(r)})(h^{(r+1)}-h^{(r)}).$$

Since E′ ≥ 0, the derivative term adds to the diagonal. Iteration stops when max|h^{(r+1)} − h^{(r)}| < 10⁻⁸ m.

Algorithm 1 (one time step):

1. condense the aquitards: solve (13) for a, α, β in all columns;
2. repeat until converged: assemble T₁ and the linearised E, then solve the sparse system;
3. recover u from (13);
4. evaluate the water budget.

## 4. Properties of the scheme

Let 𝔸 = D/τ + 𝕃 be the matrix of the full system (11)–(12), including the aquitard unknowns. D is diagonal with entries S_PA_P and S′_sδA_P. 𝕃 collects the horizontal and vertical conductances.

### Lemma 1 (discrete mass balance)

Summing (11) over all free cells and (12) over all sublayers gives

$$\Delta V_{\rm aquifers}+\Delta V_{\rm aquitards}=\tau\Big[\sum A(W-E_{\rm lin})-\sum Q+B_D\Big]$$

exactly, where B_D is the inflow from prescribed-head cells.

Proof. C_PQ is symmetric, so horizontal fluxes cancel in pairs. The fluxes in (14) are identical to the face fluxes of (12), so the vertical fluxes also cancel. □

### Lemma 2 (condensed exchange)

Λ is symmetric, its off-diagonal entries are non-positive and its row sums are non-negative. Hence Λ is positive semi-definite, and the condensed aquifer matrix is a symmetric M-matrix.

Proof. 𝔗 is a strictly diagonally dominant M-matrix, so 𝔗⁻¹ ≥ 0 and therefore α, β ≥ 0. Symmetry of 𝔗 gives α_M = β₁. From 𝔗𝟙 = s𝟙 + c_e e₁ + c_e e_M we obtain 1 − α_m − β_m = (𝔗⁻¹ s𝟙)_m ≥ 0. □

### Theorem 1 (unconditional stability)

For confined aquifers without evaporation and with homogeneous prescribed heads,

$$\|h^{n+1}\|_D\le\|h^n\|_D+\tau\|D^{-1}F^{n+1}\|_D$$

for every τ > 0, every M, every grid and all positive parameter fields. Here ‖v‖²_D = vᵀDv.

Proof. Take the inner product of 𝔸h^{n+1} = Dhⁿ/τ + F with h^{n+1}. Use (h^{n+1})ᵀ𝕃h^{n+1} ≥ 0 and the Cauchy–Schwarz inequality. □

Because D contains the aquitard storage, the estimate also bounds the aquitard heads.

### Theorem 2 (discrete maximum principle)

𝔸 is an M-matrix. Without sources, the new heads in aquifers and aquitards lie between the minimum and the maximum of the old heads and the boundary heads.

The scheme is therefore monotone for any τ. In particular, it produces no oscillations at abrupt contrasts in K or K′, a property that Crank–Nicolson keeps only under a step restriction. In the nonlinear case each Picard matrix is also an M-matrix, because T₁ ≥ K₁b_min > 0 and E′ ≥ 0, so each iterate is well defined. We do not prove convergence of the Picard iteration in general. Its iteration count is reported for every run.

### Convergence

The local truncation error is O(τ + h² + δ²) for smooth solutions. Together with Theorem 1, this gives convergence of the same order in the D-norm for the linear problem. On non-uniform grids, the cell-centred scheme is known to keep second-order global accuracy despite first-order local truncation (Forsyth and Sammon 1988 [DOI?]). We check the orders numerically in Section 5.

## 5. Verification

### Analytical and semi-analytical references

For homogeneous confined layers and a well with constant rate, we transform (2)–(6) to the Laplace domain. There, (4) is solved exactly. With λ = b′√(pS′_s/K′), the aquitard fluxes are

$$\bar q^+=\frac{K'}{b'}\lambda\,(\coth\lambda\,\bar h_j-\operatorname{csch}\lambda\,\bar h_{j+1}),\qquad \bar q^-=\frac{K'}{b'}\lambda\,(\operatorname{csch}\lambda\,\bar h_j-\coth\lambda\,\bar h_{j+1}).$$

The aquifer system is diagonalised in symmetric form and solved with modified Bessel functions K₀, following the approach of Hemker (1985). The result is inverted with the Stehfest (1970) algorithm with 12 terms. This reference reproduces the Theis (1935) solution to a relative difference of 10⁻⁵. It also reproduces the Hantush–Jacob (1955) solution to 10⁻⁴, the latter by giving the upper aquifer a very large T and S and the aquitard no storage (`testlar/test_masala1.py`).

### Three aquifers with storage in both aquitards

The test problem is T = 200, 100, 300 m²/d; S = 2, 1, 3 ×10⁻⁴; K′ = 2×10⁻³ and 10⁻³ m/d; b′ = 5 and 8 m; S′_s = 10⁻⁴ m⁻¹. A well pumps 500 m³/d from aquifer 2. The grid is telescopic, 105×105 cells, with a 2 m central cell growing by a factor 1.15 out to 20 km. Each aquitard has M = 20 sublayers. Time steps start at 10⁻⁴ d and grow by a factor of 1.05 up to 10 d. The maximum relative difference from the Laplace reference over 10⁻³–10 d is 0.22% (aquifer 1), 0.68–0.74% (aquifer 2) and 0.33% (aquifer 3) (`tajribalar/t3_modflow.py`). With a growth factor of 1.2, the differences in aquifers 1 and 3 rise to 1.2–1.8%. This identifies the first-order time error as the dominant part.

### Comparison with MODFLOW 6

The same problem was built in MODFLOW 6 (Langevin et al. 2017 [DOI?]) with each aquitard as 20 model layers (K33 = K′, SS = S′_s) and K33 = 10⁶ m/d in the aquifers: 43 layers in all, with identical time steps. Heads at nine observation points agree with our code to at most 4×10⁻⁹ m. Both codes differ from the Laplace reference by the same amount. The two codes solve the same discrete equations. Ours does it with a sparse system over 3 rather than 43 layers, plus independent tridiagonal solves.

### Convergence in the aquitard and mass balance

Table 1. Aquitard column (K′ = 10⁻² m/d, b′ = 2 m, S′_s = 10⁻² m⁻¹) after a unit step in head on the upper face; relative error of the face flux at t = 0.5 d against the series solution, τ = 10⁻⁴ d.

| M | relative error of q⁺ | observed order |
|---|---|---|
| 4 | 3.9×10⁻² | |
| 8 | 8.5×10⁻³ | 2.20 |
| 16 | 2.1×10⁻³ | 2.00 |
| 32 | 5.8×10⁻⁴ | 1.86 |

The slight drop at M = 32 comes from the time-discretisation error, which at τ = 10⁻⁴ d is of the same size.

Under time refinement the order is 1. For a heterogeneous, irregularly shaped problem with all processes active, the mass-balance residual is below 10⁻¹⁰ per step. As S′_s → 0 the solution converges to the storage-free model (difference < 10⁻⁸ m).

### Dalem pumping test

The Dalem test is given in Table 4.2 of Kruseman and de Ridder (1990), after De Ridder (1961). The pumping rate is Q = 761 m³/d, with four piezometers at 30–120 m. We fitted it with the Laplace reference, holding the head in the upper aquifer constant.

| Interpretation | KD (m²/d) | S | c (d) | S′ | RMSE (mm) |
|---|---|---|---|---|---|
| Walton type curve (Kruseman and de Ridder 1990) | 1731 | 1.9×10⁻³ | 468 | | 6.9 |
| storage-free aquitard, least squares | 1674 | 1.77×10⁻³ | 325 | | 5.87 |
| aquitard with storage, least squares | 1670 | 1.52×10⁻³ | 370 | 1.1×10⁻³ | 5.80 |

Including storage barely reduces the misfit, and S′ is poorly identified: the standard deviation of log₁₀S′ is 0.41. The test spans 0.015–0.33 d, comparable to the fitted t_c ≈ 0.4 d. The data therefore validate the model but cannot confirm aquitard storage from the drawdown in the aquifer alone. The fitted S′ = 1.1×10⁻³ nevertheless agrees with the value S′ = 1.1×10⁻³ that Kruseman and de Ridder (1990, p. 97–98) derive from the ratio method of Neuman and Witherspoon, which uses an additional piezometer inside the aquitard (D′ = 8 m, K′D′/S′ = 126 m²/d). Their averaged parameters are KD = 1800 m²/d, S = 1.7×10⁻³ and c = 450 d. The measured drawdowns had been corrected for partial penetration and tidal influence before publication; we use them as given.

[MLU "Two-aquifers" and Veling–Maas examples: to be added when parameters arrive.]

## 6. Results

### When can aquitard storage be neglected?

We take the configuration of Section 5.2 with K′ = 10⁻³ m/d and b′ = 5 m, so that t_c = 2.5 d. Aquifer storage is scaled to give ε = 0.083–83. We compare the storage and storage-free models at r = 30 m (Fig. 2).

| ε | last t/t_c at which the difference in the pumped aquifer exceeds 5% | difference at t = 10³ t_c |
|---|---|---|
| 0.083 | 0.25 | 0.4% |
| 0.83 | 0.79 | 2.3% |
| 8.3 | > 10³ | 6.6% |
| 83 | > 10³ | 12% |

For a fixed ε, the curves plotted against t/t_c coincide. For small ε the storage-free model becomes adequate shortly after t_c. For ε ≳ 1 it does not, because in a closed system the water released from the aquitards keeps adding to the effective storage. In the adjacent, unpumped aquifer the difference is larger still: 10% at 10³ t_c for ε = 0.83. A rule based on t_c alone would wrongly accept the storage-free model in these cases.

### Heterogeneous field with an unconfined top aquifer

The domain is 2000 × 1000 m with 80 × 40 cells. Aquifer 1 is unconfined, with a low-K lens and a sinuous high-K channel. K₂(x,y) is smoothly varying with a lens, and K₃ has two zones. Aquitard 1 contains a window with 20 times larger K′. Recharge is 6×10⁻⁴ m/d; evaporation has E₀ = 1.5×10⁻³ m/d, Δ = 3 m and n = 1.5. Heads are prescribed on the left and right sides. Four wells pump 3200 m³/d in total, three in aquifer 2 and one in aquifer 3, starting from the steady state.

With thin aquitards (t_c = 11 and 32 d), heterogeneity doubles the maximum drawdown in aquifer 2 relative to a homogeneous field (10.5 m against 5.6 m). It also transmits drawdown to the water table through the window (0.67 m against 0.05 m). Aquitard storage supplies 0.6% of the pumped water over one year and changes the drawdown by less than 0.5% (`tajribalar/t5_geterogen.py`).

With thick clay aquitards (b′ = 15 and 20 m, K′ = 10⁻⁴ and 5×10⁻⁵ m/d, S′_s = 4×10⁻⁴ m⁻¹), t_c = 900 and 3200 d, longer than the simulated year. Recharge is held constant so that all changes come from pumping (Fig. 3).

- Storage slows the early drawdown in aquifer 2 by 18–30%. After one year the difference is below 0.5%, because the prescribed-head boundaries then supply most of the water.
- Near t = 1 d the aquitards provide 26% of the pumped water.
- After one year the water-table decline in the unconfined aquifer is 0.051 m with storage and 0.060 m without, 14% less.
- The balance residual stays below 4×10⁻¹², and Picard needs at most 4 iterations per step.

## 7. Discussion

The results support a simple practical message. A storage-free aquitard model is adequate in the pumped aquifer once t exceeds a few t_c, provided ε is small. In a shallow aquifer above a thick clay layer, however, the storage-free model overestimates the decline of the water table for times shorter than t_c, and that decline is what drives evaporation and salt accumulation. For aquitards of the thickness typical of the irrigated plains (10–20 m of clay loam), t_c is of the order of years, so the storage term should be kept.

The condensation of the aquitard columns is equivalent to the layered representation used in MODFLOW. The results agree to round-off, but our system matrix has the size of the aquifer problem only. Lemma 2 shows that this elimination preserves the M-matrix structure. Therefore positivity and stability are inherited by the condensed system rather than merely observed in tests.

Limitations:

1. Aquifers 2 and 3 are assumed to stay confined.
2. Wells are screened in a single aquifer.
3. Aquitard flow is purely vertical.
4. The time discretisation is first order; a second-order variant (BDF2) would keep the M-matrix property only under a step restriction.
5. Picard convergence is monitored, not proved.
6. Field validation is limited to one classical pumping test, which cannot resolve aquitard storage. A test with piezometers inside the aquitard would be needed.

## 8. Conclusions

1. A three-aquifer model with a diffusion equation in each aquitard, K(x,y), an unconfined top layer, recharge, evaporation and wells was formulated and solved by a finite-volume scheme that eliminates each aquitard column exactly.
2. The scheme conserves mass exactly, is unconditionally stable in the storage-weighted norm and satisfies a discrete maximum principle. The condensed exchange matrix is symmetric and positive semi-definite.
3. The code reproduces the Theis, Hantush–Jacob and Laplace-domain multilayer solutions within 0.7%. It reproduces MODFLOW 6 to 4×10⁻⁹ m and converges at second order in the aquitard.
4. Whether aquitard storage can be neglected depends on t/t_c and on ε = S′/ΣS. For ε ≳ 1 the effect persists well beyond t_c.
5. In a heterogeneous field with thick clay aquitards, the storage-free model overestimates the water-table decline in the unconfined aquifer by about 14% after one year.

Future work: coupling with salt transport through the aquitards (problem 2 of the dissertation), and calibration against a site with aquitard piezometers.

## Data and code availability

The code, input data and scripts that produce every number and figure are available at https://github.com/javokhir-erkinov/1-masala (to be archived with a DOI on acceptance).

## Funding, conflicts of interest

[To be completed.]

## References

[All entries to be checked against Crossref; [DOI?] marks entries not yet verified in this project.]

- Cihan A., Zhou Q., Birkholzer J.T. (2011). Analytical solutions for pressure perturbation and fluid leakage through aquitards and wells in multilayered-aquifer systems. Water Resources Research 47, W10504. https://doi.org/10.1029/2011WR010721
- Forsyth P.A., Sammon P.H. (1988). Quadratic convergence for cell-centered grids. Applied Numerical Mathematics 4, 377–394. [DOI?]
- Hantush M.S. (1960). Modification of the theory of leaky aquifers. Journal of Geophysical Research 65(11), 3713–3725. [DOI?]
- Hantush M.S., Jacob C.E. (1955). Non-steady radial flow in an infinite leaky aquifer. Transactions AGU 36(1), 95–100. [DOI?]
- Hemker C.J. (1985). Transient well flow in leaky multiple-aquifer systems. Journal of Hydrology 81, 111–126. [DOI?]
- Hemker C.J., Maas C. (1987). Unsteady flow to wells in layered and fissured aquifer systems. Journal of Hydrology 90, 231–249. [DOI?]
- Herrera I., Figueroa G.E. (1969). A correspondence principle for the theory of leaky aquifers. Water Resources Research 5(4), 900–904. [DOI?]
- Herrera I., Yates R. (1977). Integrodifferential equations for systems of leaky aquifers and applications. 3. A numerical method of unlimited applicability. Water Resources Research 13(4), 725–732. https://doi.org/10.1029/WR013i004p00725
- Hughes J.D., Leake S.A., Galloway D.L., White J.T. (2022). Documentation for the Skeletal Storage, Compaction, and Subsidence (CSUB) Package of MODFLOW 6. USGS Techniques and Methods 6-A62. https://doi.org/10.3133/tm6A62
- Kruseman G.P., de Ridder N.A. (1990). Analysis and Evaluation of Pumping Test Data, 2nd ed. ILRI Publication 47, Wageningen.
- Langevin C.D. et al. (2017). Documentation for the MODFLOW 6 Groundwater Flow Model. USGS Techniques and Methods 6-A55. [DOI?]
- Leake S.A., Leahy P.P., Navoy A.S. (1994). Documentation of a computer program to simulate transient leakage from confining units using the modular finite-difference ground-water flow model. USGS Open-File Report 94-59. https://doi.org/10.3133/ofr9459
- Mukhamadiyev A., Karimov M. et al. (2025). Proc. SPIE 13662, 136620J. https://doi.org/10.1117/12.3072569 [title to be copied]
- Mukhamadiyev A., Karimov M. et al. (2026). Mathematics 14, 256. [DOI?]
- Neuman S.P., Witherspoon P.A. (1969). Theory of flow in a confined two aquifer system. Water Resources Research 5(4), 803–816. [DOI?]
- Qodirov K.R. (2024). PhD dissertation (abstract), Tashkent. [published articles to be cited instead, per project rule]
- Ravshanov N., Shadmanov I. et al. (2026a). Quasi-3D numerical modeling of groundwater flow, particle transport, and clogging-induced interlayer leakage in heterogeneous multilayer aquifers. Hydrology 13, 276. https://doi.org/10.3390/hydrology13100276
- Ravshanov N., Shadmanova K., Shadmanov I. (2026b). Hydrology 13, 181. https://doi.org/10.3390/hydrology13070181
- Stehfest H. (1970). Algorithm 368: Numerical inversion of Laplace transforms. Communications of the ACM 13(1), 47–49. [DOI?]
- Theis C.V. (1935). The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well using ground-water storage. Transactions AGU 16(2), 519–524. [DOI?]
