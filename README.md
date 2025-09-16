# A First-Principles Physical Theory of the Information Bottleneck

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17129965.svg)](https://doi.org/10.5281/zenodo.17129965)

This repository contains the official code for the paper **"A First-Principles Physical Theory of the Information Bottleneck: From Hebbian Dynamics to Cognitive Economy"**. We propose and experimentally verify a new physical principle for the Information Bottleneck (IB) phenomenon. Our theory posits that the IB dynamic is not a temporal evolution, but a direct consequence of a meta-system's strategy to achieve "Cognitive Economy" by optimally allocating cognitive resources (model capacity, N). This is demonstrated via a novel "N-Sweep" experiment, where a series of models with capacities that first increase and then decrease are trained on a fixed task, perfectly reproducing the classic IB trajectory in our semantic state space.

---

## The Core Hypothesis: IB as Cognitive Resource Allocation

The central thesis of this work is that the classic two-phase Information Bottleneck dynamic—**Fitting followed by Compression**—is a macroscopic manifestation of a system's management of its internal cognitive resources, rather than a process that unfolds over training time.

We propose that this dynamic can be understood by simulating the allocation and de-allocation of "cognitive space" (model capacity, `N`) for a fixed task:

1.  **The Fitting Phase**: Corresponds to the meta-system allocating **increasing** internal resources (`N` increases) to robustly capture a concept's complexity. In our semantic state space, this manifests as a decrease in Cognitive Cost ($H'_{tse}$) and an increase in Semantic Robustness ($H'_{sie}$).

2.  **The Compression Phase**: Corresponds to the subsequent **reduction** of these resources (`N` decreases) to find a maximally efficient and generalizable representation. This forces the system to "prune" redundant internal pathways, leading to an increase in Cognitive Cost ($H'_{tse}$) and a decrease in Semantic Robustness ($H'_{sie}$).

Our "N-Sweep" experiment directly simulates this process and provides strong evidence for this new physical interpretation of the Information Bottleneck.

<img width="6600" height="3000" alt="n_sweep_ib_summary_plot_multirun" src="https://github.com/user-attachments/assets/f3a4722d-5600-4adf-a30b-06f8d5573885" />

*Figure 1: The IB trajectory revealed by the N-Sweep experiment, aggregated over 5 independent runs. The clear two-phase dynamic provides strong evidence for our hypothesis.*

## Repository Structure

```
.
├── assets                                 \# Images for README
├── Multi run/                    
│   ├── n_sweep_ib_verifier_multirun.ipynb \# Main experiment script
│   └── plot_n_sweep_ib_trajectory_multirun.py  \# Plotting script   
├── single run/                    
│   ├── n_sweep_ib_verifier.ipynb 
│   └── plot_n_sweep_ib_trajectory.py       
├── requirements.txt                         \# Python dependencies
└── README.md                                \# This file

````

## How to Reproduce the Results

### 1. Setup Environment

Clone the repository and set up the Python environment. We recommend using Conda.

```bash
git clone [https://github.com/alicethegod/First-Principles-Information-Bottleneck.git](https://github.com/alicethegod/First-Principles-Information-Bottleneck.git)
cd First-Principles-Information-Bottleneck
conda create -n ib_theory python=3.9
conda activate ib_theory
pip install -r requirements.txt
````

*(Note: You will first need to generate the `requirements.txt` file from your active environment using `pip freeze > requirements.txt`)*

### 2\. Run the Main Experiment

Execute the main verification script. This will perform the full N-Sweep experiment for the number of runs specified in the script's `CONFIG` and save the raw data.

This process is computationally intensive. Upon completion, it will generate a file named `n_sweep_ib_results_multirun.json`.

### 3\. Generate the Final Figure

Once the raw data has been generated, use the plotting script to create the final, publication-quality summary figure.

```bash
python plot_n_sweep_ib_trajectory_multirun.py
```

This script will read the `.json` file and save the final plot as `n_sweep_ib_summary_plot_multirun.png`.

## How to Cite

If you find this work useful in your research, please consider citing our paper:

```bibtex
@misc{Liu2025InformationBottleneck,
  author       = {Liu, Zhangchi},
  title        = {A First-Principles Physical Theory of the Information Bottleneck: From Hebbian Dynamics to Cognitive Economy},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {doi.org/17129965},
  url          = {[https://doi.org/17129965](https://doi.org/17129965)}
}
```

## License

This project is licensed under the MIT License.

-----


# 信息瓶颈的第一性原理物理解释


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17129965.svg)](https://doi.org/10.5281/zenodo.17129965)

本仓库为论文 **《信息瓶颈的第一性原理物理解释：从赫布动力学到认知经济》** 的官方实现代码。

我们为信息瓶颈（IB）现象提出了一个全新的第一性原理物理解释。我们的核心论点是：信息瓶颈的动力学轨迹并非单一训练过程中的时间演化，而是一个元系统为了寻求“认知经济”而动态调配其内部认知资源（即模型容量N）所产生的宏观现象。

本仓库通过一个原创的“N-Sweep”实验——即在一项固定任务上，训练一系列模型容量先增加后减少的模型——清晰地复现了经典的信息瓶颈轨迹，从而为我们的理论提供了强有力的实验证明。

-----

## 核心假说：作为认知资源分配的IB现象

本工作的核心论点是，经典的信息瓶颈两阶段动力学——**“拟合”后进行“压缩”**——是一个系统管理其内部认知资源的宏观体现，而非一个在训练时间中展开的过程。

我们提出，这个动力学过程可以通过模拟对一个固定任务的“认知空间”（模型容量 `N`）的分配与回收来理解：

1.  **拟合阶段**: 对应于元系统分配**不断增加**的内部资源（`N`增加），以鲁棒地捕获一个概念的全部复杂性。在我们的语义状态空间中，这表现为认知成本（$H'*{tse}$）的下降和语义鲁棒性（$H'*{sie}$）的上升。

2.  **压缩阶段**: 对应于后续对这些资源的**削减**（`N`减少），以寻求一个最高效、最泛化的表示。这迫使系统“修剪”冗余的内部通路，导致认知成本（$H'*{tse}$）的上升和语义鲁棒性（$H'*{sie}$）的下降。

我们的“N-Sweep”实验直接模拟了这一过程，并为这个全新的物理解释提供了强有力的证据。

<img width="6600" height="3000" alt="n_sweep_ib_summary_plot_multirun" src="https://github.com/user-attachments/assets/4358bdb6-ddb3-4006-9c76-2a61b1ff666b" />

*图1: 通过N-Sweep实验揭示的IB轨迹（5次独立实验的平均结果）。清晰的两阶段动力学为我们的假说提供了强有力的证据。*

## 仓库结构

```
.
├── assets                                 \# Images for README
├── Multi run/                    
│   ├── n_sweep_ib_verifier_multirun.ipynb  \# Main experiment script
│   └── plot_n_sweep_ib_trajectory_multirun.py  \# Plotting script   
├── single run/                    
│   ├── n_sweep_ib_verifier.ipynb 
│   └── plot_n_sweep_ib_trajectory.py       
├── requirements.txt                         \# Python dependencies
└── README.md                                \# This file
```

## 如何复现实验结果

### 1\. 配置环境

克隆本仓库并配置Python环境。我们推荐使用 Conda。

```bash
git clone [https://github.com/alicethegod/First-Principles-Information-Bottleneck.git](https://github.com/alicethegod/First-Principles-Information-Bottleneck.git)
cd First-Principles-Information-Bottleneck
conda create -n ib_theory python=3.9
conda activate ib_theory
pip install -r requirements.txt
```

*(请注意: 您需要先在您的环境中运行 `pip freeze > requirements.txt` 命令来生成依赖项文件)*

### 2\. 运行主实验

执行主验证脚本。这将根据脚本`CONFIG`中设定的运行次数，完整地执行N-Sweep实验，并保存原始数据。


这个过程计算量较大。完成后，它将生成一个名为 `n_sweep_ib_results_multirun.json` 的文件。

### 3\. 生成最终图表

在原始数据生成后，使用绘图脚本来创建最终的、论文级别的汇总图。

```bash
python plot_n_sweep_ib_trajectory_multirun.py
```

该脚本会读取`.json`文件，并将最终的图表保存为 `n_sweep_ib_summary_plot_multirun.png`。

## 如何引用

如果您在您的研究中发现本工作有用，请考虑引用我们的论文：

```bibtex
@misc{Liu2025InformationBottleneck,
  author       = {刘章驰},
  title        = {信息瓶颈的第一性原理物理解释：从赫布动力学到认知经济},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {doi.org/17129965},
  url          = {[https://doi.org/17129965](https://doi.org/17129965)}
}
```

## 许可证

本项目采用 MIT 许可证。
