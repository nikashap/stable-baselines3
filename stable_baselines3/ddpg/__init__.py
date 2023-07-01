from stable_baselines3.ddpg.ddpg import DDPG
from stable_baselines3.ddpg.policies import CnnPolicy, MlpPolicy, MultiInputPolicy
from stable_baselines3.ddpg.clipddpg import ClipDDPG
__all__ = ["CnnPolicy", "MlpPolicy", "MultiInputPolicy", "DDPG", "ClipDDPG"]
