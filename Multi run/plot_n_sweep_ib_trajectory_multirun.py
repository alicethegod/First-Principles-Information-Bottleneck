# -*- coding: utf-8 -*-
"""
Plotting Script for the Multi-Run N-Sweep IB Verification Experiment

This script visualizes the aggregated results from `n_sweep_ib_verifier_multirun.py`.

It loads the raw JSON data containing multiple independent runs and generates
a summary plot that visualizes:
1.  The individual trajectory of each run in the Semantic State Space.
2.  The average trajectory across all runs.
3.  The standard deviation across all runs, shown as a shaded area.
4.  The evolution of the average entropy metrics over time.

This approach provides a robust visualization of the learning dynamics,
highlighting both the general trend and its variability.
"""
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import minmax_scale

def plot_ib_trajectory_from_n_sweep_multirun(json_path, figure_filename):
    """Loads and plots the aggregated results from the N-Sweep experiment."""
    try:
        with open(json_path, 'r') as f:
            all_runs_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{json_path}' was not found.")
        return

    if not all_runs_data:
        print("Error: The results file is empty."); return
    
    # --- Data Aggregation and Processing ---
    num_runs = len(all_runs_data)
    num_steps = len(all_runs_data[0])

    htse_all_runs = np.zeros((num_runs, num_steps))
    hsie_all_runs = np.zeros((num_runs, num_steps))

    for i, run_data in enumerate(all_runs_data):
        df = pd.DataFrame(run_data)
        htse_all_runs[i, :] = minmax_scale(df['final_htse'])
        hsie_all_runs[i, :] = minmax_scale(df['final_hsie'])

    mean_htse = np.mean(htse_all_runs, axis=0)
    std_htse = np.std(htse_all_runs, axis=0)
    mean_hsie = np.mean(hsie_all_runs, axis=0)
    std_hsie = np.std(hsie_all_runs, axis=0)
    
    steps = np.arange(num_steps)

    # --- Visualization ---
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(22, 10))
    fig.suptitle('IB Dynamics Revealed by N-Sweep (Aggregated over {} Runs)'.format(num_runs), fontsize=22, y=0.98)

    # --- Plot 1: Trajectory in Semantic State Space ---
    ax1 = axes[0]
    cmap = plt.get_cmap('viridis')
    
    for i in range(num_runs):
        ax1.plot(htse_all_runs[i, :], hsie_all_runs[i, :], lw=1.5, alpha=0.2, color='grey')

    points = ax1.scatter(mean_htse, mean_hsie, c=steps, cmap=cmap, s=80, zorder=3, ec='black', lw=0.5)
    
    turning_point_idx = np.argmax(mean_hsie)
    ax1.plot(mean_htse[0], mean_hsie[0], 'o', color='blue', markersize=15, label='Start (N increases)', zorder=4)
    ax1.plot(mean_htse[turning_point_idx], mean_hsie[turning_point_idx], 'o', color='red', markersize=15, label='Turning Point (Compression Starts)', zorder=4)

    cbar = fig.colorbar(points, ax=ax1)
    cbar.set_label('N-Sweep Step', fontsize=14)
    ax1.set_xlabel("Normalized Cognitive Cost ($H'_{tse}$) $\\rightarrow$", fontsize=16)
    ax1.set_ylabel("Normalized Semantic Robustness ($H'_{sie}$) $\\rightarrow$", fontsize=16)
    ax1.set_title('1. Mean Trajectory in Semantic State Space', fontsize=18, pad=15)
    ax1.legend(fontsize=12)
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

    # --- Plot 2: Entropy Evolution Over N-Sweep Steps ---
    ax2 = axes[1]
    
    ax2.plot(steps, mean_htse, color='darkgreen', lw=2.5, label="$H'_{tse}$ (Mean)")
    ax2.fill_between(steps, mean_htse - std_htse, mean_htse + std_htse, color='darkgreen', alpha=0.2, label="Std. Dev.")

    ax2.plot(steps, mean_hsie, color='darkblue', lw=2.5, label="$H'_{sie}$ (Mean)")
    ax2.fill_between(steps, mean_hsie - std_hsie, mean_hsie + std_hsie, color='darkblue', alpha=0.2)
    
    ax2.axvline(x=turning_point_idx, color='red', linestyle='--', label=f'Mean Compression Starts (Step {turning_point_idx})')

    ax2.set_xlabel('N-Sweep Step (Model Capacity N increases then decreases)', fontsize=16)
    ax2.set_ylabel('Normalized Entropy Value', fontsize=16)
    ax2.set_title('2. Mean Entropy Evolution with Std. Dev.', fontsize=18, pad=15)
    ax2.legend(fontsize=12)
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    plt.savefig(figure_filename, dpi=300)
    print(f"\nAggregated summary plot saved to: {figure_filename}")
    
    plt.show()

if __name__ == '__main__':
    json_results_path = "n_sweep_ib_results_multirun.json" 
    output_figure_path = "n_sweep_ib_summary_plot_multirun.png"
    plot_ib_trajectory_from_n_sweep_multirun(json_results_path, output_figure_path)