<<<<<<< HEAD
import os
import sys
from typing import List, Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from env import Environment, InitGameMessage, InitPolicyMessage, PieceArg, ActionSet
from local_input import IInputMethod, InputMethodManager


class Controller:
    """游戏交互框架：模式选择、初始化、回合响应、回合播放"""

    def __init__(self):
        self.environment: Optional[Environment] = None
        self.input_manager: Optional[InputMethodManager] = None
        self.game_mode: str = "single"  # 单机"single" 双人"double"
        self.current_round: int = 0

    def select_mode(self, mode: str):
        """选择游戏模式"""
        self.game_mode = mode
        # TODO: 模式校验（single or double）

    def create_environment(self) -> Environment:
        """创建并返回游戏环境"""
        # TODO: 根据模式创建 Environment
        self.environment = Environment()
        return self.environment

    def init_board(self, width: int, height: int, boarder: int = 0):
        """初始化棋盘数据并写入 environment"""
        if self.environment is None:
            self.create_environment()

        # TODO: 调用 Environment API 初始化棋盘（宽、高、边界、默认格子）
        self.environment.board = self.environment.create_board(width, height, boarder)
        return self.environment.board

    def init_piece_by_player(self, player_id: int, init_message: InitGameMessage,
                             input_method: IInputMethod) -> InitPolicyMessage:
        """使用输入方法完成单个玩家的棋子初始化"""
        # TODO: 校验 init_message, 走初始化流程
        return input_method.handle_init_input(init_message)

    def initialize_game(self, input_methods: List[IInputMethod]):
        """完成所有玩家的棋子初始化"""
        if self.environment is None:
            self.create_environment()

        # TODO: 依次调用 init_piece_by_player
        for player_id, method in enumerate(input_methods, start=1):
            init_msg = InitGameMessage()
            policy = self.init_piece_by_player(player_id, init_msg, method)
            # TODO: 将 policy 应用到 environment

    def handle_turn_request(self, player_id: int, env: Environment) -> ActionSet:
        """根据当前回合请求获取玩家行动（界面按钮点击后触发）"""
        if self.input_manager is None:
            raise RuntimeError("Input manager not set")

        action = self.input_manager.handle_action_input(player_id, env)
        # TODO: 根据 action.move/action.attack/action.spell 处理“移动/攻击/法术”逻辑与校验
        # TODO: 将本回合动作信息写入 JSON 日志
        return action

    def play_turn(self, action: ActionSet):
        """执行一回合动作并推进游戏状态（仅接口，内部逻辑在 TODO）"""
        # TODO: 解包 action，并按 action.move/action.attack/action.spell 调用具体处理函数
        # TODO: 更新 environment 中棋子位置、血量、行动点、死活状态等
        # TODO: 记录并返回本回合结束后的状态快照
        pass

    def save_turn_log(self, log_entry: dict, file_path: str = "turn_logs.json"):
        """把单回合动作与结果写入 JSON 文件"""
        # TODO: 打开 file_path，追加本回合 log_entry JSON
        pass

    def load_turn_logs(self, file_path: str = "turn_logs.json") -> List[dict]:
        """从 JSON 文件读取回合日志，用于回放"""
        # TODO: 读取 file_path，返回回合日志列表
        return []

    def replay_rounds(self, file_path: str = "turn_logs.json"):
        """基于 JSON 日志回放回合过程（独立播放逻辑）"""
        logs = self.load_turn_logs(file_path)
        # TODO: 遍历 logs，按回合序列还原环境状态并执行可视化
        # TODO: 这里需要与 UI 交互，控制每一回合的播放按钮事件
        pass

    def run_round(self):
        """主循环：每回合请求玩家行动并播放回合"""
        if self.environment is None:
            raise RuntimeError("Environment is not initialized")
        if self.input_manager is None:
            raise RuntimeError("Input manager is not set")

        self.current_round += 1
        # TODO: 获取当前玩家和当前棋子
        # TODO: 调用 handle_turn_request 获取 ActionSet
        # TODO: 调用 play_turn(action)
        # TODO: 用 save_turn_log 存储回合信息


if __name__ == "__main__":
    controller = Controller()
    controller.select_mode("manual")
    env = controller.create_environment()
    print("Controller framework initialized", controller.game_mode, env)
=======
import os
import sys
from typing import List, Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from env import Environment, InitGameMessage, InitPolicyMessage, PieceArg, ActionSet
from local_input import IInputMethod, InputMethodManager


class Controller:
    """游戏交互框架：模式选择、初始化、回合响应、回合播放"""

    def __init__(self):
        self.environment: Optional[Environment] = None
        self.input_manager: Optional[InputMethodManager] = None
        self.game_mode: str = "single"  # 单机"single" 双人"double"
        self.current_round: int = 0

    def select_mode(self, mode: str):
        """选择游戏模式"""
        self.game_mode = mode
        # TODO: 模式校验（single or double）

    def create_environment(self) -> Environment:
        """创建并返回游戏环境"""
        # TODO: 根据模式创建 Environment
        self.environment = Environment()
        return self.environment

    def init_board(self, width: int, height: int, boarder: int = 0):
        """初始化棋盘数据并写入 environment"""
        if self.environment is None:
            self.create_environment()

        # TODO: 调用 Environment API 初始化棋盘（宽、高、边界、默认格子）
        self.environment.board = self.environment.create_board(width, height, boarder)
        return self.environment.board

    def init_piece_by_player(self, player_id: int, init_message: InitGameMessage,
                             input_method: IInputMethod) -> InitPolicyMessage:
        """使用输入方法完成单个玩家的棋子初始化"""
        # TODO: 校验 init_message, 走初始化流程
        return input_method.handle_init_input(init_message)

    def initialize_game(self, input_methods: List[IInputMethod]):
        """完成所有玩家的棋子初始化"""
        if self.environment is None:
            self.create_environment()

        # TODO: 依次调用 init_piece_by_player
        for player_id, method in enumerate(input_methods, start=1):
            init_msg = InitGameMessage()
            policy = self.init_piece_by_player(player_id, init_msg, method)
            # TODO: 将 policy 应用到 environment

    def handle_turn_request(self, player_id: int, env: Environment) -> ActionSet:
        """根据当前回合请求获取玩家行动（界面按钮点击后触发）"""
        if self.input_manager is None:
            raise RuntimeError("Input manager not set")

        action = self.input_manager.handle_action_input(player_id, env)
        # TODO: 根据 action.move/action.attack/action.spell 处理“移动/攻击/法术”逻辑与校验
        # TODO: 将本回合动作信息写入 JSON 日志
        return action

    def play_turn(self, action: ActionSet):
        """执行一回合动作并推进游戏状态（仅接口，内部逻辑在 TODO）"""
        # TODO: 解包 action，并按 action.move/action.attack/action.spell 调用具体处理函数
        # TODO: 更新 environment 中棋子位置、血量、行动点、死活状态等
        # TODO: 记录并返回本回合结束后的状态快照
        pass

    def save_turn_log(self, log_entry: dict, file_path: str = "turn_logs.json"):
        """把单回合动作与结果写入 JSON 文件"""
        # TODO: 打开 file_path，追加本回合 log_entry JSON
        pass

    def load_turn_logs(self, file_path: str = "turn_logs.json") -> List[dict]:
        """从 JSON 文件读取回合日志，用于回放"""
        # TODO: 读取 file_path，返回回合日志列表
        return []

    def replay_rounds(self, file_path: str = "turn_logs.json"):
        """基于 JSON 日志回放回合过程（独立播放逻辑）"""
        logs = self.load_turn_logs(file_path)
        # TODO: 遍历 logs，按回合序列还原环境状态并执行可视化
        # TODO: 这里需要与 UI 交互，控制每一回合的播放按钮事件
        pass

    def run_round(self):
        """主循环：每回合请求玩家行动并播放回合"""
        if self.environment is None:
            raise RuntimeError("Environment is not initialized")
        if self.input_manager is None:
            raise RuntimeError("Input manager is not set")

        self.current_round += 1
        # TODO: 获取当前玩家和当前棋子
        # TODO: 调用 handle_turn_request 获取 ActionSet
        # TODO: 调用 play_turn(action)
        # TODO: 用 save_turn_log 存储回合信息


if __name__ == "__main__":
    controller = Controller()
    controller.select_mode("manual")
    env = controller.create_environment()
    print("Controller framework initialized", controller.game_mode, env)
>>>>>>> origin/main
