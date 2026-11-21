---
title: "A Mass-Conservative Numerical Model of Groundwater Flow in a Three-Aquifer System with Storage in Both Aquitards, Heterogeneous Transmissivity and an Unconfined Top Layer"
---

*Article*

Normakhmad Ravshanov ^1^ and Javokhir Erkinov ^2,\*^

^1^ Digital Technologies and Artificial Intelligence Development Research Institute, 17A Buz-2, Tashkent 100125, Uzbekistan; ravshanzade-09@mail.ru

^2^ Samarkand State University named after Sharof Rashidov, Samarkand 140104, Uzbekistan; erkinovjavohir@samdu.uz

\* Correspondence: erkinovj110@gmail.com

**Abstract:** In layered aquifer systems, water released from elastic storage in the aquitards delays the response of the adjacent aquifers, yet numerical models used for irrigated plains often treat aquitards as storage-free leakance interfaces. We formulate a model of three aquifers coupled through two aquitards, each governed by a one-dimensional vertical diffusion equation with continuity of head and flux at both faces. Conductivity varies in plan in all units, and the upper aquifer is unconfined, with recharge, depth-dependent evaporation and wells. The model is discretised with cell-centred finite volumes and backward Euler time stepping. The aquitard unknowns are eliminated column by column, leaving one sparse symmetric system for the aquifer heads. We prove exact discrete mass conservation, unconditional stability in an energy norm and a discrete maximum principle. The code reproduces the Theis, Hantush–Jacob and a Laplace-domain multilayer solution with aquitard storage within 0.7% and agrees with MODFLOW 6 to $4\times10^{-9}$ m. Experiments show that the aquitard time scale $t_c$ alone does not decide when storage can be neglected; the storage ratio $\varepsilon$ matters as well. With thick clay aquitards, a storage-free model overestimates the water-table decline by 14% after one year.

**Keywords:** multilayer aquifer; aquitard storage; leaky aquifer; finite volume method; unconditional stability; unconfined aquifer; evaporation

## 1. Introduction

Irrigated plains of Central Asia overlie sequences of sandy aquifers separated by clay and loam layers. Pumping from a deeper aquifer lowers the water table in the shallow unconfined aquifer through the separating layers. This, in turn, changes evaporation from the water table and the salt balance of the root zone. Predicting the shallow response requires a model that couples the aquifers through the aquitards in a physically consistent way.

The school of N. Ravshanov has developed a sequence of quasi-three-dimensional models for such systems. Ravshanov et al. [1] solved three heterogeneous aquifers coupled through two aquitards with an ADI scheme, harmonic face averaging and a mass-conserving exchange term, together with particle transport and clogging. Ravshanov et al. [2] treated a four-layer system with head-dependent conductivity. Karimov et al. [3] and Mukhamadiyev et al. [4] describe one three-layer model with an unconfined top layer, variable transmissivity, evaporation and a low-permeability layer with elastic storage. In that model, however, the storage layer lies at the bottom of the sequence and its base is impermeable, so it does not connect two aquifers. Kodirov [5,6] derived analytical solutions for a main aquifer bounded above and below by aquitards with elastic storage (the arrangement of Hantush [7]), with prescribed drawdown or an impermeable base beyond them, and for a linearised system with an overlying water table and evaporation. All parameters there are constant, and the aquitard storage is considered in one aquitard–aquifer–aquitard unit rather than between three coupled aquifers. In all of these numerical models the aquitards between aquifers carry no storage. None of them gives a stability proof for the coupled scheme.

Outside this school, aquitard storage has a long history. Hantush [7] and Neuman and Witherspoon [8] showed that the release of water from aquitard storage changes early-time drawdown. Hemker [9] and Hemker and Maas [10] solved the $n$-layer problem with storage in all aquitards in the Laplace domain. Cihan et al. [11] extended this to many aquifers with leaky wells. Herrera and Yates [12] wrote the aquitard response as a memory integral. In MODFLOW, aquitard storage is available through the TLK1 package [13] and through delay interbeds in the CSUB package [14]. An aquitard can also be represented as several thin model layers. Hence aquitard storage itself is not new.

What these tools do not provide together is the combination needed for the irrigated-plain problem: (i) storage in each aquitard between aquifers; (ii) conductivity that varies in plan within each aquifer and aquitard; (iii) a nonlinear unconfined top layer with recharge and depth-dependent evaporation; and (iv) a single discrete scheme for which mass conservation, stability and monotonicity are proved rather than assumed. The analytical solutions fail on (ii) and (iii). Discretising the aquitard as MODFLOW layers solves the same discrete problem as ours (Section 3.1), but it multiplies the number of three-dimensional unknowns and comes without a stability analysis of the coupled system.

This paper makes four contributions.

1. A three-aquifer model with a vertical diffusion equation in each aquitard, continuity of head and flux at both aquitard faces, $K(x,y)$ in all units, and an unconfined top aquifer with recharge, Averyanov-type evaporation and wells (Section 2.1).
2. A finite-volume scheme in which the aquitard columns are condensed exactly by a tridiagonal solve. We prove exact discrete mass conservation, symmetry and positive semi-definiteness of the condensed exchange, unconditional energy stability and a discrete maximum principle (Sections 2.2 and 2.3).
3. Verification against classical solutions, a Laplace-domain multilayer solution with aquitard storage, the published examples of Hemker and Maas [10] and MLU, MODFLOW 6 and the Dalem pumping test (Section 3.1).
4. A parametric study showing that the decision to neglect aquitard storage depends on two numbers, $t/t_c$ and $\varepsilon=S'/\sum S$. We also quantify the effect of storage on the water table in a heterogeneous field (Sections 3.2 and 3.3).

## 2. Materials and Methods

### 2.1. Mathematical Model

**Setting and assumptions**

The system consists of three aquifers numbered $k=1,2,3$ from the top and two aquitards $j=1,2$. Aquitard $j$ lies between aquifers $j$ and $j+1$. The plan domain $\Omega\subset\mathbb R^2$ has an arbitrary shape (Figure 1). We adopt the following assumptions:

- (A1) flow is horizontal in the aquifers (Dupuit) and vertical in the aquitards (Hantush), since $K'\ll K_k$;
- (A2) storage in confined units and aquitards is linear and elastic;
- (A3) aquifer 1 is unconfined, with saturated thickness $h_1-z_0$ and specific yield $\mu$, while aquifers 2 and 3 stay confined;
- (A4) evaporation from the water table depends on its depth;
- (A5) each well is screened in one aquifer;
- (A6) each medium is locally isotropic, with conductivity varying in $x$ and $y$.

![](rasm1_sxema.png){width=16cm}

**Figure 1.** Schematic cross-section of the three-aquifer system: unconfined aquifer 1 with water table $h_1$, recharge $W$ and evaporation $E(h_1)$; confined aquifers 2 and 3; aquitards 1 and 2 with the vertical coordinate $\zeta$ and face fluxes $q^\pm_j$; a well $Q_2$ in aquifer 2.

**Derivation of the aquifer equations**

Consider a vertical prism of aquifer $k$ with base $dx\,dy$ that spans the saturated thickness. Water enters and leaves the prism through its lateral faces, through its top and bottom, and through wells. Conservation of mass for a slightly compressible fluid in an elastic skeleton gives

$$\frac{\partial V_k}{\partial t}=-\nabla\cdot\mathbf Q_k+(\text{vertical inflow})-(\text{vertical outflow})-\sum_iQ_{ki}\,\delta(\mathbf x-\mathbf x_i),\tag{1}$$

where $V_k$ is the water volume per unit plan area and $\mathbf Q_k$ is the horizontal discharge per unit width. Under the Dupuit assumption (A1) the head does not change across the thickness, so Darcy's law $\mathbf q=-K_k\nabla h_k$ integrates over the saturated thickness to

$$\mathbf Q_k=-K_k\,b_k\,\nabla h_k=-T_k\nabla h_k .\tag{2}$$

In a confined aquifer the stored volume changes with head through compression of water and skeleton: $\partial V_k/\partial t=S_{s,k}b_k\,\partial h_k/\partial t=S_k\,\partial h_k/\partial t$. In the unconfined aquifer the saturated thickness is $h_1-z_0$, so $b_1$ in (2) is replaced by $h_1-z_0$. The stored volume changes mainly by drainage at the moving water table, $\partial V_1/\partial t=\mu\,\partial h_1/\partial t$; elastic storage of the saturated part is small against $\mu$ and is neglected. At the top of aquifer 1 water enters by recharge $W$ and leaves by evaporation $E$. Through the face it shares with aquitard $j$, aquifer $j$ loses the downward flux $q^+_j$ and aquifer $j+1$ gains $q^-_j$. Inserting these terms into (1) gives

$$\mu\frac{\partial h_1}{\partial t}=\nabla\cdot\big(K_1(h_1-z_0)\nabla h_1\big)+W-E(h_1)-q^{+}_1-\sum_i Q_{1i}\delta(\mathbf x-\mathbf x_i),\tag{3}$$

$$S_2\frac{\partial h_2}{\partial t}=\nabla\cdot(T_2\nabla h_2)+q^{-}_1-q^{+}_2-\sum_i Q_{2i}\delta(\mathbf x-\mathbf x_i),\tag{4}$$

$$S_3\frac{\partial h_3}{\partial t}=\nabla\cdot(T_3\nabla h_3)+q^{-}_2-\sum_i Q_{3i}\delta(\mathbf x-\mathbf x_i).\tag{5}$$

The base of aquifer 3 is taken as impermeable. A leaky base would add a term of the same form as $q^+_j$.

**Derivation of the aquitard equation**

Let $\zeta\in[0,b'_j]$ be the depth below the top of aquitard $j$. Mass conservation in a volume element of the aquitard reads $S'_{s,j}\,\partial u_j/\partial t=-\nabla\cdot\mathbf q'$, with the Darcy flux $\mathbf q'=-K'_j\nabla u_j$. The horizontal part of $\nabla\cdot\mathbf q'$ relates to the vertical part as $(b'/L)^2$, where $L$ is the horizontal length over which the head changes. For an aquitard a few metres thick and $L$ of tens to hundreds of metres this ratio is small. In addition, refraction at a contrast $K'\ll K$ turns the streamlines in the aquitard nearly vertical [7]. Keeping only the vertical part, with $q_z=-K'_j\,\partial u_j/\partial\zeta$ positive downward, gives

$$S'_{s,j}\frac{\partial u_j}{\partial t}=-\frac{\partial q_z}{\partial\zeta}=K'_j\frac{\partial^2u_j}{\partial\zeta^2},\qquad 0<\zeta<b'_j.\tag{6}$$

At each face the aquitard and the aquifer share one head, because a jump would require an infinite flux. The face fluxes are the Darcy fluxes of the aquitard evaluated at the faces:

$$u_j|_{\zeta=0}=h_j,\qquad u_j|_{\zeta=b'_j}=h_{j+1},\tag{7}$$

$$q^{+}_j=-K'_j\frac{\partial u_j}{\partial\zeta}\Big|_{\zeta=0},\qquad q^{-}_j=-K'_j\frac{\partial u_j}{\partial\zeta}\Big|_{\zeta=b'_j}.\tag{8}$$

Here $K'_j$, $b'_j$ and $S'_{s,j}$ may vary with $(x,y)$. Equations (7) and (8) express continuity of head and flux.

Integrating (6) over the aquitard thickness and using (8) gives

$$\frac{d}{dt}\int_0^{b'_j}S'_{s,j}u_j\,d\zeta=q^+_j-q^-_j .\tag{9}$$

The difference between the inflow at the top and the outflow at the bottom is the rate of change of the water stored in the aquitard. If $S'_s=0$, the right-hand side of (6) vanishes, $u_j$ is linear in $\zeta$ and (8) reduces to

$$q^+_j=q^-_j=\frac{K'_j}{b'_j}\,(h_j-h_{j+1}).\tag{10}$$

This is the storage-free exchange used by Ravshanov et al. [1]. The coupled model (3)–(8) contains (10) as the limit $S'_s\to0$.

Evaporation follows the law of Averyanov:

$$E(h_1)=E_0\Big(1-\frac{z_s-h_1}{\Delta}\Big)^n\ \text{ for } 0\le z_s-h_1\le\Delta,\qquad E=0\ \text{ for } z_s-h_1>\Delta.\tag{11}$$

Initial heads $h_k^0$ are taken from the steady state without wells, which makes the initial aquitard heads $u_j^0$ linear in $\zeta$. Boundary conditions are prescribed head $h_k=g_k$ on $\Gamma_{D,k}$ and no flow $T_k\,\partial h_k/\partial n=0$ on $\Gamma_{N,k}$.

**Global balance and time scales**

Integrating (3)–(5) over $\Omega$ and adding (9) integrated over $\Omega$ for both aquitards, the exchange terms $q^\pm_j$ cancel:

$$\frac{d}{dt}\Big[\int_\Omega(\mu h_1+S_2h_2+S_3h_3)\,d\mathbf x+\sum_j\int_\Omega\!\int_0^{b'_j}S'_{s,j}u_j\,d\zeta\,d\mathbf x\Big]=\int_\Omega(W-E)\,d\mathbf x-\sum Q+\sum_k\oint_{\Gamma_{D,k}}T_k\frac{\partial h_k}{\partial n}\,ds.\tag{12}$$

The storage change of the aquifers plus that of the aquitards equals recharge minus evaporation, minus pumping, plus boundary inflow. The discrete scheme of Section 2.2 reproduces (12) exactly (Lemma 1).

With the dimensionless depth $\xi=\zeta/b'$ and time $\theta=t/t_c$, equation (6) becomes $\partial u/\partial\theta=\partial^2u/\partial\xi^2$ when

$$t_c=\frac{b'^2S'_s}{K'}=\frac{b'S'}{K'},\qquad S'=S'_sb'.\tag{13}$$

For $t\ll t_c$ the aquitard responds only near its faces and releases water from storage; for $t\gg t_c$ its head profile approaches the linear profile of (10). The memory time of Herrera and Figueroa [15], $3S'b'/(\pi^2K')$, equals $0.30\,t_c$. The time scale (13) says how fast the aquitard equilibrates, but not how much water it releases compared with the aquifers. That is measured by the storage ratio

$$\varepsilon=S'\Big/\sum_kS_k,\tag{14}$$

which plays the role of $S'/S$ in the solutions of Hantush [7] and Neuman and Witherspoon [8].

### 2.2. Numerical Method

**Finite-volume discretisation of the aquifers**

$\Omega$ is covered by a tensor-product grid with variable spacing; cells outside $\Omega$ are inactive. Integrating (4) over cell $P$ with area $A_P$ and over the step $[t^n,t^{n+1}]$, and applying the divergence theorem to the flux term, gives

$$\int_{t^n}^{t^{n+1}}\!\!\int_{A_P}S\,\frac{\partial h}{\partial t}\,dA\,dt=\int_{t^n}^{t^{n+1}}\Big[\sum_{Q}\int_{e_{PQ}}T\,\frac{\partial h}{\partial n}\,d\ell+\int_{A_P}(q^--q^+)\,dA-Q_P\Big]dt ,\tag{15}$$

where $e_{PQ}$ is the face shared with neighbour $Q$. Three approximations turn (15) into an algebraic equation: the head in a cell is represented by its value at the cell centre; the integrals in time are evaluated at $t^{n+1}$ (backward Euler); and the flux through $e_{PQ}$ is approximated from the two neighbouring centre values.

The face flux is derived as follows. Let $T_P$ and $T_Q$ be constant in each cell, $d_P$ and $d_Q$ the cell widths normal to the face, and $h_e$ the unknown head on the face. Darcy's law on the two half-cells gives the same flux per unit face length, $F=2T_P(h_P-h_e)/d_P=2T_Q(h_e-h_Q)/d_Q$. Eliminating $h_e$ gives $F=(h_P-h_Q)\big/\big(d_P/2T_P+d_Q/2T_Q\big)$, so the face conductance is

$$C_{PQ}=\ell_{PQ}\Big(\frac{d_P}{2T_P}+\frac{d_Q}{2T_Q}\Big)^{-1},\tag{16}$$

where $\ell_{PQ}$ is the face length. This is the harmonic mean of the two transmissivities. It keeps the flux continuous across a jump in $T$ and is exact when $T$ is piecewise constant. In aquifer 1 we set $T_1=K_1\max(h_1-z_0,b_{\min})$ with a small $b_{\min}>0$, so that a cell that drains does not decouple. The resulting equation for cell $P$ is

$$\frac{S_PA_P}{\tau}(h_P^{n+1}-h_P^n)+\sum_QC_{PQ}(h_P^{n+1}-h_Q^{n+1})+A_P(q^+_P-q^-_P)^{n+1}=A_P(W-E)_P^{n+1}-Q_P,\tag{17}$$

with $S_P=\mu$ in aquifer 1. A well enters as a point sink in the cell that contains it.

**Discretisation of the aquitard columns**

In each aquifer cell the aquitard below it is a vertical column. The column is divided into $M$ sublayers of thickness $\delta=b'/M$, with nodes at the sublayer centres $\zeta_m=(m-\tfrac12)\delta$. Integrating (6) over sublayer $m$ and over the step gives

$$\frac{S'_s\delta}{\tau}(u_m^{n+1}-u_m^n)=c_{m-1/2}(u_{m-1}^{n+1}-u_m^{n+1})+c_{m+1/2}(u_{m+1}^{n+1}-u_m^{n+1}),\qquad m=1,\dots,M,\tag{18}$$

with $u_0=h_j$ and $u_{M+1}=h_{j+1}$. Between two interior nodes the distance is $\delta$, so the conductance is $c=K'/\delta$. The first and last nodes lie $\delta/2$ from the faces, where the head equals the aquifer head by (7), so the end conductance is $c_e=2K'/\delta$. The face fluxes that enter (17) are the end fluxes of (18):

$$q^+=c_e(h_j-u_1),\qquad q^-=c_e(u_M-h_{j+1}).\tag{19}$$

Because (17) and (18) use the same flux (19), the water that leaves an aquifer through a face enters the aquitard exactly. The truncation error of (18) is $O(\tau+\delta^2)$.

**Condensation of the aquitards**

In each column (18) is a symmetric tridiagonal system $\mathfrak Tu=s\,u^n+c_ee_1h_j+c_ee_Mh_{j+1}$, with $s=S'_s\delta/\tau$, where $e_1$ and $e_M$ are the first and last unit vectors. The system is linear and its right-hand side depends on the two aquifer heads only through the last two terms. By superposition the solution is

$$u=a+\alpha\,h_j+\beta\,h_{j+1},\qquad \mathfrak Ta=su^n,\ \ \mathfrak T\alpha=c_ee_1,\ \ \mathfrak T\beta=c_ee_M.\tag{20}$$

The three vectors $a$, $\alpha$, $\beta$ are found with one Thomas (progonka) sweep for three right-hand sides. Substituting $u_1$ and $u_M$ from (20) into (19) makes the face fluxes linear in the two aquifer heads:

$$\begin{pmatrix}q^+\\-q^-\end{pmatrix}=\Lambda\begin{pmatrix}h_j\\h_{j+1}\end{pmatrix}-c_e\begin{pmatrix}a_1\\a_M\end{pmatrix},\qquad\Lambda=c_e\begin{pmatrix}1-\alpha_1&-\beta_1\\-\alpha_M&1-\beta_M\end{pmatrix}.\tag{21}$$

The tridiagonal solves are vectorised over all columns and depend only on $\tau$ and $u^n$, so they are done once per step. Inserting (21) into (17) gives one sparse symmetric system for the aquifer heads. After it is solved, $u$ is recovered from (20). For $M=0$ the column has no storage and $\Lambda=(K'/b')\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, which is (10).

**Nonlinearity and algorithm**

$T_1(h_1)$ and $E(h_1)$ are handled by Picard iteration. At iterate $r$ we use $T_1(h^{(r)})$ and expand $E$ in a Taylor series about $h^{(r)}$, keeping the linear term:

$$E(h^{(r+1)})\approx E(h^{(r)})+E'(h^{(r)})\,(h^{(r+1)}-h^{(r)}).\tag{22}$$

The derivative $E'=nE_0(1-d/\Delta)^{n-1}/\Delta$, with $d=z_s-h_1$, is non-negative, so the term $A_PE'h^{(r+1)}$ moves to the left-hand side and adds to the diagonal. Iteration stops when $\max|h^{(r+1)}-h^{(r)}|<10^{-8}$ m.

Algorithm 1 (one time step):

1. condense the aquitards: solve (20) for $a$, $\alpha$, $\beta$ in all columns;
2. repeat until converged: assemble $T_1$ and the linearised $E$, then solve the sparse system (17) with (21);
3. recover $u$ from (20);
4. evaluate the water budget.

### 2.3. Properties of the Scheme

Let $\mathbb A=D/\tau+\mathbb L$ be the matrix of the full system (17)–(18), including the aquitard unknowns. $D$ is diagonal with entries $S_PA_P$ and $S'_s\delta A_P$. $\mathbb L$ collects the horizontal and vertical conductances.

**Lemma 1 (discrete mass balance)**

Summing (17) over all free cells and (18) over all sublayers gives

$$\Delta V_\mathrm{aquifers}+\Delta V_\mathrm{aquitards}=\tau\Big[\sum A(W-E_\mathrm{lin})-\sum Q+B_D\Big]$$

exactly, where $B_D$ is the inflow from prescribed-head cells.

Proof. $C_{PQ}$ is symmetric, so horizontal fluxes cancel in pairs. The fluxes in (21) are identical to the face fluxes (19), so the vertical fluxes also cancel. □

**Lemma 2 (condensed exchange)**

$\Lambda$ is symmetric, its off-diagonal entries are non-positive and its row sums are non-negative. Hence $\Lambda$ is positive semi-definite, and the condensed aquifer matrix is a symmetric M-matrix.

Proof. $\mathfrak T$ is a strictly diagonally dominant M-matrix, so $\mathfrak T^{-1}\ge0$ and therefore $\alpha,\beta\ge0$. Symmetry of $\mathfrak T$ gives $\alpha_M=\beta_1$. From $\mathfrak T\mathbb 1=s\mathbb 1+c_ee_1+c_ee_M$ we obtain $1-\alpha_m-\beta_m=(\mathfrak T^{-1}s\mathbb 1)_m\ge0$. □

**Theorem 1 (unconditional stability)**

For confined aquifers without evaporation and with homogeneous prescribed heads,

$$\|h^{n+1}\|_D\le\|h^n\|_D+\tau\|D^{-1}F^{n+1}\|_D$$

for every $\tau>0$, every $M$, every grid and all positive parameter fields. Here $\|v\|^2_D=v^{\top}Dv$.

Proof. Take the inner product of $\mathbb Ah^{n+1}=Dh^n/\tau+F$ with $h^{n+1}$. Use $(h^{n+1})^{\top}\mathbb Lh^{n+1}\ge0$ and the Cauchy–Schwarz inequality. □

Because $D$ contains the aquitard storage, the estimate also bounds the aquitard heads.

**Theorem 2 (discrete maximum principle)**

$\mathbb A$ is an M-matrix. Without sources, the new heads in aquifers and aquitards lie between the minimum and the maximum of the old heads and the boundary heads.

The scheme is therefore monotone for any $\tau$. In particular, it produces no oscillations at abrupt contrasts in $K$ or $K'$, a property that Crank–Nicolson keeps only under a step restriction. In the nonlinear case each Picard matrix is also an M-matrix, because $T_1\ge K_1b_{\min}>0$ and $E'\ge0$, so each iterate is well defined. We do not prove convergence of the Picard iteration in general. Its iteration count is reported for every run.

**Convergence**

The local truncation error is $O(\tau+h^2+\delta^2)$ for smooth solutions. Together with Theorem 1, this gives convergence of the same order in the $D$-norm for the linear problem. On non-uniform grids, the cell-centred scheme is known to keep second-order global accuracy despite first-order local truncation [16]. We check the orders numerically in Section 3.1.

## 3. Results

### 3.1. Verification

**Analytical and semi-analytical references**

For homogeneous confined layers and a well with constant rate, we transform (4)–(8) to the Laplace domain. There, (6) is solved exactly. With $\lambda=b'\sqrt{pS'_s/K'}$, the aquitard fluxes are

$$\bar q^+=\frac{K'}{b'}\lambda\,(\coth\lambda\,\bar h_j-\operatorname{csch}\lambda\,\bar h_{j+1}),\qquad \bar q^-=\frac{K'}{b'}\lambda\,(\operatorname{csch}\lambda\,\bar h_j-\coth\lambda\,\bar h_{j+1}).$$

The aquifer system is diagonalised in symmetric form and solved with modified Bessel functions $K_0$, following the approach of Hemker [9]. The result is inverted with the Stehfest [17] algorithm with 12 terms. This reference reproduces the Theis [18] solution to a relative difference of $10^{-5}$. It also reproduces the Hantush–Jacob [19] solution to $10^{-4}$, the latter by giving the upper aquifer a very large $T$ and $S$ and the aquitard no storage (`testlar/test_masala1.py`).

**Three aquifers with storage in both aquitards**

The test problem is $T=200$, 100, 300 m²/d; $S=2$, 1, $3\times10^{-4}$; $K'=2\times10^{-3}$ and $10^{-3}$ m/d; $b'=5$ and 8 m; $S'_s=10^{-4}$ m⁻¹. A well pumps 500 m³/d from aquifer 2. The grid is telescopic, 105×105 cells, with a 2 m central cell growing by a factor 1.15 out to 20 km. Each aquitard has $M=20$ sublayers. Time steps start at $10^{-4}$ d and grow by a factor of 1.05 up to 10 d. The maximum relative difference from the Laplace reference over $10^{-3}$–10 d is 0.22% (aquifer 1), 0.68–0.74% (aquifer 2) and 0.33% (aquifer 3) (`tajribalar/t3_modflow.py`). With a growth factor of 1.2, the differences in aquifers 1 and 3 rise to 1.2–1.8%. This identifies the first-order time error as the dominant part.

**Comparison with MODFLOW 6**

The same problem was built in MODFLOW 6 [20] with each aquitard as 20 model layers (K33 $=K'$, SS $=S'_s$) and K33 $=10^6$ m/d in the aquifers: 43 layers in all, with identical time steps. Heads at nine observation points agree with our code to at most $4\times10^{-9}$ m. Both codes differ from the Laplace reference by the same amount. The two codes solve the same discrete equations. Ours does it with a sparse system over 3 rather than 43 layers, plus independent tridiagonal solves.

**Grid and time-step convergence and mass balance**

**Table 1.** Aquitard column ($K'=10^{-2}$ m/d, $b'=2$ m, $S'_s=10^{-2}$ m⁻¹) after a unit step in head on the upper face; relative error of the face flux $q^+$ at $t=0.5$ d against the series solution, $\tau=10^{-4}$ d.

| $M$ | relative error of $q^+$ | observed order |
|---|---|---|
| 4 | $3.9\times10^{-2}$ | |
| 8 | $8.5\times10^{-3}$ | 2.20 |
| 16 | $2.1\times10^{-3}$ | 2.00 |
| 32 | $5.8\times10^{-4}$ | 1.86 |

The slight drop at $M=32$ comes from the time-discretisation error, which at $\tau=10^{-4}$ d is of the same size.

Table 2 checks the coupled three-aquifer scheme as a whole (`tajribalar/t8_yaqinlashish.py`). The domain is 1000 × 1000 m with no-flow boundaries. $K_1$ and $K_2$ vary smoothly in $x$ and $y$, as does $K'$ of aquitard 1. Both aquitards have storage ($b'=4$ m, $S'_s=2\times10^{-3}$ m⁻¹). The initial head is a Gaussian mound of 1 m in aquifer 1, and the solution is compared at $t=5$ d. In space, the cell size $h$ and the sublayer thickness $\delta$ are halved together, and errors are root-mean-square differences of the three aquifer heads from cell averages of a 160 × 160, $M=32$ solution. In time, $\tau$ is halved on a 40 × 40, $M=8$ grid against $\tau=1/256$ d.

**Table 2.** Grid and time-step convergence of the coupled scheme, root-mean-square head error at $t=5$ d.

| $n\times n$, $M$ | error (m) | order | $\tau$ (d) | error (m) | order |
|---|---|---|---|---|---|
| 20 × 20, 4 | $1.49\times10^{-4}$ | | 0.5 | $8.0\times10^{-4}$ | |
| 40 × 40, 8 | $3.55\times10^{-5}$ | 2.07 | 0.25 | $3.95\times10^{-4}$ | 1.02 |
| 80 × 80, 16 | $7.10\times10^{-6}$ | 2.32 | 0.125 | $1.94\times10^{-4}$ | 1.03 |
| | | | 0.0625 | $9.39\times10^{-5}$ | 1.05 |

The orders confirm $O(h^2+\delta^2+\tau)$. The value 2.32 on the finest grid is slightly inflated because that grid is only one refinement away from the reference.

Under time refinement of a single aquitard column the order is also 1. For a heterogeneous, irregularly shaped problem with all processes active, the mass-balance residual is below $10^{-10}$ per step. As $S'_s\to0$ the solution converges to the storage-free model (difference $<10^{-8}$ m).

**Dalem pumping test**

The Dalem test is given in Table 4.2 of Kruseman and de Ridder [21]. The pumping rate is $Q=761$ m³/d, with four piezometers at 30–120 m. We fitted it with the Laplace reference, holding the head in the upper aquifer constant.

**Table 3.** Dalem pumping test: parameters and root-mean-square misfit of three interpretations (`tajribalar/t4_dalem.py`).

| Interpretation | $KD$ (m²/d) | $S$ | $c$ (d) | $S'$ | RMSE (mm) |
|---|---|---|---|---|---|
| Walton type curve [21] | 1731 | $1.9\times10^{-3}$ | 468 | | 6.9 |
| storage-free aquitard, least squares | 1674 | $1.77\times10^{-3}$ | 325 | | 5.87 |
| aquitard with storage, least squares | 1670 | $1.52\times10^{-3}$ | 370 | $1.1\times10^{-3}$ | 5.80 |

Including storage barely reduces the misfit, and $S'$ is poorly identified: the standard deviation of $\log_{10}S'$ is 0.41. The test spans 0.015–0.33 d, comparable to the fitted $t_c\approx0.4$ d. The data therefore validate the model but cannot confirm aquitard storage from the drawdown in the aquifer alone. The fitted $S'=1.1\times10^{-3}$ nevertheless agrees with the value $S'=1.1\times10^{-3}$ that Kruseman and de Ridder ([21], pp. 97–98) derive from the ratio method of Neuman and Witherspoon, which uses an additional piezometer inside the aquitard ($D'=8$ m, $K'D'/S'=126$ m²/d). Their averaged parameters are $KD=1800$ m²/d, $S=1.7\times10^{-3}$ and $c=450$ d. The measured drawdowns had been corrected for partial penetration and tidal influence before publication; we use them as given.

**Published multilayer examples**

Olsthoorn [22] lists drawdowns for two aquifers ($kD=100$, $S=10^{-4}$) between three aquitards with storage ($c=100$, $S'=0.0016$), with zero drawdown above and below the system, at $r=10$ and $t=10^{-5}$–5. The column states that these values equal those of Hemker and Maas [10]. Our Laplace solution, extended with the two outer aquitards, reproduces all 36 tabulated values to the four printed decimals (`testlar/test_masala1.py`). The numerical model, with the outer heads represented by two fixed-head layers and $M=20$ sublayers per aquitard, differs from the reference at the nearest grid radius ($r=10.69$) by at most 0.25% for $t\ge10^{-3}$ (`tajribalar/t7_maas_mlu.py`). Larger differences occur only in the first time steps.

The "Two-aquifers" verification example of the MLU tutorial [23] is a phreatic layer, a 10 m aquitard and a pumped aquifer ($Q=180$ m³/d). There, aquitard storage and horizontal flow are carried by three thin layers, giving six layers in all. Our Laplace solution gives 0.29826 m at $r=5.01$ m after 1 min, the MLU value to all printed digits, and 0.0496 m at 15.85 m, where MLU prints 0.050 m. The numerical model applied to the same six-layer system differs from the reference by 0.04% and 0.3% at the two nearest grid radii.

### 3.2. When Can Aquitard Storage Be Neglected?

We take the configuration of Section 3.1 with $K'=10^{-3}$ m/d and $b'=5$ m, so that $t_c=2.5$ d. Aquifer storage is scaled to give $\varepsilon=0.083$–83. We compare the storage and storage-free models at $r=30$ m (Figure 2).

**Table 4.** Relative difference between the models with and without aquitard storage in the pumped aquifer at $r=30$ m (`tajribalar/t2_tc_mezoni.py`).

| $\varepsilon$ | last $t/t_c$ at which the difference exceeds 5% | difference at $t=10^3\,t_c$ |
|---|---|---|
| 0.083 | 0.25 | 0.4% |
| 0.83 | 0.79 | 2.3% |
| 8.3 | $>10^3$ | 6.6% |
| 83 | $>10^3$ | 12% |

![](t2_tc_mezoni_en.png){width=16cm}

**Figure 2.** Relative difference $|s-s_0|/s$ (%) between drawdown $s$ with aquitard storage and $s_0$ without it, plotted against dimensionless time $t/t_c$ for four values of $\varepsilon$; (a) pumped aquifer 2, (b) adjacent aquifer 1.

For a fixed $\varepsilon$, the curves plotted against $t/t_c$ coincide. For small $\varepsilon$ the storage-free model becomes adequate shortly after $t_c$. For $\varepsilon\gtrsim1$ it does not, because in a closed system the water released from the aquitards keeps adding to the effective storage. In the adjacent, unpumped aquifer the difference is larger still: 10% at $10^3\,t_c$ for $\varepsilon=0.83$. A rule based on $t_c$ alone would wrongly accept the storage-free model in these cases.

### 3.3. Heterogeneous Field with an Unconfined Top Aquifer

The domain is 2000 × 1000 m with 80 × 40 cells. Aquifer 1 is unconfined, with a low-$K$ lens and a sinuous high-$K$ channel. $K_2(x,y)$ is smoothly varying with a lens, and $K_3$ has two zones. Aquitard 1 contains a window with 20 times larger $K'$. Recharge is $6\times10^{-4}$ m/d; evaporation has $E_0=1.5\times10^{-3}$ m/d, $\Delta=3$ m and $n=1.5$. Heads are prescribed on the left and right sides. Four wells pump 3200 m³/d in total, three in aquifer 2 and one in aquifer 3, starting from the steady state.

With thin aquitards ($t_c=11$ and 32 d), heterogeneity doubles the maximum drawdown in aquifer 2 relative to a homogeneous field (10.5 m against 5.6 m). It also transmits drawdown to the water table through the window (0.67 m against 0.05 m). Aquitard storage supplies 0.6% of the pumped water over one year and changes the drawdown by less than 0.5% (`tajribalar/t5_geterogen.py`).

With thick clay aquitards ($b'=15$ and 20 m, $K'=10^{-4}$ and $5\times10^{-5}$ m/d, $S'_s=4\times10^{-4}$ m⁻¹), $t_c=900$ and 3200 d, longer than the simulated year. Recharge is held constant so that all changes come from pumping (Figure 3).

![](t6_qalin_ajratuvchi_en.png){width=16cm}

**Figure 3.** Thick clay aquitards: (a) drawdown at four points with aquitard storage (solid) and without it (dashed); (b) sources of the pumped water as a percentage of the total rate, for the model with storage.

Storage slows the early drawdown in aquifer 2 by 18–30%. Near $t=1$ d the aquitards supply 26% of the pumped water. Later the prescribed-head boundaries take over, and after one year the difference in the pumped aquifer is below 0.5%. The unconfined aquifer behaves differently: after one year its water table has declined by 0.051 m with storage and by 0.060 m without, a difference of 14% that is still present at the end of the run. The balance residual stays below $4\times10^{-12}$ and Picard needs at most 4 iterations per step.

## 4. Discussion

The results support a simple practical message. A storage-free aquitard model is adequate in the pumped aquifer once $t$ exceeds a few $t_c$, provided $\varepsilon$ is small. In a shallow aquifer above a thick clay layer, however, the storage-free model overestimates the decline of the water table for times shorter than $t_c$, and that decline is what drives evaporation and salt accumulation. For aquitards of the thickness typical of the irrigated plains (10–20 m of clay loam), $t_c$ is of the order of years, so the storage term should be kept.

The condensation of the aquitard columns is equivalent to the layered representation used in MODFLOW. The results agree to round-off, but our system matrix has the size of the aquifer problem only. Lemma 2 shows that this elimination preserves the M-matrix structure. Therefore positivity and stability are inherited by the condensed system rather than merely observed in tests.

The model has limits that a user should know. Aquifers 2 and 3 are assumed to stay confined, and each well is screened in one aquifer. Flow in the aquitards is vertical only. For the MLU example of Section 3.1, replacing the three storage layers by the continuous equation (6) ($b'=10$ m, $K'=0.1$ m/d, $S'=0.004$) changes the drawdown in the pumped aquifer at $r=5.01$ m by −7% after 1 min and by +1.2% after 7 d; at 15.85 m the change is −16% and +1.3%. Part of this comes from the coarse vertical lumping in the MLU representation and part from the horizontal aquitard flow that our model omits. We have not separated the two effects. The time discretisation is first order. A second-order variant such as BDF2 would lose the M-matrix property unless the step is restricted, so we kept backward Euler and control the error by step growth. Convergence of the Picard iteration is monitored in every step, not proved. Field validation rests on one classical pumping test, and that test cannot resolve aquitard storage. A test with piezometers inside the aquitard, as at Dalem, is needed for that purpose.

## 5. Conclusions

1. A three-aquifer model with a diffusion equation in each aquitard, $K(x,y)$, an unconfined top layer, recharge, evaporation and wells was derived from mass conservation and Darcy's law and solved by a finite-volume scheme that eliminates each aquitard column exactly.
2. The scheme conserves mass exactly, is unconditionally stable in the storage-weighted norm and satisfies a discrete maximum principle. The condensed exchange matrix is symmetric and positive semi-definite.
3. The code reproduces the Theis, Hantush–Jacob and Laplace-domain multilayer solutions within 0.7%. It reproduces MODFLOW 6 to $4\times10^{-9}$ m and converges at second order in space (aquifer grid and aquitard sublayers) and first order in time.
4. Whether aquitard storage can be neglected depends on $t/t_c$ and on $\varepsilon=S'/\sum S$. For $\varepsilon\gtrsim1$ the effect persists well beyond $t_c$.
5. In a heterogeneous field with thick clay aquitards, the storage-free model overestimates the water-table decline in the unconfined aquifer by about 14% after one year.

Future work: coupling with salt transport through the aquitards, and calibration against a site with aquitard piezometers.

**Author Contributions:** Conceptualization, N.R.; methodology, N.R. and J.E.; software, J.E.; validation, J.E.; formal analysis, J.E.; investigation, J.E.; writing—original draft preparation, J.E.; writing—review and editing, N.R. and J.E.; supervision, N.R. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research received no external funding.

**Data Availability Statement:** The program code, input data and scripts that produce every number and figure in this article are openly available at https://github.com/javokhir-erkinov/1-masala.

**Acknowledgments:** During the preparation of this manuscript, the authors used Claude (Anthropic) for assistance with program code, figure preparation and language editing. The authors have reviewed and edited the output and take full responsibility for the content of this publication.

**Conflicts of Interest:** The authors declare no conflicts of interest.

## Nomenclature

The following symbols are used in this manuscript:

| Symbol | Meaning | Unit |
|---|---|---|
| $h_k$ | head in aquifer $k$ | m |
| $u_j$ | head in aquitard $j$ | m |
| $K_k$, $T_k$ | hydraulic conductivity and transmissivity of aquifer $k$ | m/d, m²/d |
| $b_k$ | thickness of confined aquifer $k$ | m |
| $S_k$, $\mu$ | storage coefficient of aquifer $k$, specific yield of aquifer 1 | – |
| $S_{s,k}$ | specific storage of aquifer $k$ | 1/m |
| $K'_j$, $b'_j$ | vertical conductivity and thickness of aquitard $j$ | m/d, m |
| $S'_{s,j}$, $S'_j$ | specific storage and storage coefficient $S'_sb'$ of aquitard $j$ | 1/m, – |
| $c$ | hydraulic resistance $b'/K'$ | d |
| $\mathbf q$, $q_z$ | horizontal and vertical Darcy flux | m/d |
| $q^+_j$, $q^-_j$ | flux through the top and bottom face of aquitard $j$, positive downward | m/d |
| $W$, $E$ | recharge and evaporation rate | m/d |
| $E_0$, $\Delta$, $n$ | evaporation at the surface, extinction depth, exponent | m/d, m, – |
| $z_0$, $z_s$ | base of aquifer 1, ground surface | m |
| $Q$ | well discharge, positive for extraction | m³/d |
| $\zeta$ | depth below the top of an aquitard | m |
| $t_c$ | aquitard time scale $b'^2S'_s/K'$ | d |
| $\varepsilon$ | storage ratio $S'/\sum_kS_k$ | – |
| $\tau$, $\delta$, $M$ | time step, aquitard sublayer thickness, number of sublayers | d, m, – |
| $C_{PQ}$, $A_P$ | face conductance, cell area | m²/d, m² |
| $\Lambda$ | condensed $2\times2$ exchange matrix of an aquitard column | m/d |

Subscripts $k=1,2,3$ number the aquifers from the top and $j=1,2$ the aquitards; a prime marks an aquitard property.

## References

1. Ravshanov, N.; Shadmanov, I.; Adizova, F.; Shadmanova, K.; Sayidova, N.; Jurayeva, N.; Kamalova, M. Quasi-3D Numerical Modeling of Groundwater Flow, Particle Transport, and Clogging-Induced Interlayer Leakage in Heterogeneous Multilayer Aquifers. *Hydrology* **2026**, *13*, 276. https://doi.org/10.3390/hydrology13100276
2. Ravshanov, N.; Shadmanova, K.; Shadmanov, I. Numerical Modeling of Nonlinear Groundwater Flow in a Heterogeneous Four-Layer Porous Medium. *Hydrology* **2026**, *13*, 181. https://doi.org/10.3390/hydrology13070181
3. Karimov, M.; Yakhshiboev, M.; Rakhimova, F.; Yadgarova, L. Modeling of Groundwater Flow in a Multilayer Porous Medium Based on a Nonlinear Mathematical Model. *Proc. SPIE* **2025**, *13662*, 136620J. https://doi.org/10.1117/12.3072569
4. Mukhamadiyev, A.; Karimov, M.; Khujakulov, T.; Sattarov, O.; Cho, J. A Nonlinear Model of Three-Layer Groundwater Flow with Evaporation Dependent on the Critical Groundwater Level. *Mathematics* **2026**, *14*, 256. https://doi.org/10.3390/math14020256
5. Kodirov, K.R. Mathematical Models and Approximate Analytical Methods of Mass Transfer in Multilayer Media. Ph.D. Thesis, Digital Technologies and Artificial Intelligence Development Research Institute, Tashkent, Uzbekistan, 2023. (In Russian)
6. Ravshanov, N.; Kodirov, K.; Islamov, Yu.N.; Kukanova, M.A. Mathematical Model of Flow Filtration in a Three-Layer Stratum and Its Analytical Solution. *Probl. Comput. Appl. Math.* **2017**, *1*, 47–53. (In Russian)
7. Hantush, M.S. Modification of the Theory of Leaky Aquifers. *J. Geophys. Res.* **1960**, *65*, 3713–3725. https://doi.org/10.1029/JZ065i011p03713
8. Neuman, S.P.; Witherspoon, P.A. Theory of Flow in a Confined Two Aquifer System. *Water Resour. Res.* **1969**, *5*, 803–816. https://doi.org/10.1029/WR005i004p00803
9. Hemker, C.J. Transient Well Flow in Leaky Multiple-Aquifer Systems. *J. Hydrol.* **1985**, *81*, 111–126. https://doi.org/10.1016/0022-1694(85)90170-2
10. Hemker, C.J.; Maas, C. Unsteady Flow to Wells in Layered and Fissured Aquifer Systems. *J. Hydrol.* **1987**, *90*, 231–249. https://doi.org/10.1016/0022-1694(87)90069-2
11. Cihan, A.; Zhou, Q.; Birkholzer, J.T. Analytical Solutions for Pressure Perturbation and Fluid Leakage through Aquitards and Wells in Multilayered-Aquifer Systems. *Water Resour. Res.* **2011**, *47*, W10504. https://doi.org/10.1029/2011WR010721
12. Herrera, I.; Yates, R. Integrodifferential Equations for Systems of Leaky Aquifers and Applications: 3. A Numerical Method of Unlimited Applicability. *Water Resour. Res.* **1977**, *13*, 725–732. https://doi.org/10.1029/WR013i004p00725
13. Leake, S.A.; Leahy, P.P.; Navoy, A.S. *Documentation of a Computer Program to Simulate Transient Leakage from Confining Units Using the Modular Finite-Difference Ground-Water Flow Model*; Open-File Report 94-59; U.S. Geological Survey: Reston, VA, USA, 1994. https://doi.org/10.3133/ofr9459
14. Hughes, J.D.; Leake, S.A.; Galloway, D.L.; White, J.T. *Documentation for the Skeletal Storage, Compaction, and Subsidence (CSUB) Package of MODFLOW 6*; Techniques and Methods 6-A62; U.S. Geological Survey: Reston, VA, USA, 2022. https://doi.org/10.3133/tm6A62
15. Herrera, I.; Figueroa V., G.E. A Correspondence Principle for the Theory of Leaky Aquifers. *Water Resour. Res.* **1969**, *5*, 900–904. https://doi.org/10.1029/WR005i004p00900
16. Forsyth, P.A.; Sammon, P.H. Quadratic Convergence for Cell-Centered Grids. *Appl. Numer. Math.* **1988**, *4*, 377–394. https://doi.org/10.1016/0168-9274(88)90016-5
17. Stehfest, H. Algorithm 368: Numerical Inversion of Laplace Transforms. *Commun. ACM* **1970**, *13*, 47–49. https://doi.org/10.1145/361953.361969
18. Theis, C.V. The Relation between the Lowering of the Piezometric Surface and the Rate and Duration of Discharge of a Well Using Ground-Water Storage. *Trans. Am. Geophys. Union* **1935**, *16*, 519–524. https://doi.org/10.1029/TR016i002p00519
19. Hantush, M.S.; Jacob, C.E. Non-Steady Radial Flow in an Infinite Leaky Aquifer. *Trans. Am. Geophys. Union* **1955**, *36*, 95–100. https://doi.org/10.1029/TR036i001p00095
20. Langevin, C.D.; Hughes, J.D.; Banta, E.R.; Niswonger, R.G.; Panday, S.; Provost, A.M. *Documentation for the MODFLOW 6 Groundwater Flow Model*; Techniques and Methods 6-A55; U.S. Geological Survey: Reston, VA, USA, 2017. https://doi.org/10.3133/tm6A55
21. Kruseman, G.P.; de Ridder, N.A. *Analysis and Evaluation of Pumping Test Data*, 2nd ed.; ILRI Publication 47; International Institute for Land Reclamation and Improvement: Wageningen, The Netherlands, 1990.
22. Olsthoorn, T.N. Matlab Function hantushn (Column of C. Maas). *Stromingen* **2003**, *9*, 48–50. (In Dutch)
23. Hemker, C.J.; Randall, J. *Modeling with MLU: Applying the Multilayer Approach to Aquifer Test Analysis*; Tutorial; Microfem: Amsterdam, The Netherlands, 2010.
