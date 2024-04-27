import random
from openai import OpenAI

def generateAns(question, ans):
    client = OpenAI()
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
            "role": "system",
            "content": "You are a fortunate-teller. Now I will ask my questions and please answer my questions based on the keywords " + ans['explanation']
        }, {
            "role": "user",
            "content": question
        },
      ]
    )

    print("您的卦象是：", ans["name"], "。含义是：", ans["explanation"], ".\n")
    print()
    print(response.choices[0].message.content)

# 易经六十四卦的名称和简要解释
guas = [
  {
    "name": "乾卦",
    "explanation": "创始，强大，成功。",
    "lines": ["九阳爻", "九阳爻", "九阳爻", "九阳爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "坤卦",
    "explanation": "顺从，柔弱，耐心。",
    "lines": ["六阴爻", "六阴爻", "六阴爻", "六阴爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "屯卦",
    "explanation": "初步困难，积累力量。",
    "lines": ["九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "蒙卦",
    "explanation": "启蒙，初学，不安定。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "需卦",
    "explanation": "等待时机，等待机会。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "讼卦",
    "explanation": "争论，纠纷，诉讼。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "师卦",
    "explanation": "带领，教导，学习。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "比卦",
    "explanation": "联合，合作，竞争。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "小畜卦",
    "explanation": "小步前进，积累资源。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "履卦",
    "explanation": "前进，稳步，谨慎。",
    "lines": ["九阳爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "泰卦",
    "explanation": "平衡，成功，繁荣。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "九阳爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "否卦",
    "explanation": "困难，挫折，不利。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "同人卦",
    "explanation": "团结，合作，成功。",
    "lines": ["九阳爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "大有卦",
    "explanation": "丰富，繁荣，成功。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "九阳爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "谦卦",
    "explanation": "谦虚，谨慎，谦逊。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "六阴爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "豫卦",
    "explanation": "喜悦，兴奋，不安定。",
    "lines": ["六阴爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "随卦",
    "explanation": "跟随，顺从，柔顺。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "蛊卦",
    "explanation": "毒害，腐蚀，危险。",
    "lines": ["九阳爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "临卦",
    "explanation": "威严，领导，坚决。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "观卦",
    "explanation": "观察，观看，等待。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "噬嗑卦",
    "explanation": "破坏，冲突，矛盾。",
    "lines": ["九阳爻", "六阴爻", "六阴爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "贲卦",
    "explanation": "变化，不稳定，积极。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "剥卦",
    "explanation": "剥夺，减少，困难。",
    "lines": ["六阴爻", "六阴爻", "六阴爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "复卦",
    "explanation": "重复，返回，复苏。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "六阴爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "无妄卦",
    "explanation": "无知，轻率，不稳定。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "大畜卦",
    "explanation": "积累，储备，充实。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "颐卦",
    "explanation": "滋养，关心，谨慎。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "大过卦",
    "explanation": "过度，冒险，超越。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "坎卦",
    "explanation": "危险，障碍，陷阱。",
    "lines": ["九阳爻", "六阴爻", "六阴爻", "六阴爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "离卦",
    "explanation": "激情，热情，光明。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "咸卦",
    "explanation": "互相感染，亲密，合作。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "恒卦",
    "explanation": "恒定，持久，稳定。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "遁卦",
    "explanation": "隐遁，躲避，逃避。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "大壮卦",
    "explanation": "强大，成功，兴奋。",
    "lines": ["九阳爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "晋卦",
    "explanation": "进步，前进，增长。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "明夷卦",
    "explanation": "毁灭，光明，觉醒。",
    "lines": ["九阳爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "家人卦",
    "explanation": "家庭，团聚，社交。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "睽卦",
    "explanation": "分歧，冲突，矛盾。",
    "lines": ["九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "蹇卦",
    "explanation": "困难，阻碍，困境。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "解卦",
    "explanation": "解决，释放，解脱。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "损卦",
    "explanation": "损失，削弱，减少。",
    "lines": ["九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "益卦",
    "explanation": "增加，提升，增益。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "夬卦",
    "explanation": "决策，决断，判断。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "姤卦",
    "explanation": "危险，不安，逆境。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "萃卦",
    "explanation": "聚集，团结，社交。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "升卦",
    "explanation": "进步，上升，提升。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "困卦",
    "explanation": "困难，困境，逆境。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "九阳爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "井卦",
    "explanation": "井，供水，照明，社交。",
    "lines": ["九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "革卦",
    "explanation": "变革，改变，转变。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "鼎卦",
    "explanation": "烹饪，变革，改进。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "震卦",
    "explanation": "震动，激发，觉醒。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "艮卦",
    "explanation": "停滞，静止，守护。",
    "lines": ["六阴爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "渐卦",
    "explanation": "渐进，逐渐，进展。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "六阴爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "归妹卦",
    "explanation": "归妹，家庭团聚，喜庆。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "丰卦",
    "explanation": "丰收，繁荣，成功。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "旅卦",
    "explanation": "旅行，流动，外出。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "六阴爻"]
  },
  {
    "name": "巽卦",
    "explanation": "柔顺，顺从，谨慎。",
    "lines": ["六阴爻", "六阴爻", "六阴爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "兑卦",
    "explanation": "兑现，喜悦，幸福。",
    "lines": ["九阳爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "涣卦",
    "explanation": "涣散，分散，分离。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "节卦",
    "explanation": "节制，克制，谨慎。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "中孚卦",
    "explanation": "诚信，中正，交流。",
    "lines": ["六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻", "九阳爻"]
  },
  {
    "name": "小过卦",
    "explanation": "小有过失，小失误。",
    "lines": ["六阴爻", "六阴爻", "九阳爻", "九阳爻", "六阴爻", "九阳爻"]
  },
  {
    "name": "既济卦",
    "explanation": "已经完成，成功。",
    "lines": ["九阳爻", "六阴爻", "九阳爻", "六阴爻", "九阳爻", "六阴爻"]
  },
  {
    "name": "未济卦",
    "explanation": "未完成，失败，不圆满。",
    "lines": ["六阴爻", "九阳爻", "六阴爻", "六阴爻", "九阳爻", "六阴爻"]
  }
]

user_input = input("Press enter to your question here: ")

result = random.randint(1, 64)

generateAns(user_input, guas[result])