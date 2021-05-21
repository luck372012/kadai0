### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def check(n):
            
    ### ここに検索ロジックを書く
    for _ in source:
        if _ == n:
            print(f"{n}が見つかりした")
            return
    print(f"{n}は見つかりません")
        
check("たんじろう")
check("ねこ")    
    
source.append("ねこ")
print(source) 