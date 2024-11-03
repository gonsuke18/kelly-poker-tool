# kelly_poker_tool.py

def calculate_kelly_bet(pot_size, call_size, win_probability):
    """
    ケリー基準に基づく最適なベット割合を計算します。

    Args:
        pot_size (float): 現在のポットのサイズ
        call_size (float): コールするための額
        win_probability (float): 勝つ確率 (0から1の範囲)

    Returns:
        float: 資金に対する最適なベット割合（パーセンテージ）
    """
    lose_probability = 1 - win_probability
    b = pot_size / call_size
    kelly_fraction = (b * win_probability - lose_probability) / b
    return max(0, kelly_fraction * 100)  # 負の値を防ぐため max(0, ...) を使用

# 使用例
if __name__ == "__main__":
    pot_size = float(input("ポットサイズを入力してください: "))
    call_size = float(input("コールサイズを入力してください: "))
    win_probability = float(input("勝率（0〜1の範囲）を入力してください: "))

    optimal_bet_percentage = calculate_kelly_bet(pot_size, call_size, win_probability)
    print(f"最適なベット割合: {optimal_bet_percentage:.2f}%")
