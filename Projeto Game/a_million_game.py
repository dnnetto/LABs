class Pergunta:
     def __init__(self, prompt, resposta):
          self.prompt = prompt
          self.resposta = resposta

pergunta_prompts = [
     "Qual a cor da maca?\n(a) Vermelho/Verde\n(b)Laranja",
     "Qual a cor da banana?\n(a) Vermelho/Verde\n(b)Amarelo",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)