"""
*
* Uso: Chamar a função passando a senha e o salt como parâmetro, por exemplo:
*
* secr = criptografar("senha", "salt")
* 
* Ele retornará uma string em hash SHA-256 criptografado.
*
* Caso não tenha salt na senha, passar a string vazia, dessa forma:
*
* secr = criptografar("senha", "")
"""

from hashlib import md5, sha1, sha256

def criptografar(texto, sal):
    texto = texto.strip().encode("utf-8")
    sal = sal.strip().encode("utf-8")

    if not texto:
        raise Exception("Passe um Valor em Texto!")

    hashTex = sha1(texto).hexdigest()
    hashSal = ""

    if sal:
        hashSal = md5(sal).hexdigest()

    cript = sha256(hashTex.encode("utf-8") + hashSal.encode("utf-8")).hexdigest()

    return cript
