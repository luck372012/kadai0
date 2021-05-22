source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

def search():
    word =input("ねずこ")
  
    if word in source:
        print("{}が見つかりした".format(word))
        return
    print("{}が見つかりません".format(word))

        
if __name__ == "__main__":
    search()