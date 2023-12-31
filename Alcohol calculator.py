"""
@author: Jung Jinwoong
"""

def calculate_alcohol_percentage(ingredients):
    total_volume = 0
    total_alcohol = 0
    
    for ingredient in ingredients:
        alcohol_present = input(f"{ingredient}はアルコールが入った飲み物ですか？ (はい/いいえ): ").lower()
        
        if alcohol_present == "はい":
            alcohol_percentage = float(input(f"{ingredient}のアルコール度数を教えてください(%) 。: "))
            volume = float(input(f"{ingredient}は何mlですか？"))
        else:
            alcohol_percentage = 0
            volume = float(input(f"{ingredient}の容量を教えてください (ml)。 "))
        
        alcohol_amount = (volume * alcohol_percentage) / 100
        total_alcohol += alcohol_amount 
        total_volume += volume
    
    if total_volume > 0:
        alcohol_percentage = (total_alcohol / total_volume) * 100
        print(f"お酒のアルコール度数: {alcohol_percentage:.2f}%")
        recommended_daily_male = 20  # 男性の1日の適量
        recommended_daily_female = 10  # 女性の1日の適量
        print(f"摂取した純アルコール量: {0.8 * total_alcohol:.2f} g")
        
        if 0.8 * total_alcohol > recommended_daily_male:
            print("「節度ある適度な飲酒量」は、男性基準1日純アルコールで約20g程度であるとされています。")
            print("摂取されたアルコール量が男性と女性の基準を超えています。")
        elif 0.8 * total_alcohol > recommended_daily_female:
            print("「節度ある適度な飲酒量」は、女性基準1日純アルコールで約10g程度であるとされています。")
            print("摂取されたアルコール量が女性の基準を超えています。")
        else:
            print("摂取されたアルコール量は「節度ある適度な飲酒量」の基準内です。")
    else:
        print("情報がないです。")

def main():
    print("アルコールの体に対する影響は摂取した純アルコール量が基準となります。")
    print("簡単に純アルコール摂取量を調べてみましょう。")
    print("ビール、RTD・チューハイなどの商品は1を入力してください。")
    print("カクテルなど複数の材料が入る場合は、材料の数を入力してください。")

    while True:  #  "終了"まで
        num_ingredients = input("商品や材料の数を教えてください。終了を希望する場合は「終了」と入力してください。 ")

        if num_ingredients.lower() == "終了":
            print("プログラムを終了します。")
            break  # 終了
        elif num_ingredients.isdigit() and int(num_ingredients) > 0:
            num_ingredients = int(num_ingredients)
            ingredients_list = []
            for i in range(num_ingredients):
                ingredient = input(f"{i + 1}番目の商品や材料の名前を教えてください。: ")
                ingredients_list.append(ingredient)
            
            calculate_alcohol_percentage(ingredients_list)
        else:
            print("有効な数値を入力してください。")

if __name__ == "__main__":
    main()
