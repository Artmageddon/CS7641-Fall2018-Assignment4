import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='FrozenLake15x15-v1',
    entry_point='frozen_lake.envs.frozenlake_env:FrozenLakeEnv',
    max_episode_steps=5000,
    reward_threshold=0.99,  # optimum = 1
    kwargs={'map_name': '15x15'}
)

register(
    id='FrozenLake25x25-v1',
    entry_point='frozen_lake.envs.frozenlake_env:FrozenLakeEnv',
    max_episode_steps=5000,
    reward_threshold=0.99,  # optimum = 1
    kwargs={'map_name': '25x25'}
)

register(
    id='FrozenLake4x4-v1',
    entry_point='frozen_lake.envs.frozenlake_env:FrozenLakeEnv',
    max_episode_steps=5000,
    reward_threshold=0.99,  # optimum = 1
    kwargs={'map_name': '4x4'}
)
register(
    id='FrozenLake8x8-v1',
    entry_point='frozen_lake.envs.frozenlake_env:FrozenLakeEnv',
    max_episode_steps=5000,
    reward_threshold=0.99,  # optimum = 1
    kwargs={'map_name': '8x8'}
)