class BaseLogger:
    """基本のロガー"""

    @classmethod
    def output(cls, logged_data: dict):
        """デフォルトのログ"""
        print(f"APIレスポンスがありませんでした。: {logged_data}")
