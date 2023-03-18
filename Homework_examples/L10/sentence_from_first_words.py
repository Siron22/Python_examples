"""
Есть фрагмент текста, состоящий из предложений. 
Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).
Предложение может состоять из одного слова.
Составить предложение из первых слов предложений фрагмента. 
Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой. 
Предложение должно заканчиваться точкой.

def generate_sentence(text: str) -> str:
    pass

"Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.." -> "Hello and who or yes claro." 
"Hola..." -> Hola.

"""
import re


def generate_sentence(text: str) -> str:
    regex = r"[A-Z]{1}.*?[\.\?\!]+"
    sentences = re.findall(regex, text)
    if not sentences:
        return ""
    words = []
    for sentence in sentences:
        regex2 = r"[A-Z]{1}[a-zA-Z]*[\ \,\.\?\!]"
        first_word = re.findall(regex2, sentence)
        words.append(first_word[0])
    updated_words = [word.lower()[:-1] for word in words]
    final_sentence = " ".join(updated_words)
    final_sentence = f"{final_sentence[0].upper()}{final_sentence[1:]}."
    return final_sentence


text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
"Hello and who or yes claro."
print(generate_sentence(text))
print(generate_sentence("Hola..."))


assert generate_sentence("Hello.") == "Hello."
assert generate_sentence("Hello and hi.") == "Hello."
assert generate_sentence("Hello and hi. Second sentence.") == "Hello second."
assert generate_sentence("Nothing, but more. ") == "Nothing."

text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
assert generate_sentence(text) == "Hello and who or yes claro."

assert generate_sentence('') == ''
assert generate_sentence('ajfdk') == ''
assert generate_sentence('Ahffhf') == ''
assert generate_sentence('Ahffhf dsdf') == ''
assert generate_sentence("Hello and hi. Second sentence") == "Hello."
