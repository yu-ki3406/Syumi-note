# Syumi-note 📚

![Commit Activity](https://img.shields.io/github/commit-activity/m/yu-ki3406/Syumi-note)
![File Count](https://img.shields.io/github/directory-file-count/yu-ki3406/Syumi-note/notebooks)

## インストール方法 🛠️

Anacondaを使用している場合、以下のコマンドで環境を構築し、`syumi-note`をインストールできます。

```shell
conda create --name syumi-note python==3.9
conda activate syumi-note
python setup.py install
```

---

## 概要 📝

このリポジトリは, 日々の勉強(主に強化学習に関するもの)について記録を残すために作っています，

## 目次📋


- 確率論
  - [Hoeffdingの不等式](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Hoeffding_inequality.ipynb "Hoeffding_inequality")
  - [Bernsteinの不等式](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Bernstein_inequality.ipynb "Bernstein_inequalit")
  - [中心極限定理](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Central_limit_theorem.ipynb 'CLT') 
  - [lim_sup,lim_infの解説](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/lim_sup_inf.ipynb 'lim_supinf')
  - [重点サンプリング](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/importance_sampling.ipynb 'imp_samp')
  - [マルチンゲール (2023.5.18)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Martingale.ipynb 'mar')
  - [期待値と極限の順序交換(2023.06.10)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Change_E_Lim.ipynb 'e_lim')
- バンディット問題
  - [Explore-then-commit](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/explore_then_commit.ipynb "ETC")  
  - [Lin-UCB(under construction)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/LinUCB.ipynb "Lin-UCB")  
  - [Thompson_sampling](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Thompson_sampling.ipynb 'TS_bandit') 
  - [UCB ](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/UCB.ipynb 'ucb')
  - [理論限界について](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Theoretical_limit.ipynb 'tl')
  - [非定常の報酬のバンディット](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/nonstational_bandit.ipynb 'non_sta')
  - [Posterior_Samplingを使ったバンディット](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Posterior_sampling_bandit.ipynb)
  - [弱学習器を使ったUCBアルゴリズム](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/weaker_learner_bandit.ipynb 'weak')
- 関数解析
  - [凸包について](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Convex_Hull.ipynb 'conv')
  - [リプシッツ連続](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Lipschitz_continuity.ipynb 'LP')
  - [イェンセンの不等式](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Jensens_inequality.ipynb 'je')
  - [統計的学習理論](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Statistical_Learning_Theory.ipynb 'the')
  - [疑似逆行列(2023.06.11)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Moore_Penrose_Pseudoinverse.ipynb 'MPPM')
- 強化学習
  - [強化学習の基本](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/reinforcement_learing_exercise.ipynb 'RL')
  - [価値反復法](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Value_iteration.ipynb 'VI')
  - [方策反復法](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Policy_iteration.ipynb 'PI')
  - [Fitted_Q_Iteration](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/fitted_Q_iteration.ipynb 'FQI')
  - [greedy方策+エントロピー](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Greedy_with_entropy.ipynb 'rl')
  - [Mellowmax作用素について](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/mellowmax.ipynb 'mrl')
  - [Conservative_Value_Iteration](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Conservative_Value_iteration.ipynb 'cvi')
  - [ベルマン残差と期待値二乗TD誤差について(途中)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/bellman_residual.ipynb 'rl_resi')
  - [損失関数のノイズについて](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/RL_Loss_Noise.ipynb 'loss_n')
  - [強化学習のmax作用素について](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/RL_max_operator.ipynb 'max_operator')
  - [ε-greedyh法が良くない説明(コード自信ない)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/epsilon_greedy.ipynb 'eps-g')
  - [Conservative_Policy_Iteration(CPI)(説明も後で追加)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Conservative_Policy_Iteration.ipynb 'CPI')
  - [Log_Sum_Expを使用してmaxVの近似誤差](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Log_Sum_Exp.ipynb 'log_sum')
  - [OptCMDP(エラーで詰まってる)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Opt_CMDP.ipynb 'cmdp')
  - [線形計画法で強化学習](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/LP_reinforcement_learning.ipynb 'LP_RL')
  - [Asynchronous_Q-learning](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Asynchronous_Q_Learning.ipynb 'asyn')
  - [Robust_MDP(2023.05.12)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Robust_MDP.ipynb 'RMDP')
  - [GMBL(2023.5.14)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Optimistic_GMBL.ipynb 'gmbl')
  - [TD(λ)法の実装と説明(2023.5.26)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/TD_leanring.ipynb 'tdr')
  - [KLダイバージェンスをフィッシャ情報量行列で近似(2023.05.28)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/KL_and_Fisher.ipynb 'KLF')
  - [Natural_Policy_Gradient(2023.05.31)まだ途中](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/NPG.ipynb 'NPG')
  - [NPG_CMDP(2023.06.04)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/NPG_CMDP.ipynb 'NPG_CMDP')
  - [Sample_NPG_CMDP(2023.06.07)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Sample_CMDP_NPG.ipynb 'sample_n')
  - [方策のロバスト性(2023.06.18)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Tradeoff_bet_plan_robust.ipynb 'robust_policy')
  - [Tsallisエントロピーを使った価値反復法(2023.06.21)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Tsallis_Value_Iteration.ipynb 'tsa')
  - [分位点動的計画法(1日目)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Quantile_Dynamic_Programming.ipynb)
- 最適化
  - [Projected_Gradient_Descent](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Projected_Gradient_Descent.ipynb 'PGD')
  - [pulp(数理最適化ライブラリ)の基本的な実装例](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Mathematical_optimization.)
  - [非凸関数のsaddle pointsについて](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Saddle_point.ipynb 'sad')
  - [非凸関数の収束しない例](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/NonConvex_Optimization.ipynb 'nonc')
  - [KKT条件(2023.6.25)](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/KKT_Conditions.ipynb 'kkt')
- プログラミング
  - [jaxについて](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/jax_study.ipynb)
  - [pulp(数理最適化ライブラリ)の基本的な実装例](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Mathematical_optimization.ipynb 'opt')
  - [Primal-Dual法](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Mathematical_optimization.ipynb 'pr')

- 集合と位相
  - [(2023.05.21)集合の濃度](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Cardinality.ipynb 'car')


- 資料
  - [(2023.06.26)ガウス過程回帰](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Gaussian_process.pdf)

- アドベントカレンダー 🎄
  - [(1日目)分位点動的計画法](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Quantile_Dynamic_Programming.ipynb)
  - [(2日目)分位点TD学習](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Quantile_TD_Learning.ipynb)
  - [(3日目)期待値TD学習](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Quantile_TD_Learning.ipynb)
  - [(4日目)OptPess-LP](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Opt_Pess_LP.ipynb)
  - [(5日目)CMDPの説明](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/CMDP_Explain.ipynb)
  - [(6日目)Q-sampler](https://github.com/yu-ki3406/Syumi-note/blob/main/notebooks/Q_sampler.ipynb)