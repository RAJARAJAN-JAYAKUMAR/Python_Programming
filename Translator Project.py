from translate import Translator
translator=Translator(to_lang="hi")
try:
    with open(r'C:\Users\RAJARAJAN JAYAKUMAR\Desktop\Python\Translator Project.txt', mode='r') as myfile:
        text = myfile.read()
        result=translator.translate(text)
        print(result)
        # with open(r'C:\Users\RAJARAJAN JAYAKUMAR\Desktop\Python\Translator project output.txt', mode='w') as out:
        #     out.write(result)
except FileNotFoundError as e:
    print("file doesn't exist")












