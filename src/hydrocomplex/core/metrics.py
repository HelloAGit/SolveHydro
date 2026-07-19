import numpy as np

def nse(obs, sim):
    obs = np.asarray(obs)
    sim = np.asarray(sim)
    mask = ~np.isnan(obs)
    obs = obs[mask]; sim = sim[mask]
    denom = np.sum((obs - obs.mean())**2)
    if denom == 0:
        return float("nan")
    return 1 - np.sum((sim - obs)**2) / denom

def kge(obs, sim):
    obs = np.asarray(obs); sim = np.asarray(sim)
    mask = ~np.isnan(obs)
    obs = obs[mask]; sim = sim[mask]
    r = np.corrcoef(obs, sim)[0,1]
    alpha = sim.mean() / obs.mean() if obs.mean() != 0 else np.nan
    beta = (sim.std() / obs.std()) if obs.std() != 0 else np.nan
    # Kling-Gupta formulation
    return 1 - np.sqrt((r-1)**2 + (alpha-1)**2 + (beta-1)**2)
